# Acquatic Intelligence System

Proof of Concept locale per un AI Swimming Motion Analyzer a secco.

## Obiettivo

Il progetto valida a costo zero una pipeline offline di Computer Vision che
analizza un video laterale di movimenti natatori simulati a secco. MediaPipe
fornisce i landmark corporei; il motore deterministico calcola angolo del
gomito, conteggio delle bracciate e regolarita' del ritmo.

Il PoC dimostra la fattibilita' software e algoritmica. Non dimostra validita'
biomeccanica in acqua e non equivale a un sistema professionale da laboratorio.
La specifica di riferimento e' [`spec.txt`](spec.txt), versione 1.1 congelata.

## Input e output MVP

- Input primario: file MP4 laterale (profilo 90 gradi).
- Input secondario: webcam, modalita' sperimentale/best-effort.
- Output previsto: video annotato, angolo gomito live, bracciate totali,
  Fluidity Score, grafico Y del polso ed export CSV della sessione.
- Esecuzione: interamente locale, senza API o servizi a pagamento.

## Stack

- Python 3.11 come riferimento di specifica; ambiente locale validato anche con
  Python 3.12.10.
- OpenCV.
- MediaPipe Pose legacy, pinnato a `mediapipe==0.10.35`.
- Streamlit.
- NumPy e Pandas.
- CSV locale per l'export delle sessioni.

`matplotlib` non e' una dipendenza diretta del progetto: viene installato
transitivamente da MediaPipe. I grafici della dashboard useranno
`st.line_chart`.

## Stato

Aggiornato al 2026-07-13.

- M0/T01-T06: 5 task su 6 completate; T03 resta bloccata finche' non e'
  disponibile un MP4 laterale provvisorio per il test reale.
- M1/T07-T12: completata; suite sintetica corrente 19/19 verde, inclusa la
  regressione sul gate spalla stretto di T10.
- M2: T13 completata (`FrameAnalysisState` + `analyze_frame`); T14 dipende dal
  video di T03 ed e' bloccata.
- M3-M8: non iniziate.

La prossima task in ordine e' T14 (bloccata); la prossima eseguibile senza video
e' T15, scaffold della dashboard Streamlit.

Lo stato task per task e' in [`breakdown_status.md`](breakdown_status.md).

## Avvio e validazione

```powershell
.\venv\Scripts\python.exe scripts\test_metrics.py
.\venv\Scripts\python.exe vision_tracker.py --source <clip>.mp4
```

La dashboard sara' avviabile con `streamlit run app.py` dopo il completamento
del modulo M3.

## Struttura principale

```text
.
+-- app.py
+-- vision_tracker.py
+-- metrics_engine.py
+-- scripts/test_metrics.py
+-- requirements.txt
+-- spec.txt
+-- SPEC_ERRATA.md
+-- data/
+-- test_videos/
+-- breakdown_status.md
+-- prompt_log.md
+-- incidents.md
+-- HANDOFF.md
```

## Privacy e disclaimer

I frame e i video non vengono persistiti dall'MVP; vengono salvate solo
metriche aggregate nel CSV locale. Eventuali persone riprese devono essere
consenzienti e i video di terzi richiedono una licenza/base d'uso adeguata.

**Questo progetto non e' un dispositivo medico e non fornisce consigli clinici
o di prevenzione degli infortuni.**

## Governance operativa

- `breakdown_status.md`: avanzamento rispetto alle task T01-T41.
- `prompt_log.md`: iterazioni, richieste, azioni ed esiti.
- `incidents.md`: incidenti reali, impatto, mitigazioni e stato.
- `SPEC_ERRATA.md`: modifiche successive al congelamento della specifica.

Questo e' un aggiornamento intermedio di coerenza. La revisione conclusiva del
README resta prevista nel task T37, dopo la validazione end-to-end.
