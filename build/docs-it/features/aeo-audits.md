---
source_hash: a8e831ea98a893f4158e5124991eae0686f8eb64e2448fe9541f8444c4680099
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/features/aeo-audits/)

# AEO Audits

## A cosa serve

Un AEO audit (verifica dell'ottimizzazione per i motori di risposta) valuta quanto una pagina sia pronta a essere compresa, recuperata e citata da sistemi di IA come ChatGPT, Google AI Overviews, Perplexity e Gemini, e le consegna poi un piano d'azione ordinato per priorità e sostenuto da evidenze per migliorarla.

Sostituisce i «consigli AEO» sparsi con un artefatto duraturo e confrontabile: ogni audit produce una scheda di valutazione e un piano d'azione che può riconsultare, e gli audit successivi sulla stessa pagina mostrano se le sue modifiche hanno davvero spostato il punteggio.

## Che cosa viene valutato

Il punteggio complessivo è una combinazione ponderata di otto categorie, ciascuna valutata da 0 a 100:

1. **Freshness**: segnali di attualità e aggiornamento.
2. **Structure**: titoli, elenchi, tabelle e paragrafi che un motore di risposta possa analizzare.
3. **Semantic Clarity**: quanto strettamente il contenuto corrisponde alla sua query obiettivo e al suo intento.
4. **Extractability**: con quanta facilità un motore di risposta può estrarre una definizione, un dato o un punto chiave.
5. **Citation Potential**: segnali di attribuzione e di fonti, ricavati dai link di riferimento esterni della pagina.
6. **Comprehensiveness**: copertura dei sottotemi che persone e motori di risposta si attendono per quella query.
7. **Trust Signals**: coerenza, concretezza e cautela delle affermazioni nel modo in cui la pagina presenta attribuzione e fonti. Questa categoria non verifica le affermazioni presso fonti esterne: misura quanto le affermazioni della pagina stessa siano ben attribuite e concrete.
8. **Answer Readiness**: collocazione di una risposta diretta vicino all'inizio, un'idea per blocco, linguaggio referenziale chiaro (evitando «questo/esso/essi» generici) e denominazione coerente delle entità. La valutazione tiene conto della lingua per inglese, tedesco, spagnolo, francese, italiano e portoghese.

L'audit registra anche segnali di Engagement, Entity Recognition e Media Enrichment, anche se non incidono sul punteggio complessivo e non compaiono nella scheda di valutazione.

## Verifiche di infrastruttura e recuperabilità

Accanto alla valutazione dei contenuti, ogni audit verifica se un motore di risposta riesca anche solo a recuperare la pagina:

- **Accesso dei crawler di IA**: controlla le regole del robots.txt per ciascuno dei token specifici dei crawler di IA usati da OpenAI, Anthropic, Perplexity, Google e Bing (trattando separatamente i crawler di addestramento, di indicizzazione e di consultazione in tempo reale, poiché un sito può bloccarne uno e consentirne un altro). Un crawler di recupero o di indicizzazione bloccato è segnalato come critico; un agente di consultazione in tempo reale bloccato ha priorità media; un blocco limitato al solo addestramento viene annotato come scelta di policy legittima e neutra, che non incide sulle citazioni.
- **Rendering lato server e rilevamento di gusci renderizzati lato client**: la maggior parte dei crawler di IA non esegue JavaScript. Se il contenuto essenziale di una pagina compare solo dopo il rendering lato client, il fatto viene segnalato come rilievo critico e in primo piano, non come nota tecnica minore, perché è un problema di recuperabilità che viene prima di qualsiasi ottimizzazione dei contenuti.
- **Igiene di recupero**: controlla un campione di link interni alla ricerca di link rotti e catene di reindirizzamenti.
- **Presenza nell'indice di Bing**: verifica se la pagina risulti indicizzata da Bing, poiché Microsoft Copilot e parte della ricerca di ChatGPT si appoggiano all'indice di Bing. I verdetti sono volutamente prudenti: un esito non conclusivo viene riportato come tale anziché ipotizzato, e il verdetto «non elencata» compare solo quando la verifica ha un segnale reale a sostegno.

## Contesto esterno e di copertura

- **Panorama delle citazioni**: quando viene eseguita una ricerca in tempo reale, l'audit riporta quali domini un motore di risposta ha davvero citato per la query obiettivo, se il sito analizzato è tra questi e se le fonti di terzi (siti di community, siti di recensioni, Wikipedia, YouTube) dominano la risposta. Viene comunicato come contesto che in gran parte non può correggere modificando la sua pagina, anziché confluire nel punteggio.
- **La sua cronologia di visibilità**: se l'URL analizzata è stata citata nelle sue [esecuzioni di visibilità](../visibility/overview.md) recenti, l'audit la incorpora, così le raccomandazioni tengono conto di come la pagina si comporta già nelle risposte dell'IA invece di trattarla come un'incognita. Le esecuzioni fallite ne sono escluse, perché un disservizio non venga letto come assenza di citazioni.
- **Copertura fan-out**: confronta la pagina con query correlate verso cui un motore di risposta potrebbe estendere la query originale (domande da «Altre domande», ricerche correlate, parole chiave secondarie). Quando diverse di queste non sono trattate nella pagina, ne nasce una raccomandazione concreta di coprire quelle domande correlate.

## Livelli di evidenza nelle raccomandazioni

Ogni problema e ogni raccomandazione sono etichettati in base alla solidità dell'evidenza che li sostiene:

- **Proven**: presupposti di recuperabilità con solido sostegno empirico (accesso dei crawler, rendering lato server, link funzionanti, indicizzazione nei motori di ricerca).
- **Directional**: sostenuti da ricerche osservazionali su larga scala, ma senza garanzia (risposta collocata all'inizio, attualità, chiarezza strutturale).
- **Best-practice**: plausibili e poco costosi, ma senza prova che spostino le citazioni dell'IA (aggiungere statistiche, citazioni testuali o rifinire le fonti).

L'audit non raccomanda il markup schema/JSON-LD, i file `llms.txt` né le tattiche di accumulo di parole chiave come modi per migliorare le citazioni dell'IA, poiché la ricerca attuale non giustifica di trattarli come leve di citazione.

## Quante raccomandazioni riceve

Il numero di raccomandazioni dipende da quanti problemi reali vengono trovati, ponderato con il punteggio complessivo della pagina: una pagina con problemi concreti riceverà più raccomandazioni, una che già ottiene buoni punteggi ne riceverà meno, a volte nessuna. Il numero non viene mai gonfiato per raggiungere un obiettivo fisso.

## Eseguire un audit

1. Fornisca una URL in produzione o incolli una bozza, insieme alla query obiettivo che qualcuno userebbe per trovare quel contenuto.
2. Hi, Moose acquisisce un'istantanea delimitata del contenuto e della struttura della pagina, usando come evidenza principale la versione statica (senza rendering JavaScript), perché è ciò che più si avvicina a quanto vede davvero la maggior parte dei crawler di IA.
3. Quando è utile, raccoglie evidenze reali dai motori di risposta o dalle citazioni per la query obiettivo.
4. Se il suo progetto ha una proprietà [Google Search Console](../integrations/google-search-console.md) collegata per quella URL, i suoi dati di rendimento confluiscono nella definizione delle priorità e nella prudenza delle raccomandazioni. Non modificano il punteggio AEO sottostante.
5. Hi, Moose valuta la pagina, crea un riferimento (o verifica rispetto a un riferimento precedente) e assembla l'audit in un artefatto duraturo con un piano d'azione esplicito.

## Verificare il miglioramento

Poiché ogni audit viene salvato come riferimento, eseguire un nuovo audit sulla stessa pagina dopo le modifiche produce un **esito di verifica**, che mostra se il punteggio è davvero migliorato e non soltanto se lei ha apportato modifiche.

## Integrità

Gli AEO audits non inventano mai evidenze. Se Hi, Moose non riesce a raccogliere le evidenze o a completare davvero un passaggio di valutazione, l'audit fallisce in modo esplicito e le spiega perché, invece di presentare una supposizione come risultato finito. Se la ricerca in tempo reale e l'analisi dei concorrenti non riescono a concludersi in un audit gestito a pagamento, l'audit si completa comunque con le evidenze di pagina disponibili, con una nota esplicita che per quell'esecuzione la ricerca in tempo reale non era disponibile.

## Diritti in base al piano

- **Preview Mode (gratuito)** esegue gli audit su un modello locale Gemma 4 attivo. Non esiste più una dotazione gratuita mensile di audit in cloud: configuri un [modello locale](../getting-started/settings.md#local-model) e gli audit saranno gratuiti, tutte le volte che vuole.
- **I piani BYOK** eseguono gli audit in locale con la sua chiave OpenRouter.
- **I piani gestiti** usano i modelli gestiti di Hi, Moose sul normale saldo di crediti del suo account. Non c'è una valuta separata di «crediti per audit» da tenere d'occhio.

## Azioni successive a un audit

Il piano d'azione di un audit conduce direttamente ad altre funzioni: creare un [brief di contenuto](content-briefs.md), preparare una [modifica con anteprima](drafts-and-publishing.md) oppure aggiungere FAQ o key points. L'audit è quindi un punto di partenza per agire, non soltanto un report.
