from __future__ import annotations

from pathlib import Path
from typing import Any

import cv2
import pandas as pd
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
CHART_UPDATE_EVERY = 10  # frame tra due aggiornamenti del grafico (T20)
WRIST_CHART_COLUMNS = ("tempo (s)", "polso Y")
SESSION_CSV_COLUMNS = (
    "timestamp",
    "bracciate_totali",
    "fluidity_score",
    "angolo_medio",
    "angolo_max",
)

PROJECT_ROOT = Path(__file__).resolve().parent
UPLOAD_CACHE_DIR = PROJECT_ROOT / ".cache"
UPLOADED_VIDEO_PATH = UPLOAD_CACHE_DIR / "uploaded_session.mp4"
SESSIONS_CSV_PATH = PROJECT_ROOT / "data" / "sessions.csv"

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


def _update_wrist_chart(chart_slot: Any, wrist_series: list[dict[str, float]]) -> None:
    """Aggiorna il grafico dell'onda Y del polso (T20, RF-010)."""
    frame_data = pd.DataFrame(wrist_series, columns=list(WRIST_CHART_COLUMNS))
    chart_slot.line_chart(
        frame_data,
        x=WRIST_CHART_COLUMNS[0],
        y=WRIST_CHART_COLUMNS[1],
        height=260,
    )


def render_video_stream(
    source: str | int,
    placeholder: Any,
    chart_slot: Any = None,
    stroke_slot: Any = None,
    fluidity_slot: Any = None,
) -> dict[str, Any]:
    """Loop di rendering delle task T17/T18/T20/T21.

    Legge i frame dalla sorgente, esegue MediaPipe Pose con overlay scheletro
    (riuso delle funzioni di `vision_tracker`) e aggiorna il placeholder
    Streamlit: e' il sostituto di `cv2.imshow`, non utilizzabile qui (spec
    sez. 14.2). Ogni frame passa da `analyze_frame` (stato persistente T13);
    l'angolo del gomito viene sovrimpresso live (T18), l'onda Y del polso
    popola il grafico (T20) e i KPI vengono aggiornati con i valori reali sul
    picco rilevato e periodicamente (T21). Le risorse vengono sempre
    rilasciate a fine stream (RF-013).

    Restituisce il riepilogo della sessione di elaborazione:
    `frames_rendered`, `stroke_count`, `fluidity_score`, `wrist_series`,
    `elbow_angle_mean`, `elbow_angle_max` (angoli per l'export T23, RF-011).
    """
    capture = open_video_capture(source)
    frames_rendered = 0

    fps = capture.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 0:
        fps = FALLBACK_FPS

    state = FrameAnalysisState()
    wrist_series: list[dict[str, float]] = []
    elbow_angles: list[float] = []
    result: dict[str, Any] = {}

    def update_kpis() -> None:
        if stroke_slot is not None and fluidity_slot is not None and result:
            render_kpis(
                stroke_slot,
                fluidity_slot,
                result["stroke_count"],
                result["fluidity_score"],
            )

    try:
        with create_pose_estimator() as pose:
            while True:
                ok, frame = capture.read()
                if not ok:
                    break

                frame = resize_frame(frame)
                annotated_frame, landmarks = process_pose_frame(frame, pose)

                timestamp = frames_rendered / fps
                result = analyze_frame(landmarks, timestamp, state)
                draw_elbow_angle(annotated_frame, result["elbow_angle"])

                if result["elbow_angle"] is not None:
                    elbow_angles.append(float(result["elbow_angle"]))
                if result["wrist_y"] is not None:
                    wrist_series.append(
                        {
                            WRIST_CHART_COLUMNS[0]: round(timestamp, 3),
                            WRIST_CHART_COLUMNS[1]: result["wrist_y"],
                        }
                    )

                periodic_update = frames_rendered % CHART_UPDATE_EVERY == 0
                if chart_slot is not None and wrist_series and periodic_update:
                    _update_wrist_chart(chart_slot, wrist_series)
                if result["peak_detected"] or periodic_update:
                    update_kpis()

                placeholder.image(
                    cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB),
                    channels="RGB",
                    use_container_width=True,
                )
                frames_rendered += 1
    finally:
        capture.release()

    if chart_slot is not None and wrist_series:
        _update_wrist_chart(chart_slot, wrist_series)
    update_kpis()

    return {
        "frames_rendered": frames_rendered,
        "stroke_count": result.get("stroke_count", 0) if result else 0,
        "fluidity_score": result.get("fluidity_score", 0.0) if result else 0.0,
        "wrist_series": wrist_series,
        "elbow_angle_mean": (
            sum(elbow_angles) / len(elbow_angles) if elbow_angles else 0.0
        ),
        "elbow_angle_max": max(elbow_angles) if elbow_angles else 0.0,
    }


