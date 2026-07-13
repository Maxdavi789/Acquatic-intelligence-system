from __future__ import annotations

import streamlit as st


st.set_page_config(
    page_title="AI Swimming Motion Analyzer",
    page_icon="🏊",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def main() -> None:
    """Renderizza lo scaffold della dashboard Streamlit (task T15)."""
    st.title("AI Swimming Motion Analyzer")
    st.caption("Proof of Concept locale per l'analisi di movimenti natatori a secco")

    video_column, metrics_column = st.columns([2, 1], gap="large")

    with video_column:
        st.subheader("Video")
        st.info("Il caricamento del file MP4 verrà aggiunto nella task T16.")

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
