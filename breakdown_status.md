# Breakdown Status

Data aggiornamento: 2026-07-13

## Stato Generale

Repository: `https://github.com/Maxdavi789/Acquatic-intelligence-system.git`,
branch `main`, locale allineato a `origin/main` (0 ahead / 0 behind).

Questo file e' stato riallineato al nuovo documento `breakdown_tasks_v1`
(task T01-T41) e alla specifica congelata v1.1. La root della repo resta la root
logica del progetto.

> Correzione: la versione precedente di questo status (2026-05-28) indicava come
> prossima task "FASE 3 dashboard con KPI Simmetria". Indicazione SUPERATA: nella
> spec v1.1 il Symmetry Score e' fuori scope MVP (DA-01 = A). La vera prossima
> task e' M0/T01. Dettagli in `incidents.md` (INC-2026-07-13-003) e
> `SPEC_ERRATA.md`.

## Stato base esistente (pre-M0)

| Elemento | Stato | Note |
| --- | --- | --- |
| FASE 0 - scaffold e ambiente | Completata | File progetto e struttura presenti. |
| FASE 1 - `vision_tracker.py` | Implementata | Webcam/MP4, resize, MediaPipe Pose, overlay. Test reale MP4/webcam ancora da fare (vedi T03). |
| FASE 2 - `metrics_engine.py` | Implementata contro spec vecchia | Angolo gomito, StrokeCounter, Fluidity, Symmetry. Mancano selezione arto lato-camera, forward-fill, `analyze_frame` e i test. |
| FASE 3 - `app.py` | Non iniziata | File vuoto. |
| FASE 4 - persistenza/robustezza/demo | Non iniziata | Dipende da M2-M3. |

## Avanzamento per modulo (nuovo breakdown)

| Modulo | Descrizione | Task | Stato |
| --- | --- | --- | --- |
| M0 | Allineamento base esistente -> spec v1.1 | T01-T06 | In corso |
| M1 | Hardening motore metriche | T07-T12 | Da iniziare |
| M2 | Step di analisi per-frame (glue) | T13-T14 | Da iniziare |
| M3 | Dashboard Streamlit `app.py` | T15-T22 | Da iniziare |
| M4 | Persistenza CSV | T23-T25 | Da iniziare |
| M5 | Robustezza e gestione errori | T26-T29 | Da iniziare |
| M6 | Test e validazione | T30-T33 | Da iniziare |
| M7 | Sandbox demo controllato | T34-T36 | Da iniziare |
| M8 | Demo, pitch e chiusura governance | T37-T41 | Da iniziare |

## Dettaglio M0 (modulo attivo)

| Task | Descrizione | Stato | Note |
| --- | --- | --- | --- |
| T01 | Congelare spec e sostituire `spec.txt` con v1.1 | Prossima | Contenuto v1.1 pronto; vecchia spec recuperabile da Git. |
| T02 | Pin versione MediaPipe (DA-06) | Bloccata | Richiede `venv` e `pip freeze`; venv in allestimento. |
| T03 | Test reale FASE 1 su MP4 provvisorio + webcam | Bloccata | Richiede `venv` e un MP4 laterale provvisorio (assente). |
| T04 | Decisione `matplotlib` (DA-07) | Da fare | Dopo T02: valutare se e' dipendenza transitiva di MediaPipe. |
| T05 | Demossione Symmetry Score ad airbag (DA-01=A) | Da fare | Non cancellare `calculate_symmetry_score`; marcarla fuori MVP e verificare 0 chiamate attive. |
| T06 | Aggiornare governance con la nuova baseline | In corso | Questo riallineamento e' il primo passo; da finalizzare dopo T01/T05. |

## Governance

- Aggiornato Step 0 (scaffolding): creato `SPEC_ERRATA.md`; aggiornati
  `prompt_log.md`, `incidents.md` e questo file.
- Commit locali per task (prefisso task ID). Push su `origin` solo dopo OK
  esplicito dell'utente.

## Prossima Task

M0 / T01 - congelare la spec v1.1 e sostituire il contenuto di `spec.txt`.

## Task Arretrate o Bloccate

- T02 (pin MediaPipe): richiede `venv` non ancora presente in questo percorso.
- T03 (test reale FASE 1): richiede `venv` e un MP4 laterale provvisorio.
- Test reale webcam/MP4 di FASE 1 mai eseguito (arretrato storico).
- `data/sessions.csv` non creato: verra' generato dal modulo di export (M4).
- GitHub CLI (`gh`) non installato/autenticato: non blocca il push via Git HTTPS.
