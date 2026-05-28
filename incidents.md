# Incidents

## 2026-05-26

### INC-2026-05-26-001 - Git non disponibile
- Tipo: ambiente Git/GitHub.
- Evidenza: `git` non e' riconosciuto come comando in PowerShell.
- Impatto: Codex non puo' fare commit/push da terminale nello stato attuale.
- Stato: parzialmente risolto.
- Azione eseguita: installato Git for Windows 2.54.0. Nella shell corrente `git`
  non e' ancora nel PATH, ma e' utilizzabile tramite
  `C:\Program Files\Git\cmd\git.exe`.
- Azione residua: aggiornare PATH della sessione o aprire una nuova shell.

### INC-2026-05-26-002 - GitHub CLI non disponibile
- Tipo: ambiente GitHub.
- Evidenza: `gh` non e' riconosciuto come comando.
- Impatto: non e' possibile verificare o gestire login GitHub via CLI.
- Stato: parzialmente risolto.
- Azione eseguita: installato GitHub CLI 2.92.0.
- Azione residua: autenticare GitHub; `gh auth status` segnala che non esiste
  login attivo.

### INC-2026-05-26-003 - Workspace locale non e' un clone Git
- Tipo: repository locale.
- Evidenza: `C:\Acquatic intelligence system` e' vuota e non contiene `.git`.
- Impatto: non esiste ancora una base locale versionata su cui commitare.
- Stato: risolto.
- Azione eseguita: inizializzato repository locale, configurato `origin` e
  allineato `main` a `origin/main`.

### INC-2026-05-26-004 - Repo remota quasi vuota
- Tipo: stato progetto.
- Evidenza: la repo remota contiene solo `README.md` da 30 byte.
- Impatto: mancano scaffold, moduli, status, log, incidents, spec e struttura prevista dal breakdown.
- Stato: parzialmente risolto.
- Azione eseguita: creati file di governance e scaffold FASE 0.1 in locale.
- Azione residua: commit e push verso repo remota dopo verifica autenticazione.

### INC-2026-05-26-005 - File operativi richiesti assenti
- Tipo: documentazione/processo.
- Evidenza: `prompt_log`, `breakdown_status` e `incidents` non erano presenti localmente ne' nella root remota.
- Impatto: impossibile leggere uno storico operativo precedente; impossibile determinare task arretrate da status esistente.
- Stato: risolto localmente.
- Azione eseguita: creati `prompt_log.md`, `incidents.md` e
  `breakdown_status.md` locali.

### INC-2026-05-26-006 - Tool di estrazione PDF standard assenti
- Tipo: ambiente documentale.
- Evidenza: `pdftotext`, `python`, `node`, `npm` non sono utilizzabili/disponibili in questa sessione; `python.exe` punta a WindowsApps e fallisce.
- Impatto: lettura PDF non eseguibile con strumenti standard.
- Stato: mitigato.
- Azione eseguita: lettura completata decomprimendo stream PDF con PowerShell/.NET.

### INC-2026-05-26-007 - Accesso rete GitHub bloccato nel sandbox standard
- Tipo: ambiente rete.
- Evidenza: `Invoke-WebRequest` verso GitHub fallisce senza permessi elevati.
- Impatto: controllo remoto GitHub richiede approvazione rete.
- Stato: mitigato.
- Azione eseguita: ottenuta approvazione ed eseguita lettura metadati/file remoti.

### INC-2026-05-26-008 - Autenticazione GitHub push assente
- Tipo: ambiente GitHub.
- Evidenza: `gh auth status` restituisce "You are not logged into any GitHub hosts".
- Impatto: il push potrebbe non riuscire finche' non viene completato il login
  GitHub o configurato un credential helper valido.
- Stato: risolto per Git HTTPS.
- Azione eseguita: creato commit locale; push non interattivo fallito
  per assenza credenziali; tentativo di push interattivo non autorizzato.
- Aggiornamento 2026-05-28: `git push origin main` e' riuscito tramite
  credenziali Git HTTPS disponibili. GitHub CLI resta non autenticato, ma non
  blocca il push Git.
- Azione residua: autenticare GitHub CLI solo se serviranno comandi `gh`.

## 2026-05-28

### INC-2026-05-28-001 - Python command ancora puntato allo stub WindowsApps
- Tipo: ambiente Python.
- Evidenza: `python --version` continua a fallire nella shell corrente anche
  dopo installazione Python 3.11.
- Impatto: i comandi devono usare `.\venv\Scripts\python.exe` oppure il path
  esplicito di Python finche' il PATH non viene aggiornato.
- Stato: mitigato.
- Azione eseguita: installato Python 3.11, creato `venv/` e verificati import
  delle dipendenze dal virtual environment.

### INC-2026-05-28-002 - Pip bloccato dalla sandbox di rete
- Tipo: ambiente rete.
- Evidenza: `pip install -r requirements.txt` falliva con errore WinError 10013
  senza permessi elevati.
- Impatto: impossibile installare dipendenze nel sandbox standard.
- Stato: risolto.
- Azione eseguita: rilanciata installazione con permesso rete e completata con
  successo.

### INC-2026-05-28-003 - Cache Matplotlib non scrivibile nel profilo utente
- Tipo: ambiente runtime.
- Evidenza: import MediaPipe/Matplotlib tentava di creare
  `C:\Users\user\.matplotlib` e riceveva accesso negato.
- Impatto: warning ripetuti e import piu' lento.
- Stato: mitigato.
- Azione eseguita: configurato `MPLCONFIGDIR` su cache locale di progetto in
  `vision_tracker.py` e ignorata `.cache/` in Git.
