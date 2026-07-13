from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean
from typing import Any

import numpy as np


Point2D = tuple[float, float] | list[float]


def calculate_elbow_angle(shoulder: Point2D, elbow: Point2D, wrist: Point2D) -> float:
    """Calcola l'angolo interno del gomito in gradi tra 0 e 180."""
    a = np.array(shoulder, dtype=float)
    b = np.array(elbow, dtype=float)
    c = np.array(wrist, dtype=float)

    # I due vettori partono dal gomito, che e' il vertice dell'angolo.
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(
        a[1] - b[1],
        a[0] - b[0],
    )
    angle = abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360.0 - angle

    return float(angle)


# Indici MediaPipe Pose per gli arti (spalla, gomito, polso).
LEFT_ARM_LANDMARK_IDS = (11, 13, 15)   # lato sinistro
RIGHT_ARM_LANDMARK_IDS = (12, 14, 16)  # lato destro


def _landmark_field(landmark: Any, field_name: str) -> float:
    """Legge un campo (x/y/visibility) da un landmark dict o oggetto."""
    if isinstance(landmark, dict):
        return float(landmark[field_name])
    return float(getattr(landmark, field_name))


def select_camera_side_arm(landmarks: Any) -> dict | None:
    """Seleziona l'arto lato-camera (visibility media piu' alta) e ne restituisce
    spalla, gomito e polso come punti (x, y).

    landmarks: sequenza indicizzabile dei 33 landmark MediaPipe, dove ogni
    elemento e' un dict con chiavi 'x','y','visibility' (come prodotto da
    vision_tracker.extract_pose_landmarks) oppure un oggetto con gli stessi
    attributi.

    Coerente con la vista laterale (spec sez. 9.3, RF-004): tra arto sinistro
    (11/13/15) e destro (12/14/16) sceglie quello con visibility media piu' alta.

    Ritorna un dict con: arm_side ('left'/'right'), shoulder, elbow, wrist come
    tuple (x, y), mean_visibility (usata per la scelta del lato) e min_visibility
    (usata dalla logica forward-fill in T08). Ritorna None se i landmark non sono
    disponibili o insufficienti.
    """
    if not landmarks or len(landmarks) <= max(RIGHT_ARM_LANDMARK_IDS):
        return None

    def side_stats(ids: tuple[int, int, int]) -> tuple[float, float]:
        vis = [_landmark_field(landmarks[i], "visibility") for i in ids]
        return sum(vis) / len(vis), min(vis)

    left_mean, left_min = side_stats(LEFT_ARM_LANDMARK_IDS)
    right_mean, right_min = side_stats(RIGHT_ARM_LANDMARK_IDS)

    if right_mean > left_mean:
        side, ids, mean_vis, min_vis = "right", RIGHT_ARM_LANDMARK_IDS, right_mean, right_min
    else:
        side, ids, mean_vis, min_vis = "left", LEFT_ARM_LANDMARK_IDS, left_mean, left_min

    shoulder_id, elbow_id, wrist_id = ids
    return {
        "arm_side": side,
        "shoulder": (
            _landmark_field(landmarks[shoulder_id], "x"),
            _landmark_field(landmarks[shoulder_id], "y"),
        ),
        "elbow": (
            _landmark_field(landmarks[elbow_id], "x"),
            _landmark_field(landmarks[elbow_id], "y"),
        ),
        "wrist": (
            _landmark_field(landmarks[wrist_id], "x"),
            _landmark_field(landmarks[wrist_id], "y"),
        ),
        "mean_visibility": mean_vis,
        "min_visibility": min_vis,
    }


@dataclass
class ElbowAngleSmoother:
    """Calcola l'angolo del gomito con forward-fill sulle occlusioni.

    Se la visibility dei landmark scelti scende sotto la soglia, mantiene
    l'ultimo angolo valido invece di ricalcolare su coordinate inaffidabili,
    evitando picchi spuri e crash (spec sez. 9.3, RF-008, MVP-006).
    """

    visibility_threshold: float = 0.5
    _last_angle: float | None = None

    def update(
        self,
        shoulder: Point2D,
        elbow: Point2D,
        wrist: Point2D,
        min_visibility: float,
    ) -> float | None:
        """Aggiorna con un frame e restituisce l'angolo (o l'ultimo valido).

        Se min_visibility < soglia -> forward-fill dell'ultimo angolo valido
        (None finche' non se ne e' calcolato almeno uno affidabile).
        """
        if min_visibility < self.visibility_threshold:
            return self._last_angle

        self._last_angle = calculate_elbow_angle(shoulder, elbow, wrist)
        return self._last_angle

    @property
    def last_angle(self) -> float | None:
        return self._last_angle


