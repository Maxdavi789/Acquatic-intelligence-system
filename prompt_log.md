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

### Azioni eseguite in questa iterazione (M0)
- Impostata identita' Git locale (Massimo davide fedrigo, noreply Maxdavi789).
- Commit 05f13d7 (governance scaffolding): SPEC_ERRATA.md creato; prompt_log,
  incidents e breakdown_status aggiornati e riallineati a T01-T41.
- T01 (commit ca30745): spec.txt sostituito con la spec v1.1 in ASCII puro,
  stato portato a CONGELATA (2026-07-13). Vecchia spec recuperabile da Git.
- T05 (commit a7d399a): calculate_symmetry_score marcata airbag FUORI MVP v1;
  verificate 0 chiamate attive; syntax check OK.
- Creato venv con Python 3.12 e installate le dipendenze: mediapipe 0.10.35,
  opencv-python 5.0.0.93, streamlit 1.59.1, numpy 2.5.1, pandas 3.0.3. Import
  OK, nessun fallback a Python 3.11 necessario.
- T02 (commit 4c9e0bf): pinnato mediapipe==0.10.35 in requirements.txt.
- T04 (commit 61a96ea): rimosso matplotlib da requirements.txt; verificato che
  e' dipendenza transitiva di mediapipe (mediapipe Requires matplotlib), quindi
  resta installato automaticamente. Cache gestita via MPLCONFIGDIR.
- T06 (questo commit): finalizzata la baseline nei file di governance.

### Stato iterazione (fine)
- M0 completata tranne T03 (test reale su MP4/webcam): bloccata in attesa di un
  MP4 laterale provvisorio da mettere in test_videos/. Prossima task attivabile:
  M1/T07 (selezione arto lato-camera).
- Dopo il commit T06: 6 commit locali ahead di origin/main; push NON eseguito
  (in attesa di OK esplicito dell'utente, come da politica concordata).

## 2026-07-13 - Push M0, questione credenziali e modulo M1

### Messaggio utente
- Approvato: push dei commit M0; rimandare T03; continuare con M1/T07.
- Chiesto come fornire le credenziali GitHub per il push.
- (mid-turn) Incollati username/password dell'account GitHub.

### Messaggi/azioni assistente
- Tentato `git push origin main`: FALLITO con HTTP 403 (permesso negato a
  MrChuck118 sul repo di Maxdavi789). Registrato INC-2026-07-13-006 (5e8a79c).
- Avviso di sicurezza: la password dell'account GitHub non va incollata in chat
  e non funziona per il push (serve un token). Consigliato cambiarla e usare
  l'opzione "aggiungere MrChuck118 come collaboratore" (nessun segreto da
  condividere). Credenziale NON salvata ne' usata.
- M1 completata (un commit per task, ogni volta con validatore verde):
  - T07 (f50ff0e): `select_camera_side_arm` + 3 test.
  - T08 (6e30641): `ElbowAngleSmoother` (forward-fill occlusioni) + 3 test.
  - T09 (b348ef7): unit test `calculate_elbow_angle`.
  - T10 (7a2d62f): unit test `StrokeCounter` (ritmo, dead-band, debounce, gate).
  - T11 (0dd0bb7): test Fluidity + costante `FLUIDITY_K=50` documentata (DA-04).
  - T12 (5cf6ce6): runner aggregato `scripts/test_metrics.py` con auto-discovery.
- `python scripts/test_metrics.py` -> 18/18 test passati, exit 0.

### Stato iterazione (fine)
- M0 e M1 completate (restano bloccate T03 e T14 per mancanza di un MP4).
- Prossima task: M2/T13 (`analyze_frame`).
- Commit locali non ancora pushati: push bloccato da INC-2026-07-13-006, in
  attesa che l'utente dia a MrChuck118 il permesso di scrittura sul repo.

## 2026-07-13 - Push sbloccato e handoff a Codex

### Messaggio utente
- "fai push di tutto"; poi ha incollato username/password dell'account GitHub.
- Dopo il rifiuto password, ha aggiunto MrChuck118 come collaboratore del repo.
- Infine: "continuo il lavoro con Codex, crea un log finale che gli faccia capire
  da dove riprendere".

### Messaggi/azioni assistente
- Tentato push con password: rifiutato (password auth non supportata). Avviso di
  sicurezza dato; credenziale non salvata (INC-2026-07-13-006 aggiornato).
- Dopo l'aggiunta di MrChuck118 come collaboratore: `git push origin main`
  riuscito (ff016b8..9718657, poi ..8d7f8c2). Locale e origin allineati (0/0).
- Aggiornati incidents.md e breakdown_status.md: blocco push risolto.
- Creato `HANDOFF.md` per la ripresa del lavoro con Codex (stato, prossima task
  M2/T13, ambiente, git/auth, blocchi, trappole, file chiave).

### Stato iterazione (fine)
- Tutto pushato su origin/main. M0 e M1 completate; T03/T14 bloccate (manca MP4).
- Prossima task per Codex: M2/T13 `analyze_frame`. Vedi HANDOFF.md.

## 2026-07-13 11:28 +02:00 - Audit Codex e piano T13 in attesa di approvazione

### Messaggio utente
- Richiesto di continuare il breakdown usando la data odierna e di catalogare
  ogni iterazione/messaggio in `prompt_log.md` prima dell'output.
- Richiesto di mantenere `incidents.md` per tutti gli incidenti reali del
  progetto.
- Richiesto di leggere integralmente i due allegati Markdown, l'intero
  `prompt_log.md`, il breakdown status e tutti i file della repo, senza
  tralasciare contenuto.
- Richiesto di confrontare specifica, breakdown, status, prompt log e codice;
  individuare prossima task e arretrati; verificare Git locale vs `origin` e
  valutare il README.
- Vincolo: sola analisi e piano prima dell'approvazione; non inventare e non
  iniziare a costruire.
- Subtask: capire dove Claude si era fermato e riprendere da quel punto.

### Messaggi/azioni assistente
- Annunciato l'uso della skill GitHub per la verifica tracciabile di repo,
  branch locale e `origin`; nessuna azione remota di scrittura eseguita.
- Verificata l'assenza di `AGENTS.md`; nessuna istruzione locale aggiuntiva.
- Una prima istruzione PowerShell di inventario ha avuto un errore di sintassi;
  il comando e' stato corretto senza modificare file. Non e' un incidente del
  progetto.
- Letti integralmente in UTF-8 i due allegati:
  `AISwimmingAnalyzer_breakdown_tasks_v1.md` (20.985 byte, SHA256
  `951D4821A40A60F1A45937D82E8B4B57369CA80B5D2E966469C1066ACBA22A79`)
  e `AISwimmingAnalyzer_TechnicalSpec_v1_1.md` (31.507 byte, SHA256
  `99974568064C0CFD36572FFF6028ED5B059B519FE5D263CA0572E517F268B45C`).
- Letti integralmente tutti i file versionati e il file locale non tracciato:
  `prompt_log.md`, `breakdown_status.md`, `incidents.md`, `HANDOFF.md`,
  `spec.txt`, `SPEC_ERRATA.md`, `README.md`, `requirements.txt`, `.gitignore`,
  `metrics_engine.py`, `vision_tracker.py`, `scripts/test_metrics.py`, `app.py`,
  i due `.gitkeep` e `readme` vuoto. Verificati dimensioni e hash dei file.
- Ricostruito il punto di arresto di Claude: M0/T01-T06 e M1/T07-T12 svolti;
  T03 rinviata per mancanza MP4; T14 conseguentemente bloccata; nessuna modifica
  parziale a T13; prossimo lavoro dichiarato M2/T13.
- Verificata la repo GitHub corretta
  `Maxdavi789/Acquatic-intelligence-system`, pubblica, branch predefinito `main`.
- Il primo `git fetch` non ha potuto scrivere `.git/FETCH_HEAD` per il sandbox;
  ripetuto con autorizzazione sulla sola operazione di fetch e completato. Non
  e' un incidente del progetto.
- Dopo il fetch: `HEAD` e `origin/main` coincidono al commit
  `f32f661666251592e2bacd4de898ac94e791dc44`; divergenza `0 ahead / 0 behind`.
  Nessun commit da pushare o pullare nello stato iniziale dell'audit.
- Rilevato il file locale non tracciato `readme`, vuoto (0 byte), distinto dal
  `README.md`; non rimosso ne' aggiunto per rispettare il vincolo di piano.
- Validato l'ambiente: Python 3.12.10 nel `venv`, MediaPipe 0.10.35; `pip check`
  senza dipendenze rotte; import di OpenCV/MediaPipe/Streamlit/NumPy/Pandas OK.
- Una prima invocazione concatenata del Python del `venv` ha restituito un
  errore transitorio; la verifica diretta ha confermato che interprete e venv
  esistono e funzionano. Non registrato come incidente perche' non
  riproducibile.
- Eseguito il validatore corrente: `18/18` test passati, exit code 0.
- Confermato che `analyze_frame` non esiste ancora e che
  `calculate_symmetry_score` compare solo come funzione airbag, senza chiamate
  attive nella pipeline.
- Rilevata una piccola arretrata di T10: la spec richiede il gate stretto
  `peak_y < shoulder_y`, mentre il codice rifiuta solo `peak_y > shoulder_y` e
  quindi accetta impropriamente il caso di uguaglianza. Manca il relativo test.
- Rilevate derive di governance: `breakdown_status.md` dichiara M0 completata
  pur avendo T03 bloccata e contiene ancora una frase che dice che il push e'
  bloccato; `HANDOFF.md` indica come ultimo commit `8d7f8c2` invece di `f32f661`;
  `INC-2026-07-13-003` risulta ancora "in risoluzione" nonostante T01/T05 siano
  chiuse.
- Confermato che `README.md` va aggiornato: e' fermo al 2026-05-28, indica
  Python 3.10+, Matplotlib diretto e FASE 3 come prossima, in contrasto con
  spec/ambiente/stato attuali. Il completo DoD T37 resta comunque futuro.

### Piano validato, in attesa di approvazione
- Prima riallineare la governance senza marcare task future come completate:
  correggere `breakdown_status.md`, `HANDOFF.md`, lo stato di INC-003 e fare un
  aggiornamento intermedio fattuale del README; gestire il `readme` vuoto solo
  con approvazione.
- Chiudere l'arretrata T10 con gate `peak_y >= shoulder_y` rifiutato e test di
  regressione; rieseguire l'intera suite.
- Implementare solo M2/T13 in `metrics_engine.py`: stato persistente per
  `StrokeCounter` e `ElbowAngleSmoother`, orchestrazione per frame, output con
  le sei chiavi richieste e nessun campo simmetria; non aggiornare il counter su
  landmark occlusi/non validi.
- Aggiungere test sintetici T13 per contratto del dict, persistenza dello stato,
  occlusione e input senza landmark; rieseguire test/import e grep anti-simmetria.
- Aggiornare `breakdown_status.md`, `prompt_log.md` e `incidents.md` solo con
  esiti reali; mantenere T03/T14 bloccate fino alla disponibilita' di un MP4.
- Nessun codice applicativo, fix T10, README/status/incidents, commit, push o
  pull applicato in questa iterazione. Unica modifica: questa entry obbligatoria
  di `prompt_log.md`. Attesa approvazione o correzione del piano.

## 2026-07-13 12:07 +02:00 - Piano approvato, chiusura T10 e implementazione T13

### Messaggio utente
- L'utente ha approvato integralmente il piano con il messaggio: "procedi".

### Messaggi/azioni assistente
- Confermato che l'esecuzione sarebbe rimasta locale, senza push remoto.
- Riallineata la governance: M0 corretto a 5/6 con T03 bloccata; rimossa la
  frase obsoleta sul push bloccato; HANDOFF aggiornato; INC-003 chiuso.
- Aggiornato il README in modo intermedio con obiettivo onesto, MP4 primario,
  webcam sperimentale, stack reale, stato corrente, privacy e disclaimer. T37
  resta aperta per la revisione conclusiva dopo la demo.
- Eliminato il file locale vuoto e non tracciato `readme`, distinto da
  `README.md`.
- Registrato INC-2026-07-13-007 per la non conformita' stretta del gate spalla
  T10. Creato il commit locale `addf0ca` (`governance: reconcile Codex handoff
  before T13`).
- Corretto T10: un picco con `peak_y == shoulder_y` viene ora rifiutato tramite
  il confronto `peak_y >= shoulder_y`; aggiunto il test di regressione dedicato.
- Validazione dopo T10: 19/19 test passati, exit code 0. INC-007 chiuso.
- Il primo tentativo di staging T10 e' stato bloccato dal sandbox sulla scrittura
  di `.git/index.lock`; ripetuto con autorizzazione per il solo commit locale.
  Non e' un incidente del progetto e nessun push e' stato eseguito.
- Creato il commit locale `4877e80` (`T10: enforce strict shoulder gate
  regression`).
- Implementato T13 in `metrics_engine.py`: aggiunta la dataclass
  `FrameAnalysisState` con `StrokeCounter` ed `ElbowAngleSmoother` persistenti;
  aggiunta `analyze_frame(landmarks, timestamp, state)`.
- Il risultato T13 contiene sempre le sei chiavi richieste: `arm_side`,
  `elbow_angle`, `stroke_count`, `fluidity_score`, `wrist_y`, `peak_detected`;
  nessun campo simmetria.
- Su landmark occlusi l'angolo viene forward-filled, il counter non viene
  modificato e `wrist_y` e' `None`. Su frame senza landmark lo stato resta
  invariato.
- Aggiunti quattro test T13: contratto del dict, persistenza del counter,
  occlusione senza contaminazione e assenza landmark.
- Validazione finale: 23/23 test passati, exit code 0; compilazione Python di
  motore, tracker e test riuscita; `git diff --check` verde; grep conferma che
  la simmetria resta solo nella funzione airbag e non nella nuova pipeline.
- Aggiornati `breakdown_status.md`, `HANDOFF.md` e README: T13 completata, T14
  bloccata dal video, prossima task eseguibile senza video M3/T15.
- Preparato il commit locale T13 in chiusura della presente iterazione. Nessun
  pull o push eseguito.

### Stato iterazione
- Governance riallineata, arretrata T10 chiusa e M2/T13 completata.
- Suite corrente: 23/23 test verdi.
- T03 e T14 restano bloccate finche' l'utente non fornisce un MP4 laterale.
- Prossima task in ordine: T14 (bloccata). Prossima eseguibile: M3/T15.
- Tutto il nuovo lavoro resta in commit locali; push non autorizzato ne'
  eseguito.

## 2026-07-13 12:21 +02:00 - Valutazione del video candidato per T03/T14

### Messaggio utente
- Fornito `C:\Users\user\Downloads\videoplayback.mp4` e chiesto se il video e'
  idoneo; in caso contrario, richiesta una descrizione piu' specifica del video
  necessario.

