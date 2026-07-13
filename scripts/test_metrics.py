"""Runner di validazione del motore metriche (metrics_engine).

Esegue check deterministici su input sintetici, senza dipendenze di test esterne
(niente pytest): coerente con il vincolo a costo zero del progetto.

Uso:
    python scripts/test_metrics.py

Exit code 0 se tutti i test passano, 1 se almeno uno fallisce.
"""
from __future__ import annotations

import os
import sys

# Permette di importare metrics_engine dalla root del progetto.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from metrics_engine import (  # noqa: E402
    ElbowAngleSmoother,
    LEFT_ARM_LANDMARK_IDS,
    RIGHT_ARM_LANDMARK_IDS,
    StrokeCounter,
    calculate_elbow_angle,
    calculate_fluidity_score,
    select_camera_side_arm,
)


def _make_landmarks(default_visibility: float = 0.5) -> list[dict]:
    """Crea 33 landmark sintetici (formato di extract_pose_landmarks)."""
    return [
        {
            "id": float(i),
            "x": round(0.01 * i, 3),
            "y": round(0.02 * i, 3),
            "z": 0.0,
            "visibility": default_visibility,
        }
        for i in range(33)
    ]


# --- T07: selezione arto lato-camera -------------------------------------------------

def test_select_camera_side_arm_picks_more_visible_side() -> None:
    lms = _make_landmarks()
    for i in LEFT_ARM_LANDMARK_IDS:
        lms[i]["visibility"] = 0.4
    for i in RIGHT_ARM_LANDMARK_IDS:
        lms[i]["visibility"] = 0.9

    result = select_camera_side_arm(lms)
    assert result is not None, "atteso un risultato, ottenuto None"
    assert result["arm_side"] == "right", f"lato errato: {result['arm_side']}"
    wrist_id = RIGHT_ARM_LANDMARK_IDS[2]
    assert result["wrist"] == (lms[wrist_id]["x"], lms[wrist_id]["y"]), result["wrist"]
    assert abs(result["mean_visibility"] - 0.9) < 1e-9, result["mean_visibility"]


def test_select_camera_side_arm_left_side() -> None:
    lms = _make_landmarks()
    for i in LEFT_ARM_LANDMARK_IDS:
        lms[i]["visibility"] = 0.95
    for i in RIGHT_ARM_LANDMARK_IDS:
        lms[i]["visibility"] = 0.30

    result = select_camera_side_arm(lms)
    assert result is not None
    assert result["arm_side"] == "left", f"lato errato: {result['arm_side']}"


def test_select_camera_side_arm_empty_returns_none() -> None:
    assert select_camera_side_arm([]) is None
    assert select_camera_side_arm(None) is None


# --- T08: forward-fill occlusioni sull'angolo del gomito ------------------------------

def test_elbow_smoother_forward_fill_on_occlusion() -> None:
    smoother = ElbowAngleSmoother()

    # Braccio disteso ~180 gradi, landmark ben visibili.
    a1 = smoother.update((0, 0), (1, 0), (2, 0), min_visibility=0.9)
    assert a1 is not None and abs(a1 - 180.0) < 1e-6, a1

    # Frame occluso: coordinate "sporche" ma visibility sotto soglia -> forward-fill.
    a2 = smoother.update((0, 0), (1, 0), (0, 10), min_visibility=0.2)
    assert a2 == a1, f"forward-fill fallito: {a2} != {a1}"

    # Ritorno alla visibilita': gomito a ~90 gradi, valore ricalcolato.
    a3 = smoother.update((0, 1), (0, 0), (1, 0), min_visibility=0.8)
    assert abs(a3 - 90.0) < 1e-6, a3


def test_elbow_smoother_none_before_first_valid() -> None:
    smoother = ElbowAngleSmoother()
    # Prima misura gia' occlusa: nessun angolo valido da mantenere.
    assert smoother.update((0, 0), (1, 0), (2, 0), min_visibility=0.1) is None


def test_elbow_smoother_no_exception_on_repeated_occlusion() -> None:
    smoother = ElbowAngleSmoother()
    smoother.update((0, 0), (1, 0), (2, 0), min_visibility=0.9)
    for _ in range(5):
        angle = smoother.update((0, 0), (1, 0), (0, 5), min_visibility=0.0)
        assert abs(angle - 180.0) < 1e-6, angle  # resta sull'ultimo valido


# --- T09: angolo del gomito (calculate_elbow_angle) ----------------------------------

def test_elbow_angle_straight_arm() -> None:
    # spalla-gomito-polso allineati in versi opposti -> braccio disteso ~180.
    assert abs(calculate_elbow_angle((0, 0), (1, 0), (2, 0)) - 180.0) < 1e-6


def test_elbow_angle_right_angle() -> None:
    assert abs(calculate_elbow_angle((0, 1), (0, 0), (1, 0)) - 90.0) < 1e-6


def test_elbow_angle_acute_45() -> None:
    assert abs(calculate_elbow_angle((1, 1), (0, 0), (1, 0)) - 45.0) < 1e-6


def test_elbow_angle_within_bounds() -> None:
    samples = [
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (0, 0), (1, 0)),
        ((1, 1), (0, 0), (1, 0)),
        ((2, 0), (1, 0), (2, 0)),
        ((-1, -1), (0, 0), (1, 1)),
    ]
    for shoulder, elbow, wrist in samples:
        angle = calculate_elbow_angle(shoulder, elbow, wrist)
        assert 0.0 <= angle <= 180.0, (shoulder, elbow, wrist, angle)


