---
source_hash: 67912e0c53e927d4836f8b9c545fb59268db0fbc9165037df2930f6cfada0988
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/integrations/webflow/)

# Webflow

## A cosa serve

Collegare un sito Webflow perché Hi, Moose possa esaminarne pagine e contenuti e preparare modifiche visualizzabili in anteprima per la pubblicazione: FAQ, key points, bozze basate su brief e raccomandazioni degli AEO audits.

## Configurare una connessione

1. Apra **Connessioni** nell'app desktop e scelga Webflow.
2. Faccia clic su **Collega Webflow MCP**. Si apre la pagina di autorizzazione di Webflow nel suo browser. Completi lì la procedura OAuth per concludere la connessione.
3. Una volta connesso, scelga quale sito Webflow autorizzato Hi, Moose debba usare per questo [progetto](../getting-started/projects.md).

## Preparare una destinazione di anteprima

Hi, Moose può individuare **superfici di contenuto** sul suo sito Webflow collegato: pagine, articoli, elementi di collection e codice personalizzato, oltre a una pagina vuota per contenuti che ancora non esistono. Scelga una destinazione, aggiunga note sulla modifica o sull'intenzione di pubblicazione e la prepari come destinazione di anteprima. Da lì rivede la bozza preparata esattamente come con qualsiasi altra connessione. Veda [Bozze, anteprima e pubblicazione](../features/drafts-and-publishing.md).

## Prontezza per anteprima e pubblicazione

Non tutte le connessioni Webflow riescono ancora a fare tutto. Hi, Moose segnala per il suo sito collegato uno tra vari stati: pronto sia a preparare anteprime sia a pubblicare, solo anteprima, solo pubblicazione, oppure collegato ma non ancora pronto per nessuna delle due. Le superfici gestibili unicamente nel Designer (modifiche che richiedono direttamente il Webflow Designer) non sono ancora supportate.

## Pubblicare nelle collection

Quando pubblica in una collection, Hi, Moose carica prima gli altri campi obbligatori di quella collection e le chiede di compilarli, perché una pubblicazione non fallisca a metà strada per un campo che lei non poteva vedere.

## Sicurezza

L'autorizzazione di Webflow avviene tramite il suo browser, e la connessione che ne deriva viene usata soltanto dal processo in background dell'app desktop; non viene esposta all'interfaccia utente.
