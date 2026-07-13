from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit as st

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


def main() -> None:
    """Renderizza la dashboard: layout T15 + selettore input T16."""
    st.title("AI Swimming Motion Analyzer")
    st.caption("Proof of Concept locale per l'analisi di movimenti natatori a secco")

    video_column, metrics_column = st.columns([2, 1], gap="large")

    with video_column:
        st.subheader("Video")
        render_input_selector()

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