# --- T10: conteggio bracciate (StrokeCounter) ----------------------------------------

def _triangle_wave(cycles: int, dt: float = 0.1, top: float = 0.5,
                   bottom: float = 0.1, steps_half: int = 4) -> list[tuple[float, float]]:
    """Onda triangolare di Y del polso: un minimo (punto 'alto') per ciclo.

    In MediaPipe Y cresce verso il basso, quindi il minimo di Y e' il punto piu'
    alto del polso. Con steps_half=4 e dt=0.1 il ciclo dura 0.8 s (> debounce).
    """
    step = (top - bottom) / steps_half
    series = [(top, 0.0)]
    t, y = 0.0, top
    for _ in range(cycles):
        for _ in range(steps_half):  # discesa fisica: Y decresce
            t += dt
            y = round(y - step, 4)
            series.append((y, t))
        for _ in range(steps_half):  # risalita fisica: Y cresce
            t += dt
            y = round(y + step, 4)
            series.append((y, t))
    return series


def test_stroke_counter_counts_regular_rhythm() -> None:
    counter = StrokeCounter()
    for wrist_y, timestamp in _triangle_wave(cycles=3):
        counter.update(wrist_y, timestamp, shoulder_y=0.3)
    assert counter.stroke_count == 3, counter.stroke_count


def test_stroke_counter_deadband_ignores_jitter() -> None:
    counter = StrokeCounter()
    timestamp = 0.0
    for i in range(50):
        timestamp += 0.1
        wrist_y = 0.199 if i % 2 == 0 else 0.201  # |delta| = 0.002 < min_delta 0.003
        counter.update(wrist_y, timestamp, shoulder_y=0.5)
    assert counter.stroke_count == 0, counter.stroke_count


def test_stroke_counter_debounce_blocks_fast_second_peak() -> None:
    counter = StrokeCounter()
    # Due minimi a 0.2 s di distanza: sotto il debounce di 0.6 s -> conta 1 solo.
    for wrist_y, timestamp in [(0.5, 0.0), (0.1, 0.1), (0.5, 0.2), (0.1, 0.3), (0.5, 0.4)]:
        counter.update(wrist_y, timestamp, shoulder_y=0.3)
    assert counter.stroke_count == 1, counter.stroke_count


def test_stroke_counter_shoulder_gate_blocks_low_wrist() -> None:
    counter = StrokeCounter()
    # Minimo del polso a y=0.4 con spalla a y=0.3: polso SOTTO la spalla -> non conta.
    for wrist_y, timestamp in [(0.6, 0.0), (0.4, 0.1), (0.6, 0.2)]:
        counter.update(wrist_y, timestamp, shoulder_y=0.3)
    assert counter.stroke_count == 0, counter.stroke_count


def test_stroke_counter_shoulder_gate_blocks_equal_height() -> None:
    counter = StrokeCounter()
    # RF-006 richiede peak_y < shoulder_y: alla stessa altezza non deve contare.
    for wrist_y, timestamp in [(0.6, 0.0), (0.3, 0.1), (0.6, 0.2)]:
        counter.update(wrist_y, timestamp, shoulder_y=0.3)
    assert counter.stroke_count == 0, counter.stroke_count


# --- T11: Fluidity Score (calculate_fluidity_score) ----------------------------------

def test_fluidity_regular_intervals_high() -> None:
    # Intervalli identici -> std 0 -> punteggio massimo.
    score = calculate_fluidity_score([0.0, 1.0, 2.0, 3.0, 4.0])
    assert abs(score - 100.0) < 1e-9, score


def test_fluidity_irregular_intervals_low() -> None:
    regular = calculate_fluidity_score([0.0, 1.0, 2.0, 3.0, 4.0])
    irregular = calculate_fluidity_score([0.0, 0.1, 4.1, 4.2, 8.2])
    assert irregular < regular, (irregular, regular)
    assert 0.0 <= irregular < 10.0, irregular


def test_fluidity_fewer_than_three_peaks_zero() -> None:
    assert calculate_fluidity_score([]) == 0.0
    assert calculate_fluidity_score([0.0]) == 0.0
    assert calculate_fluidity_score([0.0, 1.0]) == 0.0


def test_fluidity_never_negative() -> None:
    # Intervalli molto irregolari: il punteggio e' troncato a 0, mai negativo.
    score = calculate_fluidity_score([0.0, 0.01, 10.0, 10.01, 25.0])
    assert score >= 0.0, score


def _collect_tests() -> list:
    """Raccoglie tutte le funzioni test_* del modulo, in ordine di definizione."""
    module = sys.modules[__name__]
    tests = [
        obj
        for name, obj in vars(module).items()
        if name.startswith("test_") and callable(obj)
    ]
    tests.sort(key=lambda fn: fn.__code__.co_firstlineno)
    return tests


def main() -> int:
    print("=== Validazione motore metriche (metrics_engine) ===")
    tests = _collect_tests()
    failures = 0
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            failures += 1
            print(f"[FAIL] {test.__name__}: {exc}")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"[ERROR] {test.__name__}: {exc!r}")
        else:
            print(f"[PASS] {test.__name__}")

    passed = len(tests) - failures
    print(f"\nRiepilogo: {passed}/{len(tests)} test passati, {failures} falliti")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
