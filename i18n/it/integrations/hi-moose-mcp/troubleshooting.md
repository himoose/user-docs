---
source_hash: 44a098b9f501f2117290c2037c5635c5aa9f250b49d72a34e103dba9d3cb8b5b
---

# Risoluzione dei problemi

Cosa fare quando Hi, Moose MCP non risponde come ti aspetti. La maggior parte dei problemi dipende dal dispositivo host: il computer dove Hi, Moose resta aperto e fa il lavoro.

## «Il dispositivo host di questo progetto non si è collegato»

Il computer scelto come dispositivo host è spento, in sospensione, offline, oppure Hi, Moose è chiuso o disconnesso lì.

1. Apri Hi, Moose su quel computer ed effettua l'accesso.
2. Aspetta un minuto e chiedi di nuovo. Il dispositivo host si collega ogni pochi minuti finché Hi, Moose è aperto.
3. Se il computer non c'è più, scegline un altro in **Impostazioni → Hi, Moose MCP**. Solo il proprietario dell'account può cambiare il dispositivo host.

I lavori aspettano il dispositivo host fino a 15 minuti. Dopo scadono e l'app riceve un messaggio che lo segnala; chiedi di nuovo quando il dispositivo host è tornato.

## «Questo progetto non ha un dispositivo host»

Nessuno ha ancora scelto un dispositivo host per il progetto. Apri Hi, Moose sul computer che deve fare il lavoro, vai in **Impostazioni → Hi, Moose MCP** e sceglilo. Ogni progetto ha il proprio dispositivo host, quindi anche un nuovo progetto ne ha bisogno di uno.

## L'app dice che il lavoro è ancora in corso

Brief, bozze, audit e audio richiedono minuti, e alcune app smettono di aspettare prima che il lavoro sia finito. Chiedi all'app di controllare di nuovo; ritira il risultato con l'id del lavoro che ha ricevuto. Il lavoro viene salvato anche nella tua [Library](../../library/overview.md) in Hi, Moose, quindi non si perde nulla se la chat va avanti.

L'audio è il più lungo: circa 5 minuti per un episodio short, 9 per standard e 15 per deep. Nel frattempo il dispositivo host non lavora su nient'altro, quindi una seconda richiesta aspetta dietro la prima.

## L'app ha scelto il progetto sbagliato

Gli strumenti ricevono il progetto per nome. Dillo nella richiesta, per esempio «per il progetto Acme», oppure chiedi all'app di elencare prima i progetti e poi scegliere. Se due progetti hanno nomi simili, usa esattamente quello mostrato in Hi, Moose.

## Il connettore non si collega

- **La pagina di accesso non si apre.** Controlla che l'indirizzo del server sia `https://mcp.himoose.com/mcp`, senza caratteri in più, e che l'app usi OAuth, non una chiave API.
- **Il codice di accesso è scaduto.** Il codice vale due minuti. Riavvia il collegamento dall'app.
- **Claude Team o Enterprise.** Un owner deve aggiungere il connettore per l'organizzazione prima che i membri possano collegarsi.
- **ChatGPT.** I server MCP personalizzati richiedono un piano a pagamento, e negli spazi Business ed Enterprise un owner potrebbe dover prima consentire i connettori personalizzati o attivare la Modalità sviluppatore. I nomi dei menu cambiano; vedi [Collegare in ChatGPT](../hi-moose-mcp.md#connect-in-chatgpt).

## L'app era collegata e ora non lo è più

L'accesso scade da solo dopo 30 giorni senza utilizzo, e il proprietario dell'account può revocare un'app in **Impostazioni → Hi, Moose MCP**. Collegati di nuovo dall'app.

## I risultati sembrano vecchi

- **Copertura del sito e link interni** leggono l'ultima scansione del tuo sito e ne indicano la data. Le pagine pubblicate dopo non sono incluse. Avvia una scansione in Hi, Moose e chiedi di nuovo.
- **Visibilità e opportunità** leggono solo i risultati salvati e non avviano mai nuove verifiche. Coprono i prompt monitorati sui motori monitorati nel periodo indicato nella risposta. Per vedere un nuovo argomento, aggiungi un prompt per esso nella schermata Visibilità e lascia che avvenga un'esecuzione.

## È stato eseguito qualcosa che non ti aspettavi

La tabella **Lavori recenti degli agenti** in **Impostazioni → Hi, Moose MCP** elenca ogni lavoro: cosa è stato chiesto, da quale app, quando e se è terminato. I lavori vengono eseguiti con l'account connesso sul dispositivo host, quindi un'app collegata può leggere e scrivere solo la Library di quell'account.

## Ancora bloccato

Scrivi al supporto con il nome del progetto, l'app che stavi usando, più o meno quando è successo e cosa ha detto l'app. Anche la tabella dei lavori degli agenti aiuta.
