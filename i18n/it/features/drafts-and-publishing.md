---
source_hash: d13fbe0e44e283bca3759e24ae06c4632b5ccb20e66f5806145543eb82fe5f65
---
# Bozze, anteprima e pubblicazione

## A cosa serve

Hi, Moose non si ferma alla raccomandazione: l'accompagna da un brief o da un'idea di modifica fino alla modifica pubblicata, con un passaggio di anteprima e uno di approvazione nel mezzo, e una registrazione di ciò che è avvenuto.

## Draft Studio

Nel Draft Studio le bozze vengono scritte e rifinite. La generazione delle bozze è costruita per appoggiarsi a un [brief di contenuto](content-briefs.md) invece di funzionare come un espansore di testo alla cieca: se un lavoro richiede pianificazione strutturata, Hi, Moose crea o conferma prima il brief e poi scrive a partire da quello. Il Draft Studio supporta anche la modifica diretta di testi lunghi.

### Tipi di contenuto

La generazione delle bozze segue gli stessi tipi di modello disponibili quando si [crea un brief di contenuto](content-briefs.md#creare-un-brief). Quattro hanno un proprio avvio rapido nella Chat, ciascuno con la sua struttura: [bozza di articolo del blog](blog-post-draft.md), [voce di glossario](glossary-post.md), [contenuti per landing page](landing-page-content.md) e [contenuti per pagina prodotto](product-page-content.md). Il modello per le pagine di soluzioni è disponibile anch'esso quando si crea un brief, ma senza avvio rapido dedicato.

Tutti i modelli seguono lo stesso flusso con brief anteposto; cambia solo la struttura, perciò la bozza di una landing page viene pianificata e modellata in modo diverso da un articolo del blog, anche se entrambe partono da un [brief di contenuto](content-briefs.md).

Quando chiede un articolo e Hi, Moose produce un brief, prosegue e genera la bozza invece di fermarsi ad aspettare che lei lo chieda di nuovo.

### Collegamenti interni

Le nuove bozze vengono confrontate con il suo sito indicizzato e i collegamenti interni pertinenti vengono inseriti dove hanno davvero senso. Questo richiede un [indice di ricerca](../site-monitoring/overview.md) già costruito: senza di esso non c'è nulla a cui collegarsi, e Hi, Moose non inventa link.

## Preparare una modifica

Che nasca da una bozza basata su un brief, dalle [FAQ](faq-generator.md), dai [key points](key-points.md) o da una raccomandazione di un [AEO audit](aeo-audits.md), una modifica proposta viene preparata come **proposta di modifica**, un artefatto duraturo e non un semplice testo di chat, prima che qualsiasi cosa tocchi il suo sito in produzione.

## Anteprima

Prima che approvi qualcosa, Hi, Moose può generare un'anteprima della modifica preparata perché lei veda che aspetto avrà sulla pagina reale. Per le modifiche che devono essere riviste da qualcun altro, Hi, Moose può generare un link di revisione condiviso, firmato e con scadenza, così un collega o un cliente può esaminarla senza accedere all'app desktop.

## Approvare e pubblicare

- **Approvare**: accettare esplicitamente una modifica preparata prima che possa essere pubblicata. Anteprima e pubblicazione sono sempre passaggi distinti; generare una bozza o un'anteprima non viene mai considerato «fatto» di per sé.
- **Pubblicare**: una volta approvata, Hi, Moose pubblica la modifica tramite la connessione corrispondente ([WordPress](../integrations/wordpress.md), [Webflow](../integrations/webflow.md) o [Grav](../integrations/grav.md)) e registra che cosa è stato pubblicato, quando e perché.

### Comportamento per CMS

**WordPress**: le bozze possono essere inviate a un sito collegato come bozze preparate anziché andare direttamente in produzione, e il flusso di pubblicazione si adatta a seconda che la destinazione sia già preparata o pubblicata. Una volta inviata una bozza, Hi, Moose se ne ricorda, così non può inviare la stessa più volte per errore.

**Webflow**: pubblicare in una collection carica prima gli altri campi obbligatori di quella collection e le chiede di compilarli, perché una pubblicazione non fallisca a metà strada per un campo che lei non poteva vedere.

Una pubblicazione fallita arriva nella sua [Inbox](../inbox/overview.md). Una riuscita no, di proposito.

## Work Queue

Nella Work Queue si raccolgono le modifiche preparate, le anteprime in sospeso e le voci in attesa della sua approvazione, così nulla resta soltanto dentro una conversazione di chat in attesa di essere dimenticato.

## Library e cronologia

- La **[Library](../library/overview.md)** conserva gli artefatti duraturi che ha generato (brief, bozze, insiemi di FAQ, key points, AEO audits) perché possa ritrovarli e riutilizzarli invece di rigenerarli.
- **[Chat (cronologia)](../chat/chats-history.md)** è la cronologia delle sue sessioni di chat salvate: riapra, rinomini o elimini una conversazione passata. È cronologia di conversazioni, non un registro di pubblicazioni o di risultati di visibilità; un registro dedicato che colleghi le modifiche pubblicate al segnale di visibilità che le ha provocate è previsto ma non ancora realizzato.

## Perché conta

Questo percorso di anteprima, approvazione e pubblicazione è ciò che trasforma una raccomandazione in un'azione compiuta e tracciabile. Un flusso che produce soltanto consigli è incompleto; un flusso che si conclude con una modifica esaminata, approvata e pubblicata, con una registrazione che la collega al segnale di visibilità originario, è il senso stesso di Hi, Moose.
