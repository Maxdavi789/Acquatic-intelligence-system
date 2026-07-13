# HANDOFF - Punto di ripresa del lavoro

Data: 2026-07-13 (aggiornato in serata dalla sessione casa)
Scopo: consentire a un altro assistente di riprendere il progetto senza
ricostruire il contesto. Leggere questo file per PRIMO, poi `spec.txt`,
`breakdown_status.md`, `prompt_log.md`, `incidents.md`, `SPEC_ERRATA.md`.

> Nota multi-macchina: il progetto viene sviluppato da due postazioni.
> Ufficio: workspace storico, autenticato come MrChuck118 (collaboratore).
> Casa: clone in `C:\none\Acquatic-intelligence-system`, venv ricreato e
> baseline rivalidata il 2026-07-13; credenziali push da verificare al primo
> push. Il video provvisorio untracked va ricopiato a mano su ogni macchina
> (SHA256 di riferimento in incidents.md, INC-009).

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
  - M6 (T30-T33): COMPLETATA sul video provvisorio. T30: manuale 1 vs auto
    2, entro tolleranza +-1 (dettagli in incidents). T33: riproducibilita'
    PERFETTA (KPI e serie identiche tra due run). T30/T33 da ripetere sul
    video ufficiale T35. Prossimo modulo: M7 (sandbox, FISICO).
- Stato Git verificato all'inizio dell'audit Codex: locale e `origin/main`
  allineati al commit `f32f661` (0/0). Il lavoro successivo resta locale fino a
  un OK esplicito per il push; usare `git status` per lo stato corrente.
- Convenzione commit: UN commit per task, messaggio con prefisso task ID
  (es. `T13: analyze_frame ...`). Push su `origin` SOLO dopo OK dell'utente.

## 2. PUNTO DI RIPRESA -> T34/T35 (sandbox: serve l'utente)

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
- M6 e' completata sul video provvisorio (T30-T32 in 38b29ac, esiti in
  incidents.md; T33: due run -> KPI e serie IDENTICHE, 7/7).
- Le prossime task in ordine sono FISICHE e richiedono l'utente:
  - T34: montare il sandbox controllato (spec sez. 3.4, DA-08): camera su
    supporto fisso a 90 gradi, sfondo neutro, luci uniformi, marker a
    terra, costo 0, foto del setup da salvare.
  - T35: registrare nel sandbox il video ufficiale
    `test_videos/profilo_test.mp4`: dryland di profilo, un solo soggetto
    interamente visibile, continuo, con BRACCIATE RITMICHE (>= 4-5 cicli):
    requisito emerso dal T30 (il debounce 0,6 s e' calibrato su gesto
    ritmico, non su demo lente con pause).
- Dopo T35 il software riprende con: T36 (pipeline completa sul video
  ufficiale: KPI plausibili, niente picchi spuri, CSV), ripetizione
  T30/T33 sul video ufficiale, poi M8 (T37 README finale, T38 screenshot,
  T39 slide pitch, T40 rehearsal x2, T41 chiusura governance).
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

- Il campione provvisorio e' presente su entrambe le macchine come
  `test_videos/profilo_provvisorio.mp4` (SHA256 identico, vedi INC-009), ma
  resta fuori da Git per possibile licenza di terzi. Non pubblicarlo finche'
  provenienza e diritti non sono chiariti. Il video ufficiale sara' quello
  proprio del sandbox T35.
- Webcam: assente sulla macchina ufficio, presente e funzionante sulla
  macchina casa (INC-010). Non blocca il percorso MP4 primario.
- I commit della sessione casa (governance, T14, T16) sono locali: push solo
  dopo OK esplicito dell'utente.
- `data/sessions.csv` non ancora creato: lo generera' il modulo di export (M4).

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
- `app.py` - scaffold Streamlit T15; qui proseguono T16-T22.
- `scripts/test_metrics.py` - runner di validazione del motore (auto-discovery,
  23 test).
- `breakdown_status.md` - avanzamento per modulo/task (T01-T41).
- `prompt_log.md` / `incidents.md` / `SPEC_ERRATA.md` - governance.
