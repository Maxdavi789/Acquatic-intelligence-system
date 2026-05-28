# Acquatic Intelligence System

Proof of Concept locale per un AI Swimming Motion Analyzer a secco.

## Obiettivo

Il progetto mira a validare una pipeline offline di Computer Vision per analisi
biomeccanica del gesto natatorio, usando webcam o file MP4 laterali. L'MVP segue
la specifica tecnica e il breakdown operativo forniti nei PDF di progetto.

## Stack Previsto

- Python 3.10+
- OpenCV
- MediaPipe Pose
- Streamlit
- NumPy
- Pandas
- Matplotlib
- CSV locale per export sessioni

## Struttura

```text
.
+-- app.py
+-- vision_tracker.py
+-- metrics_engine.py
+-- requirements.txt
+-- spec.txt
+-- data/
+-- test_videos/
+-- breakdown_status.md
+-- prompt_log.md
+-- incidents.md
```

## Stato

Aggiornato al 2026-05-28.

- FASE 0: completata.
- FASE 1: implementata in `vision_tracker.py`; test reale webcam/MP4 ancora da fare.
- FASE 2: implementata in `metrics_engine.py` con test sintetici.
- FASE 3: prossima, dashboard Streamlit in `app.py`.
- FASE 4: non iniziata.

## Governance Operativa

- `breakdown_status.md`: stato avanzamento rispetto alla roadmap.
- `prompt_log.md`: log catalogato delle iterazioni e dei messaggi rilevanti.
- `incidents.md`: registro incidenti, blocchi e mitigazioni.
