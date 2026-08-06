---
source_hash: 1d027fe8d7c0bf155818720c05a7777b1744c302a9ab057860377dc301df1947
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/integrations/grav/)

# Grav

## A cosa serve

Collegare un sito [Grav](https://getgrav.org) in produzione tramite il plugin di Hi, Moose per Grav, perché l'app desktop possa esaminare i contenuti di Grav ed eseguire direttamente da remoto azioni di creazione, aggiornamento, pubblicazione e annullamento.

## Installare il plugin

1. Da **Connections → Grav** nell'app desktop, apra il link di download e scarichi lo ZIP del plugin di Hi, Moose. La versione attuale è la **0.1.1** e richiede Grav 1.7.0 o successivo.
2. Nell'amministrazione di Grav apra **Plugins**, carichi lo ZIP e completi l'installazione.
3. Attivi il plugin e apra poi le sue impostazioni nell'amministrazione di Grav.
4. Copi il pacchetto di connessione mostrato lì: lo incollerà in Hi, Moose al passaggio successivo.

## Collegarsi in Hi, Moose

1. Apra **Connections** nell'app desktop e scelga Grav.
2. Inserisca la URL del suo sito Grav.
3. Lasci vuota la rotta del connettore, salvo che il suo plugin Grav usi una rotta diversa da quella predefinita. In caso contrario Hi, Moose usa la rotta del pacchetto di connessione oppure ripiega su `/himoose-connector`.
4. Incolli il pacchetto di connessione copiato dal plugin e salvi.
5. Faccia clic su **Test connector** per verificare la connessione con il suo sito Grav in produzione.

## Stato della connessione

Dopo la prova, Hi, Moose segnala uno tra vari stati: il connettore non è ancora del tutto configurato, è salvato ma non ancora verificato, ha risposto ma le azioni di scrittura da remoto non sono pienamente abilitate (sola lettura), è del tutto pronto per azioni di lettura e di scrittura da remoto, oppure l'ultima verifica è fallita e occorre controllare le impostazioni del sito o i segreti del plugin.

## Che cosa consente la connessione

Una volta pronta, il connettore Grav può elencare i contenuti, leggere il contenuto grezzo e creare, aggiornare e pubblicare contenuti direttamente, seguendo lo stesso percorso preparato e rivedibile usato da [Bozze, anteprima e pubblicazione](../features/drafts-and-publishing.md) per le altre connessioni.

## Sicurezza

La URL del suo sito Grav e il pacchetto di connessione sono salvati in locale e accessibili soltanto al processo in background dell'app desktop; non vengono mai esposti all'interfaccia utente.
