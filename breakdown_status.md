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
| M3 | Dashboard Streamlit `app.py` | T15-T22 | Completata: 8/8 |
| M4 | Persistenza CSV | T23-T25 | Completata: 3/3 |
| M5 | Robustezza e gestione errori | T26-T29 | Completata: 4/4 |
| M6 | Test e validazione | T30-T33 | Completata: 4/4; T30/T33 RIPETUTI sul video ufficiale (T30: diff 0; T33: identici) |
| M7 | Sandbox demo controllato | T34-T36 | Completata: 3/3 in deroga DA-05 (video licenziato al posto del sandbox fisico, vedi SPEC_ERRATA) |
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

Validatore dopo T22: `python scripts/test_metrics.py` -> 23/23 test, exit 0
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
| T18 | Completata | `analyze_frame` (stato T13, timestamp da fps sorgente) in ogni frame del loop; `draw_elbow_angle` sovrimprime l'angolo con testo bordato (21d0a56). Validazione: 11/11 check, spy sugli angoli reali [4,40; 179,92], contact sheet coerente con le fasi (catch 169,0 / pull 117,9 / push 179,4). |
| T19 | Completata | Due blocchi `st.metric` (Bracciate totali, Fluidity Score) via slot `render_kpis`, letti da session_state con default 0 (5980826). Nessun KPI simmetria (DA-01). AppTest verde. |
| T20 | Completata | Slot grafico creato prima del loop; serie (tempo, polso Y) da `analyze_frame`, `st.line_chart` aggiornato ogni 10 frame + render finale (7b6a480). Sul video reale: 46 aggiornamenti incrementali, 448 campioni, frame occlusi esclusi. |
| T21 | Completata | KPI aggiornati live sul picco e periodicamente con i valori reali; il loop restituisce il riepilogo di sessione (77ba2a1). Sul video reale: progressione 0->1->2, conteggio finale 2 coerente col video, fluidity 0.0. |
| T22 | Completata | Riepilogo persistito in `st.session_state` a fine loop; KPI e grafico ri-renderizzati dai valori persistiti a ogni rerun (5678103). AppTest 11/11: i KPI sopravvivono ai cambi di widget; sessione pulita resta a 0. |

## Governance

- Step 0 (05f13d7): SPEC_ERRATA.md + riallineamento a T01-T41.
- Ambiente: venv Python 3.12; MediaPipe 0.10.21, OpenCV contrib 4.11.0.86,
  NumPy 1.26.4 e protobuf 4.25.9. Installazione pulita verificata.
- Commit locali per task (prefisso task ID). Il blocco INC-2026-07-13-006 e'
  risolto; il push resta comunque subordinato all'OK esplicito dell'utente.
- README riallineato in modo intermedio il 2026-07-13; il DoD completo T37 resta
  futuro, dopo la validazione end-to-end.

## Dettaglio M4

| Task | Stato | Note |
| --- | --- | --- |
| T23 | Completata | Riepilogo loop esteso con angolo medio/max; `build_session_dataframe` (timestamp ISO, bracciate, fluidity, angolo medio/max) e bottone "Termina Sessione ed Esporta Dati" con preview (8e877ad). 14/14 check; sul video reale: medio 146,25 / max 179,92. |
| T24 | Completata | `append_session_to_csv`: header alla prima scrittura, append mai distruttivo (8031b20). 9/9 check: doppio append su path temporaneo e via click AppTest reali su `data/sessions.csv`. |
| T25 | Completata | Ispezione: `data/` contiene solo `sessions.csv` + `.gitkeep`; nessun media persistito nel progetto; CSV gitignored. Nota di design sul file transitorio `.cache/uploaded_session.mp4` registrata in incidents.md. |

## Dettaglio M5

