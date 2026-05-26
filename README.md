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

Aggiornato al 2026-05-26.

- FASE 0: in corso.
- FASE 0.1: completata con scaffold iniziale.
- FASE 0.2: bloccata finche' l'ambiente Python locale non viene sistemato.
- FASI 1-4: non iniziate.

## Governance Operativa

- `breakdown_status.md`: stato avanzamento rispetto alla roadmap.
- `prompt_log.md`: log catalogato delle iterazioni e dei messaggi rilevanti.
- `incidents.md`: registro incidenti, blocchi e mitigazioni.