### Messaggi/azioni assistente
- Comunicato che la valutazione avrebbe coperto integrita' tecnica,
  inquadratura laterale 90 gradi e tracciabilita' MediaPipe, senza copiare il
  file nella repo ne' modificare codice/dipendenze.
- Verificato il file: 23.585.142 byte, SHA256
  `F6A7E6959BE5826E3E1D0CB15C70B967EB27932E15A3866172D123F282D2F716`.
- Estratti metadati con OpenCV: H.264, 640x360, 30 fps, 7.660 frame, durata
  255,3 secondi.
- Eseguita decodifica sequenziale completa: 7.660/7.660 frame letti; il file e'
  tecnicamente integro.
- Creata in `C:\tmp` una contact sheet diagnostica di 12 frame distribuiti nel
  video e ispezionata visivamente.
- Riscontro visivo comunicato: montaggio subacqueo lungo, intro, cambi scena e
  prospettiva, soggetti diversi, bolle/occlusioni, tratti senza atleta e
  inquadratura non costantemente laterale. Non rispetta il protocollo dryland
  controllato della spec.
- Tentato un campionamento MediaPipe a 1 fps per misurare detection/visibility.
  Il test si e' fermato prima dell'analisi perche' `mediapipe==0.10.35` non
  espone `mp.solutions`.
- Verificato che non esistono `mediapipe.python` o
  `mediapipe.python.solutions`; `vision_tracker.py` importa ma non puo' eseguire
  `mp.solutions.pose` nell'ambiente corrente. Registrato INC-008.
- Registrato INC-009 per il video candidato non idoneo. Nessun downgrade,
  migrazione, modifica applicativa, commit o push eseguito.

### Esito
- Il file e' valido come MP4 ma NON idoneo a chiudere T03/T14 e non va copiato
  in `test_videos/` come riferimento.
- Puo' essere usato in futuro soltanto come stress test subacqueo/fuori
  distribuzione, separato dalla validazione MVP.
- Serve una clip propria a secco, continua, con camera fissa a 90 gradi, una
  sola persona completamente visibile, sfondo semplice, luce uniforme e
  ripetizioni chiare del gesto.
- Prima di eseguire T03 va inoltre risolto separatamente INC-008 sull'API
  MediaPipe legacy.

## 2026-07-13 12:29 +02:00 - Prosecuzione senza video: completamento M3/T15

### Messaggio utente
- L'utente ha chiesto di procedere con le altre task mentre cerca un video
  laterale idoneo.

### Messaggi/azioni assistente
- Selezionata M3/T15 come prossima task eseguibile senza video; T03/T14 e
  INC-008 restano bloccati e separati.
- Annunciato l'uso della skill browser per verificare la pagina locale richiesta
  dal DoD T15. Letta integralmente la relativa procedura prima dei test UI.
- Salvata la precedente valutazione video nel commit locale `adc161b`
  (`governance: assess candidate video and log MediaPipe blocker`). Nessun push.
- Implementato `app.py` senza anticipare T16-T22: `st.set_page_config` wide,
  titolo, caption, due colonne asimmetriche 2:1, intestazioni Video/Metriche,
  placeholder informativi e disclaimer.
- Evitato intenzionalmente l'import MediaPipe nello scaffold: INC-008 non blocca
  l'avvio della pagina T15.
- Validazione statica: `py_compile` e import `app` riusciti; `git diff --check`
  verde. Il warning Streamlit in bare mode e' atteso e non e' un incidente.
- Avviato Streamlit in locale su `127.0.0.1:8501`: health endpoint HTTP 200,
  corpo `ok`.
- La skill browser non ha trovato alcuna scheda/browser integrato disponibile;
  seguita la procedura di troubleshooting prevista, che ha confermato lista
  browser vuota. Nessun fallback verso strumenti browser non autorizzati.
- Eseguito il validatore nativo `streamlit.testing.v1.AppTest`: 0 eccezioni,
  titolo corretto, subheader Video/Metriche, esattamente 2 colonne con pesi
  0,6667 / 0,3333 e i due placeholder attesi.
- Arrestato il server locale dopo la verifica. Nessun processo lasciato in
  ascolto sulla porta 8501.
- Aggiornati README, HANDOFF e breakdown status: T15 completata; T14 bloccata;
  T16 prossima task eseguibile. Preparato commit locale T15; nessun push.

### Stato iterazione
- M3/T15 completata secondo il DoD strutturale/runtime.
- Screenshot visivo non disponibile per assenza del browser integrato; la
  struttura e' stata verificata con AppTest e server reale.
- Prossima task in ordine: T14 bloccata. Prossima eseguibile: M3/T16.

## 2026-07-13 12:31 +02:00 - Valutazione secondo video candidato

### Messaggio utente
- Fornito `C:\Users\user\Downloads\videoplayback (1).mp4` e chiesto se questo
  secondo video e' idoneo.

### Messaggi/azioni assistente
- Comunicato che sarebbero stati applicati gli stessi criteri del primo video e
  che il file non sarebbe stato copiato nella repo prima dell'approvazione.
- Verificato il file: 788.954 byte, SHA256
  `EA5A67AF8B8A0BB504AA7FF5E9F07DFF5E7D038632D0C56811B4E82C9D4BC8B7`.
- Estratti metadati: H.264, 360x640 verticale, 30 fps, 277 frame, durata 9,23 s.
- Decodifica completa riuscita: 277/277 frame; file tecnicamente integro.
- Creata e ispezionata una contact sheet di 12 frame distribuiti nella clip.
- Riscontro: video molto migliore del precedente per durata, continuita',
  singolo soggetto e ripresa prevalentemente laterale. Resta pero' una clip di
  nuoto reale in vasca, non una simulazione dryland controllata.
- Acqua, riflessi e immersione occludono parti del corpo; la risoluzione utile e'
  bassa e il formato verticale riduce l'inquadratura. Presente anche un
  watermark, con licenza/consenso da verificare.
- Decisione: non approvato come riferimento T03/T14 e non copiato in
  `test_videos/`; puo' essere usato in futuro come stress test fuori
  distribuzione dopo la risoluzione di INC-008.
- Aggiornati INC-009 e breakdown status. Nessun codice, dipendenza, commit o
  push modificato/eseguito.

### Stato iterazione
- T03/T14 restano bloccate: serve ancora una clip propria a secco, laterale e
  controllata; resta inoltre aperto INC-008 sull'API MediaPipe legacy.

## 2026-07-13 12:36 +02:00 - Valutazione terzo video candidato

### Messaggio utente
- Fornito `C:\Users\user\Downloads\videoplayback (2).mp4`, indicandolo come
  candidato potenzialmente migliore.

### Messaggi/azioni assistente
- Ribadita la distinzione tra file utilizzabile per upload/decodifica e video
  valido per chiudere T03/T14; nessuna copia preventiva nella repo.
- Verificato il file: 1.182.093 byte, SHA256
  `49702466FF32DA10D633A2FCF41BA2BB594F7A57C979BAF9BAA95D6FCCE906A3`.
- Metadati: H.264, 360x640 verticale, 30 fps, 448 frame, durata 14,93 s.
- Decodifica completa riuscita: 448/448 frame; file tecnicamente integro.
- Creata e ispezionata una contact sheet con 12 campioni temporali.
- Riscontro: un solo soggetto, movimento simulato a secco su supporto, camera
  fissa, vista sufficientemente laterale e ciclo completo con spalla, gomito e
  polso visibili. E' il primo candidato coerente col protocollo dryland.
- Limiti rilevati: 360x640 verticale, sovraimpressioni con testo/frecce,
  possibile contenuto di terzi e un solo ciclo lento; non e' il video ufficiale
  T35 e non e' ideale per validazione finale/Fluidity.
- Decisione comunicata: accettato come MP4 PROVVISORIO per T03/T14, con
  idoneita' effettiva del pose tracking da verificare dopo INC-008.
- Aggiornati INC-009, breakdown status e HANDOFF. Nessuna copia del video,
  modifica al codice/dipendenze, commit o push eseguita.

### Stato iterazione
- Il blocco "manca un candidato MP4" e' mitigato.
- T03/T14 restano formalmente bloccate da INC-008; T03 richiede anche il test
  webcam. Il video ufficiale del sandbox T35 resta futuro.

## 2026-07-13 13:05 +02:00 - Correzione runtime MediaPipe e chiusura T03

### Messaggio utente
- L'utente ha approvato il passo successivo con: "bene procediamo vai con il
  prossimo passo".

### Messaggi/azioni assistente
- Confermato il perimetro: rendere riproducibile MediaPipe legacy, copiare il
  terzo video come campione locale provvisorio, validare il tracking completo e
  tentare la webcam; il video non sarebbe stato pubblicato senza licenza.
- Copiato `videoplayback (2).mp4` in
  `test_videos/profilo_provvisorio.mp4`; verificato SHA256
  `49702466FF32DA10D633A2FCF41BA2BB594F7A57C979BAF9BAA95D6FCCE906A3`.
- Il primo avvio del launcher `venv` nel sandbox ha segnalato l'interprete base
  come non disponibile; rieseguito con il permesso richiesto. Non era una
  rottura del venv: fuori dal sandbox `pip check` e gli import sono riusciti.
- Verificato il runtime di lavoro: OpenCV 4.11.0, MediaPipe 0.10.21, NumPy
  1.26.4, protobuf 4.25.9; `mp.solutions.pose` presente e inizializzabile.
- Processato l'intero video con `process_pose_frame` e `analyze_frame`: 448/448
  frame decodificati, posa 100%, arto selezionato affidabile 100%, arto sinistro
  selezionato 448 volte, visibilita' minima 0,9341 e media 0,9814.
- Angolo gomito osservato tra 4,40 e 179,92 gradi; conteggio finale 2. Fluidity
  Score 0 coerente con la regola che richiede almeno tre picchi.
- Creata in `C:\tmp` e ispezionata una contact sheet di 12 frame con overlay:
  scheletro coerente nelle fasi catch, pull, push e recovery.
- Tentata la webcam con `VideoCapture(0)`: nessuna camera disponibile,
  `Camera index out of range`. Registrato INC-010 come limite hardware
  best-effort non bloccante.
- Testato il ramo di chiusura con `q` sul video reale mediante sostituzione delle
  sole funzioni GUI: un frame mostrato, un `waitKey`, una chiamata a
  `destroyAllWindows`, exit 0. Il primo validatore temporaneo aveva passato un
  `Path` invece della stringa prevista; corretto e rilanciato, senza modifiche al
  progetto e senza aprire un incidente applicativo.
- Regressione: 23/23 test metrici, `py_compile` riuscito, Streamlit AppTest con
  0 eccezioni e 2 colonne.
- Corretto `requirements.txt` al set compatibile e registrata l'errata DA-06 in
  `SPEC_ERRATA.md`. Installazione completa da requirements riuscita anche in un
  venv temporaneo pulito: `pip check` verde e `legacy_pose=True`.
- Creato il commit locale `3c89374` (`T02: restore compatible MediaPipe legacy
  runtime`). Nessun push eseguito.
- Aggiornati README, HANDOFF, breakdown status e incidents: M0 6/6, INC-008
  risolto, T03 completata con webcam best-effort non disponibile, T14 sbloccata
  e prossima.
- Eseguito `git fetch origin` in sola lettura: remoto 0 commit avanti, branch
  locale 6 commit avanti prima del commit T03. Nessun pull o push eseguito.
- Preparato un commit locale dedicato alla chiusura T03; il video provvisorio
  resta escluso dallo staging.

### Stato iterazione
- T02 corretta e validata in ambiente pulito; INC-008 risolto.
- T03 completata sul percorso MP4 primario; INC-010 resta aperto ma non
  bloccante per assenza di hardware webcam.
- T14 e' la prossima task in ordine. La prova temporanea ha gia' mostrato valori
  plausibili; resta da creare e validare lo script CLI previsto dal breakdown.
- Il video provvisorio resta solo locale e fuori da Git per possibile licenza
  di terzi. Nessun push eseguito.

## 2026-07-13 13:09 +02:00 - Richiesta commit/push per handoff

### Messaggio utente
- L'utente ha chiesto di eseguire commit e push appena terminato, per poter
  continuare il lavoro da casa.

### Messaggi/azioni assistente
- Verificato lo stato prima del push: branch locale 7 commit avanti e 0
  indietro rispetto a `origin/main`.
- Confermato che le modifiche tecniche e di governance sono gia' committate.
- Preparato questo commit di handoff del prompt log.
- Il file `test_videos/profilo_provvisorio.mp4` resta deliberatamente untracked
  ed escluso dal commit/push per la possibile licenza di terzi.
- Azione autorizzata: push dei commit locali su `origin/main`, seguito da
  verifica ahead/behind. Nessun altro file locale viene pubblicato.

### Esito
- Push riuscito: `origin/main` aggiornato da `f32f661` a `e52a264`.
- Verifica successiva al push: locale 0 commit avanti e 0 indietro rispetto a
  `origin/main`.
- Unico file residuo: `test_videos/profilo_provvisorio.mp4`, untracked e non
  pubblicato intenzionalmente.

## 2026-07-13 18:10 +02:00 - Ripresa da casa: clone, audit completo e piano in attesa di approvazione

### Messaggio utente
- Richiesto di continuare il breakdown con la data odierna, catalogando ogni
  iterazione in `prompt_log.md` prima dell'output e mantenendo `incidents.md`.
- Metodo: leggere integralmente gli allegati (spec v1.1 e breakdown_tasks_v1),
  l'intero `prompt_log.md` e `breakdown_status.md`; analizzare le discordanze
  tra progetto e documenti; individuare prossima task e arretrati; verificare
  l'allineamento Git locale vs origin; valutare il README; validare il piano ed
  esporlo in attesa di approvazione. Vincoli: non inventare, non costruire.
- Subtask: il progetto esisteva solo su GitHub (lavoro svolto in ufficio);
  clonarlo sulla macchina di casa, dare alla cartella locale il nome corretto
  della repo ed eliminare il file locale `b` inutile dopo la pull.
- Nel messaggio il link repo indicato era di nuovo
  `MrChuck118/live-draft-companion` (refuso ricorrente, vedi INC-001);
  a richiesta l'utente ha confermato `Maxdavi789/Acquatic-intelligence-system`.

### Messaggi/azioni assistente
- Verificata l'esistenza di entrambe le repo con `git ls-remote`; segnalata la
  discordanza del link; l'utente ha confermato la repo corretta.
- Clonata `Maxdavi789/Acquatic-intelligence-system` in
  `C:\none\Acquatic-intelligence-system` (nome cartella = nome repo GitHub).
  Eliminato il file vuoto `C:\none\b` (0 byte) come richiesto.
