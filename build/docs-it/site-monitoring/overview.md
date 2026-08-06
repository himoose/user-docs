---
source_hash: 87a7b6f091685fae0a59b09ee8abe0ec965085647eb82bd29c1661777efb87ab
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/site-monitoring/overview/)

# Monitoraggio del sito

## A cosa serve

Hi, Moose mantiene un quadro locale del suo sito: quali pagine esistono, che cosa contengono e che cosa è cambiato dall'ultima volta. Quel quadro alimenta tre cose: gli avvisi sulle modifiche rilevanti per l'AEO nella sua [Inbox](../inbox/overview.md), l'indice di ricerca semantica che Moose usa per rispondere alle domande sul suo sito, e l'inventario delle pagine a cui attingono [audit](../features/aeo-audits.md) e [brief](../features/content-briefs.md).

Tutto questo si trova in **Impostazioni → Monitoraggio del sito**, delimitato al progetto corrente.

## La scansione pianificata

Attivi **Esegui scansione settimanale del sito** e Hi, Moose aggiornerà le pagine monitorate con cadenza settimanale, avvisandola quando emergono modifiche significative. Scelga giorno e ora nel suo orario locale.

Le scansioni manuali restano comunque disponibili. **Esegui scansione ora** avvia subito una scansione completa, con l'avanzamento nella barra di stato in fondo alla finestra. Può **interrompere** una scansione in corso: le pagine trovate fino a quel momento vengono conservate anziché scartate.

Sui siti grandi servono alcuni minuti.

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

## Percorsi bloccati

Le scansioni saltano i percorsi bloccati e tutto ciò che ne dipende, e le pagine corrispondenti vengono rimosse dal monitoraggio.

La corrispondenza avviene per prefisso di segmento del percorso. Bloccare `/results/` copre `/results/` e tutti i suoi sottopercorsi, ma **non** `/results-archive/`: deve corrispondere il segmento, non semplicemente la stringa.

È lo strumento adatto per pagine di risultati di ricerca, pagine di elenco filtrate, archivi paginati e qualsiasi altra cosa generi un gran numero di URL quasi identiche che preferisce non scansionare, non indicizzare e su cui non vuole avvisi.

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
