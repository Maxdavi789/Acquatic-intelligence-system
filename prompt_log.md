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
