---
source_hash: 1d8f1dffb939a9b3587c4b3a3f298386f6f202a5a02672b6b3dfd79bbccc2135
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/features/entity-graph/)

# Entity Graph

## A cosa serve

Un entity graph è la mappa di ciò di cui parla davvero il suo sito: le persone, i prodotti, i luoghi, le organizzazioni e i temi che le sue pagine nominano, e come queste cose si collegano tra loro.

Conta perché i motori di risposta non leggono il suo sito come un elenco di pagine. Lo leggono come un insieme di cose e di relazioni. Un sito che stabilisce con chiarezza «siamo questa azienda, produciamo questi prodotti, per questi clienti, in questa categoria» dà al motore qualcosa da recuperare e citare. Un sito in cui tutto ciò è sottinteso ma mai dichiarato lo lascia a indovinare.

L'entity graph le mostra quali di queste cose il suo sito ha già reso chiare, quali sono deboli e con che cosa un motore se ne andrebbe.

Lo avvii da **Strumenti → Creare un entity graph**, oppure lo chieda semplicemente in [chat](../chat/overview.md).

## Prima di poterne costruire uno

Il grafo si costruisce dalle pagine che Hi, Moose ha già scansionato, quindi al progetto servono **un sito web e almeno una scansione completata**. Se non ce n'è ancora nessuna, la scheda di avvio glielo dice e la rimanda a [Monitoraggio del sito](../site-monitoring/overview.md) per eseguirne una.

La scheda le indica su che cosa sta lavorando: quante pagine scansionate e la data dell'ultima scansione completata.

## Rapido o completo

Due profondità:

- **Rapido**: solo dati strutturati. Legge il markup schema, i metadati e la struttura di pagina che il suo sito già pubblica. È istantaneo e non costa nulla.
- **Completo**: tutto quello del rapido, più un passaggio di IA che legge le sue pagine principali e nomina le entità che non sono marcate da nessuna parte. Richiede qualche minuto.

In modalità completa sceglie quante pagine principali il passaggio di IA può leggere. Le esecuzioni più ampie richiedono più tempo e, nei piani gestiti, le chiamate al modello in cloud consumano la sua dotazione mensile. Il passaggio gira sul modello selezionato nel menu dei modelli della chat, quindi scelga prima il modello se ne vuole uno specifico: un modello locale caricato tiene tutto sul suo computer e a costo zero.

## Che cosa ottiene

Il grafo riporta:

- **Entità**: tutto ciò che è stato trovato, con il tipo, gli alias, su quante pagine compare e un punteggio di **salienza** che dice quanto è centrale per il sito.
- **Relazioni**: come quelle entità si collegano, divise in tre tipi:
    - **Etichettate**: una relazione che i suoi dati strutturati o il passaggio di IA dichiarano esplicitamente.
    - **Pagina condivisa**: due entità che continuano a comparire sulle stesse pagine.
    - **Semantiche**: due entità che il linguaggio tratta come collegate anche dove nulla le lega.
- **Entità per tipo**: la ripartizione, spesso la singola vista più utile. Un sito che vende software e mostra quaranta persone e tre prodotti ha un problema di racconto che vale la pena conoscere.

Una tabella delle **entità principali** mostra le più salienti con tipo, numero di pagine e salienza. L'insieme completo si esporta in **CSV** o in **PDF**; la tabella a schermo è limitata e indica quante altre ne contengono le esportazioni.

## Quando il passaggio di IA non parte

La modalità completa degrada invece di fallire. Se il passaggio di IA non può girare, ottiene comunque il grafo da dati strutturati, pagine condivise e somiglianza semantica, e la scheda le dice quale caso si è verificato:

- **Nessun modello disponibile**: carichi un modello locale o aggiunga una chiave OpenRouter, poi ricostruisca in modalità completa.
- **Niente di nuovo da leggere**: tutte le pagine idonee erano già state analizzate in un'esecuzione precedente.
- **Il passaggio è fallito**: non è riuscito a completarsi.
- **Dotazione esaurita**: nei piani gestiti il passaggio si ferma quando finiscono i crediti mensili, e il grafo comprende tutto ciò che è stato analizzato fino a quel punto.

## Moose può rileggerlo

Una volta che il grafo esiste, la [chat](../chat/tools-and-specialists.md) può interrogarlo direttamente. Chieda su quali entità il suo sito è più forte, che cosa è collegato a un certo prodotto o che cosa manca accanto a un tema che vuole conquistare, e Moose legge il grafo invece di riscansionare o tirare a indovinare.

Anche [Send Moose](../send-moose/overview.md) lo legge, come parte dell'intelligenza sul sito che porta con sé in un lavoro.

## Dove andare da qui

- **[Monitoraggio del sito](../site-monitoring/overview.md)**: la scansione da cui nasce il grafo.
- **[Content Briefs](content-briefs.md)**: trasformare un vuoto del grafo in una pagina.
- **[Audit AEO](aeo-audits.md)**: verificare se una singola pagina dichiara con chiarezza le proprie entità.
