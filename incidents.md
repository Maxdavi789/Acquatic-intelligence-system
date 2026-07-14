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
- Aggiornamento 2026-07-13 (sessione casa): il refuso si e' ripresentato
  identico nella consegna di ripresa da casa. Causa ormai nota: la macchina
  ufficio e' autenticata come MrChuck118, proprietario del repo
  live-draft-companion, e il link finisce nei template di consegna. Verificate
  entrambe le repo con `git ls-remote`; l'utente ha riconfermato quella
  corretta e il clone e' stato eseguito dalla repo giusta. Nessun impatto.

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
  il set corretto MediaPipe 0.10.21 / OpenCV contrib 4.11.0.86 / NumPy 1.26.4 /
  protobuf 4.25.9 funziona su 3.12. Nessun fallback a Python 3.11 necessario.

### INC-2026-07-13-005 - requirements.txt non pinnato, matplotlib da valutare
- Tipo: dipendenze.
- Evidenza: `requirements.txt` elenca pacchetti senza versione; `matplotlib` e'
  presente ma nel codice serve solo a impostare `MPLCONFIGDIR` (cache), non per
  grafici (i grafici useranno `st.line_chart`).
- Impatto: rischio di rotture da upgrade (in particolare MediaPipe) e
  dipendenza potenzialmente inutile.
- Stato: risolto.
- Azione eseguita: il primo pin `mediapipe==0.10.35` e' stato corretto dopo
  INC-008 a `mediapipe==0.10.21`, con pin compatibili di OpenCV contrib, NumPy e
  protobuf. Verificato che matplotlib e' dipendenza transitiva di mediapipe;
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

### INC-2026-07-13-008 - MediaPipe 0.10.35 non espone l'API legacy solutions
- Tipo: dipendenza/runtime.
- Evidenza: nell'ambiente corrente `mediapipe==0.10.35` importa, ma
  `hasattr(mediapipe, "solutions")` e' `False`; non esistono neppure i moduli
  `mediapipe.python` / `mediapipe.python.solutions`. Il pacchetto installato
  contiene solo `modules` e `tasks` al top level.
- Impatto: `vision_tracker.py` usa `mp.solutions.pose` e quindi T03/T14 non
  possono eseguire il pose tracking con l'ambiente attuale, indipendentemente
  dalla qualita' del video. I precedenti import check non esercitavano questa
  API runtime.
- Stato: risolto (2026-07-13).
- Azione eseguita: sostituito il runtime con `mediapipe==0.10.21`,
  `opencv-contrib-python==4.11.0.86`, `numpy==1.26.4` e
  `protobuf==4.25.9`; rimosso il pacchetto parallelo `opencv-python` per evitare
  conflitti sul namespace `cv2`. `pip check` e inizializzazione Pose riusciti
  nel venv corrente; installazione da `requirements.txt` riuscita anche in un
  venv temporaneo pulito. Registrata la correzione in `SPEC_ERRATA.md`.

### INC-2026-07-13-009 - Selezione video candidato per T03/T14
- Tipo: input di validazione / protocollo di ripresa.
- Evidenza: `videoplayback.mp4` e' un H.264 640x360 a 30 fps, durata 255,3 s,
  tecnicamente integro (7.660/7.660 frame decodificati). Visivamente e' pero'
  un montaggio subacqueo con intro, cambi scena/inquadratura, piu' soggetti,
  bolle/occlusioni, tratti vuoti, watermark e prospettive non costantemente
  laterali a 90 gradi.
- Impatto: non consente una misura riproducibile ne' il confronto manuale del
  conteggio; viola il protocollo dryland controllato della spec e non puo'
  soddisfare il DoD T03/T14.
- Stato: risolto per T03; restano limiti noti per la validazione finale.
- Azione prevista: richiedere una clip propria, continua e fissa, a secco, con
  una sola persona interamente visibile di profilo e ripetizioni chiare del
  movimento. Il file rifiutato puo' essere conservato solo come futuro stress
  test fuori distribuzione, non come validazione ufficiale.
- Aggiornamento 2026-07-13: valutato anche `videoplayback (1).mp4` (H.264,
  360x640 verticale, 30 fps, 277 frame, 9,23 s; 277/277 frame decodificati).
  E' nettamente migliore del primo candidato per continuita', singolo soggetto
  e vista prevalentemente laterale, ma mostra nuoto reale in vasca: acqua,
  riflessi e immersione occludono parti del corpo; il formato verticale e la
  bassa risoluzione utile limitano il tracking. Rifiutato come riferimento
  T03/T14; idoneo soltanto come futuro stress test fuori distribuzione.
