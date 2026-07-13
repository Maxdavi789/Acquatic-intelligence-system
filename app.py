from __future__ import annotations

from pathlib import Path
from typing import Any

import cv2
import streamlit as st

# vision_tracker configura MPLCONFIGDIR prima di importare mediapipe.
from vision_tracker import (
    create_pose_estimator,
    open_video_capture,
    process_pose_frame,
    resize_frame,
)

from metrics_engine import FrameAnalysisState, analyze_frame

FALLBACK_FPS = 30.0

PROJECT_ROOT = Path(__file__).resolve().parent
UPLOAD_CACHE_DIR = PROJECT_ROOT / ".cache"
UPLOADED_VIDEO_PATH = UPLOAD_CACHE_DIR / "uploaded_session.mp4"

INPUT_MP4 = "File MP4 (primario)"
INPUT_WEBCAM = "Webcam (sperimentale)"
WEBCAM_DEVICE_INDEX = 0


st.set_page_config(
    page_title="AI Swimming Motion Analyzer",
    page_icon="🏊",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def persist_uploaded_video(uploaded_file: Any) -> Path:
    """Scrive l'MP4 caricato in `.cache/` per renderlo leggibile da OpenCV.

    Non è una persistenza di sessione: il file viene sovrascritto a ogni nuovo
    upload, vive in una cartella gitignored e resta fuori da `data/` (spec
    sez. 8.3: il video non viene salvato, si conservano solo metriche).
    """
    UPLOAD_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    UPLOADED_VIDEO_PATH.write_bytes(uploaded_file.getbuffer())
    return UPLOADED_VIDEO_PATH


def render_input_selector() -> None:
    """Selettore sorgente della task T16: MP4 primario, webcam best-effort.

    MP4 è il default (DA-02, MVP-001); la webcam è dichiarata sperimentale
    con avviso esplicito (MVP-009, RF-014). Il percorso selezionato viene
    esposto alla pipeline in `st.session_state["video_source"]`, che il loop
    di elaborazione consumerà dalla task T17.
    """
    source_choice = st.radio(
        "Sorgente video",
        options=(INPUT_MP4, INPUT_WEBCAM),
        index=0,
        horizontal=True,
    )

    if source_choice == INPUT_MP4:
        uploaded_file = st.file_uploader(
            "Carica un video laterale (profilo 90 gradi)",
            type=["mp4"],
            accept_multiple_files=False,
        )
        if uploaded_file is not None:
            video_path = persist_uploaded_video(uploaded_file)
            st.session_state["video_source"] = str(video_path)
            size_mb = uploaded_file.size / (1024 * 1024)
            st.success(
                f"File pronto per l'analisi: {uploaded_file.name} ({size_mb:.1f} MB)"
            )
        else:
            st.session_state.pop("video_source", None)
            st.info("Carica un file MP4: il rendering verrà collegato nella task T17.")
    else:
        st.session_state["video_source"] = WEBCAM_DEVICE_INDEX
        st.warning(
            "Modalità webcam SPERIMENTALE (best-effort): il rendering real-time "
            "in Streamlit può essere instabile. Il percorso primario resta il "
            "file MP4."
        )


def draw_elbow_angle(frame: Any, angle: float | None) -> Any:
    """Disegna l'angolo del gomito sul frame (task T18, RF-005).

    Testo bianco con bordo nero per restare leggibile su sfondi chiari e
    scuri. I font Hershey di OpenCV non rendono i caratteri non ASCII,
    quindi si usa "deg" al posto del simbolo dei gradi.
    """
    label = "Gomito: n/d" if angle is None else f"Gomito: {angle:5.1f} deg"
    position = (12, 34)
    cv2.putText(
        frame, label, position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 4, cv2.LINE_AA
    )
    cv2.putText(
        frame, label, position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA
    )
    return frame


def render_video_stream(source: str | int, placeholder: Any) -> int:
    """Loop di rendering delle task T17/T18 (RF-003, RF-005).

    Legge i frame dalla sorgente, esegue MediaPipe Pose con overlay scheletro
    (riuso delle funzioni di `vision_tracker`) e aggiorna il placeholder
    Streamlit: e' il sostituto di `cv2.imshow`, non utilizzabile qui (spec
    sez. 14.2). Ogni frame passa da `analyze_frame` (stato persistente T13) e
    l'angolo del gomito viene sovrimpresso live (T18). Restituisce il numero
    di frame renderizzati; le risorse vengono sempre rilasciate a fine stream
    (RF-013).
    """
    capture = open_video_capture(source)
    frames_rendered = 0

    fps = capture.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 0:
        fps = FALLBACK_FPS

    state = FrameAnalysisState()

    try:
        with create_pose_estimator() as pose:
            while True:
                ok, frame = capture.read()
                if not ok:
                    break

                frame = resize_frame(frame)
                annotated_frame, landmarks = process_pose_frame(frame, pose)

                result = analyze_frame(landmarks, frames_rendered / fps, state)
                draw_elbow_angle(annotated_frame, result["elbow_angle"])

                placeholder.image(
                    cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB),
                    channels="RGB",
                    use_container_width=True,
                )
                frames_rendered += 1
    finally:
        capture.release()

    return frames_rendered


def render_video_section() -> None:
    """Colonna video: selettore input (T16) + rendering annotato (T17)."""
    render_input_selector()
    source = st.session_state.get("video_source")

    if isinstance(source, str):
        if st.button("Avvia elaborazione video", type="primary"):
            placeholder = st.empty()
            frames_rendered = render_video_stream(source, placeholder)
            st.caption(f"Elaborazione terminata: {frames_rendered} frame renderizzati.")
    elif source == WEBCAM_DEVICE_INDEX:
        st.info(
            "L'elaborazione live della webcam verrà collegata nella task T28 "
            "(percorso best-effort)."
        )


def main() -> None:
    """Renderizza la dashboard: layout T15 + input T16 + rendering video T17."""
    st.title("AI Swimming Motion Analyzer")
    st.caption("Proof of Concept locale per l'analisi di movimenti natatori a secco")

    video_column, metrics_column = st.columns([2, 1], gap="large")

    with video_column:
        st.subheader("Video")
        render_video_section()

    with metrics_column:
        st.subheader("Metriche")
        st.info("KPI e grafico verranno collegati nelle task T19-T21.")

    st.divider()
    st.caption(
        "Questo PoC valida la pipeline software: non è un dispositivo medico "
        "e non fornisce consigli clinici o di prevenzione degli infortuni."
    )


if __name__ == "__main__":
    main()
