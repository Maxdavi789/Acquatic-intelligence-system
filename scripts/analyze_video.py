"""Validazione CLI della pipeline metriche su un video reale (task T14).

Collega l'output reale di ``vision_tracker.extract_pose_landmarks`` (via
``process_pose_frame``) al motore deterministico ``metrics_engine.analyze_frame``
e stampa in console angolo del gomito e conteggio bracciate mentre il video
scorre (spec sez. 5.1, RF-004/005/006).

Esecuzione headless: nessuna finestra video, solo output testuale. Il rendering
UI appartiene alla dashboard Streamlit (task T17+).

Uso:
    python scripts/analyze_video.py [--source PATH] [--print-every N]

Exit code 0 se il video viene processato fino in fondo, 1 su sorgente non
valida (messaggio leggibile, nessun traceback: RF-001).
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Permette di importare i moduli dalla root del progetto.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import cv2  # noqa: E402

# vision_tracker configura MPLCONFIGDIR prima di importare mediapipe.
from vision_tracker import (  # noqa: E402
    DEFAULT_MAX_WIDTH,
    create_pose_estimator,
    open_video_capture,
    process_pose_frame,
    resize_frame,
)

from metrics_engine import FrameAnalysisState, analyze_frame  # noqa: E402


DEFAULT_SOURCE = PROJECT_ROOT / "test_videos" / "profilo_provvisorio.mp4"
FALLBACK_FPS = 30.0


def _format_angle(angle: float | None) -> str:
    return "n/d" if angle is None else f"{angle:6.2f}"


def analyze_video(
    source: str,
    max_width: int = DEFAULT_MAX_WIDTH,
    print_every: int = 15,
) -> dict[str, float | int]:
    """Processa l'intero video e restituisce le metriche aggregate finali."""
    capture = open_video_capture(source)

    fps = capture.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 0:
        fps = FALLBACK_FPS

    state = FrameAnalysisState()
    frame_index = 0
    frames_with_pose = 0
    min_angle: float | None = None
    max_angle: float | None = None
    result: dict = {}

    try:
        with create_pose_estimator() as pose:
            while True:
                ok, frame = capture.read()
                if not ok:
                    break

                frame = resize_frame(frame, max_width=max_width)
                # L'overlay non serve in modalita' console: si salta il disegno.
                _frame, landmarks = process_pose_frame(frame, pose, draw_overlay=False)

                timestamp = frame_index / fps
                result = analyze_frame(landmarks, timestamp, state)

                if landmarks:
                    frames_with_pose += 1

                angle = result["elbow_angle"]
                if angle is not None:
                    min_angle = angle if min_angle is None else min(min_angle, angle)
                    max_angle = angle if max_angle is None else max(max_angle, angle)

                if result["peak_detected"] or frame_index % print_every == 0:
                    peak_marker = "  <-- PICCO (bracciata)" if result["peak_detected"] else ""
                    print(
                        f"frame {frame_index:4d}  t={timestamp:6.2f}s  "
                        f"arto={result['arm_side'] or 'n/d':5s}  "
                        f"angolo={_format_angle(angle)}  "
                        f"bracciate={result['stroke_count']}"
                        f"{peak_marker}"
                    )

                frame_index += 1
    finally:
        capture.release()

    return {
        "frames": frame_index,
        "frames_with_pose": frames_with_pose,
        "fps": fps,
        "min_angle": min_angle,
        "max_angle": max_angle,
        "stroke_count": result.get("stroke_count", 0) if result else 0,
        "fluidity_score": result.get("fluidity_score", 0.0) if result else 0.0,
    }


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Valida la pipeline landmark reali -> analyze_frame su un MP4, "
            "stampando angolo gomito e conteggio bracciate in console."
        )
    )
    parser.add_argument(
        "--source",
        default=str(DEFAULT_SOURCE),
        help="Percorso MP4 (default: test_videos/profilo_provvisorio.mp4).",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=DEFAULT_MAX_WIDTH,
        help="Larghezza massima del frame elaborato.",
    )
    parser.add_argument(
        "--print-every",
        type=int,
        default=15,
        help="Stampa una riga ogni N frame (i picchi vengono sempre stampati).",
    )
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()

    try:
        summary = analyze_video(
            source=args.source,
            max_width=args.max_width,
            print_every=max(1, args.print_every),
        )
    except RuntimeError as error:
        print(f"ERRORE: {error}")
        return 1

    print("\n=== Riepilogo T14 ===")
    print(f"Frame totali:        {summary['frames']} (fps sorgente: {summary['fps']:.2f})")
    print(f"Frame con posa:      {summary['frames_with_pose']}")
    print(
        "Angolo gomito:       "
        f"min {_format_angle(summary['min_angle'])} / max {_format_angle(summary['max_angle'])}"
    )
    print(f"Bracciate totali:    {summary['stroke_count']}")
    print(f"Fluidity Score:      {summary['fluidity_score']:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
