---
source_hash: bf06b2d4371815f46d4209e9c058c88a274ce098682e93731da1f9cafde41e72
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/visibility/second-turn-queries/)

# Query di secondo turno

## A cosa serve

I motori di IA spesso chiudono una risposta invitando a fare la domanda successiva. Una query di secondo turno è quella domanda successiva, scritta per intero in modo che sia comprensibile da sola. Hi, Moose le rileva durante le esecuzioni di visibilità e le elenca nella scheda **Query di secondo turno**, insieme alla frequenza con cui è comparsa ciascuna e all'indicazione se il suo sito la copre.

Per esempio, un motore può chiudere una risposta con «Vuole che confronti queste due opzioni fianco a fianco?». La query di secondo turno è ciò che una persona scriverebbe per accettare, come «Confrontare i rialzi per scrivania e le scrivanie regolabili complete per un piccolo ufficio in casa».

## Come attivarla

Apra le [Impostazioni di Visibility](settings.md#query-di-secondo-turno) e vada alla sezione **Query di secondo turno**. Attivi **Rileva le query di secondo turno**. L'opzione è disattivata per impostazione predefinita e si attiva separatamente per ogni progetto.

Finché l'opzione è disattivata, non viene rilevato nulla e la scheda Query di secondo turno resta nascosta.

Può attivare l'opzione con i piani gestiti a pagamento, BYOK Premium e BYOK Agency. In Preview Mode e BYOK Free l'interruttore è disabilitato e mostra la nota **Disponibile nei piani a pagamento**.

L'attivazione aggiunge una piccola chiamata al modello per ogni risposta di un'esecuzione. Nei piani gestiti a pagamento queste chiamate vengono conteggiate nella dotazione del suo piano. In BYOK Premium e BYOK Agency vengono addebitate sulla sua chiave OpenRouter.

## La scheda Query di secondo turno

La scheda si trova subito dopo **Opportunità** nel pannello Visibility. Compare solo quando l'opzione è attiva. Resta vuota fino alla prima esecuzione di visibilità successiva all'attivazione, perché le risposte delle esecuzioni precedenti non vengono elaborate.

La scheda segue il periodo e i filtri selezionati nella parte alta di Visibility. Una query viene elencata quando una risposta di quel periodo la conteneva.

### Viste

- **Più frequenti** è la vista predefinita. Mostra un unico elenco ordinato in base al numero di risposte che contenevano ciascuna query.
- **Per prompt** raggruppa le query sotto il prompt monitorato che ciascuna ha seguito.

### Che cosa mostra una riga

- La query.
- **Risposte con questa query: N**, dove N è il numero di risposte che la contenevano.
- I motori e il tema.
- Il risultato della [copertura del sito](#copertura-del-sito).
- **Mostra dettagli**, che elenca i prompt seguiti dalla query sotto **Compare dopo questi prompt**, con un link **Vedi risposta** per ogni prompt. Mostra anche le parole finali del motore.

## Come vengono ordinate le nuove query

La prima volta che compare una nuova query, Hi, Moose controlla se è abbastanza specifica e pertinente al tema da essere monitorata. Controlla anche se ha lo stesso significato di una query già presente nell'elenco. Le query che hanno lo stesso significato vengono conteggiate insieme. Quelle generiche, come «mi dica di più», vengono escluse.

Questo ordinamento avviene all'apertura della scheda. La prima volta che la apre dopo un'esecuzione, la scheda mostra **Ordinamento delle nuove query: X di Y**.

## Copertura del sito

Ogni query viene controllata una volta rispetto alle pagine scansionate del sito del suo progetto. La riga mostra poi uno di questi risultati:

- **Coperta sul sito:** seguito dalla pagina.
- **Coperta in parte sul sito:** seguito dalla pagina.
- **Non coperta sul sito**.

La copertura viene controllata di nuovo quando termina una nuova scansione del sito.

Il controllo richiede una scansione del sito completata sul suo dispositivo, oppure sul dispositivo che ospita l'indice del sito. Senza una scansione completata, la riga mostra **Copertura del sito non verificata**. Nell'app web senza un dispositivo desktop host, la copertura non viene controllata.

## Pulsanti di ogni riga

- **Aggiungi ai prompt monitorati** aggiunge la query come prompt monitorato sotto lo stesso tema del prompt che ha seguito. Il pulsante indica poi **Monitorato**.
- **Crea una bozza** compare quando il suo sito non copre la query. Apre una nuova chat con il modulo del [content brief](../features/content-briefs.md) già compilato.
- **Aggiorna questa pagina** compare quando il suo sito copre la query in parte. Apre il modulo di aggiornamento dei contenuti per quella pagina, con la query come obiettivo.
- **Scarta** nasconde la riga. **Mostra le query scartate** fa ricomparire le righe scartate e **Ripristina** riporta una riga nell'elenco.

## Quando si aggiorna l'elenco

Finché l'opzione è attiva, le nuove query vengono rilevate da ogni risposta a ogni esecuzione di visibilità. Vengono ordinate alla successiva apertura della scheda.

Poiché la scheda segue il periodo selezionato, una query non viene più elencata quando nessuna risposta di quel periodo la conteneva. Scelga un periodo più lungo per vederla di nuovo.

## Team e piani

Nei piani gestiti a pagamento, le query rilevate, le query scartate e i risultati di copertura vengono sincronizzati con il cloud, così i membri del team vedono lo stesso elenco. In BYOK Premium e BYOK Agency, tutto resta sul suo dispositivo.

## Che cosa non è incluso

- Le domande «Related» di Perplexity e le domande «People also ask» di Google non vengono rilevate.
- Le query di secondo turno non fanno parte del [report esecutivo PDF](overview.md#esportare).
- Le query di secondo turno non sono disponibili tramite gli strumenti di [Hi, Moose MCP](../integrations/hi-moose-mcp.md).
