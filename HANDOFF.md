# HANDOFF - Punto di ripresa del lavoro

Data: 2026-07-14 (aggiornato dalla sincronizzazione ufficio dopo la sessione casa)
Scopo: consentire a un altro assistente di riprendere il progetto senza
ricostruire il contesto. Leggere questo file per PRIMO, poi `spec.txt`,
`breakdown_status.md`, `prompt_log.md`, `incidents.md`, `SPEC_ERRATA.md`.

> Nota multi-macchina: il progetto viene sviluppato da due postazioni.
> Ufficio: workspace storico, autenticato come MrChuck118 (collaboratore).
> Casa: clone in `C:\none\Acquatic-intelligence-system`, venv ricreato e
> baseline rivalidata il 2026-07-13; primo push da casa RIUSCITO. L'ufficio ha
> poi sincronizzato con `git pull --ff-only` (2026-07-14): entrambe le
> postazioni sono allineate a `origin/main` (0/0). Il video UFFICIALE
> `profilo_test.mp4` E' versionato e viaggia con Git; il vecchio provvisorio
> `profilo_provvisorio.mp4` e' ora escluso via `.gitignore` (obsoleto, INC-009).

---

## 1. Dove siamo

- Progetto: AI Swimming Motion Analyzer (PoC a secco). Spec di riferimento:
  `spec.txt` = versione v1.1 CONGELATA (2026-07-13). NON modificarla senza
  registrare l'errata in `SPEC_ERRATA.md`.
- Moduli completati prima dell'audit Codex:
  - M0: 6/6 task completate. T02 e' stata corretta con il runtime MediaPipe
    legacy compatibile; T03 e' validata sul MP4 provvisorio. La webcam
    best-effort non e' disponibile sull'hardware corrente (INC-010).
  - M1 (T07-T12): hardening del motore metriche + suite di test. Codex ha
    corretto anche il bordo T10 `peak_y == shoulder_y` con test di regressione.
  - M2 (T13-T14): completata. `analyze_frame` validata su input sintetici e,
    con `scripts/analyze_video.py`, sul video reale provvisorio (448/448 frame,
    angolo in [4,40; 179,92], conteggio 2).
  - M3 (T15-T22): COMPLETATA. Dashboard con selettore input (MP4 primario,
    webcam sperimentale), video annotato con scheletro e angolo gomito live,
    KPI reali (bracciate, fluidity), grafico onda Y del polso e persistenza
    dei risultati tra i rerun.
  - M4 (T23-T25): COMPLETATA. Bottone "Termina Sessione ed Esporta Dati":
    aggrega timestamp ISO, bracciate, fluidity, angolo medio/max in un
    DataFrame con preview e lo accoda a `data/sessions.csv` (header alla
    prima scrittura, append mai distruttivo). Verifica privacy T25 passata.
  - M5 (T26-T29): COMPLETATA. Occlusioni verificate nel loop app (INC-011:
    falso negativo post-occlusione = limite MediaPipe documentato); errori
    sorgente gestiti in UI (`_execute_processing`); anteprima webcam
    sperimentale a frame limitati validata con hardware reale; cleanup
    risorse garantito anche su stop a meta'.
  - M6 (T30-T33): COMPLETATA. Sul VIDEO UFFICIALE: T30 manuale 10 vs auto
    10 (diff 0); T33 due run bit-identici.
  - M7 (T34-T36): COMPLETATA in deroga DA-05 (SPEC_ERRATA 2026-07-14):
    video ufficiale = clip Pexels licenziata `test_videos/profilo_test.mp4`
    VERSIONATA in repo (HD 720x1280, 7 s, 10 mulinelli ritmici). T36:
    175/175 frame, 10 bracciate, Fluidity 93,1, CSV esportato, nessun
    picco spurio. Prossimo modulo: M8 (demo e pitch).