def calculate_fluidity_score(peak_timestamps: list[float]) -> float:
    """Stima la regolarita' del ritmo dalle distanze temporali tra picchi."""
    if len(peak_timestamps) < 3:
        return 0.0

    intervals = np.diff(np.array(peak_timestamps, dtype=float))
    standard_deviation = float(np.std(intervals))
    return max(0.0, 100.0 - (standard_deviation * 50.0))


# FUORI MVP v1 - vedi spec sez. 4.2: il Symmetry Score bilaterale contraddice la
# vista laterale (l'arto lontano e' strutturalmente occluso), quindi e' escluso
# dalla pipeline e dai KPI dell'MVP. Funzione conservata come AIRBAG, NON
# invocata da alcun modulo. Riattivabile in v2 con cambio di protocollo di
# ripresa (frontale/45 gradi) o misura in due passaggi. Vedi decisione DA-01 = A
# e breakdown task T05.
def calculate_symmetry_score(right_angles: list[float], left_angles: list[float]) -> float:
    """Confronta le medie degli angoli massimi destro/sinistro.

    FUORI MVP v1 (airbag): non collegata alla pipeline, conservata per una
    futura v2. Vedi il commento sopra e spec sez. 4.2 / DA-01 = A.
    """
    if not right_angles or not left_angles:
        return 0.0

    right_mean = mean(right_angles)
    left_mean = mean(left_angles)
    largest = max(right_mean, left_mean)

    if largest <= 0:
        return 0.0

    return (min(right_mean, left_mean) / largest) * 100.0


@dataclass
class StrokeCounter:
    """Conteggia bracciate rilevando picchi nella coordinata Y del polso."""

    debounce_seconds: float = 0.6
    min_delta: float = 0.003
    peak_timestamps: list[float] = field(default_factory=list)
    stroke_count: int = 0
    _last_y: float | None = None
    _last_direction: int = 0
    _last_peak_time: float | None = None

    def update(
        self,
        wrist_y: float,
        timestamp: float,
        shoulder_y: float | None = None,
    ) -> dict[str, float | int | bool]:
        """Aggiorna lo stato con un nuovo frame e restituisce metriche correnti.

        MediaPipe usa coordinate normalizzate con asse Y crescente verso il
        basso. Un picco alto del polso e' quindi un minimo locale di Y.
        """
        current_y = float(wrist_y)
        peak_detected = False

        if self._last_y is None:
            self._last_y = current_y
            return self.snapshot(peak_detected=False)

        delta = current_y - self._last_y
        direction = self._direction_from_delta(delta)

        if direction != 0:
            peak_detected = self._is_valid_peak(
                peak_y=self._last_y,
                direction=direction,
                timestamp=timestamp,
                shoulder_y=shoulder_y,
            )
            self._last_direction = direction

        self._last_y = current_y
        return self.snapshot(peak_detected=peak_detected)

    def snapshot(self, peak_detected: bool = False) -> dict[str, float | int | bool]:
        return {
            "stroke_count": self.stroke_count,
            "fluidity_score": calculate_fluidity_score(self.peak_timestamps),
            "peak_detected": peak_detected,
        }

    def _direction_from_delta(self, delta: float) -> int:
        if abs(delta) < self.min_delta:
            return 0
        return 1 if delta > 0 else -1

    def _is_valid_peak(
        self,
        peak_y: float,
        direction: int,
        timestamp: float,
        shoulder_y: float | None,
    ) -> bool:
        changed_from_up_to_down = self._last_direction == -1 and direction == 1
        if not changed_from_up_to_down:
            return False

        if shoulder_y is not None and peak_y > shoulder_y:
            return False

        if self._last_peak_time is not None:
            elapsed = timestamp - self._last_peak_time
            if elapsed < self.debounce_seconds:
                return False

        self.stroke_count += 1
        self._last_peak_time = timestamp
        self.peak_timestamps.append(timestamp)
        return True
