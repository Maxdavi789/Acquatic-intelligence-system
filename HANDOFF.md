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
  - M3: T15 (scaffold due colonne) e T16 (selettore input MP4 primario /
    webcam sperimentale con uploader) completate; T17 e' la prossima task.
- Stato Git verificato all'inizio dell'audit Codex: locale e `origin/main`
  allineati al commit `f32f661` (0/0). Il lavoro successivo resta locale fino a
  un OK esplicito per il push; usare `git status` per lo stato corrente.
- Convenzione commit: UN commit per task, messaggio con prefisso task ID
  (es. `T13: analyze_frame ...`). Push su `origin` SOLO dopo OK dell'utente.

## 2. PUNTO DI RIPRESA -> T17 pronta

- T14 e' completata: `scripts/analyze_video.py` collega l'output reale di
  `extract_pose_landmarks` ad `analyze_frame` (headless) e stampa angolo e
  conteggio in console. Validata sul video provvisorio: 448/448 frame con
  posa, angolo in [4,40; 179,92], conteggio finale 2, fluidity 0 (<3 picchi),
  exit 0; sorgente non valida -> messaggio leggibile, exit 1.
- T16 e' completata: radio "File MP4 (primario)" (default) / "Webcam
  (sperimentale)" con avviso esplicito; uploader `.mp4` che persiste il file
  in `.cache/` (gitignored, fuori da `data/`) ed espone il percorso in
  `st.session_state["video_source"]` (webcam -> indice 0). Validazione:
  AppTest 16/16 check, server health 200.
- T17 e' la prossima task in ordine: loop di lettura frame nella colonna
  sinistra con overlay scheletro via `st.image` su placeholder, riusando le
  funzioni di `vision_tracker` e consumando
  `st.session_state["video_source"]`. Sostituire `cv2.imshow` (vietato in
  Streamlit) con l'aggiornamento del placeholder.
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
