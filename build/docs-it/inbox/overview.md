---
source_hash: 9705deb0dc37b51cf84f956088049d0d7d87b416de55439c84ef17b2ef0d3d9c
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/inbox/overview/)

# Inbox

## A cosa serve

L'Inbox è il luogo in cui Hi, Moose porta in evidenza ciò che merita la sua attenzione: riscontri selezionati, audit ed eventi di pubblicazione, ciascuno legato a un artefatto reale anziché a una notifica generica. Trasforma segnali sparsi (variazioni di sentiment nella visibilità, scostamenti narrativi, imprecisioni sulla copertura funzionale, esiti degli AEO audits, risultati delle pubblicazioni e richieste di approvazione) in un'unica coda di lavoro ordinata per priorità.

## Che cosa compare nell'Inbox

Ogni voce dell'Inbox rimanda a qualcosa di concreto che può aprire e su cui può agire:

- **Segnali di visibilità**: sentiment negativo o misto rilevato in una risposta dell'IA, scostamento narrativo o imprecisione sulla copertura funzionale rispetto al suo [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), oppure un'[esecuzione di visibilità](../visibility/overview.md) completata o fallita.
- **Esiti degli AEO audits**: un audit completato, o un audit il cui piano d'azione ha fatto emergere una raccomandazione ad alta priorità.
- **Modifiche rilevate sul sito**: un unico riepilogo per ogni scansione di [site monitoring](../site-monitoring/overview.md), che si apre in una tabella con tutte le pagine modificate e il relativo livello di impatto. Le pagine irraggiungibili e i disservizi dell'intero sito sono segnalati come tipi di modifica a sé stanti.
- **Report dei workflows**: esiti dell'esecuzione di un [workflow](../workflows/overview.md), per esempio un'analisi pianificata che ha generato nuovi articoli o segnalato un'opportunità nella ricerca con IA.
- **Eventi di pubblicazione**: una pubblicazione **fallita**, o una modifica in attesa della sua approvazione. Le pubblicazioni riuscite non creano più una voce nell'Inbox, perché un muro di avvisi «ha funzionato» finisce per seppellire quelli che richiedono la sua attenzione.
- **Un messaggio di benvenuto** di Moose al termine della configurazione iniziale, con un primo passo sensato.

Ogni voce propone un'azione successiva quando ha senso: aprire l'artefatto, avviare un brief, dare seguito a un audit, rivedere una bozza, approvare una modifica o riprovare un'esecuzione fallita. Così non legge soltanto una notifica, ma è a un clic dall'agire.

I riepiloghi di site monitoring includono inoltre l'azione **Ask Moose about all of this**, che consegna l'istantanea della scansione alla [chat](../chat/overview.md) e le chiede da dove cominciare.

## Filtrare l'Inbox

Due filtri determinano che cosa vede:

- **Stato**: il valore predefinito è **Active**, cioè tutto ciò che non è stato scartato (voci aperte, in corso e completate). Passi a uno stato specifico oppure ad **All** per includere le voci scartate che potrebbe voler riprendere.
- **Gravità**: **Critical**, **Warning**, **Notice**, **Info**, oppure tutte.

Le voci sono raggruppate per data (per esempio «Ieri», «Meno recenti») con un contatore per gruppo, così vede subito quanto la attende. Le caselle voluminose vengono paginate anziché caricate tutte insieme.

**Segna tutto come letto** azzera l'indicatore su tutta la sua Inbox, non solo sulla pagina che sta guardando.

!!! note "L'Inbox conserva le 200 voci più recenti"
    Le più vecchie vengono rimosse automaticamente. L'Inbox è una coda di lavoro, non un archivio: tutto ciò che è duraturo si trova nella [Library](../library/overview.md) o nell'artefatto a cui la voce rimanda.

## Decidere che cosa la avvisa

Faccia clic su **Notifications** per aprire le sue preferenze di notifica per progetto. Che cosa fa ciascuna impostazione è spiegato in [Notifiche dell'Inbox](notifications.md).

## Gestito e BYOK

L'Inbox funziona allo stesso modo sia che il suo spazio di lavoro sia gestito sia che sia BYOK: le voci vengono scritte dal lato che ha davvero generato l'evento sottostante (il cloud per i workflows gestiti, il processo desktop locale per BYOK) e lei vede in entrambi i casi un'unica coda unificata.