- Aggiornamento 2026-07-13: valutato `videoplayback (2).mp4` (H.264, 360x640
  verticale, 30 fps, 448 frame, 14,93 s; 448/448 frame decodificati). Mostra un
  singolo soggetto a secco su supporto, camera fissa, vista sufficientemente
  laterale e un ciclo completo di bracciata con spalla/gomito/polso visibili.
  Accettato come MP4 PROVVISORIO per T03/T14. Limiti: bassa risoluzione, formato
  verticale, testo/frecce sovrapposti e possibile licenza di terzi. L'idoneita'
  effettiva del tracking resta da misurare dopo la risoluzione di INC-008. Non
  sostituisce il video ufficiale dryland del sandbox T35.
- Aggiornamento 2026-07-13 (test reale): copiato localmente come
  `test_videos/profilo_provvisorio.mp4`, hash SHA256 invariato. MediaPipe Pose ha
  rilevato la posa in 448/448 frame e l'arto lato-camera affidabile in 448/448
  frame (visibilita' minima 0,9341); overlay ispezionato su 12 campioni. Il file
  resta intenzionalmente non tracciato da Git finche' la licenza non e'
  chiarita.
- Aggiornamento 2026-07-13 (sessione casa): il campione provvisorio non viaggia
  con Git (untracked di proposito) ed era rimasto sulla macchina ufficio.
  L'utente lo ha riscaricato sulla macchina di casa: SHA256 verificato e
  IDENTICO (`49702466FF32DA10D633A2FCF41BA2BB594F7A57C979BAF9BAA95D6FCCE906A3`),
  ricopiato in `test_videos/profilo_provvisorio.mp4` e mantenuto untracked.
  Restano validi i limiti noti (risoluzione, formato verticale, possibile
  licenza di terzi): non sostituisce il video ufficiale del sandbox T35.

### 2026-07-13 - Verifica privacy T25 (esito positivo, nessun incidente)
- Tipo: verifica pianificata dal breakdown (T25; spec sez. 8.3 e 10).
- Esito: `data/` contiene SOLO `sessions.csv` (piu' il `.gitkeep`); nessun
  frame, immagine o video persistito altrove nel progetto;
  `data/sessions.csv` e' coperto da `.gitignore` (riga 8) e non finisce su Git.
- Nota di design documentata: l'upload della dashboard scrive un file
  transitorio `.cache/uploaded_session.mp4` (cartella gitignored),
  sovrascritto a ogni nuovo upload; serve a OpenCV per leggere il video
  caricato. Non e' una persistenza di sessione, non tocca `data/` e non
  viene versionato. Comportamento dichiarato nel docstring di
  `persist_uploaded_video` (T16).

### 2026-07-13 - T30: conteggio manuale vs automatico sul video provvisorio
- Tipo: esito test M6 (spec sez. 1.2, tolleranza +-1), non incidente bloccante.
- Conteggio manuale documentato: 1 bracciata completa. Evidenza: sequenza
  frame 300-440 ispezionata (una sola recovery sopra la spalla, frame
  ~340-420) e tracciato polso/spalla (il polso supera la quota spalla UNA
  volta, con oscillazione sul plateau).
- Conteggio automatico: 2 (picchi a frame 358 e 402).
- |differenza| = 1 -> ENTRO la tolleranza +-1 del criterio di successo.
- Causa del +1: il video provvisorio e' una demo didattica LENTA; durante
  la recovery la mano resta ferma vicino alla testa (~1,5 s) e oscilla,
  producendo due inversioni valide sopra la spalla distanti 1,47 s (oltre
  il debounce di 0,6 s, calibrato su bracciate ritmiche).
- Conseguenza per T35: il video ufficiale del sandbox deve contenere
  bracciate CONTINUE e RITMICHE (>= 4-5 cicli), per cui il debounce e il
  criterio +-1 sono progettati; su quel protocollo il plateau anomalo
  scompare.
- Aggiornamento 2026-07-14 (T30 ripetuto sul VIDEO UFFICIALE): conteggio
  manuale dal tracciato polso/spalla e dalla sequenza frame = 10 creste
  complete sopra la quota spalla; conteggio automatico = 10.
  |differenza| = 0: criterio pienamente soddisfatto. Bonus: attorno al
  frame 100 c'e' un'oscillazione parziale che NON supera la spalla,
  correttamente SCARTATA dal gate (prova visiva anti-falsi-positivi).
  Anche T33 ripetuto sul video ufficiale: due run -> KPI e serie angoli
  identici frame per frame.

### 2026-07-13 - T32: casi limite eseguiti e verificati (esito positivo)
- Tipo: esito test M6, non incidente.
- Input non valido: percorso inesistente -> `st.error` leggibile in UI e
  exit 1 con messaggio controllato da CLI; nessuna eccezione non gestita
  (esecuzioni formali T27, 11/11 check).
- Fine stream: video completo e clip sintetica senza persona -> chiusura
  pulita con "Elaborazione terminata", KPI coerenti (esecuzioni T27).
- Stop a meta': interruzione simulata al frame 15 (MP4) e 5 (webcam) ->
  `capture.release()` esattamente una volta, nessun handle appeso,
  webcam subito riapribile (esecuzioni formali T29, 6/6 check).

### INC-2026-07-13-011 - Occlusione prolungata: falso negativo post-occlusione (limite documentato)
- Tipo: comportamento del tracking / limite del modello upstream.
- Evidenza (test T26): su un MP4 con la zona del braccio coperta da un box
  nero per 100 frame (3,3 s), la pipeline NON crasha, NON genera picchi
  spuri e il forward-fill scarta correttamente i dati inaffidabili
  (wrist_y=None su 100/100 frame occlusi). Pero' il tracking MediaPipe
  successivo all'occlusione resta degradato e il secondo picco reale non
  viene rilevato: conteggio finale 1 invece di 2.
- Isolamento della causa: (a) baseline ri-encodata identica senza box ->
  2 picchi come l'originale (il re-encoding non c'entra); (b) iniezione
  deterministica di visibility<0.5 sugli stessi 100 frame con video
  originale -> forward-fill esatto e conteggio finale 2 (il motore
  metriche e' corretto). Il degrado sta nei landmark prodotti da MediaPipe
  dopo un'occlusione lunga, fuori dal controllo della pipeline.
- Impatto: possibile sottostima conservativa delle bracciate dopo
  occlusioni prolungate. Nessuna sovrastima: i picchi spuri restano
  esclusi (RF-008 rispettato).
- Stato: chiuso come limite documentato (coerente con il rischio "falsi
  positivi/negativi dello stroke counter" gia' dichiarato, spec sez. 14.2).
  Mitigazione gia' prevista: sandbox controllato T34-T35 senza occlusioni
  per la validazione ufficiale; conteggio manuale di confronto in T30.
- Aggiornamento 2026-07-13: questa verifica costituisce anche l'esito
  formale del test di occlusione T31 (M6): scenario controllato eseguito,
  nessun picco spurio, nessun crash, esito registrato.

### 2026-07-14 - Video ufficiale adottato in deroga (T35 via DA-05)
- Tipo: decisione di progetto / input di validazione.
- Contesto: la registrazione in proprio (sandbox T34/T35) non e'
  realizzabile. Su richiesta dell'utente e' stata cercata e validata una
  clip stock con licenza libera (opzione gia' prevista da DA-05).
- Selezione: valutati 4 candidati Pexels; 3 scartati (stretching statico,
  vista posteriore, seduta). Adottato Pexels 37264420, HD 720x1280 25fps,
  7,0 s, `test_videos/profilo_test.mp4`, SHA256
  `2102C40B880F6BF5EC3AA04EBC22F769F1A628A4942E042D7AEAD4E1BBF5CD83`,
  VERSIONATO nella repo (licenza Pexels, watermark assenti).
- Validazione pipeline: 175/175 frame con posa, arto destro selezionato,
  10 bracciate con cadenza regolare ~0,7 s, Fluidity 93,1, angoli
  [58,49; 179,92]. Primo KPI Fluidity vivo su footage reale.
- Limiti onesti: 7 secondi; vista laterale non perfetta nei primi istanti
  (3/4); gesto = mulinello in piedi (dorso a secco), non stile libero
  prono; primo picco a t=0,16 s perche' la clip inizia a braccio alzato.
- Dettagli formali in SPEC_ERRATA.md (deroga T34/T35).

### INC-2026-07-14-012 - Segmentation fault del processo Streamlit durante l'uso della dashboard (macchina ufficio)
- Tipo: crash nativo runtime / stabilita' della demo.
- Contesto: dashboard avviata in background per la cattura manuale dello
  screenshot (sessione remota/virtualizzata, vedi INC-010). L'utente stava
  usando l'app; il log mostra un burst di rendering frame (~28 fps, timestamp
  10:34:01) e subito dopo la terminazione del processo Python con
  "Segmentation fault" (exit code 139). Nessuna eccezione Python nel log:
  crash nello strato nativo (MediaPipe/OpenCV), non intercettabile da
  try/except applicativi.
- Evidenza: output del task in background (304 KB); ultima riga
  `Segmentation fault ./venv/Scripts/python.exe -m streamlit run app.py`.
  Browser lato utente: ERR_CONNECTION_REFUSED (processo morto).
- Causa: NON isolata. Ipotesi principale: rerun di Streamlit innescato da
  un'interazione con i widget mentre il loop di elaborazione era attivo puo'
  distruggere l'oggetto Pose a meta' inferenza nativa. Da notare che la
  rehearsal T40 (2 giri consecutivi senza interazioni durante il run) era
  stata pulita, e che l'ambiente e' una sessione RDP/Hyper-V.
- Impatto: il processo muore e la pagina diventa irraggiungibile; nessuna
  perdita di dati persistiti (il CSV non era coinvolto); lo stato KPI in
  session_state va perso. Riavvio immediato possibile e verificato.
- Mitigazioni per la demo: (1) durante l'elaborazione (~4 s) NON toccare i
  widget; (2) tenere pronto il comando di riavvio
  `.\venv\Scripts\python.exe -m streamlit run app.py`; (3) provare la
  rehearsal umana sulla macchina della presentazione, non in sessione RDP.
- Stato: aperto non bloccante, da monitorare; se si ripete, isolare con
  run senza interazioni vs run con interazione deliberata a meta'.
- Aggiornamento 2026-07-14 (bug check su richiesta utente): revisione del
  codice di `app.py` e `vision_tracker.py` alla ricerca della causa.
  (1) CAUSA PLAUSIBILE individuata: `render_input_selector` chiama
  `persist_uploaded_video` a OGNI rerun dello script, riscrivendo
  `.cache/uploaded_session.mp4` da capo (write_bytes = truncate + write).
  Se un rerun parte mentre il loop di elaborazione sta ancora leggendo lo
  STESSO file, il decoder nativo FFmpeg/OpenCV si trova il file troncato
  sotto i piedi: crash nativo non intercettabile, coerente con il segfault
  osservato a meta' rendering. Fix proposto: persistere il file solo quando
  l'upload cambia davvero (confronto `file_id` in session_state).
  (2) CONFERMATO minore: `placeholder.image(..., use_container_width=True)`
  e' deprecato e emette un warning PER FRAME (6.228 righe nel log della
  sessione crashata): rumore e overhead inutili. Fix: `width="stretch"`.
  (3) Limite architetturale non fixabile lato app: il rerun di Streamlit
  puo' interrompere l'inferenza nativa a meta' (spec sez. 14.2); il pattern
  `with create_pose_estimator()` per-run e' invece corretto (nessun oggetto
  Pose condiviso tra thread). Fix (1)+(2) in attesa di approvazione utente.
- Aggiornamento 2026-07-14 (fix applicati con approvazione utente):
  (1) `persist_uploaded_video` ora riscrive la cache SOLO quando il
  `file_id` dell'upload cambia (guard in session_state + controllo
  esistenza file); check funzionale dedicato 4/4: scrittura al primo
  upload, NESSUNA riscrittura al rerun con lo stesso file, riscrittura su
  upload nuovo, rigenerazione se la cache sparisce. (2) `placeholder.image`
  usa `width="stretch"`: eliminato il warning di deprecazione per frame.
  Validazione completa: py_compile OK, AppTest 0 eccezioni, suite 23/23.
