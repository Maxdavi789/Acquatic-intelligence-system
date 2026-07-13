# Breakdown Status

Data aggiornamento: 2026-07-13

## Stato Generale

Repository: `https://github.com/Maxdavi789/Acquatic-intelligence-system.git`,
branch `main`. All'inizio dell'audit Codex del 2026-07-13, locale e
`origin/main` coincidevano al commit `f32f661` (0 ahead / 0 behind). Le modifiche
della ripresa Codex restano locali fino a un nuovo OK esplicito per il push.

Ripresa da casa (2026-07-13, sera): repo clonata pulita in
`C:\none\Acquatic-intelligence-system` al commit `9d33510` (allineato a
`origin/main`, 0/0). Ambiente ricreato e rivalidato su questa macchina:
venv Python 3.12.10, install da `requirements.txt`, `pip check` pulito,
`mp.solutions.pose` inizializzabile, suite `scripts/test_metrics.py` 23/23,
AppTest Streamlit 0 eccezioni / 2 colonne. Su questa macchina la webcam
all'indice 0 ESISTE e legge frame (INC-010 risolto per la macchina di casa).
Il video provvisorio e' stato riscaricato dall'utente, hash SHA256 identico a
quello approvato, e ricopiato untracked in `test_videos/`.

Allineato a `breakdown_tasks_v1` (task T01-T41) e alla spec congelata v1.1.

> Correzione storica: la versione 2026-05-28 indicava "FASE 3 con KPI Simmetria".
> Superata: la simmetria e' fuori scope MVP (DA-01 = A). Vedi SPEC_ERRATA.md.

## Stato base esistente

| Elemento | Stato | Note |
| --- | --- | --- |
| FASE 0 - scaffold e ambiente | Completata | Struttura presente; venv 3.12 ricreato in questo percorso. |
| FASE 1 - `vision_tracker.py` | Implementata e validata | Runtime legacy ripristinato; MP4 provvisorio: posa 448/448 frame, chiusura `q` pulita. Webcam tentata ma hardware assente (best-effort, INC-010). |
| FASE 2 - `metrics_engine.py` | Implementata + hardening M1 + T13 | Angolo gomito, StrokeCounter, Fluidity (K documentata), selezione arto, smoothing e `analyze_frame`. Symmetry resta airbag fuori pipeline. |
| FASE 3 - `app.py` | Iniziata | T15 completata: scaffold Streamlit e layout asimmetrico a due colonne. |
| FASE 4 - persistenza/robustezza/demo | Non iniziata | Dipende da M2-M3. |

## Avanzamento per modulo (nuovo breakdown)

| Modulo | Descrizione | Task | Stato |
| --- | --- | --- | --- |
| M0 | Allineamento base esistente -> spec v1.1 | T01-T06 | Completata: 6/6 |
| M1 | Hardening motore metriche | T07-T12 | Completata, inclusa correzione stretta gate spalla T10 |
| M2 | Step di analisi per-frame (glue) | T13-T14 | Completata: 2/2 |
| M3 | Dashboard Streamlit `app.py` | T15-T22 | In corso: T15-T17 completate, T18 prossima |
| M4 | Persistenza CSV | T23-T25 | Da iniziare |
| M5 | Robustezza e gestione errori | T26-T29 | Da iniziare |
| M6 | Test e validazione | T30-T33 | Da iniziare |
| M7 | Sandbox demo controllato | T34-T36 | Da iniziare |
| M8 | Demo, pitch e chiusura governance | T37-T41 | Da iniziare |

## Dettaglio M0

| Task | Stato | Note |
| --- | --- | --- |
| T01 | Completata | spec.txt = v1.1 ASCII, CONGELATA (ca30745). |
| T02 | Completata (corretta) | Pin compatibile: MediaPipe 0.10.21 + OpenCV contrib 4.11.0.86 + NumPy 1.26.4 + protobuf 4.25.9. Installazione pulita e `mp.solutions.pose` OK (3c89374). |
| T03 | Completata | MP4 provvisorio copiato solo in locale: 448/448 frame con posa e arto affidabile, overlay verificato, EOF e ramo `q` puliti. Webcam best-effort tentata: dispositivo assente (INC-010). |
| T04 | Completata | matplotlib rimosso; transitivo via mediapipe (61a96ea). |
| T05 | Completata | `calculate_symmetry_score` airbag, 0 chiamate (a7d399a). |
| T06 | Completata | Baseline registrata nei file di governance (9f4a085). |

