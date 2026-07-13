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

## 2026-07-13

### INC-2026-07-13-001 - Link repo errato fornito nella consegna
- Tipo: governance/documentazione.
- Evidenza: nel messaggio utente il link repo indicato era
  `https://github.com/MrChuck118/live-draft-companion`, che corrisponde a un
  progetto diverso (Draft Whisperer / Live Draft Companion, fantasy football).
- Impatto: rischio di clonare o pushare sul repository sbagliato.
- Stato: risolto.
- Azione eseguita: segnalata la discordanza; l'utente ha confermato che la repo
  corretta e' `Maxdavi789/Acquatic-intelligence-system`, coerente con spec e
  breakdown.

### INC-2026-07-13-002 - Workspace locale vuoto, base non clonata qui
- Tipo: repository locale.
- Evidenza: `c:\AcquaticIntelligenceSystem` conteneva solo un file `readme`
  vuoto e nessun `.git`. Il percorso usato in passato aveva spazi
  (`C:\Acquatic intelligence system`), diverso da quello attuale.
- Impatto: nessuna base versionata locale su cui lavorare; il `venv` precedente
  non e' presente in questo percorso.
- Stato: risolto (per la base Git).
- Azione eseguita: `git init`, collegato `origin`, `fetch` e checkout di `main`.
  Branch locale allineato a `origin/main` (0 ahead / 0 behind, commit ff016b8).

### INC-2026-07-13-003 - spec.txt e governance obsoleti rispetto a v1.1
- Tipo: allineamento specifica.
- Evidenza: il `spec.txt` in repo e' la spec vecchia (contiene Symmetry Score,
  overclaiming, Python 3.10+, SQLite). Il `breakdown_status.md` indicava come
  prossima task "FASE 3 dashboard con KPI Simmetria".
- Impatto: seguendo lo status obsoleto si costruirebbe la simmetria, fuori
  scope MVP per la v1.1 (trappola di scope creep documentata nel breakdown).
- Stato: risolto (2026-07-13).
- Azione eseguita: T01 ha congelato `spec.txt` v1.1; T05 ha demansionato la
  simmetria ad airbag senza chiamate attive; `breakdown_status.md`, `HANDOFF.md`
  e README sono stati riallineati allo stato reale nell'audit Codex. Il README
  conclusivo resta pianificato in T37.

### INC-2026-07-13-004 - Python 3.12 sul PATH, la spec fissa 3.11
- Tipo: ambiente Python.
- Evidenza: `python --version` sul PATH restituisce 3.12.10; la spec v1.1
  indica Python 3.11.
- Impatto: possibile incompatibilita' di MediaPipe legacy con Python 3.12.
- Stato: risolto.
- Azione eseguita: creato `venv` con Python 3.12 e installate le dipendenze;
  mediapipe 0.10.35 e le altre librerie importano correttamente su 3.12.
  Nessun fallback a Python 3.11 necessario.

### INC-2026-07-13-005 - requirements.txt non pinnato, matplotlib da valutare
- Tipo: dipendenze.
- Evidenza: `requirements.txt` elenca pacchetti senza versione; `matplotlib` e'
  presente ma nel codice serve solo a impostare `MPLCONFIGDIR` (cache), non per
  grafici (i grafici useranno `st.line_chart`).
- Impatto: rischio di rotture da upgrade (in particolare MediaPipe) e
  dipendenza potenzialmente inutile.
- Stato: risolto.
- Azione eseguita: pinnato `mediapipe==0.10.35` (T02). Verificato che matplotlib
  e' dipendenza transitiva di mediapipe (mediapipe Requires: ...matplotlib...);
  rimosso da requirements.txt, resta installato via mediapipe (T04).

### INC-2026-07-13-006 - Push negato: credenziali GitHub di un altro account
- Tipo: ambiente GitHub / permessi.
- Evidenza: `git push origin main` fallisce con HTTP 403: "Permission to
  Maxdavi789/Acquatic-intelligence-system.git denied to MrChuck118".
- Impatto: impossibile pushare i 6 commit di M0 sul remoto. Le credenziali Git
  memorizzate su questa macchina appartengono all'account GitHub MrChuck118, che
  NON ha permesso di scrittura sul repo di Maxdavi789. (MrChuck118 e' anche il
  proprietario del repo live-draft-companion, non collegato a questo progetto.)
- Stato: risolto (2026-07-13).
- Azione residua: autenticarsi come Maxdavi789 (proprietario del repo) tramite
  credential manager / personal access token, oppure aggiungere MrChuck118 come
  collaboratore con permesso di scrittura sul repo di Maxdavi789. I commit
  restano al sicuro in locale finche' l'autenticazione non e' risolta.
- Aggiornamento 2026-07-13: tentato push con username/password dell'account
  Maxdavi789 (one-shot, credential helper disabilitato): RIFIUTATO da GitHub
  ("Password authentication is not supported for Git operations"). Conferma che
  serve un Personal Access Token oppure l'aggiunta di MrChuck118 come
  collaboratore. La credenziale NON e' stata salvata su disco. In quel momento
  i commit locali in attesa di push erano 14.
- Aggiornamento 2026-07-13 (risoluzione): l'utente ha aggiunto MrChuck118 come
  collaboratore con permesso Write sul repo di Maxdavi789. `git push origin main`
  riuscito (ff016b8..9718657) usando le credenziali gia' presenti; locale e
  `origin/main` allineati (0/0).

### INC-2026-07-13-007 - Gate spalla T10 non strettamente conforme alla spec
- Tipo: logica deterministica / allineamento specifica.
- Evidenza: la spec richiede un picco valido solo con `peak_y < shoulder_y`, ma
  `StrokeCounter` rifiuta soltanto `peak_y > shoulder_y`; l'uguaglianza viene
  quindi accettata. La suite esistente non copre questo bordo.
- Impatto: un campione esattamente all'altezza della spalla puo' essere contato
  come bracciata nonostante il criterio stretto RF-006.
- Stato: risolto (2026-07-13).
- Azione eseguita: il confronto usa `peak_y >= shoulder_y` per rifiutare il
  picco; aggiunto il test `test_stroke_counter_shoulder_gate_blocks_equal_height`.
  Validatore completo: 19/19 test passati, exit code 0.