- Stato: MITIGATO. La causa plausibile del segfault (troncamento della
  cache sotto il decoder) e' rimossa; resta il limite architetturale del
  rerun durante l'inferenza nativa (documentato sopra), per cui vale
  ancora la raccomandazione di non toccare i widget durante il run.

### INC-2026-07-13-010 - Webcam non disponibile sulla macchina di test
- Tipo: hardware / input secondario best-effort.
- Evidenza: `cv2.VideoCapture(0)` restituisce `isOpened() == False` e OpenCV
  segnala `Camera index out of range`; nessun frame acquisito.
- Impatto: non e' possibile verificare visivamente la modalita' webcam su questo
  hardware. Il percorso MP4 primario e il pose tracking non sono coinvolti.
- Stato: aperto non bloccante.
- Azione eseguita: tentata l'apertura non interattiva e rilasciato il capture.
  T03 considera soddisfatto il requisito webcam come best-effort; ripetere la
  prova quando sara' collegata una webcam reale.
- Aggiornamento 2026-07-13 (macchina casa): risolto su questa macchina. Dopo la
  ripresa da casa e la ricreazione del venv, `cv2.VideoCapture(0)` apre
  correttamente (`isOpened() == True`) e legge un frame reale 480x640x3.
  La modalita' webcam best-effort (RF-014) torna quindi verificabile
  visivamente; la prova UI completa resta in T28. Stato: risolto sulla
  macchina di casa, non bloccante.
