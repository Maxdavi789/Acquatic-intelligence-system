# Prompt Log

## 2026-05-26 17:56 +02:00 - Iterazione di analisi e piano

### Messaggio utente
- Richiesta di usare `prompt_log` per catalogare ogni messaggio prima dell'output finale.
- Richiesta di usare un file `incidents` per registrare incidenti e funzioni collegate.
- Obiettivo: continuare a seguire il breakdown, aggiornando lo status con data odierna.
- Metodo richiesto: leggere integralmente i PDF allegati, `prompt_log`, `breakdown status`, analizzare progetto/repo e discordanze, individuare prossima task e arretrati, verificare README, validare piano e attendere approvazione.
- Vincoli: non inventare, non iniziare a costruire, mostrare prima il piano.
- Subtask: verificare che l'ambiente GitHub sia pronto per commit/push gestiti da Codex durante il progetto.

### Messaggi/azioni assistente
- Avviata analisi in sola modalita' piano, senza costruire funzionalita' applicative.
- Verificato ambiente Git/GitHub: `git` e `gh` non sono disponibili nel PATH.
- Verificato workspace locale: `C:\Acquatic intelligence system` e' vuoto e non contiene `.git`.
- Verificati PDF in `C:\Users\user\Downloads` e calcolati hash SHA256.
- Letti integralmente i PDF tramite estrazione dei flussi PDF interni, pagina per pagina.
- Verificata repo GitHub `Maxdavi789/Acquatic-intelligence-system`: pubblica, branch `main`, contiene solo `README.md`.
- Verificato README remoto: contiene solo il titolo `# Acquatic-intelligence-system`.
- Rilevata assenza di `prompt_log`, `breakdown_status` e `incidents` nella repo remota e nel workspace locale.
- Preparato piano d'azione da sottoporre all'approvazione dell'utente prima di procedere.

### Stato iterazione
- Nessuna funzionalita' applicativa implementata.
- Creati solo i registri operativi locali richiesti per tracciabilita': `prompt_log.md` e `incidents.md`.

## 2026-05-26 18:10 +02:00 - Iterazione approvata: setup repo e FASE 0.1

### Messaggio utente
- L'utente ha approvato il piano proposto con il messaggio: "approvo".

### Messaggi/azioni assistente
- Installato Git for Windows 2.54.0 tramite `winget`.
- Installato GitHub CLI 2.92.0 tramite `winget`.
- Verificato che GitHub CLI non e' ancora autenticato.
- Inizializzato il repository Git locale in `C:\Acquatic intelligence system`.
- Collegato `origin` a `https://github.com/Maxdavi789/Acquatic-intelligence-system.git`.
- Configurati localmente `user.name` e `user.email` con identita' GitHub noreply.
- Eseguito fetch di `origin/main` e allineato il branch locale `main`.
- Creato `breakdown_status.md` datato 2026-05-26.
- Aggiornato `README.md` con obiettivo, stack, struttura, stato e governance.
- Creato scaffold FASE 0.1: `app.py`, `vision_tracker.py`,
  `metrics_engine.py`, `requirements.txt`, `spec.txt`, `data/`,
  `test_videos/`.
- Aggiornato `incidents.md` con lo stato reale dei blocchi risolti e residui.

### Stato iterazione
- FASE 0.1 completata localmente.
- FASE 0.2 bloccata da ambiente Python non funzionante.
- Creato commit locale con messaggio `Initialize project governance and scaffold`.
- Push remoto non completato: il push non interattivo e' fallito per assenza
  credenziali e il tentativo di push interattivo non e' stato autorizzato.

## 2026-05-26 18:20 +02:00 - Verifica commit/push prima cambio ambiente

### Messaggio utente
- L'utente chiede se commit e push di tutto sono stati completati per poter
  continuare dall'ambiente di casa.

### Verifica assistente
- Eseguito controllo Git: branch `main` risulta `ahead 1` rispetto a
  `origin/main`.
- Ultimo commit locale verificato: `80cf88e Initialize project governance and scaffold`.
- Verificata autenticazione GitHub CLI: assente (`gh auth status` segnala
  utente non loggato).

### Stato comunicato
- Commit locale completato.
- Push remoto non completato.
- Per continuare da casa serve completare il push da questa macchina oppure
  portare manualmente i file/commit locali.

## 2026-05-28 - Continuazione progetto

### Messaggio utente
- L'utente ha chiesto: "continua con il progetto".

### Messaggi/azioni assistente
- Verificato che la repo locale e `origin/main` sono allineati al commit
  `321804d`.
- Letti `breakdown_status.md`, `prompt_log.md`, `incidents.md`,
  `requirements.txt` e `spec.txt`.
