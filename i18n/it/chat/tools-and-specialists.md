---
source_hash: 6b12d8d972a33f212f60d823c287d184f083cfb60d8934f6b9ac8571ceb3c32e
---
# Strumenti e specialisti della chat

## A cosa serve

Oltre a digitare una richiesta, il campo di composizione della chat le offre alcuni modi in più per orientare ciò che Hi, Moose fa con il suo messaggio: allegare contesto, scegliere uno specialista per mettere a fuoco la conversazione oppure avviare un percorso rapido.

## Allegati

Faccia clic sul pulsante degli allegati nel campo di composizione per aggiungere contesto al suo messaggio:

- **Caricare un file o un'immagine**: `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg` e `.png`. I fogli di calcolo vengono convertiti in testo leggibile, così può consegnare a Moose una cartella di lavoro e chiedergli che cosa contiene.
- **Catturare una schermata**: scelga uno schermo o una finestra, poi trascini per ritagliare esattamente l'area da inviare. Su macOS, la prima volta dovrà concedere a Hi, Moose l'accesso alla registrazione dello schermo.
- **Aggiungere dalla Library**: alleghi un artefatto salvato della [Library](../library/overview.md) (un brief, una bozza, key points o FAQ) come contesto invece di reincollarlo.
- **Database vettoriale del sito**: alleghi il sito indicizzato del suo progetto perché Moose risponda a partire dalle sue pagine reali e non da ciò che presume vi si trovi. Costruisca l'indice da [Site Monitoring](../site-monitoring/overview.md).

## Strumenti che Moose può usare

La chat non si limita a generare testo. Nel corso di una conversazione Moose può usare strumenti per suo conto e le mostra quando lo fa.

| Strumento | Funzione |
|---|---|
| Ricerca web | Risultati in tempo reale, nei piani che includono la ricerca web nella chat |
| Leggere una pagina | Consultare una URL specifica |
| Ricerca nell'indice del sito | Rispondere a partire dalle sue pagine indicizzate |
| Search Console | Interrogare i suoi dati collegati di [Search Console](../integrations/google-search-console.md) |
| Verifica istantanea del marchio | Interrogare una query su cinque motori di IA; veda [Verifica istantanea del marchio](../tools/instant-brand-check.md) |
| Verifica di copertura | Stabilire se il suo sito copre già un argomento |
| Generazione di immagini | Produrre un'immagine per una bozza |
| Aiuto sull'app | Indirizzarla alla documentazione giusta o al supporto |

L'uso degli strumenti funziona allo stesso modo nei piani gestiti, nei piani BYOK e sui modelli locali Gemma 4.

!!! note "Le domande su Search Console ricevono una risposta agentica"
    Moose interroga i suoi dati di Search Console in modo iterativo anziché eseguire un report fisso. Se pone una domanda vaga, restringe il campo attraverso più interrogazioni per rispondere, invece di restituire un estratto generico.

## Specialisti

Gli specialisti sono punti di ingresso mirati allo stesso operatore principale. Non sono strumenti né memorie separate, soltanto un modo per orientare la conversazione su un'attività precisa. Apra il selettore degli specialisti per sceglierne uno:

- **Specialista Content Brief**: costruire un brief essenziale con struttura e passi successivi.
- **Specialista Google Search Console**: interrogare Moose sui suoi dati collegati di [Google Search Console](../integrations/google-search-console.md). Questo specialista richiede un account Search Console collegato o una proprietà salvata per il progetto attivo prima di poter rispondere a partire dai suoi dati.
- **Specialista generazione audio**: trasformare una richiesta in un copione parlato pulito.
- **Specialista bozze**: generare contenuti in bozza pronti per la revisione e la modifica.
- **Specialista FAQ**: redigere FAQ sintetiche attorno alle domande di maggior valore.
- **Specialista Key Points**: far emergere per prime le conclusioni più importanti.

Quando uno specialista è attivo, la sua etichetta compare sulla conversazione e può rimuoverla in qualsiasi momento per tornare alla chat generale.

### Specialisti personalizzati

Può anche creare un suo specialista locale: gli dia un nome e una sintesi del lavoro di cui deve occuparsi, poi scelga a quali parti del suo contesto può accedere: contesto di progetto, profilo di marca, contesto del sito, cronologia della chat, output orientato alla bozza oppure output in formato markdown. Gli specialisti personalizzati possono anche essere importati, se qualcuno ne condivide uno con lei.

## Avvii rapidi

Il campo di composizione propone avvii rapidi con un clic per le attività più comuni, tra cui:

- [Eseguire un AEO audit](../features/aeo-audits.md)
- [Creare un brief di contenuto fondato sulla ricerca](../features/content-briefs.md)
- [Creare FAQ fondate sulla ricerca](../features/faq-generator.md)
- [Generare key points ottimizzati](../features/key-points.md)
- [Creare una bozza di articolo del blog](../features/blog-post-draft.md)
- [Creare una voce di glossario](../features/glossary-post.md)
- [Creare contenuti per landing page](../features/landing-page-content.md)
- [Creare contenuti per pagina prodotto](../features/product-page-content.md)
- [Acquisire le query di grounding di Google AI Mode per un prompt](../features/grounding-queries.md)
- [Acquisire le query fan-out di ChatGPT per un prompt](../features/fan-out-queries.md)
- [Trasformare contenuti testuali in audio](../audio/overview.md)

Lo stesso insieme è disponibile dal **[menu Tools](../tools/overview.md)** nella barra superiore, raggruppato per attività e con ricerca.

Gli avvii rapidi per le query di grounding e per le query fan-out le mostrano le ricerche che un motore di IA collegato al web ha eseguito rispondendo a un prompt, insieme alle fonti citate. Entrambi funzionano effettuando una chiamata gestita a Gemini o a OpenAI e rileggendo poi le ricerche compiute da quella chiamata: sono quindi un'approssimazione molto vicina a ciò che fanno AI Mode e ChatGPT Search, non una registrazione di quei prodotti. Poiché quella chiamata gira sulla nostra infrastruttura, entrambi richiedono uno **spazio di lavoro gestito a pagamento**, e vale anche nei piani BYOK, perché il passaggio di acquisizione usa l'infrastruttura gestita di Hi, Moose e non la sua chiave locale.

L'avvio rapido dell'audio apre la schermata [Audio](../audio/overview.md) nell'app desktop. In passato rimandava alla vecchia app web; non è più così.