- Stato Git verificato all'inizio dell'audit Codex: locale e `origin/main`
  allineati al commit `f32f661` (0/0). Il lavoro successivo resta locale fino a
  un OK esplicito per il push; usare `git status` per lo stato corrente.
- Convenzione commit: UN commit per task, messaggio con prefisso task ID
  (es. `T13: analyze_frame ...`). Push su `origin` SOLO dopo OK dell'utente.

## 2. PUNTO DI RIPRESA -> BREAKDOWN COMPLETATO (restano azioni utente)

- M2 e' completata (T13-T14: `analyze_frame` + script CLI
  `scripts/analyze_video.py`, validati sul video provvisorio).
- M3 e' completata (T15-T22, un commit per task: ab917d0, 21d0a56, 5980826,
  7b6a480, 77ba2a1, 5678103). Architettura attuale di `app.py`:
  - `render_input_selector` (T16): radio MP4/webcam + uploader; sorgente in
    `st.session_state["video_source"]` (percorso file o indice 0).
  - `render_video_stream(source, placeholder, chart_slot, stroke_slot,
    fluidity_slot)` (T17/T18/T20/T21): loop frame -> posa -> `analyze_frame`
    (stato T13, timestamp da fps) -> overlay scheletro+angolo -> `st.image`;
    aggiorna grafico e KPI live; ritorna il riepilogo
    `{frames_rendered, stroke_count, fluidity_score, wrist_series}`.
  - `render_kpis` (T19): due `st.metric`, nessuna simmetria.
  - La colonna metriche viene costruita PRIMA della colonna video cosi' che
    gli slot esistano quando il loop li aggiorna.
  - T22: a fine loop il riepilogo va in `st.session_state["last_kpi"]` e
    `["wrist_series"]`; a ogni rerun KPI e grafico si ri-renderizzano dai
    valori persistiti.
- Tutte le task software del breakdown (T01-T41) sono completate; vedi
  breakdown_status.md per il dettaglio con commit ed evidenze.
- Numeri di riferimento della demo (video ufficiale, riproducibili):
  175/175 frame con posa, 10 bracciate (manuale 10, diff 0), Fluidity
  93,1, angolo medio 163,17 / max 179,92; elaborazione ~3,6 s a giro
  (~48 fps). Avvio: `.\venv\Scripts\python.exe -m streamlit run app.py`.
