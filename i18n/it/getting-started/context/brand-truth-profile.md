---
source_hash: c5ff2a271e0bd65a359303913cb736f19793b0f0562c6c4941f37c02efd742fb
---
# Brand Truth Profile

## A cosa serve

Il Brand Truth Profile è una fonte di verità leggibile dalle macchine su come l'IA deve descrivere la sua azienda: che cosa vende, chi serve e con che cosa non deve mai essere confusa. Hi, Moose lo utilizza durante le esecuzioni di [Visibility](../../visibility/overview.md) per rilevare quando la risposta di un motore di IA travisa il suo marchio o ripete una narrazione superata, invece di affidare quel giudizio a un generico punteggio di sentiment.

Come la Brand Voice, il Brand Truth Profile è delimitato al [progetto](../projects.md) corrente.

Tutti i campi sono facoltativi, ma più ne compila, più Hi, Moose potrà segnalare con precisione i travisamenti e raccomandare correzioni.

## Campi che può compilare

### Descrizione principale

- **Come deve descrivere l'IA la sua azienda oggi?**: la descrizione canonica, in una o due frasi, che vorrebbe leggere in una risposta di ChatGPT, Perplexity, Gemini o Google AI.
- **Chi è oggi il suo cliente ideale?**: da scegliere tra segmenti comuni (PMI, fascia media, grandi imprese, agenzie, marchi di e-commerce e altri), con note in testo libero.

### Che cosa offre

- **Prodotti, servizi o categorie di prodotto che l'IA deve sapere che lei offre**: l'essenziale di ciò che l'IA deve sapere che lei fornisce; non serve elencare ogni funzione.
- **Funzioni o capacità che l'IA deve menzionare**: una per riga. Aiuta Hi, Moose a rilevare quando l'IA tralascia qualcosa di importante.

### Dove le descrizioni sbagliano

- **Che cosa sbagliano spesso l'IA o il mercato sulla sua azienda?**: da scegliere tra i modelli di travisamento più comuni: tipo di cliente errato, categoria di prodotto errata, posizionamento superato, prodotti o funzioni nuovi mancanti, concorrenti sbagliati, sopravvalutazione o sottovalutazione delle capacità, confusione con un altro marchio e altri.
- **Un esempio di ciò che l'IA o il mercato sbagliano**: un esempio concreto a sostegno del modello indicato sopra.
- **Descrizioni superate da segnalare**: vecchie categorie, clienti target o limitazioni che non valgono più.
- **Quali errori dell'IA sarebbero più dannosi?**: le categorie di errore più critiche (descrizione errata dell'azienda, cliente target sbagliato, prezzi o disponibilità errati, sentiment negativo o fuorviante, confusione di marchio e altri).

### Lessico

- **Parole o espressioni che l'IA deve usare**: lessico preferito, uno per riga.
- **Parole o espressioni che l'IA deve evitare**: lessico da evitare, uno per riga.

### Contesto competitivo

- **Principali concorrenti o alternative**: da 3 a 5 concorrenti, alternative o categorie di strumenti, ciascuno con una nota facoltativa (per esempio «posizionato solo per grandi imprese»). Serve a testare i prompt di confronto.
- **Confronti che vale la pena monitorare**: ricerche di confronto o di categorie alternative precise che Hi, Moose deve tenere d'occhio (per esempio «migliori strumenti AEO per piccole imprese»).

### Fiducia ed evidenze

- **Domande dei clienti a cui l'IA deve rispondere correttamente**: domande diagnostiche in linea con il modo in cui i potenziali clienti acquistano davvero.
- **Affermazioni da trattare con cautela**: prezzi, prestazioni, certificazioni o altre affermazioni che richiedono un linguaggio prudente e circostanziato.
- **Pagine o fonti che provano il suo posizionamento attuale**: pagine, documenti o casi di studio precisi da considerare prove importanti, ciascuno con una nota facoltativa.
- **Fonti già note come superate o inesatte**: pagine di terzi, elenchi o citazioni precedenti dell'IA che notoriamente descrivono male la sua azienda, ciascuna con una nota su che cosa non va.

## Come viene utilizzato

### Rilevare le rappresentazioni errate

Durante un'esecuzione di visibilità, Hi, Moose carica il Brand Truth Profile del progetto (quando contiene informazioni significative) e lo utilizza per valutare ogni risposta dell'IA alla ricerca di travisamenti o scostamenti, confrontandola con la sua descrizione canonica, la sua offerta, i suoi concorrenti, il lessico preferito e da evitare e i modelli noti di travisamento, invece di limitarsi a controllare se compare il nome del suo marchio.

### Scrivere contenuti mirati al suo acquirente

Il profilo alimenta anche gli strumenti di contenuto. I [content brief](../../features/content-briefs.md), le [bozze di articolo](../../features/blog-post-draft.md), i [key points](../../features/key-points.md) e le [FAQ](../../features/faq-generator.md) lo leggono prima di scrivere qualsiasi cosa, compresi i suoi **segmenti di cliente ideale** e le note libere accanto a essi.

È la differenza tra un brief scritto per «lettori interessati all'argomento» e uno scritto per team operativi di media impresa che stanno valutando un cambio di fornitore. Compilare una sola volta i campi del cliente ideale cambia il risultato di ogni strumento di scrittura da quel momento in poi, e questo li rende tra i campi più redditizi di questa schermata.

Anche [Send Moose](../../send-moose/overview.md) legge il profilo nei lavori sulla sua marca.

## In cosa si differenzia dalla Brand Voice

La [Brand Voice](brand-voice.md) riguarda lo **stile**: come deve suonare il suo marchio. Il Brand Truth Profile riguarda i **fatti**: che cosa è vero sulla sua azienda e quali narrazioni errate sorvegliare. Compili la Brand Voice per definire il tono; compili il Brand Truth Profile per cogliere quando l'IA sbaglia i fatti che la riguardano.

## Sincronizzazione in cloud

Come la Brand Voice, il Brand Truth Profile è salvato per impostazione predefinita in locale per il progetto corrente. Sincronizzarlo con il cloud, per conservarlo e condividerlo con il team, richiede un piano a pagamento. Maggiori dettagli in [Context](overview.md).

## Monitoraggio dei concorrenti

L'elenco dei concorrenti di questa pagina è condiviso con le [impostazioni di Visibility](../../visibility/settings.md). I concorrenti aggiunti in uno dei due punti compaiono in entrambi e alimentano [Share of Voice, citazioni dei concorrenti e lacune](../../visibility/competitors.md).