- Stato Git dopo il clone: `main` allineato a `origin/main` al commit `9d33510`
  (0 ahead / 0 behind), working tree pulito. Nulla da pushare o pullare.
- Letti integralmente: i due allegati, `prompt_log.md`, `breakdown_status.md`,
  `incidents.md`, `HANDOFF.md`, `SPEC_ERRATA.md`, `README.md`,
  `requirements.txt`, `app.py`, `vision_tracker.py`, `metrics_engine.py`
  (sezioni chiave verificate anche via grep) e la history dei commit.
- Verificato: `spec.txt` = v1.1 CONGELATA; `analyze_frame`/`FrameAnalysisState`
  presenti; `calculate_symmetry_score` airbag con 0 chiamate attive; suite di
  test e scaffold T15 coerenti con lo status.
- Discordanza operativa rilevata: HANDOFF e status dichiarano "T14 sbloccata",
  ma il campione `test_videos/profilo_provvisorio.mp4` e' deliberatamente
  untracked (licenza terzi) ed e' rimasto sulla macchina ufficio. Su questa
  macchina `test_videos/` contiene solo `.gitkeep`: T14 e' localmente ribloccata
  finche' il video non viene trasferito/riscaricato o sostituito.
- Ambiente casa: Python 3.12.10 sul PATH (stessa versione validata in ufficio);
  py launcher con default 3.14 da NON usare per il venv; `venv/` assente
  (gitignored), da ricreare da `requirements.txt`.
- README valutato: aggiornamento intermedio del 2026-07-13 ancora accurato
  rispetto allo stato reale; nessuna modifica necessaria ora (DoD completo in
  T37).
- Nessun codice applicativo scritto, nessun commit, nessun push. Unica modifica:
  questa entry obbligatoria di `prompt_log.md`.

### Piano proposto, in attesa di approvazione
- Step A (setup ambiente casa): venv con Python 3.12, install da
  `requirements.txt`, `pip check`, verifica `mp.solutions.pose`, validatore
  `scripts/test_metrics.py` (atteso 23/23) e AppTest Streamlit su `app.py`.
  Opportunita': ritestare la webcam best-effort su questa macchina (INC-010).
- Step B (governance): aggiornare INC-001 (refuso link ricorrente, causa nota:
  credenziali ufficio MrChuck118), `breakdown_status.md` con la nota di ripresa
  da casa e il riblocco locale di T14; commit locale di governance.
- Step C (input utente): trasferire `profilo_provvisorio.mp4` dal PC ufficio o
  riscaricarlo (SHA256 noto per verifica:
  `49702466FF32DA10D633A2FCF41BA2BB594F7A57C979BAF9BAA95D6FCCE906A3`).
- Step D (build, previa approvazione): M3/T16 selettore input (eseguibile senza
  video); M2/T14 appena il video e' disponibile.
- Push su `origin` solo dopo OK esplicito, come da politica concordata.

## 2026-07-13 20:35 +02:00 - Piano approvato: Step A-B eseguiti, video verificato, T14 e T16 completate

### Messaggio utente
- Approvazione: "vai con A e B intanto poi quando ti mando il video procedi con
  la C e con la D e la E".
- Follow-up: "prosegui, il video e' in download, e' il piu' recente"
  (riferito alla cartella Downloads).

### Messaggi/azioni assistente - Step A (ambiente casa)
- Impostata l'identita' git locale del repo a quella dei commit precedenti
  (Maxdavi789 noreply); l'identita' globale della macchina e' MrChuck118.
- Creato `venv` con Python 3.12.10; installate le dipendenze pinnate da
  `requirements.txt`; `pip check` senza rotture.
- Verificato `mediapipe==0.10.21` con `mp.solutions.pose` inizializzabile.
- Validatore motore: 23/23 test passati, exit 0, anche su questa macchina.
- AppTest su `app.py` (stato T15): 0 eccezioni, 2 colonne, titolo e subheader
  corretti.
- Webcam best-effort: su questa macchina `VideoCapture(0)` APRE e legge un
  frame reale 480x640x3. INC-010 risolto per la macchina di casa.

### Step B (governance)
- Aggiornati INC-001 (refuso link ricorrente, causa nota), INC-010 (webcam
  presente a casa) e `breakdown_status.md` (nota di ripresa da casa).
- Commit locale `50952f2` (`governance: resume from home, rebuild venv,
  revalidate baseline`). Nessun push.

### Step C (video provvisorio)
- Individuato `Downloads\videoplayback.mp4` (file piu' recente, 1.182.093
  byte). SHA256 calcolato: IDENTICO al riferimento approvato in ufficio
  (`49702466...906A3`).
- Copiato in `test_videos/profilo_provvisorio.mp4` e mantenuto untracked;
  aggiornato INC-009 con la nota della sessione casa.

### Step E/D - T14 (prima, come da ordine breakdown) e T16
- T14: creato `scripts/analyze_video.py`, script CLI headless che collega
  l'output reale di `extract_pose_landmarks` ad `analyze_frame` e stampa
  angolo/conteggio per frame piu' riepilogo aggregato.
- Validazione T14 sul video provvisorio: 448/448 frame con posa, angolo in
  [4,40; 179,92], conteggio finale 2, fluidity 0 (<3 picchi, coerente), exit 0.
  Valori identici alla prova temporanea dell'ufficio. Sorgente non valida ->
  messaggio leggibile ed exit 1 (RF-001). Regressione 23/23; py_compile OK.
  Commit `2c8eb82`.
- T16: aggiunto in `app.py` il selettore radio "File MP4 (primario)" (default)
  / "Webcam (sperimentale)" con avviso esplicito; uploader `.mp4` che persiste
  il file in `.cache/` (gitignored, fuori da `data/`) ed espone il percorso
  alla pipeline via `st.session_state["video_source"]` (webcam -> indice 0).
  Nessuna anticipazione del rendering T17.
- Validazione T16: AppTest 16/16 check (default MP4 senza warning, webcam con
  warning e device 0, cleanup dello stato, integrita' della persistenza fuori
  da `data/`); server reale health 200 e arrestato pulito; py_compile OK.
  Commit `6a23f00`.
- Governance finale: `breakdown_status.md` (M2 2/2, T16 completata, prossima
  T17), `HANDOFF.md` (punto di ripresa T17, nota multi-macchina, git/auth,
  blocchi), README (stato intermedio, comando analyze_video, struttura),
  questa entry di prompt_log. Commit di governance in chiusura.

### Stato iterazione
- M2 completata (2/2); M3 a 2/8 (T15-T16 fatte). Prossima task in ordine: T17
  (rendering video nella colonna sinistra).
- Suite 23/23 verde; ambiente casa pienamente operativo; webcam disponibile.
- Commit locali della sessione: 50952f2, 2c8eb82, 6a23f00 + governance finale.
  Push NON eseguito: resta subordinato all'OK esplicito dell'utente.

## 2026-07-13 21:05 +02:00 - Push autorizzato e completamento M3/T17

### Messaggio utente
- "bene fai un push e procediamo".

### Messaggi/azioni assistente - push
- Eseguito `git push origin main`: riuscito, `9d33510..3afeae5`. Primo push
  dalla macchina di casa: le credenziali GitHub presenti funzionano.
  Dopo il push: locale e `origin/main` allineati (0/0); unico file residuo
  l'MP4 provvisorio, untracked di proposito.

### T17 - Rendering video annotato nella dashboard
- Refactor propedeutico: estratto `create_pose_estimator()` in
  `vision_tracker.py` come UNICO punto di configurazione del modello (spec
  sez. 9.2), riusato da `run_pose_tracking`, `scripts/analyze_video.py` e
  dalla dashboard. Eliminata la triplicazione dei parametri Pose.
- Implementato in `app.py` `render_video_stream(source, placeholder)`: loop
  di lettura frame, overlay scheletro via `process_pose_frame`, conversione
  BGR->RGB e aggiornamento del placeholder `st.empty`/`st.image`
  (sostituto di `cv2.imshow`, non utilizzabile in Streamlit, spec sez. 14.2).
  Risorse rilasciate nel `finally` (RF-013).
- Bottone "Avvia elaborazione video" visibile solo con un MP4 caricato;
  per la webcam la UI rimanda esplicitamente a T28 (best-effort), evitando
  un loop live non arrestabile prima di T29.
- Validazione (15/15 check): 448/448 frame renderizzati sul video provvisorio
  con payload RGB corretti; sorgente non valida -> RuntimeError controllato;
  AppTest pulito su percorso default e webcam; contact sheet 2x2 dei frame
  annotati ispezionata visivamente (scheletro coerente su catch/pull/push/
  recovery); suite 23/23; riepilogo `analyze_video` INVARIATO dopo il
  refactor (448/448, angolo [4,40; 179,92], conteggio 2); py_compile OK;
  server reale health 200 anche con l'import MediaPipe all'avvio pagina.
- Commit `ab917d0` (T17). Governance aggiornata: breakdown_status (T17
  completata, prossima T18), HANDOFF (punto di ripresa T18 con indicazioni
  implementative), README (stato intermedio).

### Stato iterazione
- M3 a 3/8 (T15-T17). Prossima task in ordine: T18 (overlay angolo live).
- Suite 23/23 verde; nessuna regressione su CLI e script T14.
- Commit locali post-push: ab917d0 (T17) + commit di governance in chiusura.
  Push dei nuovi commit subordinato al prossimo OK esplicito.

## 2026-07-13 22:20 +02:00 - Autorizzazione push di sessione e completamento M3 (T18-T22)

### Messaggio utente
- "esegui push e proseguiamo, ricordati di aggiornare i documenti necessari".
- Letta come autorizzazione di sessione per i push (proposta "OK cumulativo"
  della iterazione precedente): push eseguiti senza richiedere conferma a
  ogni task, sempre con verifica dello stato prima/dopo.

### Push iniziale
- `git push origin main`: riuscito, `3afeae5..abb9c63` (T17 + governance).

### T18 - Overlay angolo gomito live (commit 21d0a56)
- `analyze_frame` (stato persistente T13, timestamp da fps sorgente) eseguita
  su ogni frame del loop; `draw_elbow_angle` sovrimprime l'angolo con testo
  bordato (font Hershey solo ASCII -> "deg" al posto del simbolo gradi).
- Validazione 11/11: pixel-diff sul disegno, spy sugli angoli reali
  (448 chiamate, escursione 4,40-179,92), contact sheet coerente con le fasi
  del gesto (catch 169,0 / pull 117,9 / push 179,4 deg). Suite 23/23.

### T19 - KPI bracciate e fluidity (commit 5980826)
- Due blocchi `st.metric` via slot `render_kpis`, letti da session_state con
  default 0. Nessun riferimento alla simmetria (DA-01 rispettata).
- AppTest: 0 eccezioni, entrambi i KPI renderizzati.

### T20 - Grafico onda Y del polso (commit 7b6a480)
- Slot grafico creato prima del loop (la colonna metriche viene costruita
  prima di quella video); serie (tempo, polso Y) accumulata da
  `analyze_frame`, `st.line_chart` aggiornato ogni 10 frame + render finale.
- Sul video reale: 46 aggiornamenti incrementali, serie monotona fino a 448
  campioni, frame occlusi esclusi; loop retrocompatibile senza chart_slot.

### T21 - KPI collegati ai dati reali (commit 77ba2a1)
- KPI aggiornati live sul picco rilevato e periodicamente; il loop restituisce
  il riepilogo `{frames_rendered, stroke_count, fluidity_score, wrist_series}`.
- Sul video reale: progressione conteggio 0->1->2 in 48 aggiornamenti live,
  conteggio finale 2 COERENTE con le bracciate visibili, fluidity 0.0.

### T22 - Persistenza tra i rerun (commit 5678103)
- Riepilogo persistito in `st.session_state` a fine elaborazione; KPI e
  grafico ri-renderizzati dai valori persistiti a ogni rerun.
- AppTest 11/11: i valori sopravvivono ai cambi radio avanti/indietro, il
  grafico sostituisce la caption placeholder, una sessione pulita resta a 0.
- Health finale server: 200. Suite finale: 23/23.

### Governance
- breakdown_status: M3 completata 8/8 con evidenze per task; prossima M4/T23
  (con nota: aggiungere angolo medio/max al riepilogo del loop).
- HANDOFF: punto di ripresa T23 con architettura attuale di `app.py`.
- README: stato M3 completata, prossime T23-T25.
- Push di chiusura sessione eseguito dopo il commit di governance.

### Stato iterazione
- M0-M3 COMPLETATI (T01-T22). Prossima task: M4/T23 (export dati).
- Suite 23/23; dashboard end-to-end funzionante sul video provvisorio.
- Restano aperti: video ufficiale sandbox (T35), webcam UI (T28), export CSV
  (M4), robustezza formale (M5), test finali (M6).

## 2026-07-13 23:05 +02:00 - Prosecuzione approvata: modulo M4 completato (T23-T25)

### Messaggio utente
- "procediamo". Autorizzazione push di sessione ancora attiva.

### T23 - Aggregazione metriche di fine sessione (commit 8e877ad)
- Esteso il riepilogo di `render_video_stream` con `elbow_angle_mean` e
  `elbow_angle_max` (nota lasciata in HANDOFF); il riepilogo completo viene
  persistito in `st.session_state["last_summary"]`.
- `build_session_dataframe`: una riga con timestamp ISO, bracciate_totali,
  fluidity_score, angolo_medio, angolo_max. Bottone "Termina Sessione ed
  Esporta Dati" visibile solo dopo un'elaborazione; click -> preview.
- Validazione 14/14 sul video reale: angolo medio 146,25, max 179,92,
  bracciate 2; AppTest conferma gating del bottone e preview DataFrame.

### T24 - Append su data/sessions.csv (commit 8031b20)
- `append_session_to_csv`: crea cartella e header alla prima scrittura,
  append mai distruttivo (RF-011). Messaggio di conferma in UI.
- Validazione 9/9: doppio append su path temporaneo (header unico, righe
  preservate) + due click AppTest reali -> `data/sessions.csv` con due righe
  identiche al riferimento. Rimosso `use_container_width` deprecato dalla
  preview.

### T25 - Verifica privacy (commit f4f86e6)
- Ispezione: `data/` contiene SOLO `sessions.csv` + `.gitkeep`; nessun
  frame/media persistito nel progetto; CSV gitignored (riga 8).
