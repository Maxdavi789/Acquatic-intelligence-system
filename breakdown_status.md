# Breakdown Status

Data aggiornamento: 2026-07-13

## Stato Generale

Repository: `https://github.com/Maxdavi789/Acquatic-intelligence-system.git`,
branch `main`, locale AVANTI di 6 commit rispetto a `origin/main` (push non
ancora eseguito, in attesa di OK utente).

Questo file e' allineato al documento `breakdown_tasks_v1` (task T01-T41) e alla
specifica congelata v1.1. La root della repo resta la root logica del progetto.

> Correzione storica: la versione 2026-05-28 di questo status indicava come
> prossima task "FASE 3 dashboard con KPI Simmetria". Indicazione SUPERATA:
> nella spec v1.1 il Symmetry Score e' fuori scope MVP (DA-01 = A). Dettagli in
> `incidents.md` (INC-2026-07-13-003) e `SPEC_ERRATA.md`.

## Stato base esistente

| Elemento | Stato | Note |
| --- | --- | --- |
| FASE 0 - scaffold e ambiente | Completata | File progetto e struttura presenti; venv 3.12 ricreato in questo percorso. |
| FASE 1 - `vision_tracker.py` | Implementata | Webcam/MP4, resize, MediaPipe Pose, overlay. Test reale ancora da fare (T03). |
| FASE 2 - `metrics_engine.py` | Implementata + allineata | Angolo gomito, StrokeCounter, Fluidity. Symmetry ora airbag (T05). Mancano ancora selezione arto lato-camera, forward-fill, `analyze_frame` e i test (M1/M2). |
| FASE 3 - `app.py` | Non iniziata | File vuoto (M3). |
| FASE 4 - persistenza/robustezza/demo | Non iniziata | Dipende da M2-M3. |

## Avanzamento per modulo (nuovo breakdown)

| Modulo | Descrizione | Task | Stato |
| --- | --- | --- | --- |
| M0 | Allineamento base esistente -> spec v1.1 | T01-T06 | Completata (T03 bloccata) |
| M1 | Hardening motore metriche | T07-T12 | Prossima |
| M2 | Step di analisi per-frame (glue) | T13-T14 | Da iniziare |
| M3 | Dashboard Streamlit `app.py` | T15-T22 | Da iniziare |
| M4 | Persistenza CSV | T23-T25 | Da iniziare |
| M5 | Robustezza e gestione errori | T26-T29 | Da iniziare |
| M6 | Test e validazione | T30-T33 | Da iniziare |
| M7 | Sandbox demo controllato | T34-T36 | Da iniziare |
| M8 | Demo, pitch e chiusura governance | T37-T41 | Da iniziare |

## Dettaglio M0

| Task | Descrizione | Stato | Note |
| --- | --- | --- | --- |
| T01 | Congelare spec e sostituire `spec.txt` con v1.1 | Completata | spec.txt = v1.1 ASCII, stato CONGELATA (commit ca30745). |
| T02 | Pin versione MediaPipe (DA-06) | Completata | `mediapipe==0.10.35` pinnato; import OK su venv 3.12 (commit 4c9e0bf). |
| T03 | Test reale FASE 1 su MP4 provvisorio + webcam | Bloccata | venv pronto; manca un MP4 laterale provvisorio in `test_videos/`. |
| T04 | Decisione `matplotlib` (DA-07) | Completata | Rimosso da requirements; resta transitivo via mediapipe (commit 61a96ea). |
| T05 | Demossione Symmetry Score ad airbag (DA-01=A) | Completata | `calculate_symmetry_score` marcata airbag, 0 chiamate attive (commit a7d399a). |
| T06 | Aggiornare governance con la nuova baseline | Completata | Baseline registrata in prompt_log/incidents/questo file. |

## Governance

- Step 0 (scaffolding): creato `SPEC_ERRATA.md`; aggiornati `prompt_log.md`,
  `incidents.md` e questo file; riallineamento a T01-T41 (commit 05f13d7).
- Ambiente: creato `venv` (Python 3.12), dipendenze installate; mediapipe
  0.10.35 importa senza fallback a 3.11.
- Commit locali per task (prefisso task ID). Push su `origin` solo dopo OK
  esplicito dell'utente.

## Prossima Task

M1 / T07 - selezione arto lato-camera in `metrics_engine.py` (hardening motore
metriche, non richiede video reale). In alternativa, appena disponibile un MP4
laterale provvisorio, sbloccare T03 (test reale FASE 1).

## Task Arretrate o Bloccate

- T03 (test reale FASE 1): venv pronto; manca un MP4 laterale provvisorio da
  mettere in `test_videos/`. Sblocca anche la validazione T14/T30.
- `data/sessions.csv` non creato: verra' generato dal modulo di export (M4).
- GitHub CLI (`gh`) non installato/autenticato: non blocca il push via Git HTTPS.
- 6 commit locali non ancora pushati su `origin/main` (in attesa di OK utente).
