# Pitch Deck - AI Swimming Motion Analyzer (bozza T39)

Sorgente testuale delle slide. Il PDF bozza e' `pitch_deck_bozza.pdf`
(generato da questo contenuto). Stato: BOZZA in attesa di revisione dello
studente (DoD T39: "slide esportate in PDF, riviste").

Angolo di vendita: "il rischio software e' azzerato, finanziate il rischio
hardware". Il dry-run va presentato onestamente: prova che il software
funziona, NON la validita' biomeccanica in acqua (spec sez. 14.4).

---

## Slide 1 - Titolo
**AI Swimming Motion Analyzer**
Analisi biomeccanica del nuoto, a partire da un video.
Proof of Concept funzionante - costo di sviluppo e di esercizio: 0 euro.
[Nome studente] - ITS ICT Academy Roma, corso AI Projects Development.

## Slide 2 - Il problema
- L'analisi biomeccanica del nuoto oggi e' roba d'elite: sistemi
  professionali costosi, installazioni in vasca complesse.
- L'occhio dell'allenatore non misura: niente angoli, niente frequenze,
  niente numeri confrontabili nel tempo.
- Chi vuole innovare qui affronta subito costi hardware ALTI senza sapere
  se il software reggera'.

## Slide 3 - L'idea
- Separare il rischio software dal rischio hardware.
- PRIMA: dimostrare che la pipeline di analisi funziona, a secco, a costo
  zero, su un PC qualsiasi. (<- questo PoC, FATTO)
- POI: investire in hardware (telecamere subacquee, edge, sensori) sopra
  un software gia' provato. (<- la richiesta di oggi)

## Slide 4 - La soluzione (come funziona)
- Video laterale -> rete neurale di pose estimation (33 punti del corpo,
  in locale, senza cloud) -> motore matematico deterministico ->
  dashboard con KPI live ed export CSV.
- AI dove serve percepire, matematica dove serve misurare: risultati
  riproducibili bit a bit, verificabili, difendibili.
- Zero API, zero abbonamenti, zero dati che lasciano la macchina.
[immagine: demo_frame_annotato.png]

## Slide 5 - Demo dal vivo
- Ora, davanti a voi: carico il video di riferimento e il sistema conta
  10 bracciate in tempo reale, misura l'angolo del gomito frame per frame
  e calcola un indice di regolarita' del ritmo (Fluidity 93/100).
- Ripetibile all'infinito con gli STESSI numeri: due esecuzioni producono
  risultati identici bit a bit (test di riproducibilita' documentato).
[immagine: demo_onda_polso.png]

## Slide 6 - Validazione onesta
- Conteggio bracciate: manuale 10 vs automatico 10 (differenza 0).
- Robustezza: braccio coperto per 100 frame -> nessuna bracciata
  inventata, nessun crash (il sistema puo' sottostimare dopo occlusioni
  lunghe, MAI sovrastimare: limite documentato).
- Privacy by design: nessun video salvato, solo metriche anonime.
- Ogni numero di questa presentazione e' riproducibile dal repository.
[immagine: demo_export_csv.png]

## Slide 7 - Cosa NON dimostra questo PoC (e perche' e' un pregio)
- Non dimostra la validita' biomeccanica in acqua: quella richiede la
  fase hardware ed e' esattamente cio' che chiediamo di finanziare.
- Ogni claim e' verificabile: specifica congelata, 41 task tracciate,
  registro incidenti pubblico nel repository.
- Sappiamo esattamente cosa abbiamo provato e cosa resta da provare.

## Slide 8 - Architettura pronta a crescere
- Tre moduli disaccoppiati: visione / metriche / interfaccia.
- Il motore metriche e' gia' testato (23 unit test) e riusabile identico
  nella versione con telecamere subacquee.
- Il modello di posa e' sostituibile (oggi MediaPipe, domani modelli
  custom addestrati sui dati raccolti in vasca).

## Slide 9 - Roadmap con i fondi
- Fase 1 (finanziata): sandbox di ripresa proprietario + protocollo di
  acquisizione + prime riprese in vasca (camere sopra/sott'acqua).
- Fase 2: mini-PC edge a bordo vasca, analisi in tempo reale.
- Fase 3: sensor fusion (IMU/LiDAR), multi-atleta, validazione
  scientifica con preparatori e atleti.
- Il software di analisi c'e' gia': i fondi comprano hardware e dati.

## Slide 10 - La richiesta
- Il rischio software e' azzerato: pipeline end-to-end funzionante,
  riproducibile, a costo zero, dimostrata dal vivo oggi.
- Chiediamo [importo da definire] per la fase hardware.
- Repository completo e verificabile:
  github.com/Maxdavi789/Acquatic-intelligence-system
- Disclaimer: non e' un dispositivo medico e non fornisce consigli
  clinici o di prevenzione degli infortuni.

---

### Note per il presentatore
- La demo live va tra la slide 5 e la 6 (2-3 minuti, gia' provata).
- Eventuale momento webcam live (best-effort): decidere prima, provarlo
  in sala; se le condizioni sono cattive, saltarlo senza segnalarlo.
- Se qualcuno chiede "dov'e' l'AI?": slide 4, riga 2 (percezione neurale
  + misura deterministica: scelta di design, non ripiego).
