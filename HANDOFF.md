# HANDOFF - Stato corrente del progetto

Data: 2026-07-14 (audit pre-presentazione)

Scopo: consentire a un altro assistente di riprendere il progetto senza
ricostruire la history. Leggere nell'ordine: `HANDOFF.md`, `spec.txt`,
`SPEC_ERRATA.md`, `breakdown_status.md`, ultima entry di `prompt_log.md`,
`incidents.md`.

## 1. Punto di ripresa

- Progetto: AI Swimming Motion Analyzer, PoC a secco locale/offline.
- Spec: `spec.txt` v1.1 CONGELATA; ogni delta successivo vive in
  `SPEC_ERRATA.md`.
- Breakdown T01-T41: COMPLETATO. Non esistono task arretrate o bloccate.
- T39: chiusa e revisionata il 2026-07-14 (nome Massimo Davide Fedrigo,
  richiesta fondi qualitativa senza cifra).
- T38: asset reali completi, incluso screenshot dashboard e diagramma della
  pipeline.
- Prossimo deliverable: presentazione finale `.pptx`, esterna al breakdown
  originario. Attendere che l'utente indichi la cartella sorgente sul Desktop;
  poi usare la skill Presentations e completare render + QA visiva.
- Rehearsal umana con proiettore e decisione sulla webcam live restano attivita'
  di preparazione alla giornata, non task software aperte.

## 2. Baseline validata

- Python 3.12.10.
- MediaPipe 0.10.21 legacy (`mp.solutions.pose`).
- OpenCV contrib 4.11.0.86, NumPy 1.26.4, protobuf 4.25.9.
- Streamlit 1.59.1 e Pandas 3.0.3, pinnati nell'audit finale.
- `pip check`: pulito.
- `scripts/test_metrics.py`: 23/23.
- `scripts/test_project_smoke.py`: controlla default video ufficiale,
  MediaPipe legacy e primo render Streamlit.
- Video ufficiale `test_videos/profilo_test.mp4`: 175/175 frame con posa,
  manuale 10 / automatico 10, Fluidity 93,1, angolo medio 163,17 e massimo
  179,92. Due run producono KPI e serie identici.
- Comando demo:
  `.\venv\Scripts\python.exe -m streamlit run app.py`.
- Comando CLI ufficiale senza argomenti:
  `.\venv\Scripts\python.exe scripts\analyze_video.py`.

## 3. Architettura corrente

- `vision_tracker.py`: acquisizione MP4/webcam, resize, MediaPipe Pose,
  estrazione landmark e overlay.
- `metrics_engine.py`: selezione arto lato-camera, angolo gomito,
  `StrokeCounter`, Fluidity Score, forward-fill e `analyze_frame` stateful.
- `app.py`: Streamlit a due colonne, upload MP4 primario, webcam sperimentale,
  rendering annotato, KPI/grafico live, riepilogo ed export CSV append.
- `scripts/analyze_video.py`: pipeline headless sul video ufficiale.
- `scripts/test_metrics.py`: 23 unit test deterministici.
- `scripts/test_project_smoke.py`: smoke test installazione/entrypoint/UI.
- Symmetry Score: funzione airbag fuori MVP, con zero chiamate attive. Non
  reintrodurla nella pipeline o nei KPI (DA-01).

## 4. Dati, privacy e demo

- `data/sessions.csv` contiene solo metriche aggregate ed e' gitignored.
- Il video non viene esportato come risultato ne' versionato dall'upload.
  OpenCV richiede pero' un percorso: l'upload viene materializzato in
  `.cache/uploaded_session.mp4`, file locale gitignored che puo' restare dopo
  la sessione. Non descriverlo come "mai salvato" senza questa precisazione.
- Video ufficiale: clip Pexels licenziata, hash e fonte in `SPEC_ERRATA.md`.
- Video provvisorio: `profilo_provvisorio.mp4`, storico, gitignored e non
  necessario. Il default CLI e' stato corretto in INC-013.
- Claim pitch approvati: il rischio software e' stato ridotto e misurato sul
  protocollo testato; non "azzerato". Il PoC non valida biomeccanica in acqua.

## 5. Limiti e incidenti da ricordare

- INC-011: dopo occlusioni lunghe MediaPipe puo' perdere picchi reali. Nel test
  controllato non ha prodotto falsi positivi, ma non usare "mai sovrastima"
  come garanzia universale.
- INC-012: segfault Streamlit osservato in RDP. La causa concreta piu'
  plausibile (riscrittura/troncamento della cache upload durante un rerun) e'
  stata rimossa; il limite di interrompere inferenza nativa con un rerun resta.
  Durante i circa quattro secondi di demo MP4 non toccare i widget.
- INC-010: webcam funzionante a casa; in ufficio non visibile dalla sessione
  RDP senza redirezione camera. E' best-effort e non blocca la demo MP4.
- Fluidity K=50: indice relativo euristico, non misura clinica o assoluta.

## 6. Git e politica operativa

- Repo: `https://github.com/Maxdavi789/Acquatic-intelligence-system`, branch
  `main`.
- All'inizio dell'audit del 2026-07-14, dopo `git fetch --prune`, locale e
  `origin/main` coincidevano a `a959c6c` (0 ahead / 0 behind).
- L'hardening pre-presentazione viene raccolto in un commit locale dedicato.
- Push solo dopo OK esplicito dell'utente.
- Macchina ufficio: Git HTTPS configurato tramite account collaboratore.
- Non inserire password/token in chat o nei file del progetto.

## 7. Asset presentazione

- Idonei: `demo_dashboard.png`, `demo_frame_annotato.png`,
  `demo_onda_polso.png`, `architettura_pipeline.png`.
- `demo_export_csv.png`: versione pulita con la sola sessione ufficiale.
- `demo_sequenza.jpg`: versione rigenerata senza il frame 100 degradato.
- `pitch_deck.md`: sorgente narrativa revisionata e prudente.
- `pitch_deck_bozza.pdf`: snapshot storico T39, non il deliverable finale.
- Deliverable futuro richiesto: `.pptx` nella cartella che indichera' l'utente,
  con render e verifica di ogni slide prima della consegna.

## 8. Trappole da non ripetere

- Non usare il video provvisorio per demo o test di default.
- Non reintrodurre Symmetry Score.
- Non presentare il PoC come validazione in acqua o dispositivo medico.
- Non usare claim assoluti non sostenuti dalle prove.
- Non modificare `spec.txt` congelata: usare `SPEC_ERRATA.md`.
- Aggiornare `prompt_log.md` prima di ogni output finale e registrare in
  `incidents.md` ogni incidente reale.
