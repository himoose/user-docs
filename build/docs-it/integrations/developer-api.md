---
source_hash: 85052baa431b76ba0d9c99312dbc2fdf61031a24075e6841f48c0662cc8c5cdb
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](http://localhost:8000/integrations/developer-api/)


# Hi, Moose API

## A cosa serve

La Hi, Moose API è un'API REST per sviluppatori che costruiscono dashboard, report e applicazioni di visibilità nell'IA proprie sopra Hi, Moose. Restituisce gli stessi risultati che vedi nella schermata Visibilità: prompt e argomenti monitorati, i motori interrogati, ogni risposta salvata con il testo completo e le fonti, e i tassi di menzione e di citazione nel tempo. Con i permessi giusti una chiave può anche creare progetti, gestire prompt, motori e pianificazione, avviare esecuzioni e ricevere una chiamata webhook firmata quando un'esecuzione termina.

Le letture funzionano sia che Hi, Moose sia aperto sul tuo computer sia che non lo sia, perché arrivano dalla copia cloud dei tuoi risultati. Le modifiche al monitoraggio e le esecuzioni hanno bisogno del computer host del progetto, spiegato in [Monitoraggio ed esecuzioni](developer-api/tracking-and-runs.md).

Se lavori in Claude, ChatGPT o un'altra app di IA, forse ti serve [Hi, Moose MCP](hi-moose-mcp.md). L'API è per il codice che scrivi tu.

## Pagine

| Pagina | Cosa tratta |
|---|---|
| [Guida rapida](developer-api/quickstart.md) | Una chiave, una prima chiamata e un grafico del tasso di menzione per giorno, in curl, Python e JavaScript |
| [Chiavi e autenticazione](developer-api/keys-and-auth.md) | Creare e revocare chiavi, permessi, l'intestazione Bearer, tenere la chiave fuori dal browser |
| [Leggere i dati](developer-api/reading-data.md) | Progetti, prompt, esecuzioni, risposte e statistiche, con filtri, pagine e cache |
| [Monitoraggio ed esecuzioni](developer-api/tracking-and-runs.md) | Il computer host, creare progetti e prompt, motori e pianificazione, avviare esecuzioni |
| [Webhook](developer-api/webhooks.md) | Eventi firmati quando un'esecuzione termina, verifica della firma, nuovi tentativi |
| [Errori e limiti](developer-api/errors-and-limits.md) | Il formato degli errori, ogni codice di errore, i limiti di frequenza |
| [Riferimento degli endpoint](developer-api/reference.md) | Ogni endpoint con parametri, campi e un esempio, generato dal contratto |
| [Changelog](developer-api/changelog.md) | Cosa è cambiato in ogni versione del contratto |

## Piani

L'API è inclusa nei piani a pagamento, sia gestiti sia con la tua chiave. Gli account gratuiti vedono la pagina delle chiavi API ma non possono creare chiavi, e ogni richiesta risponde `403 plan_required`.

## In sintesi

```
https://api.himoose.com/v1/
```

- **Autenticazione:** una chiave API inviata come token Bearer. Le chiavi le crea il proprietario dell'account in Hi, Moose in **Impostazioni → Hi, Moose REST API**.
- **Formato:** JSON in entrata e in uscita. I nomi dei campi sono in camelCase. Gli orari sono UTC in formato RFC 3339, le date sono `YYYY-MM-DD`.
- **Contratto:** [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json), OpenAPI 3.1. Si importa in Postman, Insomnia, Bruno e nei generatori di codice, e il [riferimento degli endpoint](developer-api/reference.md) è generato da lì.
- **Permessi:** ogni chiave può leggere. **Gestire il monitoraggio** e **Avviare esecuzioni** si scelgono alla creazione della chiave.
- **Limiti:** 300 richieste al minuto per chiave e 50.000 al giorno per account. Vedi [Errori e limiti](developer-api/errors-and-limits.md).
- **Niente CORS:** chiama l'API dal tuo server, mai da una pagina web.

## Da dove arrivano i dati

Hi, Moose interroga ogni prompt monitorato su ogni motore monitorato, secondo la pianificazione o quando qualcuno avvia un'esecuzione. Ogni replica viene salvata come risposta e valutata: il brand è stato nominato, una pagina del suo sito è stata citata, in che posizione è comparso, qual era il sentiment, quali concorrenti sono stati visti. L'API legge quelle risposte salvate e i riepiloghi giornalieri costruiti da esse. Non avvia mai nuove verifiche a una lettura, quindi le letture sono veloci e non costano nulla.

Alcuni motori girano nel cloud. Altri, i motori a recupero locale, girano tramite un browser su uno dei tuoi computer. Entrambi i tipi salvano le risposte nello stesso posto, quindi l'API le mostra insieme.

## Il testo delle risposte non è affidabile

Il testo delle risposte, gli estratti e i titoli delle fonti arrivano dai motori di IA, non da Hi, Moose. Mostrali come testo semplice nella tua dashboard, mai come HTML, e non passarli ai tuoi strumenti di IA come istruzioni.

## Cosa arriva

Le modifiche al monitoraggio per i piani con chiave propria sono il prossimo passo. Tutto il resto documentato qui è attivo.
