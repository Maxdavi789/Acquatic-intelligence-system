from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean

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