def build_session_dataframe(summary: dict[str, Any]) -> pd.DataFrame:
    """Aggrega le metriche finali di sessione in un DataFrame (T23, RF-011).

    Una riga per sessione: data/ora dell'export (ISO), bracciate totali,
    Fluidity Score, angolo del gomito medio e massimo. Solo metriche
    aggregate anonime: nessun frame o dato grezzo (spec sez. 8.3, 10.1).
    """
    row = {
        "timestamp": pd.Timestamp.now().isoformat(timespec="seconds"),
        "bracciate_totali": int(summary["stroke_count"]),
        "fluidity_score": round(float(summary["fluidity_score"]), 1),
        "angolo_medio": round(float(summary["elbow_angle_mean"]), 2),
        "angolo_max": round(float(summary["elbow_angle_max"]), 2),
    }
    return pd.DataFrame([row], columns=list(SESSION_CSV_COLUMNS))


def append_session_to_csv(
    session_df: pd.DataFrame,
    csv_path: Path = SESSIONS_CSV_PATH,
) -> Path:
    """Accoda la sessione a `data/sessions.csv` (T24, RF-011).

    Crea cartella e header alla prima scrittura; le righe precedenti non
    vengono mai sovrascritte (append). Nel CSV finiscono solo metriche
    aggregate anonime con timestamp (spec sez. 8.3).
    """
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not csv_path.exists()
    session_df.to_csv(csv_path, mode="a", header=write_header, index=False)
    return csv_path


def render_export_section() -> None:
    """Fine sessione: aggrega le metriche (T23) ed esporta su CSV (T24)."""
    if "last_summary" not in st.session_state:
        return

    if st.button("Termina Sessione ed Esporta Dati"):
        session_df = build_session_dataframe(st.session_state["last_summary"])
        st.dataframe(session_df, hide_index=True)
        csv_path = append_session_to_csv(session_df)
        st.success(f"Sessione esportata in data/{csv_path.name} (append).")


def render_kpis(
    stroke_slot: Any,
    fluidity_slot: Any,
    stroke_count: int,
    fluidity_score: float,
) -> None:
    """KPI della task T19 (MVP-004/005, RF-006/007).

    Due soli blocchi: bracciate totali e Fluidity Score. Nessun KPI di
    simmetria: fuori scope MVP (spec sez. 4.2, DA-01 = A).
    """
    stroke_slot.metric("Bracciate totali", int(stroke_count))
    fluidity_slot.metric("Fluidity Score", f"{fluidity_score:.1f}")


def render_video_section(
    chart_slot: Any = None,
    stroke_slot: Any = None,
    fluidity_slot: Any = None,
) -> None:
    """Colonna video: selettore input (T16) + rendering annotato (T17/T18)."""
    render_input_selector()
    source = st.session_state.get("video_source")

    if isinstance(source, str):
        if st.button("Avvia elaborazione video", type="primary"):
            placeholder = st.empty()
            summary = render_video_stream(
                source, placeholder, chart_slot, stroke_slot, fluidity_slot
            )
            # T22: i risultati sopravvivono ai rerun di Streamlit (interazioni
            # con i widget) finche' non parte una nuova elaborazione.
            st.session_state["last_kpi"] = {
                "stroke_count": summary["stroke_count"],
                "fluidity_score": summary["fluidity_score"],
            }
            st.session_state["wrist_series"] = summary["wrist_series"]
            st.session_state["last_summary"] = {
                key: summary[key]
                for key in (
                    "frames_rendered",
                    "stroke_count",
                    "fluidity_score",
                    "elbow_angle_mean",
                    "elbow_angle_max",
                )
            }
            st.caption(
                f"Elaborazione terminata: {summary['frames_rendered']} frame "
                "renderizzati."
            )
    elif source == WEBCAM_DEVICE_INDEX:
        st.info(
            "L'elaborazione live della webcam verrà collegata nella task T28 "
            "(percorso best-effort)."
        )


def main() -> None:
    """Renderizza la dashboard.

    Layout a due colonne (T15), selettore input (T16), rendering video
    annotato con angolo live (T17/T18), KPI e grafico onda Y collegati ai
    dati reali (T19-T21), persistenza dei risultati tra i rerun (T22).
    """
    st.title("AI Swimming Motion Analyzer")
    st.caption("Proof of Concept locale per l'analisi di movimenti natatori a secco")

    video_column, metrics_column = st.columns([2, 1], gap="large")

    # La colonna metriche viene costruita per prima cosi' che i suoi slot
    # esistano gia' quando il loop di elaborazione (colonna video) li aggiorna.
    with metrics_column:
        st.subheader("Metriche")
        stroke_slot = st.empty()
        fluidity_slot = st.empty()
        chart_slot = st.empty()
        last_kpi = st.session_state.get(
            "last_kpi", {"stroke_count": 0, "fluidity_score": 0.0}
        )
        render_kpis(
            stroke_slot,
            fluidity_slot,
            last_kpi["stroke_count"],
            last_kpi["fluidity_score"],
        )
        persisted_series = st.session_state.get("wrist_series", [])
        if persisted_series:
            _update_wrist_chart(chart_slot, persisted_series)
        else:
            chart_slot.caption(
                "Il grafico dell'onda Y del polso si popola durante l'elaborazione."
            )
        render_export_section()

    with video_column:
        st.subheader("Video")
        render_video_section(chart_slot, stroke_slot, fluidity_slot)

    st.divider()
    st.caption(
        "Questo PoC valida la pipeline software: non è un dispositivo medico "
        "e non fornisce consigli clinici o di prevenzione degli infortuni."
    )


if __name__ == "__main__":
    main()