- Verificato che GitHub CLI non e' autenticato.
- Installato Python 3.11 tramite `winget`.
- Creato virtual environment `venv/`.
- Compilato `requirements.txt` con stack previsto dalla specifica.
- Installate dipendenze nel `venv` dopo autorizzazione rete per pip.
- Verificati import di OpenCV, MediaPipe, Streamlit, NumPy, Pandas e Matplotlib.
- Aggiunto `.gitignore` per `venv/`, cache, output locali e file editor.
- Corretto il blocco struttura in `spec.txt` usando ASCII.
- Implementata FASE 1 in `vision_tracker.py`: webcam/MP4, resize, MediaPipe
  Pose, overlay landmark e chiusura pulita con `q`.
- Implementata FASE 2 in `metrics_engine.py`: angolo gomito, StrokeCounter,
  Fluidity Score e Symmetry Score.
- Eseguiti test di compilazione, CLI help e casi numerici sintetici.

### Stato iterazione
- FASE 0 completata.
- FASE 1 implementata, test reale webcam/MP4 ancora da fare.
- FASE 2 implementata con test sintetici.
- Prossima task: FASE 3, dashboard Streamlit in `app.py`.
- Creato e pushato su `origin/main` il commit
  `Implement vision tracking and metrics engine`.

## 2026-07-13 - Ripresa progetto: riallineamento a spec v1.1 e avvio M0

### Messaggio utente
- Fornite due nuove versioni dei documenti guida: spec tecnica v1.1 e
  breakdown_tasks_v1 (task T01-T41), entrambi datati 02/07/2026.
- Richiesto: continuare a seguire il breakdown progredendo con lo status (data
  odierna), leggendo integralmente tutti i file allegati, prompt_log e
  breakdown_status; analizzare discordanze tra progetto e documenti; individuare
  prossima task e arretrati; verificare allineamento Git locale vs origin;
  controllare se il README va aggiornato; validare il piano e attendere
  approvazione prima di costruire.
- Vincoli ribaditi: non inventare, non iniziare a costruire, mostrare prima il
  piano. Subtask: aggiornare/creare prompt_log, breakdown_status, incidents e
  creare SPEC_ERRATA.
- Nota: il link repo incollato dall'utente puntava a
  `MrChuck118/live-draft-companion` (progetto diverso, Draft Whisperer).

### Messaggi/azioni assistente (analisi in sola lettura)
- Rilevato che il workspace `c:\AcquaticIntelligenceSystem` conteneva solo un
  file `readme` vuoto e nessun repo Git: la base non era ancora clonata qui.
- Segnalata la discordanza sul link repo; l'utente ha confermato che la repo
  corretta e' `Maxdavi789/Acquatic-intelligence-system`.
- Inizializzato Git nel workspace, collegato origin e fetchato `origin/main`
  (commit ff016b8). Branch locale `main` allineato: 0 ahead / 0 behind.
- Letti integralmente: breakdown_status.md, prompt_log.md, incidents.md,
  spec.txt, README.md, metrics_engine.py, vision_tracker.py, app.py,
  requirements.txt, .gitignore.
- Riscontro chiave: la repo e' allo stato PRE-M0. Il `spec.txt` in repo e'
  ancora la spec VECCHIA (con Symmetry Score), `metrics_engine.py` implementa
  `calculate_symmetry_score`, `app.py` e' vuoto. Il `breakdown_status.md`
  indicava come prossima task "FASE 3 dashboard con KPI Simmetria": indicazione
  OBSOLETA e in contrasto con la spec v1.1 (trappola di scope creep).
- Conclusione: la vera prossima task e' M0/T01 del nuovo breakdown, non FASE 3.
- Verificato ambiente: Python 3.12.10 sul PATH (spec chiede 3.11), nessun venv,
  `gh` assente, nessuna identita' Git configurata.

### Decisioni approvate dall'utente
- Repo corretta confermata: `Maxdavi789/Acquatic-intelligence-system`.
- Scope sessione: governance + task M0 non bloccate, un passo alla volta, fin
  dove si arriva con i token.
- Ambiente: venv con Python 3.12, fallback 3.11 se MediaPipe legacy si rompe.
- Commit/push: commit locali per task; push su origin solo dopo OK esplicito;
  identita' Git = quella dei commit precedenti (Maxdavi789 noreply).

### Stato iterazione
- Avviato Step 0 (scaffolding governance): creato SPEC_ERRATA.md, aggiornati
  prompt_log.md e incidents.md, riallineato breakdown_status.md al modello
  T01-T41. A seguire: M0 (T01 spec v1.1, T05 airbag simmetria, T02/T04 con venv).