## Dettaglio M1

| Task | Stato | Note |
| --- | --- | --- |
| T07 | Completata | `select_camera_side_arm` + test (f50ff0e). |
| T08 | Completata | `ElbowAngleSmoother` forward-fill + test (6e30641). |
| T09 | Completata | Unit test `calculate_elbow_angle` (b348ef7). |
| T10 | Completata | Unit test `StrokeCounter` (7a2d62f) + correzione gate stretto e test di regressione (audit Codex). |
| T11 | Completata | Test Fluidity + `FLUIDITY_K` documentata (0dd0bb7). |
| T12 | Completata | Runner aggregato `scripts/test_metrics.py`: 18/18 (5cf6ce6). |

Validatore dopo T17: `python scripts/test_metrics.py` -> 23/23 test, exit 0
(riverificato anche sulla macchina di casa).

## Dettaglio M2

| Task | Stato | Note |
| --- | --- | --- |
| T13 | Completata | `FrameAnalysisState` + `analyze_frame`; contratto a sei chiavi, persistenza, occlusione e frame senza landmark coperti da test sintetici. |
| T14 | Completata | `scripts/analyze_video.py` (2c8eb82): landmark reali -> `analyze_frame`, stampa angolo/conteggio in console. Sul video provvisorio: 448/448 frame con posa, angolo in [4,40; 179,92], conteggio 2, exit 0; sorgente non valida -> messaggio leggibile, exit 1. |

## Dettaglio M3

| Task | Stato | Note |
| --- | --- | --- |
| T15 | Completata | `app.py` con page config, intestazione e colonne Video/Metriche 2:1. Server health 200; Streamlit AppTest: 0 eccezioni, 2 colonne. |
| T16 | Completata | Selettore radio MP4 (default) / Webcam sperimentale con avviso (6a23f00); uploader `.mp4` che persiste in `.cache/` gitignored ed espone il percorso in `st.session_state["video_source"]`. AppTest: 16/16 check; server health 200. |
| T17 | Completata | Loop `render_video_stream` con overlay scheletro su placeholder `st.image` (ab917d0); bottone di avvio solo con MP4 caricato; loop live webcam rimandato a T28 con nota esplicita. Estratto `create_pose_estimator` in `vision_tracker` (config spec 9.2 in un punto solo). Validazione: 15/15 check, 448/448 frame renderizzati, contact sheet ispezionata, suite 23/23, health 200. |
| T18-T22 | Da iniziare | T18 (overlay angolo gomito live) e' la prossima: dipendenze T17 e T13 soddisfatte. Le altre seguono l'ordine del breakdown. |

## Governance

- Step 0 (05f13d7): SPEC_ERRATA.md + riallineamento a T01-T41.
- Ambiente: venv Python 3.12; MediaPipe 0.10.21, OpenCV contrib 4.11.0.86,
  NumPy 1.26.4 e protobuf 4.25.9. Installazione pulita verificata.
- Commit locali per task (prefisso task ID). Il blocco INC-2026-07-13-006 e'
  risolto; il push resta comunque subordinato all'OK esplicito dell'utente.
- README riallineato in modo intermedio il 2026-07-13; il DoD completo T37 resta
  futuro, dopo la validazione end-to-end.

## Prossima Task

- Prossima task in ordine: M3/T18, overlay dell'angolo del gomito live
  (testo sul frame e/o accanto al video, aggiornato frame per frame).
  Dipendenze T17 e T13 soddisfatte.
- A seguire: T19 (KPI), T20 (grafico onda Y), T21 (collegamento dati reali).

## Task Arretrate o Bloccate

- Webcam: sulla macchina di casa il dispositivo indice 0 esiste e legge frame
  (INC-010 risolto qui); la prova UI completa resta in T28 come da breakdown.
- Video provvisorio: riscaricato sulla macchina di casa con SHA256 identico;
  resta deliberatamente non tracciato da Git per possibile licenza di terzi.
  Va sostituito dal video proprio T35.
- Push su `origin`: i commit della sessione casa (governance + T14 + T16)
  sono locali; push subordinato all'OK esplicito dell'utente. Da verificare
  al primo push le credenziali GitHub di questa macchina.
- `data/sessions.csv` non creato: generato dal modulo di export (M4).
