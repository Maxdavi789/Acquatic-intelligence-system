from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

import cv2

PROJECT_ROOT = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(PROJECT_ROOT / ".cache" / "matplotlib"))

import mediapipe as mp


DEFAULT_MAX_WIDTH = 800
DEFAULT_WINDOW_NAME = "AI Swimming Analyzer - Pose Tracking"


def parse_video_source(source: str | int) -> str | int:
    """Converte input CLI in indice webcam o percorso video locale."""
    if isinstance(source, int):
        return source

    value = source.strip()
    if value.isdigit():
        return int(value)

    direct_path = Path(value)
    if direct_path.exists():
        return str(direct_path)

    test_video_path = Path("test_videos") / value
    if test_video_path.exists():
        return str(test_video_path)

    return value


def open_video_capture(source: str | int = 0) -> cv2.VideoCapture:
    """Apre webcam o file video e segnala subito sorgenti non valide."""
    parsed_source = parse_video_source(source)
    capture = cv2.VideoCapture(parsed_source)

    if not capture.isOpened():
        raise RuntimeError(
            "Impossibile aprire la sorgente video. "
            "Usa 0 per la webcam oppure un file MP4 dentro test_videos/."
        )

    return capture


def resize_frame(frame: Any, max_width: int = DEFAULT_MAX_WIDTH) -> Any:
    """Riduce il frame mantenendo proporzioni per alleggerire la CPU."""
    height, width = frame.shape[:2]
    if width <= max_width:
        return frame

    ratio = max_width / width
    new_size = (max_width, int(height * ratio))
    return cv2.resize(frame, new_size, interpolation=cv2.INTER_AREA)


def extract_pose_landmarks(results: Any) -> list[dict[str, float | int]]:
    """Restituisce landmark normalizzati in una forma semplice da riusare."""
    if not results.pose_landmarks:
        return []

    landmarks = []
    for index, landmark in enumerate(results.pose_landmarks.landmark):
        landmarks.append(
            {
                "id": float(index),
                "x": float(landmark.x),
                "y": float(landmark.y),
                "z": float(landmark.z),
                "visibility": float(landmark.visibility),
            }
        )

    return landmarks


def process_pose_frame(
    frame: Any,
    pose: Any,
    draw_overlay: bool = True,
) -> tuple[Any, list[dict[str, float | int]]]:
    """Esegue MediaPipe Pose su un frame BGR e disegna lo scheletro."""
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb_frame.flags.writeable = False
    results = pose.process(rgb_frame)
    rgb_frame.flags.writeable = True

    landmarks = extract_pose_landmarks(results)

    if draw_overlay and results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
        )

    return frame, landmarks


def run_pose_tracking(
    source: str | int = 0,
    max_width: int = DEFAULT_MAX_WIDTH,
    window_name: str = DEFAULT_WINDOW_NAME,
) -> None:
    """Avvia il loop OpenCV + MediaPipe e chiude tutto premendo q."""
    mp_pose = mp.solutions.pose
    capture = open_video_capture(source)

    try:
        with mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            enable_segmentation=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        ) as pose:
            while True:
                ok, frame = capture.read()
                if not ok:
                    break

                frame = resize_frame(frame, max_width=max_width)
                annotated_frame, _landmarks = process_pose_frame(frame, pose)

                cv2.imshow(window_name, annotated_frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        capture.release()
        cv2.destroyAllWindows()


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Esegue ingestione video e pose tracking per AI Swimming Analyzer."
    )
    parser.add_argument(
        "--source",
        default="0",
        help="Indice webcam, percorso MP4, o nome file dentro test_videos/.",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=DEFAULT_MAX_WIDTH,
        help="Larghezza massima del frame visualizzato.",
    )
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    run_pose_tracking(source=args.source, max_width=args.max_width)


if __name__ == "__main__":
    main()
