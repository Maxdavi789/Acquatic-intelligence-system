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
    LEFT_ARM_LANDMARK_IDS,
    RIGHT_ARM_LANDMARK_IDS,
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


TESTS = [
    test_select_camera_side_arm_picks_more_visible_side,
    test_select_camera_side_arm_left_side,
    test_select_camera_side_arm_empty_returns_none,
]


def main() -> int:
    failures = 0
    for test in TESTS:
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

    passed = len(TESTS) - failures
    print(f"\n{passed}/{len(TESTS)} test passati")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
