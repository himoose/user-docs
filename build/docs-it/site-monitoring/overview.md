---
source_hash: 29ee2dfc08c9390fc91d11ea66fc96fc6fef4439d84b5f28508c2afbf8f0c1d3
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/site-monitoring/overview/)

# Monitoraggio del sito

## A cosa serve

Hi, Moose mantiene un quadro locale del suo sito: quali pagine esistono, che cosa contengono e che cosa è cambiato dall'ultima volta. Quel quadro alimenta quattro cose: gli avvisi sulle modifiche rilevanti per l'AEO nella sua [Inbox](../inbox/overview.md), l'indice di ricerca semantica che Moose usa per rispondere alle domande sul suo sito, l'inventario delle pagine a cui attingono [audit](../features/aeo-audits.md) e [brief](../features/content-briefs.md), e l'[entity graph](../features/entity-graph.md) che mappa di che cosa parla il suo sito.

Tutto questo si trova in **Impostazioni → Monitoraggio del sito**, delimitato al progetto corrente.

## La scansione pianificata

Attivi **Esegui scansione settimanale del sito** e Hi, Moose aggiornerà le pagine monitorate con cadenza settimanale, avvisandola quando emergono modifiche significative. Scelga giorno e ora nel suo orario locale.

Le scansioni manuali restano comunque disponibili. **Esegui scansione ora** avvia subito una scansione completa, con l'avanzamento nella barra di stato in fondo alla finestra. Può **mettere in pausa**, **riprendere** o **interrompere** una scansione in corso: le pagine trovate fino a quel momento vengono conservate anziché scartate.

Sui siti grandi servono alcuni minuti.

### Il crawler trova da sé il proprio ritmo

Ogni sito ha una velocità alla quale è a suo agio nell'essere letto, ed è diversa tra un sito statico su una CDN e un negozio basato su database su un hosting condiviso. Hi, Moose non la indovina da un'impostazione: la trova.

La scansione parte con calma, accelera finché le pagine tornano rapidamente e rallenta appena il sito mostra fatica: tempi di risposta più lunghi, oppure una risposta di limite di richieste o di server occupato. Quando succede, la barra di stato dice **Sto rallentando per adattarmi al sito**, e la scansione prosegue al ritmo più lento invece di martellare il server o arrendersi.

L'effetto pratico è che gli inventari tornano completi. Una scansione che veniva limitata a metà strada restituiva un quadro parziale del suo sito, e questo rendeva parziale anche tutto ciò che ci si costruisce sopra: l'indice di ricerca, gli audit, i brief.

Non deve configurare nulla di tutto questo.

## L'indice di ricerca

Sotto i comandi di scansione si trova il **Indice di ricerca**, l'indice semantico locale che Moose usa per rispondere alle domande sulle pagine del suo sito. Indica quante pagine sono indicizzate, quanti passaggi hanno prodotto e quando è stato aggiornato l'ultima volta.

L'indicizzazione avviene a livello di passaggio, non di pagina. Una pagina lunga diventa molti passaggi ricercabili separatamente, ed è per questo che Moose può citare un paragrafo preciso invece di dirle che una pagina parla «in generale» di un argomento.

- **Ricostruisci indice** reindicizza da zero.
- Se ci sono pagine nuove o modificate dall'ultimo aggiornamento dell'indice, Hi, Moose le indica quante. Verranno indicizzate alla prossima scansione, oppure può ricostruire l'indice subito.

!!! note "L'indice è onesto su ciò che non ha"
    Se chiede a Moose di una pagina che non è stata indicizzata, glielo dice e la indirizza a eseguire una scansione, invece di dedurre qualcosa dall'URL della pagina.

## Pagine monitorate

Le pagine che Hi, Moose controlla per individuare modifiche rilevanti per l'AEO. Le pagine trovate dal rilevamento del sito, da [Google Search Console](../integrations/google-search-console.md) e dalle [esecuzioni di visibilità](../visibility/overview.md) compaiono qui automaticamente.

Può anche aggiungere pagine a mano con l'URL completa, cercare e filtrare l'elenco, sfogliarlo per pagine e rimuovere quelle che non le interessano.
Le pagine monitorate sono vincolate al dominio del progetto stesso. I suoi sottodomini vanno bene; un dominio estraneo viene rifiutato, così il monitoraggio di un progetto non può riempirsi in silenzio con le pagine di qualcun altro.

## Percorsi bloccati

Le scansioni saltano i percorsi bloccati e tutto ciò che ne dipende, e le pagine corrispondenti vengono rimosse dal monitoraggio.

La corrispondenza avviene per prefisso di segmento del percorso. Bloccare `/results/` copre `/results/` e tutti i suoi sottopercorsi, ma **non** `/results-archive/`: deve corrispondere il segmento, non semplicemente la stringa.

È lo strumento adatto per pagine di risultati di ricerca, pagine di elenco filtrate, archivi paginati e qualsiasi altra cosa generi un gran numero di URL quasi identiche che preferisce non scansionare, non indicizzare e su cui non vuole avvisi.

## Quanto è vecchia ogni pagina

Mentre scansiona, Hi, Moose legge le date di pubblicazione e di ultima modifica che le sue pagine dichiarano (nei dati strutturati, nei metadati e negli elementi `<time>`) e le registra accanto alla pagina.

Conta perché la freschezza è uno degli elementi che i motori di risposta soppesano quando decidono di quale fonte fidarsi su una domanda la cui risposta cambia nel tempo. Una pagina che non dice nulla su quando è stata scritta non può sostenere quell'argomento. I suoi [audit AEO](../features/aeo-audits.md) usano queste date nella valutazione della freschezza, ed è lì che ne vedrà il risultato.

Se una pagina non dichiara alcuna data da nessuna parte, quello è già di per sé un rilievo su cui intervenire.

## Che cosa arriva nella sua Inbox

Una scansione produce **un solo riepilogo per esecuzione**, non una voce per ogni pagina modificata. Il riepilogo si apre in una tabella delle pagine modificate con l'indicazione di che cosa è cambiato, un livello di impatto e azioni per ciascuna pagina.

I livelli di impatto sono **Critico**, **Rilevante**, **Basso**, **Non raggiungibile** e **Non esaminata**.

Due impostazioni regolano il rumore:

- **Includi modifiche AEO informative**: disattivata per impostazione predefinita. Se attivata, anche le modifiche a basso impatto generano voci nell'Inbox.
- **Gravità minima delle notifiche del sistema operativo**: solo le voci dell'Inbox di livello pari o superiore attivano una notifica desktop. La imposti su Info se desidera che anche le modifiche a basso impatto emergano a livello di sistema operativo.

## Chiedere a Moose che cosa è cambiato

Il riepilogo include l'azione **Chiedi a Moose di tutto questo**, che consegna alla chat l'istantanea completa della scansione e le chiede che cosa conta di più e da dove cominciare. Le singole pagine hanno la propria azione **Chiedi a Moose**, che trasmette soltanto la modifica registrata per quella pagina.

Entrambe si limitano all'istantanea registrata. Se da questa non risulta perché qualcosa è cambiato, Moose ha istruzione di dirlo anziché inventare una spiegazione.

## Pagine irraggiungibili

Se una pagina o l'intero sito non è raggiungibile, il fatto viene segnalato come tipo di modifica a sé stante invece di essere ignorato in silenzio. Un disservizio dell'intero sito produce un'unica voce **Sito non raggiungibile** anziché un avviso per ogni pagina.