| Task | Stato | Note |
| --- | --- | --- |
| T26 | Completata | Verifica doppia sul loop app (b4df5f2): MP4 con box nero sul braccio per 100 frame -> nessun crash, nessun picco spurio, dati inaffidabili scartati; iniezione visibility<0.5 -> forward-fill esatto, counter congelato, ripresa corretta. Trovato e documentato INC-011 (falso negativo post-occlusione, limite MediaPipe). |
| T27 | Completata | `_execute_processing` (cd704e0): sorgente non apribile -> `st.error` leggibile; fine stream -> "Elaborazione terminata"; clip sintetica senza persona -> skip pulito, KPI a 0, nessun errore. 11/11 check. |
| T28 | Completata | Anteprima webcam sperimentale a frame limitati (c4dc9a3, `WEBCAM_PREVIEW_FRAMES=300`): termina da sola e rilascia le risorse; su errore degrado documentato con rimando a MP4 primario. Validata con webcam REALE: 13/13 check inclusi click end-to-end via AppTest. |
| T29 | Completata | Verifica senza modifiche al codice: stop simulato a meta' elaborazione (MP4 e webcam) -> `capture.release()` chiamata esattamente una volta dal `finally`, interruzione propagata a Streamlit, webcam subito riapribile. 6/6 check. |

## Dettaglio M6

| Task | Stato | Note |
| --- | --- | --- |
| T30 | Completata (provvisorio) | Conteggio manuale documentato = 1 (una recovery sopra la spalla, evidenze frame 300-440 + tracciato polso/spalla); automatico = 2; differenza = 1 ENTRO tolleranza +-1. Causa del +1 e requisito per il video T35 (bracciate ritmiche continue) in incidents.md. Da ripetere sul video ufficiale T35. |
| T31 | Completata | Esito formale = verifica occlusione T26: scenario controllato (box nero 100 frame + iniezione visibility), nessun picco spurio, nessun crash; registrato in INC-011. |
| T32 | Completata | Tre casi limite eseguiti e loggati (incidents.md): input non valido -> errore leggibile UI+CLI; fine stream -> chiusura pulita; stop a meta' -> release singolo, nessun handle. |
| T33 | Completata (provvisorio) | Due run sullo stesso MP4: KPI IDENTICI (bracciate 2, fluidity 0.0, angolo medio 146,2519, max 179,9191), serie polso e serie angoli identiche frame per frame. 7/7 check. Da ripetere sul video ufficiale T35. |

## Dettaglio M7

| Task | Stato | Note |
| --- | --- | --- |
| T34 | Superata in deroga | Il sandbox fisico non e' realizzabile per l'MVP; le condizioni controllate sono garantite dalla clip scelta (camera fissa, sfondo uniforme, luce costante). Deroga DA-05/DA-08 formalizzata in SPEC_ERRATA (2026-07-14). L'allestimento proprio resta nella roadmap finanziata. |
| T35 | Completata in deroga | Video ufficiale = Pexels 37264420 HD 720x1280 25fps, `test_videos/profilo_test.mp4`, VERSIONATO (licenza Pexels, 1,9 MB), SHA256 e fonte in SPEC_ERRATA (6adac64). Mulinelli ritmici in piedi: 10 cicli in 7 s. |
| T36 | Completata | Giro completo pipeline sul video ufficiale: 175/175 frame, 10 bracciate, Fluidity 93,1, angoli [58,49; 179,92], grafico e KPI live, CSV esportato (riga: 10 / 93,1 / 163,17 / 179,92). Nessun picco spurio (intervalli >= 0,6 s; oscillazione bassa a f100 scartata dal gate spalla). 11/11 check. |

## Prossima Task

- Prossima task in ordine: M8/T37, README finale (descrizione onesta, "come
  funziona", disclaimer non-medicale, vincolo 0 euro, roadmap sensori,
  link alla spec e alla deroga video). Dipendenza T36 soddisfatta.
- A seguire: T38 (screenshot/grafici per le slide: contact sheet e onda
  gia' disponibili come base), T39 (slide pitch con richiesta fondi),
  T40 (rehearsal demo x2 con il video ufficiale; da decidere l'eventuale
  momento webcam live), T41 (chiusura governance).

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
