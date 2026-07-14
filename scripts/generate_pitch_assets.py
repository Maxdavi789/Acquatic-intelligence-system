"""Rigenera gli asset pitch derivati dalla baseline ufficiale.

Produce:
- docs/pitch/demo_export_csv.png: sola sessione ufficiale validata;
- docs/pitch/demo_sequenza.jpg: 12 frame puliti del video ufficiale, senza il
  frame 100 noto per il tracking degradato.

Gli altri asset (dashboard, onda, frame singolo, architettura) hanno sorgenti
diverse e non vengono toccati da questo script.
"""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import cv2  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

from metrics_engine import FrameAnalysisState, analyze_frame  # noqa: E402
from vision_tracker import (  # noqa: E402
    create_pose_estimator,
    open_video_capture,
    process_pose_frame,
)

PITCH_DIR = PROJECT_ROOT / "docs" / "pitch"
OFFICIAL_VIDEO = PROJECT_ROOT / "test_videos" / "profilo_test.mp4"
EXPORT_ASSET = PITCH_DIR / "demo_export_csv.png"
SEQUENCE_ASSET = PITCH_DIR / "demo_sequenza.jpg"

OFFICIAL_EXPORT_ROW = [
    "2026-07-14T00:18:46",
    "10",
    "93.1",
    "163.17",
    "179.92",
]
EXPORT_COLUMNS = [
    "timestamp",
    "bracciate_totali",
    "fluidity_score",
    "angolo_medio",
    "angolo_max",
]

# Il frame 100 dell'asset storico mostrava un arto disconnesso. Il frame 110
# conserva la copertura temporale senza usare quel campione degradato.
SEQUENCE_FRAME_IDS = (0, 10, 20, 30, 45, 60, 80, 110, 120, 140, 155, 170)
CELL_SIZE = (540, 960)  # width, height; griglia finale 2160x2880.


def generate_export_asset() -> None:
    fig, ax = plt.subplots(figsize=(12.8, 2.8), dpi=140)
    ax.axis("off")
    ax.set_title(
        "Export sessione ufficiale - data/sessions.csv",
        fontsize=17,
        fontweight="bold",
        pad=18,
    )
    table = ax.table(
        cellText=[OFFICIAL_EXPORT_ROW],
        colLabels=EXPORT_COLUMNS,
        cellLoc="center",
        colLoc="center",
        loc="center",
        colWidths=[0.24, 0.20, 0.18, 0.19, 0.19],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.0, 1.8)
    for (row, _column), cell in table.get_celld().items():
        cell.set_edgecolor("#2f3b46")
        if row == 0:
            cell.set_facecolor("#d9e9f5")
            cell.set_text_props(fontweight="bold")
        else:
            cell.set_facecolor("#eaf6ec")
    fig.text(
        0.5,
        0.08,
        "Manuale 10 | Automatico 10 | differenza 0 | Fluidity 93,1",
        ha="center",
        fontsize=12,
        color="#245c35",
        fontweight="bold",
    )
    fig.savefig(EXPORT_ASSET, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def _draw_frame_labels(frame, frame_id: int, angle: float | None) -> None:
    angle_text = "n/d" if angle is None else f"{angle:.1f} deg"
    cv2.putText(
        frame,
        f"Gomito: {angle_text}",
        (12, 28),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.72,
        (0, 0, 0),
        4,
        cv2.LINE_AA,
    )
    cv2.putText(
        frame,
        f"Gomito: {angle_text}",
        (12, 28),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.72,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    cv2.putText(
        frame,
        f"f{frame_id}",
        (12, 78),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.35,
        (0, 0, 0),
        5,
        cv2.LINE_AA,
    )
    cv2.putText(
        frame,
        f"f{frame_id}",
        (12, 78),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.35,
        (0, 230, 255),
        2,
        cv2.LINE_AA,
    )


def generate_sequence_asset() -> None:
    capture = open_video_capture(str(OFFICIAL_VIDEO))
    fps = capture.get(cv2.CAP_PROP_FPS) or 25.0
    wanted = set(SEQUENCE_FRAME_IDS)
    selected: dict[int, object] = {}
    state = FrameAnalysisState()
    frame_id = 0

    try:
        with create_pose_estimator() as pose:
            while frame_id <= max(SEQUENCE_FRAME_IDS):
                ok, frame = capture.read()
                if not ok:
                    break
                annotated, landmarks = process_pose_frame(frame, pose)
                result = analyze_frame(landmarks, frame_id / fps, state)
                if frame_id in wanted:
                    _draw_frame_labels(annotated, frame_id, result["elbow_angle"])
                    selected[frame_id] = cv2.resize(
                        annotated,
                        CELL_SIZE,
                        interpolation=cv2.INTER_AREA,
                    )
                frame_id += 1
    finally:
        capture.release()

    missing = [frame_id for frame_id in SEQUENCE_FRAME_IDS if frame_id not in selected]
    if missing:
        raise RuntimeError(f"Frame mancanti per la sequenza: {missing}")

    rows = []
    for start in range(0, len(SEQUENCE_FRAME_IDS), 4):
        row_frames = [selected[index] for index in SEQUENCE_FRAME_IDS[start : start + 4]]
        rows.append(cv2.hconcat(row_frames))
    contact_sheet = cv2.vconcat(rows)
    if not cv2.imwrite(str(SEQUENCE_ASSET), contact_sheet, [cv2.IMWRITE_JPEG_QUALITY, 92]):
        raise RuntimeError(f"Impossibile scrivere {SEQUENCE_ASSET}")


def main() -> int:
    PITCH_DIR.mkdir(parents=True, exist_ok=True)
    generate_export_asset()
    generate_sequence_asset()
    print(f"Creato: {EXPORT_ASSET.relative_to(PROJECT_ROOT)}")
    print(f"Creato: {SEQUENCE_ASSET.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
