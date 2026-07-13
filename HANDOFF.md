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
  - M0: 5/6 task completate; T03 resta bloccata per mancanza MP4.
  - M1 (T07-T12): hardening del motore metriche + suite di test. Codex ha
    corretto anche il bordo T10 `peak_y == shoulder_y` con test di regressione.
- Stato Git verificato all'inizio dell'audit Codex: locale e `origin/main`
  allineati al commit `f32f661` (0/0). Il lavoro successivo resta locale fino a
  un OK esplicito per il push; usare `git status` per lo stato corrente.
- Convenzione commit: UN commit per task, messaggio con prefisso task ID
  (es. `T13: analyze_frame ...`). Push su `origin` SOLO dopo OK dell'utente.

## 2. PROSSIMA TASK -> M2 / T13

`analyze_frame(landmarks, timestamp, state)` in `metrics_engine.py` (glue
vision -> metrics).

- Cosa fare: orchestrare un singolo frame:
  1. selezionare l'arto lato-camera con `select_camera_side_arm(landmarks)` (T07);
  2. calcolare l'angolo del gomito con forward-fill tramite `ElbowAngleSmoother`
     (T08), usando `min_visibility` restituito dalla selezione;
  3. aggiornare uno `StrokeCounter` con `wrist_y`, `timestamp`, `shoulder_y`;
  4. restituire un dict:
     `{arm_side, elbow_angle, stroke_count, fluidity_score, wrist_y, peak_detected}`.
  - NESSUN campo di simmetria (vedi trappola al par. 6).
- Design suggerito: introdurre uno `state` (dataclass o dict) che tiene le
  istanze persistenti di `StrokeCounter` e `ElbowAngleSmoother` tra un frame e
  l'altro, cosi' che `analyze_frame` sia chiamabile in un loop.
- Input reale dei landmark: `vision_tracker.extract_pose_landmarks(results)`
  restituisce una lista di 33 dict con chiavi `id,x,y,z,visibility` (formato gia'
  gestito da `select_camera_side_arm`). `wrist_y`/`shoulder_y` sono le Y
  normalizzate dei landmark scelti.
- DoD: chiamata su landmark sintetici -> dict completo e coerente; `grep` conferma
  assenza di simmetria. Aggiungere il/i test in `scripts/test_metrics.py` e far
  restare verde `python scripts/test_metrics.py`.
- Refs: spec sez. 8.1, MVP-003/004/005/006.

Dopo T13: T14 (validazione CLI su MP4) e' BLOCCATA finche' non c'e' un MP4
laterale provvisorio in `test_videos/` (vedi par. 5). Poi si passa a M3
(dashboard Streamlit in `app.py`, ancora vuoto).

## 3. Ambiente

- Python: la spec fissa 3.11; in locale c'e' 3.12.10, con cui e' stato creato il
  `venv/` (gitignored). MediaPipe 0.10.35 importa senza problemi su 3.12.
- Eseguire i test del motore:
  `.\venv\Scripts\python.exe scripts\test_metrics.py`  (atteso: 18/18, exit 0).
- Eseguire il pose tracking CLI:
  `.\venv\Scripts\python.exe vision_tracker.py --source <clip>.mp4`
- Se il `venv` non c'e' (altra macchina): `python -m venv venv` poi
  `.\venv\Scripts\python.exe -m pip install -r requirements.txt`.
- Dipendenze pinnate dove serve: `mediapipe==0.10.35`. `matplotlib` NON e' in
  `requirements.txt` (arriva transitivo da mediapipe; cache via `MPLCONFIGDIR`).

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

- T03 e T14: serve un file MP4 laterale (profilo 90 gradi) in `test_videos/`
  per il test reale della FASE 1 e la validazione CLI. Finche' manca, restano
  bloccate. Il video ufficiale sara' quello del sandbox (T35).
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
  arto, smoother; simmetria airbag). Qui va `analyze_frame` (T13).
- `vision_tracker.py` - ingestione video + MediaPipe Pose + overlay (FASE 1).
- `app.py` - VUOTO: qui va la dashboard Streamlit (M3).
- `scripts/test_metrics.py` - runner di validazione del motore (auto-discovery,
  18 test).
- `breakdown_status.md` - avanzamento per modulo/task (T01-T41).
- `prompt_log.md` / `incidents.md` / `SPEC_ERRATA.md` - governance.