- Aggiornamento 2026-07-14 (macchina ufficio, causa individuata): l'utente
  segnala che il PC ha una webcam; nuova diagnosi eseguita. OpenCV non apre
  nessun indice 0-2 ne' col backend MSMF ne' con DirectShow. L'inventario PnP
  di Windows rivela la causa: la sessione in cui gira il codice e' un ambiente
  remoto/virtualizzato (scheda video Hyper-V, NESSUN dispositivo USB) in cui
  e' presente il "Bus fotocamera Desktop remoto" (RDCAMERA_BUS) ma senza
  alcuna camera reindirizzata al suo interno. La webcam fisica appartiene al
  PC client davanti all'utente, non alla sessione remota. Le impostazioni
  privacy webcam di Windows sono su Allow: non sono loro il blocco.
- Rimedio documentato (azione utente): abilitare la redirezione della
  videocamera nel client Desktop remoto prima di connettersi (mstsc:
  Opzioni > Risorse locali > Altro... > spuntare "Dispositivi di acquisizione
  video"; nelle app Remote Desktop/Windows App: impostazioni della connessione
  > reindirizza fotocamera), poi riconnettersi. La camera comparira' sotto il
  bus RDCAMERA e OpenCV potra' aprirla all'indice 0 (modalita' T28 gia'
  pronta). Stato: aperto non bloccante in ufficio; risolto a casa.