- RESTANO ALL'UTENTE: revisione/approvazione del pitch deck (importo e
  nome da inserire in docs/pitch/pitch_deck.md, poi rigenerare il PDF o
  modificarlo a mano); rehearsal umana con proiettore (+ screenshot
  dashboard per le slide); decisione sul momento webcam live
  (best-effort, gia' implementato e validato in T28).
- Se si riprende da un'altra macchina: clone -> `python -m venv venv` ->
  `pip install -r requirements.txt` -> suite 23/23 -> demo. Il video
  ufficiale e' NEL repo; il vecchio provvisorio resta solo locale.
- Landmark occlusi: forward-fill dell'angolo, nessun aggiornamento del counter e
  `wrist_y=None`; frame senza persona: stato invariato.
- Suite sintetica: 23/23 test passati anche sulla macchina di casa.
- Sulla macchina di casa la webcam indice 0 ESISTE e legge frame reali
  (480x640x3): INC-010 e' risolto qui e la modalita' sperimentale T28 sara'
  verificabile visivamente.

## 3. Ambiente

- Python: la spec fissa 3.11; in locale c'e' 3.12.10, con cui e' stato creato il
  `venv/` (gitignored). Il runtime validato e' MediaPipe 0.10.21, OpenCV contrib
  4.11.0.86, NumPy 1.26.4 e protobuf 4.25.9.
- Eseguire i test del motore:
  `.\venv\Scripts\python.exe scripts\test_metrics.py`  (atteso: 23/23, exit 0).
- Eseguire il pose tracking CLI:
  `.\venv\Scripts\python.exe vision_tracker.py --source <clip>.mp4`
- Se il `venv` non c'e' (altra macchina): `python -m venv venv` poi
  `.\venv\Scripts\python.exe -m pip install -r requirements.txt`.
- Dipendenze di compatibilita' pinnate in `requirements.txt`; installazione
  verificata anche in un venv temporaneo pulito (`pip check` verde,
  `mp.solutions.pose` presente). `matplotlib` NON e' una dipendenza diretta
  (arriva transitivo da MediaPipe; cache via `MPLCONFIGDIR`).

## 4. Git / autenticazione

- Repo: https://github.com/Maxdavi789/Acquatic-intelligence-system (branch `main`).
- Macchina UFFICIO: autenticata su GitHub come account `MrChuck118`, aggiunto
  come collaboratore (Write) sul repo di Maxdavi789: `git push origin main`
  FUNZIONA da li'.
- Macchina CASA: identita' git globale MrChuck118; credenziali push non ancora
  esercitate da qui, da verificare al primo push autorizzato.
- Identita' dei commit configurata in locale su entrambe le postazioni:
  `Massimo davide fedrigo <115544464+Maxdavi789@users.noreply.github.com>`.
- Le password di account NON funzionano per il push (GitHub le ha disabilitate):
  usare le credenziali collaboratore gia' presenti, o un token.

## 5. Blocchi / cose in sospeso (serve l'utente)

- Nessun blocco tecnico: il breakdown T01-T41 e' completo e sincronizzato su
  entrambe le postazioni (casa ha pushato, ufficio ha pullato il 2026-07-14).
- Video ufficiale: `test_videos/profilo_test.mp4` (licenza Pexels) e'
  VERSIONATO ed e' il riferimento di demo/validazione. Il vecchio provvisorio
  `profilo_provvisorio.mp4` resta solo locale, gitignored e non piu' necessario
  (INC-009).
- Webcam: assente in ufficio, presente e funzionante a casa (INC-010). Non
  blocca il percorso MP4 primario; prova UI = modalita' sperimentale T28.
- `data/sessions.csv`: generato a runtime dal modulo di export (M4), gitignored.
- Azioni utente residue: revisione pitch deck T39 (nome fornito: Massimo Davide
  Fedrigo; importo fondi da decidere) e rehearsal umana con proiettore.

## 6. Trappole da NON ripetere

- NON reintrodurre il Symmetry Score nella pipeline o nei KPI: e' fuori scope MVP
  (spec sez. 4.2, DA-01 = A) perche' contraddice la vista laterale. La funzione
  `calculate_symmetry_score` resta in `metrics_engine.py` solo come airbag NON
  collegato. Se torna la tentazione -> entry in `incidents.md`, non codice.
- NON seguire il vecchio `breakdown_status` (pre-2026-07-13) che parlava di
  "FASE 3 con KPI Simmetria": era obsoleto.
- Documentazione di governance in ASCII con apostrofo per gli accenti
  (`e'`, `gia'`, `perche'`), per coerenza con i file esistenti.

## 7. File chiave

- `spec.txt` - specifica v1.1 CONGELATA (contesto globale per l'editor AI).
- `metrics_engine.py` - motore metriche (angolo, stroke, fluidity, selezione
  arto, smoother e `analyze_frame`; simmetria airbag fuori pipeline).
- `vision_tracker.py` - ingestione video + MediaPipe Pose + overlay (FASE 1).
- `app.py` - dashboard Streamlit completa (T15-T22): input, rendering
  annotato, angolo gomito live, KPI reali, grafico onda polso, export CSV.
- `scripts/test_metrics.py` - runner di validazione del motore (auto-discovery,
  23 test).
- `breakdown_status.md` - avanzamento per modulo/task (T01-T41).
- `prompt_log.md` / `incidents.md` / `SPEC_ERRATA.md` - governance.
