# Breakdown Status

Data aggiornamento: 2026-07-13

## Stato Generale

Repository: `https://github.com/Maxdavi789/Acquatic-intelligence-system.git`,
branch `main`. All'inizio dell'audit Codex del 2026-07-13, locale e
`origin/main` coincidevano al commit `f32f661` (0 ahead / 0 behind). Le modifiche
della ripresa Codex restano locali fino a un nuovo OK esplicito per il push.

Allineato a `breakdown_tasks_v1` (task T01-T41) e alla spec congelata v1.1.

> Correzione storica: la versione 2026-05-28 indicava "FASE 3 con KPI Simmetria".
> Superata: la simmetria e' fuori scope MVP (DA-01 = A). Vedi SPEC_ERRATA.md.

## Stato base esistente

| Elemento | Stato | Note |
| --- | --- | --- |
| FASE 0 - scaffold e ambiente | Completata | Struttura presente; venv 3.12 ricreato in questo percorso. |
| FASE 1 - `vision_tracker.py` | Implementata | Webcam/MP4, resize, MediaPipe Pose, overlay. Test reale ancora da fare (T03). |
| FASE 2 - `metrics_engine.py` | Implementata + hardening M1 | Angolo gomito, StrokeCounter, Fluidity (K documentata). Symmetry airbag (T05). Aggiunti select_camera_side_arm (T07) e ElbowAngleSmoother (T08). Manca solo `analyze_frame` (M2/T13). |
| FASE 3 - `app.py` | Non iniziata | File vuoto (M3). |
| FASE 4 - persistenza/robustezza/demo | Non iniziata | Dipende da M2-M3. |

## Avanzamento per modulo (nuovo breakdown)

| Modulo | Descrizione | Task | Stato |
| --- | --- | --- | --- |
| M0 | Allineamento base esistente -> spec v1.1 | T01-T06 | Parziale: 5/6, T03 bloccata |
| M1 | Hardening motore metriche | T07-T12 | Completata; arretrata puntuale T10 rilevata nell'audit |
| M2 | Step di analisi per-frame (glue) | T13-T14 | Prossima |
| M3 | Dashboard Streamlit `app.py` | T15-T22 | Da iniziare |
| M4 | Persistenza CSV | T23-T25 | Da iniziare |
| M5 | Robustezza e gestione errori | T26-T29 | Da iniziare |
| M6 | Test e validazione | T30-T33 | Da iniziare |
| M7 | Sandbox demo controllato | T34-T36 | Da iniziare |
| M8 | Demo, pitch e chiusura governance | T37-T41 | Da iniziare |

## Dettaglio M0

| Task | Stato | Note |
| --- | --- | --- |
| T01 | Completata | spec.txt = v1.1 ASCII, CONGELATA (ca30745). |
| T02 | Completata | `mediapipe==0.10.35` pinnato; import OK venv 3.12 (4c9e0bf). |
| T03 | Bloccata | Serve un MP4 laterale provvisorio in `test_videos/`. |
| T04 | Completata | matplotlib rimosso; transitivo via mediapipe (61a96ea). |
| T05 | Completata | `calculate_symmetry_score` airbag, 0 chiamate (a7d399a). |
| T06 | Completata | Baseline registrata nei file di governance (9f4a085). |

## Dettaglio M1

| Task | Stato | Note |
| --- | --- | --- |
| T07 | Completata | `select_camera_side_arm` + test (f50ff0e). |
| T08 | Completata | `ElbowAngleSmoother` forward-fill + test (6e30641). |
| T09 | Completata | Unit test `calculate_elbow_angle` (b348ef7). |
| T10 | Arretrata puntuale | Suite verde, ma il gate spalla accetta impropriamente `peak_y == shoulder_y`; fix e test richiesti prima di T13. |
| T11 | Completata | Test Fluidity + `FLUIDITY_K` documentata (0dd0bb7). |
| T12 | Completata | Runner aggregato `scripts/test_metrics.py`: 18/18 (5cf6ce6). |

Validatore: `python scripts/test_metrics.py` -> 18/18 test, exit 0.

## Governance

- Step 0 (05f13d7): SPEC_ERRATA.md + riallineamento a T01-T41.
- Ambiente: venv Python 3.12, dipendenze installate, mediapipe 0.10.35.
- Commit locali per task (prefisso task ID). Il blocco INC-2026-07-13-006 e'
  risolto; il push resta comunque subordinato all'OK esplicito dell'utente.
- README riallineato in modo intermedio il 2026-07-13; il DoD completo T37 resta
  futuro, dopo la validazione end-to-end.

## Prossima Task

Chiudere prima l'arretrata puntuale T10 sul gate spalla, poi M2 / T13 -
`analyze_frame(landmarks, timestamp, state)`: orchestrare per-frame
selezione arto (T07) + angolo con forward-fill (T08) + StrokeCounter, restituendo
un dict senza campo simmetria. Non richiede video reale.

## Task Arretrate o Bloccate

- T03 (test reale FASE 1) e T14 (validazione CLI): servono un MP4 laterale
  provvisorio in `test_videos/`.
- T10: gate spalla da rendere strettamente conforme a `peak_y < shoulder_y` e
  coprire con un test di regressione.
- Push su `origin`: risolto (MrChuck118 aggiunto come collaboratore); locale e
  origin erano allineati all'inizio dell'audit; il nuovo lavoro Codex non e'
  ancora stato pushato.
- `data/sessions.csv` non creato: generato dal modulo di export (M4).
