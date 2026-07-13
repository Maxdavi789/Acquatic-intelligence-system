# HANDOFF - Punto di ripresa del lavoro

Data: 2026-07-13
Scopo: consentire a un altro assistente (Codex) di riprendere il progetto senza
ricostruire il contesto. Leggere questo file per PRIMO, poi `spec.txt`,
`breakdown_status.md`, `prompt_log.md`, `incidents.md`, `SPEC_ERRATA.md`.

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
  - M2/T13: `FrameAnalysisState` e `analyze_frame` implementati e validati su
    input sintetici; T14 e' ora la prossima task, non piu' bloccata.
  - M3/T15: scaffold Streamlit con layout Video/Metriche a due colonne
    completato; T16 e' la prossima task eseguibile.
- Stato Git verificato all'inizio dell'audit Codex: locale e `origin/main`
  allineati al commit `f32f661` (0/0). Il lavoro successivo resta locale fino a
  un OK esplicito per il push; usare `git status` per lo stato corrente.
- Convenzione commit: UN commit per task, messaggio con prefisso task ID
  (es. `T13: analyze_frame ...`). Push su `origin` SOLO dopo OK dell'utente.

## 2. PUNTO DI RIPRESA -> T14 pronta

- T13 e' completata. `analyze_frame` restituisce le sei chiavi richieste, usa
  stato persistente e non contiene simmetria.
- Landmark occlusi: forward-fill dell'angolo, nessun aggiornamento del counter e
  `wrist_y=None`; frame senza persona: stato invariato.
- Validazione sintetica: 23/23 test passati, compilazione Python OK.
- T03 e' completata sul campione locale
  `test_videos/profilo_provvisorio.mp4`: 448/448 frame decodificati, posa e arto
  affidabile su 448/448 frame, visibilita' minima 0,9341; il ramo `q` rilascia
  capture e finestra senza crash. La webcam e' stata tentata ma l'indice 0 non
  esiste su questa macchina; e' best-effort e resta INC-010 non bloccante.
- T14 e' la prossima task in ordine: trasformare la validazione temporanea gia'
  riuscita in uno script CLI di progetto che colleghi landmark reali e
  `analyze_frame`, stampando angolo e conteggio.
- T15 e' completata: `app.py` espone una pagina wide con colonne Video/Metriche
  2:1. Verifica: server health 200, AppTest senza eccezioni e due colonne.
- M3/T16 resta eseguibile dopo T14: radio File MP4/Webcam sperimentale e
  uploader `.mp4` con MP4 default.

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
- Questa macchina e' autenticata su GitHub come account `MrChuck118`, aggiunto
  come collaboratore (Write) sul repo di Maxdavi789: quindi `git push origin main`
  FUNZIONA.
- Identita' dei commit configurata in locale:
  `Massimo davide fedrigo <115544464+Maxdavi789@users.noreply.github.com>`.
- Le password di account NON funzionano per il push (GitHub le ha disabilitate):
  usare le credenziali collaboratore gia' presenti, o un token.

## 5. Blocchi / cose in sospeso (serve l'utente)

- Il campione provvisorio e' copiato localmente come
  `test_videos/profilo_provvisorio.mp4`, ma resta fuori da Git per possibile
  licenza di terzi. Non pubblicarlo finche' provenienza e diritti non sono
  chiariti. Il video ufficiale sara' quello proprio del sandbox T35.
- Webcam: nessun dispositivo all'indice 0 su questa macchina (INC-010). Serve
  hardware disponibile solo per una futura prova best-effort; non blocca MP4,
  T14 o la pipeline primaria.
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