- Nota di design in incidents.md sul file transitorio gitignored
  `.cache/uploaded_session.mp4` (upload T16, non e' persistenza di sessione).

### Governance e chiusura
- breakdown_status: M4 completata 3/3 con dettaglio task; prossima M5/T26
  con note operative (T27: RuntimeError non catturato dal bottone; T28:
  webcam ora testabile sulla macchina di casa).
- HANDOFF: punto di ripresa T26 con stato M4 e indicazioni per T26-T29.
- README: stato M4, export CSV documentato.
- Suite finale 23/23; py_compile OK. Push di chiusura eseguito.

### Stato iterazione
- M0-M4 COMPLETATI (T01-T25, 25/41 task). Prossima task: M5/T26.

## 2026-07-13 23:55 +02:00 - Prosecuzione approvata: modulo M5 completato (T26-T29)

### Messaggio utente
- "bene procediamo". Autorizzazione push di sessione ancora attiva.

### T26 - Verifica occlusioni nel loop app (commit b4df5f2)
- Verifica doppia: (A) creato un MP4 reale con box nero sulla zona del
  braccio per 100 frame -> nessun crash, nessun picco spurio, wrist_y=None
  su 100/100 frame occlusi; (B) iniezione deterministica visibility<0.5 ->
  forward-fill ESATTO (angolo congelato a 137,41 deg), counter congelato,
  ripresa corretta dopo la finestra, conteggio finale 2. 13/13 check.
- FINDING (INC-011): dopo l'occlusione fisica prolungata il tracking
  MediaPipe resta degradato e il secondo picco reale viene mancato
  (conteggio 1 invece di 2). Causa isolata con baseline ri-encodata
  (2 picchi -> il re-encoding non c'entra) e con (B) (il motore e'
  corretto). Chiuso come limite documentato coerente con spec sez. 14.2:
  possibile sottostima conservativa, MAI sovrastima.

### T27 - Errori gestiti in UI (commit cd704e0)
- `_execute_processing`: sorgente non apribile -> `st.error` leggibile,
  nessuna eccezione non gestita; successo -> session_state + caption
  "Elaborazione terminata".
- Clip sintetica di 30 frame senza persona: fine stream pulita, KPI a 0,
  serie polso vuota, grafico mai disegnato, frame renderizzati senza
  overlay. 11/11 check.

### T28 - Webcam sperimentale (commit c4dc9a3)
- Bottone "Avvia anteprima webcam (sperimentale)": stesso loop con
  `max_frames=300`, cosi' termina sempre da solo; su errore st.error +
  rimando documentato al percorso MP4 primario (RF-014).
- Validata con la webcam REALE della macchina di casa: 60 frame diretti,
  click end-to-end via AppTest (300 frame, sessione salvata, caption
  finale), device inesistente -> degrado documentato. 13/13 check.

### T29 - Cleanup risorse (commit 447991f, nessuna modifica al codice)
- Stop simulato a meta' elaborazione (MP4 al frame 15, webcam al frame 5):
  `capture.release()` chiamata ESATTAMENTE una volta dal `finally`,
  interruzione propagata a Streamlit, webcam subito riapribile. 6/6 check.

### Governance e chiusura
- breakdown_status: M5 completata 4/4 con dettaglio; prossima M6/T30 con
  avvertenza sul conteggio manuale del video provvisorio (un ciclo lento
  ma 2 picchi rilevati: confronto da documentare con cura).
- HANDOFF: punto di ripresa T30; README: stato M5 e limite INC-011.
- Suite finale 23/23; server health 200. Push di chiusura eseguito.

### Stato iterazione
- M0-M5 COMPLETATI (T01-T29, 29/41 task). Prossima task: M6/T30.
- Restano: M6 (test formali T30-T33), M7 (sandbox e video ufficiale
  T34-T36), M8 (README finale, screenshot, pitch, rehearsal, chiusura).

## 2026-07-14 00:25 +02:00 - Prosecuzione approvata: modulo M6 completato (T30-T33)

### Messaggio utente
- "procedi, ricordati di aggiornare prompt log ecc ecc". Push di sessione
  ancora autorizzato.

### T30 - Conteggio manuale vs automatico (evidenze + registrazione)
- Prodotte due evidenze sul video provvisorio: sequenza densa di 12 frame
  (300-440) con numero frame sovrimpresso e tracciato polso-vs-spalla con
  i picchi rilevati marcati (salvati come diagnostica locale).
- Ispezione visiva: il soggetto esegue UNA sola bracciata completa (una
  recovery sopra la spalla, frame ~340-420); la mano resta ferma vicino
  alla testa ~1,5 s e oscilla, generando le due inversioni contate (358 e
  402, distanti 1,47 s > debounce 0,6 s).
- ESITO: manuale 1, automatico 2, |differenza| = 1 -> ENTRO tolleranza +-1
  (spec sez. 1.2). Documentato in incidents.md con il requisito derivato
  per il video T35: bracciate continue e ritmiche (>= 4-5 cicli).
- Nota onesta: test superato al limite della tolleranza su un video
  didattico lento; la validazione vera sara' sul video ufficiale T35.

### T31 - Occlusione formale
- Esito formale = scenario controllato T26 (box nero 100 frame +
  iniezione visibility): nessun picco spurio, nessun crash. Registrato
  con aggiornamento in INC-011.

### T32 - Casi limite
- Input non valido, fine stream e stop a meta' eseguiti e verificati
  (esecuzioni formali T27: 11/11 e T29: 6/6); esiti registrati in
  incidents.md.

### T33 - Riproducibilita'
- Due esecuzioni complete sullo stesso MP4: KPI IDENTICI (bracciate 2,
  fluidity 0.0, angolo medio 146,2519, max 179,9191) e serie polso/angoli
  identiche FRAME PER FRAME. 7/7 check. Determinismo confermato.

### Governance e chiusura
- incidents.md: entry T30 e T32, aggiornamento INC-011 per T31 (38b29ac).
- breakdown_status: M6 completata 4/4 (con nota: T30/T33 da ripetere sul
  video ufficiale T35); prossima task M7/T34 FISICA (serve l'utente).
- HANDOFF: punto di ripresa T34/T35 con requisiti del video ufficiale.
- README aggiornato. Push di chiusura eseguito.

### Stato iterazione
- M0-M6 COMPLETATI (T01-T33, 33/41 task). Il software del PoC e' finito e
  validato sul materiale disponibile.
- PALLA ALL'UTENTE per M7: T34 (montare il sandbox: camera fissa 90 gradi,
  sfondo neutro, luci uniformi, marker a terra, foto del setup, costo 0) e
  T35 (registrare profilo_test.mp4 con bracciate ritmiche continue).
- Dopo il video ufficiale: T36, ripetizione T30/T33, poi M8 (README
  finale, screenshot, slide pitch, rehearsal, chiusura governance).

## 2026-07-14 00:45 +02:00 - Consultazione: fattibilita' del video ufficiale T35

### Messaggio utente
- "questo video forse non puo' essere realizzato, se fosse cosi come
  facciamo? proposte?". Nessuna richiesta di build: iterazione consultiva.

### Analisi e proposte esposte (in attesa di scelta dell'utente)
- Premessa: la spec (sez. 14.2) prevede gia' la simulazione a secco IN
  PIEDI; il sandbox sez. 3.4 e' minimale per progetto. Non serve la panca
  del video provvisorio.
- Impatto del non avere un video nuovo: Fluidity mai esercitato con >= 3
  picchi su footage reale (in demo resterebbe 0), T30 passato solo al
  limite della tolleranza, pitch con footage di terzi watermarked e con
  diritti non chiariti.
- Proposta A (raccomandata con B): sandbox minimo in piedi, profilo,
  mulinelli ritmici 4-5 cicli, telefono su appoggio fisso, parete neutra.
- Proposta B (raccomandata): registrare con la webcam della macchina di
  casa (gia' validata) tramite script di cattura dedicato che salva
  direttamente test_videos/profilo_test.mp4; il PC funge da camera fissa
  del sandbox. Serve anche per ripetere T30/T33 (richiedono un file).
- Proposta C: clip open-license (Pexels/Pixabay/dataset) come consentito
  da DA-05; rischio di non trovare inquadratura idonea.
- Proposta D (ultima spiaggia): promuovere il provvisorio a riferimento
  con deroga documentata in SPEC_ERRATA (resta fuori Git per licenza);
  opzione tecnicamente funzionante ma debole per il pitch.
- Esclusa esplicitamente la manipolazione del footage (loop/montaggio per
  simulare il ritmo): contraria all'onesta' di validazione (DA-03).

### Stato iterazione
- Nessuna modifica a codice o scope; in attesa della scelta dell'utente
  tra A/B/C/D. Preparazione script di cattura (B) o ricerca clip (C)
  pronte a partire su approvazione.

## 2026-07-14 01:00 +02:00 - Video ufficiale in deroga: ricerca, adozione e validazione completa (T35/T36 + T30/T33)

### Messaggi utente (sequenza della stessa conversazione)
- Chiarimento: progetto didattico, i diritti non sono percepiti come
  problema; il video non e' registrabile IN GENERALE (non solo il giorno
  della demo). Domanda: si puo' trovare su internet?
- Domanda successiva: seguendo questa strada, cosa si presenta il giorno
  della presentazione oltre al pitch deck?
- Approvazione finale: "allora procediamo cosi poi capiamo se aggiungere
  un video live".

### Ricerca e selezione (DA-05, opzione footage con licenza)
- Cercati candidati su Pexels (stock, licenza libera, niente watermark).
  Valutati con contact sheet 4 candidati: 3 scartati (stretching statico
  6539612, vista posteriore 6011930, seduta 6012316).
- ADOTTATO Pexels 37264420 "Workout warm up arm stretch routine
  outdoors": uomo in piedi prevalentemente di profilo, camera fissa,
  sfondo pulito, MULINELLI RITMICI del braccio sopra la testa.
- Test pipeline su variante UHD: 175/175 posa, 10 bracciate, Fluidity
  93,2. Scaricata la variante HD 720x1280 (1,9 MB): risultati identici
  (10 bracciate, Fluidity 93,1) -> scelta come file ufficiale.

### T35 in deroga (commit 6adac64)
- `test_videos/profilo_test.mp4` VERSIONATO nella repo (licenza Pexels);
  SHA256 e fonte in SPEC_ERRATA (deroga T34/T35 via DA-05/DA-08);
  INC dedicata in incidents.md con limiti onesti (7 s, mulinello in piedi
  stile dorso, vista 3/4 nei primi istanti).

### T36 + T30/T33 sul video ufficiale (commit 1e315e9)
- T36 end-to-end: 175/175 frame, 10 bracciate, Fluidity 93,1, angoli
  [58,49; 179,92], grafico e KPI live, CSV esportato
  (10 / 93,1 / 163,17 / 179,92). Nessun picco spurio: intervalli >= 0,6 s
  e oscillazione bassa a f100 correttamente scartata dal gate spalla.
  11/11 check. Contact sheet con overlay e grafico onda ispezionati.
- T30 ripetuto: conteggio manuale (creste sopra la spalla nel tracciato +
  sequenza frame) = 10; automatico = 10; DIFFERENZA 0.
- T33 ripetuto: due run -> KPI e serie angoli identici frame per frame.

### Scaletta demo concordata (per T40)
- Elaborazione LIVE del video ufficiale nella dashboard (KPI 1->10,
  Fluidity 93, grafico, export CSV), ripetibile con numeri identici.
- Eventuale momento webcam live best-effort: DA DECIDERE ("poi capiamo
  se aggiungere un video live").

### Stato iterazione
- M0-M7 COMPLETATI (T01-T36, 36/41). Prossima task: M8/T37 (README
  finale), poi T38-T41. Push di chiusura eseguito.

## 2026-07-14 - Consulenze brevi: API key e ruolo dell'AI

### Domanda 1: "non mi hai ancora chiesto l'API key del modello"
- Risposta: nessuna API key esiste ne' serve, BY DESIGN. MediaPipe
  BlazePose gira in locale su CPU (spec sez. 7, 10.4, RF-012, costo 0).
  E' un punto di forza del pitch, non una mancanza. Ribadita la regola:
  eventuali segreti mai in chat, solo `.env` gitignored (cfr. INC-006).
- Nessuna azione tecnica.

### Domanda 2: "quindi il progetto fa uso dell'AI oppure no?"
- Risposta: SI', nella percezione: BlazePose e' una rete neurale profonda
  pre-addestrata (33 landmark da frame RGB, inferenza locale). NO nella
  misura: angolo/conteggio/fluidity sono matematica deterministica, per
  riproducibilita' e verificabilita'. Non e' un sistema generativo/LLM
  (spec sez. 0, 2.4, 9). Fornita la frase pronta per la presentazione.
- Nessuna azione tecnica.

## 2026-07-14 02:00 +02:00 - Approvazione "procediamo": modulo M8 (T37-T41)

### Messaggio utente
- "ok perfetto procediamo".

### T37 - README finale (commit ac22859)
- Riscrittura completa: cosa dimostra/non dimostra (DA-03), demo con
  numeri attesi riproducibili, tabella "dove sta l'AI e dove no",
  installazione pinnata, tabella criteri di validazione, video ufficiale
  con licenza e rimando alla deroga, limiti onesti (DA-04, INC-011,
  DA-01), roadmap finanziata, privacy e disclaimer, mappa governance.

### T38 - Asset per le slide (commit c5cbaed)
- `docs/pitch/`: frame annotato full-res, sequenza 12 frame annotati,
  onda del polso con i 10 picchi, tabella reale export CSV. Tutti output
  autentici della pipeline, nessun mockup.
- Tentato screenshot headless della dashboard (Edge --headless): cattura
  solo lo skeleton di caricamento (l'app importa MediaPipe al primo run);
   scartato per onesta'. Screenshot live da fare nella rehearsal umana.

### T39 - Bozza pitch deck (commit 395519f)
- `pitch_deck.md` (sorgente con note presentatore) +
  `pitch_deck_bozza.pdf` (10 slide, immagini reali incluse). Angolo:
  "rischio software azzerato, finanziate il rischio hardware"; dry-run
  inquadrato onestamente (spec sez. 14.4).
- DoD parziale: PDF esportato; REVISIONE UTENTE PENDENTE (importo, nome,
  approvazione testi).

### T40 - Rehearsal tecnica della demo
- Due giri completi consecutivi (elaborazione + export CSV) cronometrati:
  3,6 s ciascuno, ~48 fps di elaborazione (criterio spec >= 15 fps),
  KPI identici tra i giri (10 bracciate / Fluidity 93,1), zero intoppi.
- Resta raccomandata la rehearsal umana con proiettore (occasione per
  gli screenshot dashboard e per decidere il momento webcam live).

### T41 - Chiusura governance (questo commit)
- breakdown_status: FASE 3 e FASE 4 completate; dettaglio M8; sezione
  "Azioni rimanenti" (revisione deck, rehearsal umana, decisione webcam).
- HANDOFF: punto di ripresa = breakdown completato, numeri di riferimento
  demo e istruzioni di ripresa da altra macchina.
- incidents.md: 20+ entry totali (DoD T41 >= 5 superato).
- Push finale di sessione.

### Stato iterazione
- BREAKDOWN T01-T41 COMPLETATO lato software (T39 bozza in revisione
  utente; T40 rehearsal umana raccomandata). Il PoC e' pronto per la
  presentazione: demo riproducibile, deck bozza, governance completa.

## 2026-07-14 - Chiusura sessione: consegne per le prossime sessioni

### Messaggio utente
- "ok segna tutto per bene cosi nelle prossime sessioni procediamo".

### Azioni
- Verificato che tutta la governance di progetto e' gia' committata e
  pushata (ultimo commit 8fba712, locale = origin). Unico file locale
  non tracciato: `test_videos/profilo_provvisorio.mp4` (intenzionale).
- Punto di ripresa per la prossima sessione: leggere `HANDOFF.md`
  (sezione 2: breakdown completato, azioni rimanenti all'utente).
- Azioni aperte in mano all'utente: (1) revisione pitch deck con importo
  e nome, (2) rehearsal umana con proiettore + screenshot dashboard,
  (3) decisione momento webcam live nella scaletta.
- L'assistente ha inoltre salvato nella propria memoria persistente le
  coordinate del progetto e le regole di lavoro concordate, per ripartire
  senza ricostruire il contesto.

### Follow-up: portabilita' del video sul PC ufficio
- Domanda utente: come portare il video sul PC di lavoro, "non lo hai
  pushato".
- Chiarimento (con verifica `git ls-tree origin/main`): il video UFFICIALE
  `test_videos/profilo_test.mp4` E' versionato e pushato (commit 6adac64):
  sul PC ufficio basta `git pull`. Il file non tracciato visibile nei
  `git status` e' il VECCHIO provvisorio `profilo_provvisorio.mp4`,
  escluso da Git di proposito (terzi, INC-009) e ormai non piu'
  necessario: demo e validazione girano sul video ufficiale.

### Follow-up utente (stessa iterazione)
- Commit dell'entry rifiutato dall'utente con due domande: perche' non si
  puo' usare il video in Downloads? e il tutto necessita di una demo il
  giorno della presentazione.
- Risposta data: il video di Downloads E' gia' in uso come provvisorio
  (stesso SHA256); il problema e' promuoverlo a video UFFICIALE di
  demo/validazione per tre ragioni: (1) diritti - e' contenuto di terzi
  con watermark/sovraimpressioni, non pubblicabile nella repo ne'
  presentabile come pezzo centrale di un pitch di finanziamento (INC-009);
  (2) contenuto - una sola bracciata lenta: il Fluidity Score resterebbe
  0 in demo (servono >= 3 picchi), il counter e' al limite di tolleranza
  (T30), formato verticale a bassa risoluzione con testo/frecce; (3)
  coerenza con la spec - la narrativa del sandbox controllato (sez. 3.4)
  e la ripetibilita' della demo (sez. 1.2) presuppongono footage proprio
  in condizioni controllate.
- Chiarimento demo: il giorno della presentazione NON serve produrre il
  video dal vivo. Il flusso demo (T40) e': dashboard -> carica il video
  ufficiale registrato una volta nel sandbox -> elaborazione LIVE davanti
  al pubblico -> KPI/grafico -> export CSV. Con la riproducibilita'
  bit-identica dimostrata (T33) la demo da' sempre gli stessi numeri:
  e' il motivo per cui DA-02 ha reso l'MP4 percorso primario. La webcam
  live resta un momento bonus opzionale gia' implementato (T28).

## 2026-07-14 09:17 +02:00 - Sincronizzazione ufficio dopo lavoro da casa

### Messaggio utente
- L'utente ha ripetuto la richiesta di eseguire commit e push appena terminato,
  per poter continuare il lavoro da casa.

### Messaggi/azioni assistente
- Eseguito `git fetch origin`: il locale risultava 32 commit indietro e 0
  avanti rispetto a `origin/main`; nessuna modifica tracciata locale.
- Verificato che il vecchio `test_videos/profilo_provvisorio.mp4` non fosse
  tracciato sul remoto e non interferisse con l'aggiornamento.
- Eseguito `git pull --ff-only origin main`: fast-forward da `9d33510` a
  `19d9732`, senza merge commit e senza conflitti.
- Recuperati il completamento T14-T41, gli asset pitch e il video ufficiale
  versionato `test_videos/profilo_test.mp4`.
- Verifica dopo il pull: locale e `origin/main` allineati 0/0; worktree pulita
  (il vecchio video provvisorio e' ora escluso tramite `.gitignore`).
- Preparato questo solo commit di governance per catalogare il messaggio e la
  sincronizzazione; nessun codice applicativo modificato.

### Stato iterazione
- Il lavoro svolto da casa e' presente anche sulla postazione ufficio.
- Breakdown software T01-T41 completato; restano le azioni utente indicate in
  HANDOFF (revisione pitch deck e rehearsal umana).

## 2026-07-14 (ripresa ufficio) - Rifiniture: refresh governance, riproducibilita' e pitch

### Messaggio utente
- "A casa abbiamo finito il progetto praticamente ora va solo pullato da github
  e vanno messe le ultime rifiniture qui." Metodo abituale: leggere
  integralmente allegati, prompt_log e breakdown_status; analizzare discordanze
  tra progetto e documenti; individuare prossima task e arretrati; verificare
  allineamento Git locale vs origin; valutare il README; validare il piano ed
  esporlo in attesa di approvazione. Vincoli: non inventare, non costruire prima
  dell'OK.
- Approvazione: "ok A procedi. B: Massimo Davide Fedrigo. Importo fondi: essendo
  un progetto scolastico incerto se inserirlo e quanto. C: ok procedi."

### Messaggi/azioni assistente (analisi, sola lettura)
- Letti integralmente: i due allegati (spec v1.1, breakdown_tasks_v1),
  `prompt_log.md` (1176 righe), `breakdown_status.md`, `incidents.md`,
  `HANDOFF.md`, `SPEC_ERRATA.md`, `README.md`, `requirements.txt`, `.gitignore`;
  verificati `metrics_engine.py` (analyze_frame/FrameAnalysisState presenti,
  simmetria airbag con 0 chiamate attive), `scripts/analyze_video.py`,
  `pitch_deck.md`.
- Git: `git fetch` -> locale = `origin/main` = `50db4f6`, 0 ahead / 0 behind,
  worktree pulita. Riscontro: il pull da GitHub era GIA' avvenuto stamattina
  (entry 09:17): fast-forward `9d33510 -> 19d9732`, sync ufficio registrato in
  `50db4f6`. Lo snapshot Git di apertura sessione (HEAD 9d33510) era obsoleto.
- Salute su questa macchina: suite `scripts/test_metrics.py` 23/23, venv Python
  3.12.10, requirements pinnati.
- Discordanze rilevate: (1) governance non aggiornata dopo il sync ufficio -
  `50db4f6` toccava solo prompt_log, mentre `HANDOFF.md` e `breakdown_status.md`
  portavano ancora testo "commit locali / push pending" ormai superato; (2)
  `pitch_deck.md` con placeholder `[Nome studente]` e `[importo da definire]`
  (T39 in revisione utente); (3) README (T37) verificato accurato, nessuna
  modifica necessaria.

### Blocco C - Riproducibilita' su macchina ufficio
- `analyze_video.py --source test_videos/profilo_test.mp4`: 175/175 frame con
  posa, 10 bracciate, Fluidity 93,1, angoli [58,49; 179,92]. IDENTICI ai numeri
  di riferimento documentati: portabilita' confermata anche in ufficio. Warning
  MediaPipe `landmark_projection_calculator` non fatale (cosmetico upstream),
  non e' un incidente.

### Blocco A - Refresh governance
- Aggiornati `HANDOFF.md` e `breakdown_status.md`: date al 2026-07-14, nota di
  sincronizzazione ufficio (pull ff `9d33510 -> 19d9732`, 0/0), rimosso il testo
  stantio su push pending / commit locali, video provvisorio ora gitignored,
  riproducibilita' ufficio annotata. Aggiunta questa entry di prompt_log.
- Commit di governance in chiusura iterazione. Push subordinato all'OK esplicito.

### Blocco B - Pitch deck (T39): in corso
- Nome fornito: "Massimo Davide Fedrigo" (slide 1). Importo fondi: l'utente e'
  incerto se inserirlo per un progetto scolastico. Fornita raccomandazione
  (importo illustrativo con voci hardware oppure formulazione qualitativa senza
  cifra); si attende la scelta prima di finalizzare la slide fondi e rigenerare
  il PDF (chiude il DoD T39).

### Stato iterazione
- Breakdown T01-T41 completo e sincronizzato su entrambe le postazioni. Restano
  azioni utente: chiusura T39 (decisione importo), rehearsal umana + screenshot
  dashboard, decisione webcam live.

## 2026-07-14 (ripresa ufficio, seguito) - Chiusura T39, push e diagnosi webcam

### Messaggi utente
- Scelta importo fondi: opzione qualitativa SENZA cifra (slide 10 elenca
  l'hardware e rimanda il budget di dettaglio).
- "si pusha i commit, ma INVECE GUARDA CHE QUESTO PC HA LA WEBCAM, non le
  rilevi?"

### Blocco B - T39 chiusa (commit b9cf487)
- `pitch_deck.md`: nome inserito (Massimo Davide Fedrigo, slide 1), slide 10
  con richiesta fondi qualitativa senza cifra, intestazione aggiornata a
  REVISIONATA (DoD T39 soddisfatto).
- `pitch_deck_bozza.pdf` rigenerato dal markdown revisionato (matplotlib
  PdfPages, 10 slide, immagini reali della pipeline incorporate); slide 1, 4 e
  10 ispezionate visivamente prima del commit.

### Push autorizzato
- `git push origin main`: riuscito, `50db4f6..b9cf487` (governance 5a65698 +
  T39 b9cf487). Verifica post-push: locale e `origin/main` allineati 0/0.

### Diagnosi webcam macchina ufficio (INC-010 aggiornato)
- Sonda OpenCV: indici 0-2 con backend MSMF e DirectShow -> nessuna apertura.
- Inventario PnP Windows: la sessione e' un ambiente remoto/virtualizzato
  (scheda video Hyper-V, zero dispositivi USB) con "Bus fotocamera Desktop
  remoto" (RDCAMERA_BUS) presente ma VUOTO: nessuna camera reindirizzata.
  La webcam fisica sta sul PC client dell'utente, non nella sessione remota.
  Privacy webcam Windows su Allow (non e' il blocco).
- Rimedio documentato in INC-010: abilitare la redirezione dei dispositivi di
  acquisizione video nel client Desktop remoto e riconnettersi; poi ripetere
  la sonda (T28 gia' pronta a consumare l'indice 0).

### Stato iterazione
- T39 CHIUSA; tutto il breakdown T01-T41 completato e pushato. Webcam ufficio:
  spiegata (redirezione RDP assente), rimedio in mano all'utente; a casa resta
  funzionante. Restano: rehearsal umana + screenshot dashboard, decisione
  momento webcam live.

## 2026-07-14 10:20 +02:00 - Materiale per Claude Design + diagramma architettura

### Messaggi utente
- Domanda: la cartella docs caricata su Claude Design basta per una
  presentazione dettagliata o va aggiunto qualcosa?
- Richiesta: creare una cartella sul Desktop con tutto il materiale da
  caricare; aprire la dashboard cosi' lo screenshot lo cattura l'utente.

### Valutazione e azioni
- Valutazione data: pitch_deck.md + 4 immagini reali sono una base solida;
  mancavano un diagramma di architettura (slide 8 solo testuale), il contesto
  del README per il generatore e lo screenshot della dashboard live (gap noto
  di T38). Il PDF e' ridondante rispetto al markdown per un generatore.
- Creato `docs/pitch/architettura_pipeline.png` (matplotlib, 5 blocchi:
  input -> vision_tracker -> metrics_engine -> app -> CSV, etichette
  "AI - percezione" vs "matematica deterministica - misura", fascia
  "100% locale, 0 euro"); ispezionato visivamente prima dell'adozione.
  Estende gli asset pitch di T38.
- Creata `C:\Users\user\Desktop\pitch_claude_design\` con: pitch_deck.md,
  diagramma, le 4 immagini demo, README.md e LEGGIMI_upload.txt (ruolo di
  ogni file, prompt suggerito per il generatore, nota sul PDF escluso,
  promemoria dello screenshot mancante demo_dashboard.png).
- Avviata la dashboard Streamlit in background su http://localhost:8501
  (health endpoint "ok") perche' l'utente catturi a mano lo screenshot con
  KPI pieni (10 bracciate / Fluidity 93,1).

### Stato iterazione
- In attesa dello screenshot utente (demo_dashboard.png) da aggiungere alla
  cartella Desktop e a docs/pitch. Diagramma committato; codice invariato.

## 2026-07-14 10:28 +02:00 - Pulizia stringa UI da nota di sviluppo

### Messaggio utente
- Segnalata (giustamente, con fastidio) la scritta UI "Carica un file MP4:
  il rendering verra' collegato nella task T17": linguaggio da cantiere,
  non da MVP. Richiesta: tenere "Carica un file MP4" e togliere il resto.

### Azioni
- Verificato con grep che quella di riga 94 era l'UNICA stringa visibile in
  UI con riferimenti a task ID; gli altri match sono docstring/commenti di
  tracciabilita' nel codice, non mostrati all'utente.
- `app.py`: st.info ridotto a "Carica un file MP4." (la nota era stantia da
  quando T17 e' stata completata: il rendering E' collegato).
- Validazione: py_compile OK; AppTest 0 eccezioni, messaggio info pulito e
  nessun riferimento a task nella UI.
- Dashboard riavviata su http://localhost:8501 (health "ok") cosi' la pagina
  riparte gia' corretta per lo screenshot.

### Stato iterazione
- UI ripulita; resta in attesa lo screenshot utente demo_dashboard.png.

## 2026-07-14 10:40 +02:00 - Crash segfault della dashboard e riavvio (INC-012)

### Messaggio utente
- "andava bene non ho fatto lo screen ma ad una certa si e' chiusa da sola
  perche' streamlit si e' riavviato, sei stato tu?" + screenshot del browser
  con ERR_CONNECTION_REFUSED.

### Ricostruzione e risposta data
- Alle 10:28 il riavvio ERA dell'assistente (annunciato: applicava la pulizia
  della stringa UI). La chiusura successiva (~10:34), durante l'uso
  dell'utente, NON era un riavvio: il processo e' morto da solo con
  Segmentation fault (exit 139), crash nativo MediaPipe/OpenCV documentato
  nel log del task in background.
- Registrato INC-2026-07-14-012 con evidenze, ipotesi (rerun con widget
  durante il loop di elaborazione), impatto e mitigazioni per la demo
  (non toccare i widget durante il run; comando di riavvio pronto;
  rehearsal sulla macchina vera, non in RDP).
- Dashboard riavviata e verificata (health "ok"); l'utente puo' ricaricare
  la pagina e ritentare lo screenshot.

### Stato iterazione
- Server attivo; screenshot demo_dashboard.png ancora in attesa; INC-012
  aperto non bloccante, da monitorare se si ripete.

## 2026-07-14 10:55 +02:00 - Bug check sul segfault e verifica dei due screenshot

### Messaggio utente
- Richiesto un controllo in cerca di bug riguardo l'errore Streamlit
  (INC-012); poi verificare i due screenshot fatti e, se ok, aggiungerli
  alla cartella Desktop per Claude Design.

### Bug check (esito in INC-012, aggiornamento 2026-07-14)
- Causa plausibile del segfault: `persist_uploaded_video` riscrive
  `.cache/uploaded_session.mp4` a ogni rerun; un rerun durante
  l'elaborazione tronca il file sotto il decoder nativo -> crash non
  intercettabile. Fix proposto: guard con `file_id` in session_state.
- Confermato minore: `use_container_width=True` deprecato nel loop
  (un warning per frame, 6.228 nel log del crash). Fix: `width="stretch"`.
- Pattern Pose per-run corretto; il limite rerun-durante-inferenza resta
  architetturale (spec sez. 14.2). Fix in attesa di approvazione.

### Verifica screenshot (Pictures/Screenshots, 10:38)
- ESITO: NON idonei, rifatti col video sbagliato. La dashboard mostra
  `videoplayback (2).mp4` (il PROVVISORIO di terzi, INC-009: watermark,
  frecce, diritti non chiariti) con KPI 2 bracciate / Fluidity 0.0,
  in contraddizione con il deck (10 / 93,1) e non pubblicabile.
- Non copiati nella cartella Desktop. Istruzioni date: ripetere con il
  video UFFICIALE `test_videos/profilo_test.mp4` (KPI attesi 10 / 93,1).

### Stato iterazione
- Server attivo; screenshot da rifare sul video ufficiale; fix INC-012
  proposti e in attesa di OK.

## 2026-07-14 11:00 +02:00 - Screenshot rifatti sul video ufficiale: dashboard OK, gap T38 chiuso

### Messaggio utente
- "ora?" con i due nuovi screenshot allegati (rifatti dopo il rigetto dei
  precedenti).

### Verifica e azioni
- Screenshot 105353 (dashboard completa): IDONEO. Video ufficiale
  profilo_test.mp4 caricato, KPI reali 10 bracciate / Fluidity 93,1,
  grafico onda con i 10 picchi regolari, angolo live sovrimpresso.
  Numeri COERENTI con pitch deck e README. Nessun dato sensibile.
- Screenshot 105401 (primo piano frame annotato): SCARTATO. Contiene il
  popup dello Strumento di cattura sovrimpresso (con miniatura); inoltre
  ridondante con demo_frame_annotato.png gia' esistente a piena
  risoluzione. Nessuna nuova cattura necessaria.
- Copiato lo screenshot idoneo come demo_dashboard.png sia nella cartella
  Desktop pitch_claude_design sia in docs/pitch/ (versionato).
- LEGGIMI_upload.txt aggiornato: demo_dashboard.png elencato (slide 5),
  sezione "cosa manca" sostituita da "cartella COMPLETA".
- Con questo si chiude il gap dichiarato in T38 (screenshot dashboard live
  da rehearsal umana): tutti gli asset pitch sono ora reali e completi.

### Stato iterazione
- Cartella Desktop completa e pronta per l'upload su Claude Design.
- Restano in attesa di OK i due fix di INC-012 (guard file_id upload +
  width="stretch" al posto di use_container_width deprecato).

## 2026-07-14 11:10 +02:00 - Fix INC-012 approvati e applicati

### Messaggio utente
- "vai si procedi non avevo letto scusa": approvazione dei due fix.

### Azioni
- `app.py` / `persist_uploaded_video`: guard sul `file_id` in session_state
  (+ controllo esistenza file): la cache `.cache/uploaded_session.mp4` viene
  riscritta solo quando l'upload cambia davvero, mai a ogni rerun. Rimossa
  la causa plausibile del segfault (troncamento del file sotto il decoder
  nativo durante l'elaborazione).
- `app.py` riga 213: `use_container_width=True` -> `width="stretch"` nel
  rendering frame (deprecazione: un warning per frame eliminato).
- Validazione: check funzionale dedicato del guard 4/4 (su path di test,
  senza toccare la cache reale del server attivo); py_compile OK; AppTest
  0 eccezioni; suite motore 23/23. INC-012 aggiornato a MITIGATO.
- Nota operativa: Streamlit riesegue app.py dal sorgente a ogni rerun,
  quindi basta ricaricare la pagina per avere il fix attivo; nessun
  riavvio del server necessario.

### Stato iterazione
- INC-012 mitigato (resta il limite architetturale rerun-durante-inferenza,
  con la raccomandazione demo di non toccare i widget durante il run).
- Nessuna task di breakdown aperta; restano le azioni utente note
  (rehearsal con proiettore, decisione momento webcam live).

## 2026-07-14 12:01 +02:00 - Audit finale pre-presentazione e piano in attesa di approvazione

### Messaggi utente
- Richiesto di catalogare ogni iterazione e messaggio in `prompt_log.md` prima
  dell'output e di mantenere `incidents.md` come registro degli incidenti.
- Obiettivo: continuare il breakdown con data odierna, leggere integralmente i
  due allegati, l'intero prompt log e breakdown status, analizzare tutto il
  progetto e le discordanze, individuare task successive/arretrate, verificare
  Git locale vs origin, valutare il README e presentare un piano prima di
  qualsiasi costruzione.
- Subtask: il progetto e' considerato finito lato software; manca la
  presentazione. Prima eseguire un audit; in una fase successiva l'utente
  indichera' una cartella Desktop da cui creare un file `.pptx`.
- Vincolo esplicito: non inventare e non modificare/costruire prima
  dell'approvazione del piano.
- Follow-up durante l'audit: "tutto bene ti sei bloccato?". Risposta: audit non
  bloccato, in fase di registrazione finale prima della consegna del piano.

### Messaggi/azioni assistente - perimetro e letture
- Confermato che questa iterazione sarebbe rimasta un audit in sola lettura;
  nessuna funzionalita' o presentazione costruita. La skill Presentations e'
  rinviata alla fase in cui l'utente indichera' la cartella sorgente.
- Inventariata la repo completa, inclusi file tracciati, runtime ignorati e
  asset binari. Nessun `AGENTS.md` o altra istruzione locale presente.
- Letti integralmente i due allegati:
  - breakdown v1: 20.985 byte, 409 righe, SHA256
    `951D4821A40A60F1A45937D82E8B4B57369CA80B5D2E966469C1066ACBA22A79`;
  - Technical Spec v1.1: 31.507 byte, 530 righe, SHA256
    `99974568064C0CFD36572FFF6028ED5B059B519FE5D263CA0572E517F268B45C`.
- Letti integralmente `prompt_log.md` (prima di questa entry: 1.428 righe),
  `breakdown_status.md`, `incidents.md`, `HANDOFF.md`, `README.md`, `spec.txt`,
  `SPEC_ERRATA.md`, requirements, gitignore, tutto il codice Python e il
  sorgente del pitch deck. Verificata la history dei commit task T01-T41.
- La differenza byte-per-byte tra Technical Spec allegata e `spec.txt` e'
  intenzionale: la copia repo e' la versione ASCII normalizzata, portata da
  BOZZA a CONGELATA con registro freeze T01; contenuto e sezioni 0-16 restano
  semanticamente allineati. Il breakdown sorgente allegato non e' invece
  versionato nella repo: resta un piccolo gap di tracciabilita'.

### Verifica Git/GitHub
- Usata la skill GitHub per orientare il controllo remoto e il Git locale per
  la divergenza effettiva della checkout. Repo confermata:
  `Maxdavi789/Acquatic-intelligence-system`, pubblica, default branch `main`.
- Eseguito `git fetch --prune origin`; `HEAD` e `origin/main` coincidono a
  `a959c6c07069d5663e514393aa9b4d6a776147c5` (0 ahead / 0 behind).
- Working tree pulita prima di questa entry. Nessun push, pull o write remoto.
  Il connettore GitHub disponibile in questa sessione e' read-only; cio' non
  modifica lo stato delle credenziali Git locali usate in passato.

### Validazione tecnica eseguita
- Ambiente: Python 3.12.10, OpenCV 4.11.0, MediaPipe 0.10.21 con
  `mp.solutions.pose`, NumPy 1.26.4, Pandas 3.0.3, Streamlit 1.59.1.
- `pip check`: nessuna dipendenza rotta.
- Suite `scripts/test_metrics.py`: 23/23 test passati.
- `py_compile`: tutti i moduli applicativi e gli script compilano.
- Streamlit AppTest: 0 eccezioni, 2 colonne, titolo corretto.
- Pipeline CLI sul video ufficiale: 175/175 frame con posa, 10 bracciate,
  Fluidity 93,1, angoli [58,49; 179,92], exit 0.
- Verificati hash video: ufficiale
  `2102C40...5CD83`; provvisorio locale ignorato
  `49702466...906A3`. La cache upload corrente coincide con il video ufficiale.
- Asset pitch raster ispezionati uno per uno: diagramma, dashboard, export,
  frame annotato, onda del polso e sequenza. PDF strutturalmente integro
  (`%PDF-1.4`, EOF presente, 10 pagine, 406.339 byte).
- La skill PDF non ha potuto validare visivamente le pagine: Poppler non e'
  installato, Edge headless ha reso una pagina bianca e non esiste una sessione
  browser integrata. Nessuna dipendenza installata per rispettare l'ambiente.
  Questo limite non riguarda il futuro `.pptx`, che avra' un ciclo autonomo di
  rendering e verifica.

### Findings reali dell'audit
1. `scripts/analyze_video.py` usa ancora come default il video storico
   `profilo_provvisorio.mp4`, ignorato da Git. Il README presenta invece il
   comando senza argomenti come analisi del video ufficiale. Su questa macchina
   il comando produce 2 bracciate / Fluidity 0; su un clone pulito puo' fallire.
2. `breakdown_status.md` e `HANDOFF.md` contengono sezioni stale: M8/T39 ancora
   indicata come bozza in revisione e azioni utente (nome/importo/revisione)
   gia' chiuse; stato Git/punto di ripresa e prossima M8 non aggiornati.
3. Il pitch corrente contiene claim troppo assoluti rispetto alle evidenze:
   "rischio software azzerato" non e' coerente con INC-012; "MAI
   sovrastimare" e' smentito dal vecchio test provvisorio manuale 1 vs auto 2;
   "nessun video salvato" va precisato perche' l'upload viene materializzato
   su disco nella cache gitignored e oggi resta dopo la sessione.
4. Gli asset sono autentici ma da selezionare meglio per il nuovo PPTX:
   `demo_export_csv.png` mostra anche due righe storiche 2/0,0 e la sequenza
   include un evidente artefatto di tracking al frame 100. Dashboard, frame
   singolo, onda e diagramma architettura sono idonei.
5. `streamlit` e `pandas` restano non pinnati in `requirements.txt`: non viola
   il DoD T02 (che richiedeva MediaPipe), ma e' un rischio residuo per una
   reinstallazione futura realmente riproducibile.
6. Il README e' sostanzialmente buono ma va aggiornato per: default CLI
   ufficiale, wording privacy/cache, claim conservativi e mitigazione INC-012.

### Piano validato proposto - attende approvazione utente
1. Correggere il default CLI al video ufficiale e aggiungere un controllo di
   regressione/smoke test sul comando senza argomenti; registrare il finding in
   `incidents.md`.
2. Riallineare `breakdown_status.md` e `HANDOFF.md` allo stato 2026-07-14:
   T01-T41 chiuse, T39 revisionata, T38 asset completi, INC-012 mitigato,
   prossimo lavoro = presentazione PPTX.
3. Aggiornare README e sorgente pitch con formulazioni difendibili; chiarire
   cache upload e limiti; eliminare assoluti non sostenuti dalle prove.
4. Pin opzionale ma raccomandato delle versioni Streamlit/Pandas validate e
   nuova verifica `pip check`/test/AppTest/pipeline ufficiale.
5. Preparare gli asset per il deck finale: export solo della riga ufficiale e
   sequenza senza frame di tracking degradato. Versionare anche il breakdown
   sorgente allegato per tracciabilita', se approvato.
6. Aggiornare governance con soli esiti reali, creare un commit locale di
   hardening/documentazione; nessun push senza nuovo OK esplicito.
7. Dopo che l'utente indichera' la cartella Desktop, usare la skill
   Presentations per creare il `.pptx`, renderizzarlo e iterare fino a QA
   visiva completa.

### Stato iterazione
- Audit concluso; software core sano e test verdi, ma non dichiarato "tutto
  perfetto" per i finding sopra.
- Nessun codice, documento di stato, incidente, README, asset o presentazione
  modificato in questa iterazione. Unica modifica: questa entry obbligatoria di
  `prompt_log.md`.
- In attesa dell'approvazione o correzione del piano.

## 2026-07-14 12:12 +02:00 - Piano approvato: hardening pre-presentazione completato

### Messaggio utente
- "procedi": approvazione del piano in sette punti esposto dopo l'audit.
- Perimetro applicato: correzioni locali, asset e governance, validazione e
  commit locale; nessun push e nessuna creazione PPTX in questa fase.

### Correzione CLI e test
- `scripts/analyze_video.py`: `DEFAULT_SOURCE` e help spostati dal vecchio
  `profilo_provvisorio.mp4` gitignored al video ufficiale versionato
  `test_videos/profilo_test.mp4`.
- Aggiunto `scripts/test_project_smoke.py` con tre check: default ufficiale
  presente, MediaPipe legacy Pose disponibile, primo render Streamlit senza
  eccezioni e con due colonne.
- INC-2026-07-14-013 registrato e chiuso.

### Riproducibilita' dipendenze
- `requirements.txt`: pinnati `streamlit==1.59.1` e `pandas==3.0.3`, versioni
  effettivamente installate e validate in questa baseline.
- Delta documentato in `SPEC_ERRATA.md`; nessuna modifica funzionale o
  architetturale alla spec congelata.

### Governance e contenuti
- `HANDOFF.md` ricostruito sullo stato reale: T01-T41 complete, T38/T39 chiuse,
  prossimo deliverable `.pptx`, baseline, demo, privacy/cache, INC-011/012,
  Git e trappole operative.
- `breakdown_status.md` riallineato: M8 5/5, T39 revisionata, asset completi,
  hardening pre-presentazione e azioni residue fuori breakdown.
- README aggiornato con smoke test, pin completi, default CLI ufficiale,
  wording prudente su occlusioni/INC-012 e descrizione esatta della cache
  `uploaded_session.mp4`.
- `docs/pitch/pitch_deck.md`: rimosse formule assolute (rischio "azzerato",
  "mai sovrastima", ripetibilita' "all'infinito"); precisati protocollo
  testato, cache locale e necessita' di ricalibrazione nel dominio acqua;
  aggiunti riferimenti a screenshot dashboard e diagramma architettura.
- INC-2026-07-14-014 registrato e chiuso.
- Aggiunta in `docs/governance/` una copia UTF-8 con newline normalizzate del
  breakdown allegato. Confronto del contenuto normalizzato: identico alla
  sorgente Downloads.

### Asset pitch
- Aggiunto `scripts/generate_pitch_assets.py` per rigenerare in modo
  riproducibile due asset dalla baseline ufficiale.
- `demo_export_csv.png`: ora mostra soltanto la sessione ufficiale
  (10 bracciate, Fluidity 93,1, angolo medio 163,17, max 179,92), senza le due
  righe storiche 2/0,0.
- `demo_sequenza.jpg`: rigenerata su 12 frame ufficiali; il frame 100 con
  tracking degradato e' sostituito dal frame 110 pulito.
- Entrambi gli asset sono stati aperti e ispezionati visivamente: testo
  leggibile, nessun clipping, skeleton coerente e nessun artefatto evidente.
- Il primo avvio dello script asset nel sandbox non ha trovato l'interprete
  base del venv; rilanciato con il permesso previsto e completato. E' un limite
  del sandbox gia' noto, non un incidente applicativo.

### Validazione finale
- `git diff --check`: verde.
- `py_compile`: app, motore, tracker, CLI, test e generatore asset verdi.
- Versioni pin verificate a runtime: Streamlit 1.59.1, Pandas 3.0.3.
- `pip check`: nessuna dipendenza rotta.
- Suite metriche: 23/23 test passati.
- Smoke progetto: 3/3 passati.
- CLI SENZA argomenti: 175/175 frame con posa, 10 bracciate, Fluidity 93,1,
  angoli [58,49; 179,92], exit 0. Il problema INC-013 non e' riproducibile.

### Stato iterazione
- Hardening approvato completato; il core software non ha subito cambi di
  algoritmo.
- Presentazione PPTX non ancora creata: attende la cartella Desktop indicata
  dall'utente e l'uso della skill Presentations con render/QA.
- Commit locale dedicato preparato in chiusura; nessun push eseguito.

## 2026-07-14 12:27 +02:00 - Presentazione finale PPTX creata e verificata

### Messaggio utente
- `C:\Users\user\Desktop\pitch_claude_design`: indicazione della cartella
  sorgente Desktop richiesta dopo l'audit e l'hardening.

### Messaggi assistente catalogati
- Comunicato l'avvio della fase Presentations: inventario integrale della
  cartella, lettura delle regole tecniche, costruzione del deck e QA slide per
  slide prima della consegna.
- Segnalato che `pitch_deck.md`, `demo_export_csv.png` e
  `demo_sequenza.jpg` nella cartella Desktop erano precedenti all'hardening;
  dichiarata la scelta di usare la repo revisionata come fonte autorevole,
  mantenendo struttura, ordine e tono indicati dall'utente.
- Segnalato un problema ambientale del generatore: il runtime
  `@oai/artifact-tool` non veniva risolto dalla HOME implicita. Corretto senza
  installare dipendenze, usando il runtime Codex gia' presente sotto la HOME
  dell'utente e il relativo interprete Python per i tool di rendering.
- Comunicato il completamento del deck di 10 slide e l'avvio del QA PowerPoint
  reale (render, overflow, sovrapposizioni e controllo visivo).
- Comunicato il superamento del controllo slide per slide e l'aggiornamento
  obbligatorio di governance/incidenti prima della consegna.

### Lettura e verifica delle fonti
- Usata la skill Presentations; letti integralmente `content-rules.md`,
  `ARTIFACT.md`, `design_tokens.json`, `API_QUICK_START.md` e `API_DOCS.md`.
- Analizzato l'intero registro dei 26 layout Codex Grid e ispezionati il
  montage della libreria, i preview e i moduli JavaScript esatti dei layout
  selezionati/adattati (cover, image split, callout, comparison, metriche,
  evidence rail, timeline e closing).
- Letti integralmente i tre file testuali della cartella Desktop
  (`pitch_deck.md`, `README.md`, `LEGGIMI_upload.txt`); inventariati e hashati
  tutti i sei asset raster.
- Confronto con `docs/pitch/`: quattro asset coincidevano byte per byte;
  export CSV e sequenza erano snapshot precedenti. Il pitch Desktop conteneva
  i claim assoluti gia' corretti da INC-014. Registrato INC-015.
- Usato `docs/pitch/pitch_deck.md` revisionato e gli asset autentici della repo:
  frame annotato, dashboard reale, export ufficiale pulito e diagramma della
  pipeline. Nessuna immagine inventata o reperita sul web.

### Costruzione del deck
- Comunicazione definita: al termine, docenti/valutatori devono comprendere
  che la pipeline software locale e' stata provata sul protocollo testato e
  che il finanziamento richiesto serve a produrre l'evidenza hardware/in acqua.
- Creata una presentazione 16:9 di 10 slide in italiano, con sistema visivo
  Codex Grid (bianco, nero, pannelli grigi, accento azzurro), gerarchia
  tipografica da presentazione e oggetti PowerPoint editabili.
- Narrazione: problema -> separazione del rischio -> soluzione -> demo ->
  validazione onesta -> confine tra provato e da validare -> architettura ->
  roadmap -> richiesta.
- Claim mantenuti entro le evidenze: rischio software "ridotto e misurato",
  ripetibilita' limitata allo stesso MP4/condizioni validate, nessuna validita'
  biomeccanica in acqua, privacy descritta includendo la cache locale
  gitignored, disclaimer non-medicale conservato.
- Numeri mostrati: 10 bracciate, Fluidity 93,1, 175/175 frame, manuale 10 vs
  automatico 10, 23/23 test metriche e due run identiche sullo stesso MP4.

### QA e consegna
- Generatore: `@oai/artifact-tool`; nessun uso di `python-pptx`.
- Esportate preview e layout strutturali di tutte le slide; creato montage.
- Eseguito `render_slides.py` sul PPTX, quindi `slides_test.py`: test passato,
  nessun overflow.
- Ispezionate visivamente tutte le 10 slide renderizzate a piena dimensione:
  nessun clipping, testo illeggibile o sovrapposizione involontaria; flusso e
  coerenza grafica approvati.
- Copiato il file finale in
  `C:\Users\user\Desktop\pitch_claude_design\AI_Swimming_Motion_Analyzer_Final.pptx`.
  Dimensione 2.137.738 byte; SHA256
  `7DCEDA0C7EC9237580882A60038C70DBFD6554D956E61E723E45A2D0567EBA17`;
  hash identico all'artefatto QA.
- `breakdown_status.md` e `HANDOFF.md` aggiornati alla data odierna: T01-T41
  restano chiuse e anche il deliverable PPTX esterno al breakdown e' ora
  completato. Il README non richiede un'altra modifica: descrive gia'
  correttamente progetto, demo, limiti e governance; il PPTX e' consegnato
  fuori repo nella cartella esplicitamente indicata.
- Nessun push eseguito. Il branch resta con il commit di hardening locale
  `707e7b5` non pubblicato; gli aggiornamenti governance di questa iterazione
  restano modifiche locali non committate in attesa di un eventuale nuovo OK.

## 2026-07-14 12:52 +02:00 - Aggiunta slide finale di ringraziamento

### Messaggio utente
- "e' perfetta la presentazione manca solo una slide finale di
  ringraziamenti.": approvazione esplicita delle prime 10 slide e richiesta di
  una sola aggiunta conclusiva.

### Messaggi e metodo assistente
- Comunicato l'uso della skill Presentations e il vincolo di mantenere intatte
  le 10 slide approvate, aggiungendo soltanto una slide 11 coerente.
- Letti nuovamente e integralmente `SKILL.md`, le regole narrative, la guida
  template-following e la documentazione artifact-tool. Il PPTX esistente e'
  stato trattato come riferimento visuale esclusivo.
- Ispezionate tutte le 10 slide sorgente, i layout, gli oggetti, i font e gli
  asset. La slide 10 e' stata scelta come layout ereditato per la chiusura.
- Lo script di ispezione template ha richiesto `unzip` nel PATH: usata
  l'utility gia' inclusa in Git per Windows. La prima generazione del contact
  sheet cercava `python3`: ripetuta senza quella opzione e creato il montage
  con l'interprete Python gia' incluso nel runtime Codex. Nessuna dipendenza
  installata e nessuna modifica al progetto applicativo.

### Modifica eseguita
- Creato un template starter da 11 slide: output 1-10 duplicano e preservano
  le rispettive slide sorgente; output 11 duplica la slide 10.
- La slide 11 riusa soltanto oggetti ereditati. Testi finali:
  `AI SWIMMING MOTION ANALYZER`, `Grazie.`,
  `Domande, osservazioni o idee per la fase in acqua?`, repository e
  `Massimo Davide Fedrigo · ITS ICT Academy Roma`; pagina `11`.
- Il pannello "Prossimo passo" duplicato e i relativi elementi sono stati
  eliminati dalla sola slide 11 per ottenere una chiusura sobria e ariosa.
  Nessuna delle prime 10 slide e' stata modificata.

### QA e consegna
- Validazione del piano template: PASS, 0 finding.
- Template fidelity check: PASS, 0 finding; prime 10 slide preservate.
- Render PowerPoint completo di 11 slide e montage eseguiti.
- `slides_test.py`: PASS, nessun overflow. Slide 11 e flusso complessivo
  ispezionati visivamente a piena dimensione: nessun clipping,
  sovrapposizione o wrapping inatteso.
- File Desktop sovrascritto con la versione definitiva:
  `C:\Users\user\Desktop\pitch_claude_design\AI_Swimming_Motion_Analyzer_Final.pptx`.
  Dimensione 2.140.554 byte; SHA256
  `26420EC1E218161A805C5EF0356489B991F88C8644A51C02390F322B445EB3FD`;
  hash identico all'artefatto QA.
- `breakdown_status.md` e `HANDOFF.md` aggiornati: presentazione finale = 11
  slide (10 narrative + ringraziamenti). Nessun nuovo incidente applicativo e
  nessun push eseguito.

## 2026-07-14 12:59 +02:00 - Avvio cliccabile e pubblicazione finale autorizzata

### Messaggio utente
- "fai commit/push e dimmi che file devo cliccare per avviare il programma":
  autorizzazione esplicita a committare e pushare; richiesta di un entrypoint
  Windows chiaro e cliccabile.

### Verifica e decisioni
- Usata la skill `github:yeet` per delimitare lo scope di pubblicazione.
- Worktree iniziale: branch `main`, un commit locale di hardening gia' ahead
  rispetto a `origin/main`, piu' quattro modifiche governance della fase PPTX.
- Nessun launcher `.bat`, `.cmd`, `.ps1` o `.exe` era presente: il solo
  entrypoint applicativo era `app.py`, che non va avviato con doppio clic
  perche' richiede il runner Streamlit.
- GitHub CLI (`gh`) non era installato. Il tentativo di installazione e' stato
  bloccato perche' persistente e non necessario al push richiesto. Scelta la
  strada piu' sicura: `git push` HTTPS gia' configurato, senza installazioni e
  senza PR (l'utente ha chiesto il push diretto).

### Modifiche incluse
- Aggiunto `AVVIA_APP.bat` nella root: cambia directory nella repo, verifica
  `venv\Scripts\python.exe`, mostra istruzioni leggibili se manca il venv e
  avvia `python -m streamlit run app.py`. Il file mantiene aperta la finestra
  in caso di uscita, salvo `NO_PAUSE` usato dai test automatici.
- Il primo check non bloccante con `--help` ha raggiunto correttamente
  Streamlit ma il testo help di Click conteneva una freccia Unicode non
  codificabile dalla console cp1252 italiana. Non e' un difetto dell'avvio
  normale. Aggiunta l'opzione interna `--check`, che esegue soltanto
  `streamlit version` e consente di validare il launcher senza aprire il
  server o dipendere dall'help Unicode.
- README aggiornato: `AVVIA_APP.bat` indicato come avvio Windows con doppio
  clic, mantenendo il comando PowerShell come alternativa.
- Presentazione definitiva da 11 slide copiata e versionata in
  `docs/pitch/AI_Swimming_Motion_Analyzer_Final.pptx`; hash identico alla copia
  Desktop gia' validata.
- `HANDOFF.md` e `breakdown_status.md` aggiornati con launcher e percorso della
  copia PPTX versionata.

### Pubblicazione
- Scope del commit: hardening pre-presentazione gia' committato ma non ancora
  pubblicato, governance finale, INC-015, prompt log, launcher, README e PPTX
  definitivo. Nessuna modifica estranea rilevata.
- Validazioni, commit e push su `origin/main` eseguiti in chiusura di questa
  iterazione; nessuna PR richiesta o creata.

## 2026-07-14 - Audit post-pull finale e piano in attesa di approvazione

### Messaggio utente
- Richiesto di catalogare ogni messaggio in `prompt_log.md` prima dell'output
  finale e di registrare tutti gli incidenti in `incidents.md`.
- Obiettivo: leggere integralmente i due allegati, l'intero prompt log e il
  breakdown status; confrontare documenti, progetto e repository; individuare
  prossima task e arretrati; verificare Git locale/remoto e README; presentare
  un piano validato senza iniziare a costruire.
- Subtask: il progetto e' stato finito sull'altra postazione; eseguire il pull
  e concludere.

### Letture e analisi eseguite
- Usata la skill GitHub per orientare il controllo del repository corretto
  `Maxdavi789/Acquatic-intelligence-system`; nessuna PR o issue coinvolta.
- Individuata la working tree in `C:\none\Acquatic-intelligence-system`.
- Letti integralmente gli allegati Technical Spec v1.1 e breakdown task v1,
  `prompt_log.md`, `breakdown_status.md`, `incidents.md`, `HANDOFF.md`, README,
  `SPEC_ERRATA.md`, requirements, gitignore, launcher, codice applicativo,
  script di test/validazione/generazione asset e sorgente pitch.
- Il breakdown versionato in `docs/governance/` e quello allegato risultano
  identici dopo normalizzazione newline (20.620 caratteri ciascuno).
- Confermato dal codice che T01-T41 sono implementate: simmetria fuori
  pipeline, MP4 ufficiale come default, dashboard/export, gestione errori,
  test e deliverable PPTX finale presenti.

### Git e pull richiesto
- Stato iniziale: working tree pulita, `main` al commit `19d9732`, uguale al
  riferimento `origin/main` locale ma non ancora aggiornato dal server.
- `git fetch origin` ha rilevato `origin/main` avanti fino a `8c32125`.
- Eseguito `git pull --ff-only`: fast-forward pulito `19d9732 -> 8c32125`,
  senza merge o conflitti. Recuperati hardening, smoke test, breakdown
  canonico, launcher Windows, presentazione finale e governance aggiornata.
- Verifica post-pull: `HEAD == origin/main == 8c3212510ba2f9f4a03be3ab26407acd6a0c56cc`,
  divergenza 0 ahead / 0 behind.

### Findings
- Breakdown: nessuna task T01-T41 arretrata o bloccata; il prossimo lavoro e'
  fuori breakdown (rehearsal umana e decisione webcam best-effort).
- README: sostanzialmente accurato e completo; nessuna correzione contenutistica
  necessaria prima della verifica runtime locale.
- Governance: `HANDOFF.md` e l'introduzione di `breakdown_status.md` conservano
  alcune frasi storiche pre-push (`a959c6c` / correzioni ancora locali), mentre
  Git dimostra che il commit finale `8c32125` e' gia' pubblicato.
- Ambiente corrente: il `venv` locale non parte perche' punta a un interprete
  Python 3.12.10 non piu' presente; `python` e `py` non sono nel PATH. Per
  questo suite, smoke e `pip check` non hanno potuto avviarsi. Registrato
  INC-2026-07-14-016; nessuna dipendenza installata o ambiente ricreato senza
  approvazione.

### Stato iterazione
- Nessun codice, README, breakdown status o dipendenza modificati.
- Modificati soltanto `prompt_log.md` e `incidents.md`, come richiesto dalla
  governance; queste due modifiche locali non sono committate ne' pushate.
- Piano di conclusione preparato e in attesa di approvazione dell'utente.

## 2026-07-14 - Chiarimento sull'ordine pull / prompt log

### Messaggio utente
- Domanda: il pull e' stato eseguito prima di aggiornare `prompt_log.md`?

### Risposta e stato
- Si'. L'ordine e' stato: verifica working tree pulita; `git fetch origin`;
  `git pull --ff-only` da `19d9732` a `8c32125`; verifica 0 ahead / 0 behind;
  lettura e audit del contenuto aggiornato; infine aggiunta dell'entry locale
  al prompt log prima dell'output finale.
- Questo ordine non ha perso o sovrascritto messaggi: il pull era un
  fast-forward su working tree pulita e ha recuperato integralmente il prompt
  log remoto; la nuova entry e' stata poi aggiunta sopra quella baseline ed e'
  attualmente una modifica locale non committata.

## 2026-07-14 - Feedback sulla modalita' webcam sperimentale

### Messaggio utente
- La preview webcam si ferma dopo 300 frame; richiesta indicativa di aumentarla
  a 3.000 frame.
- Osservazione: il tracking sembra concentrarsi su un solo braccio e rilevare
  il secondo soltanto a tratti.

### Analisi eseguita (nessuna modifica applicativa)
- Confermato in `app.py` il limite `WEBCAM_PREVIEW_FRAMES = 300`, passato al
  loop tramite `max_frames`: e' una scelta configurativa introdotta da T28 per
  assicurare la conclusione automatica e il rilascio della webcam.
- Confermato in `metrics_engine.py` che `select_camera_side_arm` confronta i
  landmark sinistri 11/13/15 e destri 12/14/16 e sceglie a ogni frame il lato
  con visibility media maggiore. Il motore calcola quindi metriche su un solo
  arto, come richiesto da RF-004 e dalla decisione DA-01 della spec laterale.
- L'overlay MediaPipe prova comunque a disegnare entrambi gli arti. Un braccio
  intermittente e' compatibile con bassa visibility/occlusione, soprattutto
  se la webcam non e' perfettamente laterale; la selezione frame-per-frame puo'
  inoltre alternare il lato quando le visibility sono vicine.
- Registrato INC-2026-07-14-017. Nessun cambio a durata, tracking, spec o UI e'
  stato applicato prima dell'approvazione.

### Piano proposto
- Aumentare la preview webcam a 3.000 frame e aggiornare test/documentazione.
- Mostrare chiaramente nella UI quale arto viene analizzato.
- Stabilizzare il lato scelto per la sessione (lock dopo una breve fase
  affidabile, fallback solo dopo perdita prolungata) e aggiungere indicazioni
  per la ripresa laterale; mantenere fuori scope la simmetria e le metriche
  bilaterali, salvo nuova decisione esplicita dell'utente.

## 2026-07-14 - Decisione webcam 900 frame e prodotto bilaterale futuro

### Messaggio utente
- Precisato che la capacita' di considerare entrambe le braccia fara' parte
  del prodotto finito; chiesto se una metrica bilaterale con telecamera
  frontale sia tecnicamente possibile.
- Corretto il requisito di durata: 300 frame restano insufficienti, ma il
  valore richiesto e' 900 frame (non 3.000).

### Decisione tecnica
- Confermato che una modalita' bilaterale frontale e' tecnicamente possibile:
  deve mantenere due stati separati (destro/sinistro) e definire metriche di
  confronto coerenti col nuovo piano di ripresa. Non va confusa con il vecchio
  Symmetry Score del PoC laterale, escluso per ragioni geometriche.
- Per non ampliare implicitamente lo scope dell'MVP corrente, in questa
  iterazione viene applicato soltanto il requisito esplicito dei 900 frame; la
  modalita' bilaterale viene registrata nella roadmap/errata come lavoro futuro
  da specificare e validare separatamente.

### Modifiche applicate
- `app.py`: `WEBCAM_PREVIEW_FRAMES` da 300 a 900.
- `scripts/test_project_smoke.py`: nuovo controllo del budget webcam; smoke
  atteso da 3/3 a 4/4.
- README, SPEC_ERRATA, breakdown status e INC-017 aggiornati.
- Verifica statica: `git diff --check` verde; ricerca globale conferma 900 nei
  riferimenti operativi. Le occorrenze 300 residue descrivono soltanto lo stato
  storico di T28 e la segnalazione iniziale.
- Validazione runtime pendente per INC-016: il venv locale punta a un
  interprete Python non piu' presente. Nessun risultato di test inventato.

## 2026-07-14 - Ripristino Python/venv e validazione runtime completa

### Messaggio utente
- Richiesto esplicitamente di risolvere il problema del `venv` non avviabile,
  invece di lasciare i test runtime pendenti.

### Diagnosi e ripristino
- Confermata l'assenza di `python`, `py`, `winget`, Chocolatey e Scoop nella
  sessione; il percorso base registrato in `venv\pyvenv.cfg` non era presente.
- Verificata sul sito ufficiale python.org la disponibilita' dell'installer
  Windows 64-bit CPython 3.12.10, versione esatta della baseline.
- Scaricato in `C:\tmp\python-3.12.10-amd64.exe`; SHA256
  `67B5635E80EA51072B87941312D00EC8927C4DB9BA18938F7AD2D27B328B95FB`;
  firma Authenticode valida della Python Software Foundation.
- Installazione silenziosa per l'utente corrente completata con exit code 0.
  Python base, launcher del venv e pip hanno risposto come Python 3.12.10;
  non e' stato necessario cancellare o ricreare il venv.
- Controllo versioni dirette: MediaPipe 0.10.21, OpenCV 4.11.0, NumPy 1.26.4,
  Pandas 3.0.3 e protobuf 4.25.9 gia' allineati. Streamlit era 1.59.2 ed e'
  stato riportato al pin 1.59.1 tramite pip.

### Validazione finale
- `pip check`: nessuna dipendenza rotta.
- `compileall`: riuscito per app, motore, tracker e script.
- `scripts/test_metrics.py`: 23/23 passati.
- `scripts/test_project_smoke.py`: 4/4 passati, incluso il nuovo controllo
  `WEBCAM_PREVIEW_FRAMES == 900`.
- Pipeline CLI sul video ufficiale: 175/175 frame con posa, 10 bracciate,
  Fluidity 93,1, angoli [58,49; 179,92].
- `AVVIA_APP.bat --check`: exit 0, Streamlit 1.59.1.
- Un primo comando wrapper `cmd /c AVVIA_APP.bat --check` e' fallito per la
  sintassi di invocazione del comando, non per il launcher; il test diretto
  PowerShell `& .\AVVIA_APP.bat --check` e' passato.

### Stato iterazione
- INC-016 chiuso come RISOLTO; breakdown status aggiornato.
- La modifica webcam a 900 frame e' ora validata a runtime tramite smoke 4/4.
- Nessun commit o push eseguito.

## 2026-07-14 - Consultazione: telefono come camera per la demo live in VM

### Messaggio utente
- Chiesto se, qualora la webcam della virtual machine non funzionasse sul posto
  di lavoro, sia possibile presentare la modalita' live usando il telefono.

### Verifica tecnica
- La webcam corrente usa OpenCV server-side (`VideoCapture(0)`): il telefono
  deve quindi apparire come dispositivo video dentro la VM oppure il progetto
  deve acquisire lo stream dal browser/rete.
- Documentazione Microsoft verificata: Windows 11 puo' usare un telefono
  Android 10+ collegato come webcam; RDP supporta la redirezione di camera e
  dispositivi di acquisizione video verso la sessione remota, se consentita
  da client e policy.
- `st.camera_input` nativo di Streamlit restituisce singole fotografie, non un
  flusso video continuo: non sostituisce la modalita' live.
- `streamlit-webrtc` permette invece al browser del telefono di inviare video
  real-time, ma richiede nuova dipendenza e integrazione asincrona/thread-safe;
  da host remoto richiede HTTPS e puo' richiedere STUN/TURN.

### Raccomandazione
- Percorso piu' semplice senza modifiche: Android come camera collegata al PC
  Windows 11, poi redirezione video RDP nella VM; se compare come device 0, il
  codice attuale funziona.
- Percorso piu' robusto rispetto alla VM ma con sviluppo: nuova sorgente
  `Telefono (WebRTC)` nella dashboard, da implementare e provare prima della
  presentazione.
- Fallback garantito: elaborazione live del video MP4 ufficiale. E' comunque
  una demo live della pipeline; la webcam/telefono resta un bonus.
- Nessuna modifica applicativa eseguita in questa iterazione.

## 2026-07-14 - Pubblicazione modifiche e richiesta speech della presentazione

### Messaggio utente
- Richiesto, come prima azione, commit e push delle modifiche locali.
- Fornita/indicata la presentazione gia' prodotta e chiesto di verificare se
  sia aggiornata rispetto allo stato corrente del progetto.
- Richiesto di creare un file Markdown con lo speech e di collocarlo sul
  Desktop in una cartella insieme alla presentazione, spostando quest'ultima
  dalla cartella Download.

### Piano operativo avviato
- Verificato lo scope Git: sette file modificati, tutti appartenenti alle
  iterazioni approvate (webcam 900 frame, smoke 4/4, roadmap bilaterale,
  ripristino ambiente e governance). `git diff --check` verde; `main` e
  `origin/main` partivano entrambi da `8c32125`.
- La skill GitHub `yeet` richiede `gh`, non installato in questa postazione.
  Poiche' l'utente ha chiesto push diretto su `main` e Git HTTPS e' gia'
  configurato, viene usato il fallback Git nativo senza PR e senza installare
  GitHub CLI.
- Corretta prima del commit la frase stantia di INC-017: il runtime dei 900
  frame e' stato validato dallo smoke 4/4 dopo la risoluzione di INC-016.
- Fasi successive: individuare il PPTX piu' recente nei Download, confrontarlo
  con la copia finale versionata e con le modifiche post-pubblicazione,
  ispezionarlo/renderizzarlo, generare lo speech slide-per-slide e creare la
  cartella Desktop richiesta.

### Esito commit e push
- Commit applicativo creato e pubblicato su `origin/main`:
  `5c78f2a Extend webcam preview and restore runtime baseline`.
- Verificata l'identita' tra `HEAD` e `origin/main` dopo il push:
  `5c78f2a5dd8e619b30408f90f88c4a1067490599`.

### Verifica presentazione
- L'allegato nei Download era una versione precedente da 10 slide, SHA256
  `7DCEDA0C7EC9237580882A60038C70DBFD6554D956E61E723E45A2D0567EBA17`.
- La versione finale gia' approvata e versionata in `docs/pitch` contiene 11
  slide, inclusa la chiusura "Grazie", SHA256
  `26420EC1E218161A805C5EF0356489B991F88C8644A51C02390F322B445EB3FD`.
- Il contenuto delle prime 10 slide coincide; l'allegato era quindi integro ma
  non aggiornato alla revisione conclusiva. Le modifiche recenti non alterano
  i KPI centrali della presentazione e sono state integrate nel materiale del
  relatore: webcam sperimentale a 900 frame e roadmap bilaterale frontale.
- Un nuovo rendering in questa VM non e' stato possibile: il runtime di
  presentazione non dispone di `pdf2image` e PowerPoint COM/LibreOffice non
  sono installati. Non e' stato modificato il PPTX; e' stata riutilizzata la
  finale da 11 slide gia' renderizzata e validata in precedenza nella repo.

### Consegna sul Desktop
- Creata la cartella
  `C:\Users\ezioc\Desktop\AI_Swimming_Motion_Analyzer_Presentazione`.
- Spostato l'allegato dai Download e conservato come
  `AI_Swimming_Motion_Analyzer_10_slide_backup.pptx`.
- Copiata nella stessa cartella la revisione ufficiale da 11 slide come
  `AI_Swimming_Motion_Analyzer_Final.pptx`; hash verificato uguale alla copia
  versionata.
- Creato `Speech_AI_Swimming_Motion_Analyzer.md`: speech slide-per-slide,
  traccia della demo, transizioni, risposte alle domande probabili, fallback
  webcam/telefono e chiusura breve.

## 2026-07-14 - Risposta da presentazione: quale AI e' stata usata

### Messaggio utente
- Chiesto cosa rispondere se durante la presentazione viene domandato quale
  intelligenza artificiale sia stata usata nel progetto.

### Verifica e risposta preparata
- Verificato nel codice che il componente AI e' **MediaPipe Pose / BlazePose**:
  rete neurale profonda pre-addestrata per la pose estimation, eseguita
  localmente sulla CPU e capace di restituire 33 landmark corporei.
- Configurazione effettiva: `static_image_mode=False`, `model_complexity=1`,
  smoothing attivo, segmentazione disattiva e soglie detection/tracking 0,5.
- Chiarita la separazione architetturale: BlazePose riconosce i punti del
  corpo; angolo del gomito, conteggio delle bracciate e Fluidity Score sono
  calcolati successivamente con formule e regole deterministiche in Python.
- Nessun LLM o modello generativo, nessuna API cloud, nessuna API key e nessun
  addestramento proprietario del modello. Preparata una risposta orale breve e
  una versione tecnica per eventuali domande di approfondimento.