### INC-2026-07-14-013 - Default CLI rimasto sul video provvisorio locale
- Tipo: portabilita' / documentazione runtime.
- Evidenza: `scripts/analyze_video.py` impostava `DEFAULT_SOURCE` su
  `test_videos/profilo_provvisorio.mp4`, file storico gitignored e non presente
  in un clone pulito. Il README descriveva invece il comando senza argomenti
  come analisi del video ufficiale. Sulla postazione corrente il residuo locale
  produceva KPI 2 bracciate / Fluidity 0,0 invece dei valori demo 10 / 93,1.
- Impatto: comando documentato non portabile e rischio di mostrare in demo il
  materiale sbagliato.
- Stato: risolto nell'audit pre-presentazione del 2026-07-14.
- Azione eseguita: default e help spostati su
  `test_videos/profilo_test.mp4`; aggiunto `scripts/test_project_smoke.py` per
  controllare default ufficiale, MediaPipe legacy e primo render Streamlit.

### INC-2026-07-14-014 - Claim pitch troppo assoluti rispetto alle evidenze
- Tipo: governance / comunicazione tecnica.
- Evidenza: il sorgente T39 usava "rischio software azzerato", "MAI
  sovrastimare" e "nessun video salvato". INC-012 documenta un segfault poi
  mitigato; il vecchio test provvisorio T30 aveva manuale 1 vs automatico 2;
  l'upload Streamlit viene materializzato su disco in una cache locale
  gitignored necessaria a OpenCV.
- Impatto: presentazione non pienamente coerente con il principio di onesta'
  DA-03 e con la reale gestione del dato video.
- Stato: risolto nel sorgente pitch/README durante l'audit pre-presentazione.
- Azione eseguita: claim sostituiti con formulazioni limitate al protocollo
  testato; cache descritta esplicitamente; riuso subacqueo presentato come base
  da ricalibrare e rivalidare, non come trasferimento automatico.

### INC-2026-07-14-015 - Cartella sorgente Desktop non allineata all'hardening pre-presentazione
- Tipo: allineamento artefatti / rischio comunicativo.
- Evidenza: la cartella `C:\Users\user\Desktop\pitch_claude_design` conteneva
  ancora il `pitch_deck.md` precedente all'audit, con i claim assoluti corretti
  da INC-014. Gli hash di `demo_export_csv.png` e `demo_sequenza.jpg` erano
  inoltre diversi dagli asset rigenerati e validati nel repository; gli altri
  quattro asset principali coincidevano byte per byte con la baseline.
- Impatto: generare il PPTX usando ciecamente la copia Desktop avrebbe
  reintrodotto claim non difendibili, due righe CSV storiche 2/0,0 e il frame
  100 con tracking degradato.
- Azione eseguita: la presentazione finale mantiene struttura e ordine della
  cartella indicata, ma usa come fonte autorevole il sorgente revisionato e gli
  asset aggiornati in `docs/pitch/`. Nessun file sorgente Desktop esistente e'
  stato sovrascritto.
- Stato: mitigato per il PPTX finale; la cartella Desktop resta uno snapshot
  storico e non va riutilizzata come baseline senza riallinearla alla repo.
