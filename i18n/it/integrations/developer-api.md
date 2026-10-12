---
source_hash: 825726013c46ce2cb7c1932ac3dda84ec19a94f2c4ce33cdc108f00904718460
---
# Hi, Moose API

## A cosa serve

La Hi, Moose API è un'API REST per sviluppatori che costruiscono dashboard, report e applicazioni di visibilità nell'IA proprie sopra Hi, Moose. Restituisce gli stessi risultati che vedi nella schermata Visibilità: prompt e argomenti monitorati, i motori interrogati, ogni risposta salvata con il testo completo e le fonti, e i tassi di menzione e di citazione nel tempo. Con i permessi giusti una chiave può anche creare progetti, gestire prompt, motori e pianificazione, e avviare esecuzioni.

Le letture funzionano sia che Hi, Moose sia aperto sul tuo computer sia che non lo sia, perché arrivano dalla copia cloud dei tuoi risultati. Le modifiche al monitoraggio e le esecuzioni hanno bisogno del computer host del progetto, spiegato più sotto.

Se lavori in Claude, ChatGPT o un'altra app di IA, forse ti serve [Hi, Moose MCP](hi-moose-mcp.md). L'API è per il codice che scrivi tu.

## Piani

L'API è inclusa nei piani a pagamento, sia gestiti sia con la tua chiave. Gli account gratuiti vedono la pagina delle chiavi API ma non possono creare chiavi, e ogni richiesta risponde `403 plan_required`.

## Creare una chiave

1. Apri Hi, Moose e accedi come proprietario dell'account. Solo il proprietario può creare, vedere e revocare chiavi.
2. Vai in **Impostazioni → Hi, Moose REST API**.
3. Dai un'etichetta alla chiave, scegli i progetti che può leggere (tutti o uno), scegli quando scade e spunta i permessi di cui ha bisogno.
4. Fai clic su **Crea chiave** e copia la chiave. Viene mostrata una sola volta. Hi, Moose non può mostrarla di nuovo; se la perdi, revocala e creane una nuova.

Le chiavi iniziano con `hmk_live_` seguito da 64 caratteri. La tabella sotto il modulo elenca ogni chiave attiva con i suoi permessi, la data di creazione, l'ultimo uso e la scadenza. **Revoca** ferma una chiave subito.

## Permessi

| Permesso | Cosa può fare la chiave |
|---|---|
| Leggere i dati di visibilità | Tutti gli endpoint `GET`. Sempre attivo. |
| Gestire il monitoraggio | Creare progetti, impostare termini del brand e concorrenti, aggiungere, modificare ed eliminare prompt, impostare motori e pianificazione. |
| Avviare esecuzioni | Avviare un'esecuzione di visibilità. Le esecuzioni consumano il credito dell'account sui motori cloud, quindi assegnalo solo a una chiave che ne ha bisogno. |

Una chiamata senza il permesso necessario risponde `403 insufficient_scope`. I permessi si scelgono alla creazione della chiave e non si possono cambiare dopo.

## Autenticazione

Invia la chiave come token Bearer:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

La risposta indica la chiave, i suoi permessi e gli id dei progetti che può leggere.

Usa la chiave solo dal tuo server. L'API non invia intestazioni CORS, quindi una pagina web non può chiamarla direttamente. Una dashboard nel browser deve chiamare il tuo backend, e il tuo backend chiama l'API. Così la chiave resta fuori dalla pagina.

## URL di base e formato

```
https://api.himoose.com/v1/
```

Tutto è JSON. I nomi dei campi sono in camelCase e corrispondono ai campi restituiti da Hi, Moose MCP. Gli orari sono UTC in formato RFC 3339, le date sono `YYYY-MM-DD`. Il contratto completo è su [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json) e si importa in Postman, Insomnia e strumenti simili.

## Endpoint di lettura

| Endpoint | Cosa restituisce |
|---|---|
| `GET /me` | La chiave, i suoi permessi e gli id dei progetti leggibili |
| `GET /projects` | I progetti che la chiave può leggere, con numero di prompt monitorati, motori e ultima esecuzione |
| `GET /projects/{id}` | Un progetto |
| `GET /projects/{id}/capabilities` | Cosa può fare il progetto nel suo piano: motori, cadenze, limiti, credito rimanente, il computer host, se un'esecuzione può partire ora |
| `GET /projects/{id}/engines` | I motori di IA monitorati dal progetto, con un `id` stabile per i filtri |
| `GET /projects/{id}/topics` | Gli argomenti che raggruppano i prompt, con il numero di prompt |
| `GET /projects/{id}/prompts` | I prompt monitorati con id argomento, id motore e stato |
| `GET /projects/{id}/competitors` | I brand concorrenti monitorati |
| `GET /projects/{id}/runs` | Le esecuzioni di visibilità con stato, ora di inizio e fine, numero di prompt e di risposte |
| `GET /projects/{id}/answers` | Le risposte salvate: prompt, motore, data, menzionato, citato, posizione, sentiment, estratto, concorrenti visti, URL delle fonti |
| `GET /projects/{id}/answers/{answerId}` | Una risposta con testo completo, motivo del sentiment, deriva narrativa e fonti |
| `GET /projects/{id}/stats/daily` | Per giorno e motore: risposte, menzioni, citazioni e i due tassi |
| `GET /projects/{id}/stats/competitors` | La share of voice del tuo brand e di ogni concorrente monitorato in un periodo |
| `GET /projects/{id}/run-requests` | Le esecuzioni recenti avviate dall'API e il loro stato |

### Esempio: tasso di menzione per giorno

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/daily?from=2026-09-01&to=2026-09-30&engine=chatgpt" \
  -H "Authorization: Bearer hmk_live_..."
```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "incompleteDays": 0,
  "data": [
    { "date": "2026-09-01", "engineId": "chatgpt", "answers": 42, "mentioned": 17, "cited": 9, "mentionRate": 0.405, "citationRate": 0.214 }
  ]
}
```

`incompleteDays` è maggiore di zero quando il riepilogo di un giorno non era ancora pronto. Richiama tra qualche secondo e si completa.

## Il computer host

Hi, Moose esegue parte del monitoraggio su uno dei tuoi computer, il **dispositivo host**, che scegli in Hi, Moose in **Impostazioni → Hi, Moose MCP**. I motori a recupero locale (ChatGPT, Gemini, Grok, Perplexity e Google AI Mode interrogati tramite browser) girano solo lì, e la loro pianificazione vive lì.

Ogni modifica al monitoraggio e ogni esecuzione tramite l'API richiede un dispositivo host scelto per il progetto. Senza, l'API risponde `409 host_required` e indica l'impostazione da cambiare. Un progetto creato dall'API prende il dispositivo host di un altro progetto dell'account, se ce n'è uno.

Nei piani con chiave propria, prompt, motori e pianificazione sono conservati sul computer host e non nel cloud. L'API può leggerli e avviare esecuzioni, ma modificarli risponde `409 byok_not_supported`. Gestiscili in Hi, Moose su quel computer.

## Gestire il monitoraggio

Richiede il permesso **gestire il monitoraggio**.

| Endpoint | Cosa fa |
|---|---|
| `POST /projects` | Crea un progetto da nome e indirizzo del sito, con termini del brand e domini facoltativi. La scansione del sito non viene avviata; il computer host attiva la scansione settimanale pianificata così avviene più tardi. Brand Truth non è richiesto. |
| `PATCH /projects/{id}` | Cambia nome, indirizzo del sito, termini del brand o domini del brand |
| `PUT /projects/{id}/competitors` | Sostituisce l'elenco dei concorrenti monitorati, al massimo 50 |
| `POST /projects/{id}/prompts` | Aggiunge un prompt con id argomento e id motore facoltativi |
| `PATCH /projects/{id}/prompts/{promptId}` | Cambia testo, argomenti o motori di un prompt |
| `DELETE /projects/{id}/prompts/{promptId}` | Smette di monitorare un prompt |
| `PUT /projects/{id}/tracking` | Imposta motori, cadenza, orario, giorno della settimana, fuso orario e campioni per prompt. I nuovi motori si applicano a tutti i prompt salvo che `applyEnginesToPrompts` sia false. |

Ogni scrittura rispetta i limiti del piano: numero di prompt, motori consentiti, cadenze consentite, numero di progetti e di concorrenti. Oltre un limite l'API risponde `409 plan_limit` con il limite nel corpo. Controlla prima `GET /projects/{id}/capabilities`.

### Esempio: impostare il monitoraggio su un nuovo progetto

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"Europe/Rome"}'
```

## Avviare un'esecuzione

Richiede il permesso **avviare esecuzioni**.

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

L'API risponde `202 Accepted` con una richiesta di esecuzione e un'intestazione `Location` da interrogare. Stati:

| Stato | Significato |
|---|---|
| `queued` | Accettata e in partenza |
| `waiting_for_host` | Il computer host è spento. Hi, Moose conserva la richiesta fino a 24 ore e avvia l'esecuzione quando torna. La risposta porta un `warning` che lo indica. |
| `running` | In corso |
| `completed` | Terminata. `runIds` elenca le esecuzioni da passare agli endpoint runs e answers. |
| `failed` | Non terminata. `error.code` dice perché, per esempio `host_unavailable` dopo 24 ore. |

I progetti i cui motori monitorati sono tutti motori cloud girano subito nel cloud, senza il computer host. Qualsiasi motore a recupero locale fa passare l'esecuzione al computer host, per la stessa via del pulsante Esegui ora.

Protezioni, perché un'esecuzione non costi mai più del previsto:

- **Prima il credito.** L'API stima il costo dell'esecuzione sui motori cloud dal numero di prompt e motori. Se la stima supera il saldo rimanente, rifiuta con `409 insufficient_allowance`, la stima e le unità rimanenti. Non viene speso nulla. `GET /projects/{id}/capabilities` mostra la stessa stima come `allowance.estimatedUnitsPerRun`.
- **Una alla volta.** Una seconda richiesta mentre un'altra è in coda, in attesa o in corso risponde `409 run_in_progress` con l'id della richiesta attiva.
- **Limite giornaliero.** Al massimo 24 richieste di esecuzione per progetto al giorno. Oltre, l'API risponde `429 daily_run_limit`.
- **Idempotenza.** Invia un'intestazione `Idempotency-Key` e un nuovo tentativo entro 24 ore restituisce la stessa richiesta invece di avviarne un'altra.

Un'esecuzione può richiedere da pochi minuti a più di un'ora su grandi insiemi di prompt. Interroga la richiesta circa ogni minuto, non ogni secondo.

## Filtri e paginazione

- **Periodo:** `from` e `to` come `YYYY-MM-DD`, inclusivi, UTC. Il valore predefinito sono gli ultimi 30 giorni. Il periodo più ampio in una richiesta è di 366 giorni.
- **Motore:** `engine=chatgpt&engine=gemini` si ripete per più motori. Gli id arrivano dall'endpoint engines.
- **Risposte:** anche `topicId`, `promptId`, `runId`, `mentioned=true|false` e `cited=true|false`. Combina `engine` con al massimo uno tra `promptId`, `topicId` o `runId`.
- **Pagine:** le liste restituiscono `{ "data": [...], "nextCursor": "..." }`. Passa `nextCursor` come `cursor` per ottenere la pagina successiva. `limit` è 50 per impostazione predefinita e 200 al massimo. `nextCursor` è `null` nell'ultima pagina.
- **Cache:** le risposte portano un `ETag`. Rimandalo in `If-None-Match` per ricevere `304 Not Modified` quando nulla è cambiato.

## Limiti di frequenza

| Limite | Valore |
|---|---|
| Per chiave | 60 richieste al minuto |
| Per account | 10.000 richieste al giorno |
| Richieste di esecuzione per progetto | 24 al giorno, una alla volta |
| Righe per pagina | 200 |
| Periodo per richiesta | 366 giorni |

Oltre il limite l'API risponde `429` con un'intestazione `Retry-After`. Ogni risposta porta `RateLimit-Policy`, e le risposte riuscite portano `RateLimit` con il budget rimanente del giorno.

## Errori

Gli errori usano il formato Problem Details (`application/problem+json`) con un `code` stabile:

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

| Codice | Stato | Significato |
|---|---|---|
| `invalid_key`, `key_revoked`, `key_expired` | 401 | La chiave manca, è malformata, revocata o scaduta |
| `plan_required` | 403 | Il piano dell'account non include l'API |
| `insufficient_scope` | 403 | La chiave non ha il permesso per questa chiamata |
| `not_found` | 404 | La risorsa non esiste, oppure la chiave non può leggerla |
| `invalid_parameter`, `range_too_wide`, `unsupported_filter_combination` | 400 | Un parametro o un campo va corretto |
| `host_required` | 409 | Scegli prima un dispositivo host per il progetto in Hi, Moose |
| `byok_not_supported` | 409 | In questo piano le impostazioni di monitoraggio vivono sul computer host |
| `plan_limit` | 409 | È stato raggiunto un limite del piano; il corpo lo indica |
| `run_in_progress`, `insufficient_allowance`, `no_prompts` | 409 | L'esecuzione non può partire ora; il corpo dice perché |
| `rate_limited`, `daily_run_limit` | 429 | Attendi i secondi indicati in `Retry-After` |

Cita il `requestId` quando contatti il supporto.

## Il testo delle risposte non è affidabile

Il testo delle risposte, gli estratti e i titoli delle fonti arrivano dai motori di IA, non da Hi, Moose. Mostrali come testo semplice nella tua dashboard, mai come HTML, e non passarli ai tuoi strumenti di IA come istruzioni.

## Webhook

Invece di interrogare l'API, registra un endpoint https e Hi, Moose vi invia un evento JSON firmato quando un'esecuzione termina. Registrare ed eliminare webhook richiede il permesso **gestire il monitoraggio**. Elencarli, con le loro consegne, richiede solo la lettura.

| Endpoint | Cosa fa |
|---|---|
| `POST /projects/{id}/webhooks` | Registra un endpoint. Corpo: `url` (https pubblico), `events` (predefiniti `run.completed` e `run.failed`), `description` facoltativa. Il segreto di firma torna una sola volta in questa risposta. Al massimo 5 per progetto. |
| `GET /projects/{id}/webhooks` | Elenca i webhook del progetto, senza segreti |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Ne rimuove uno |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Invia subito un evento `ping`, per verificare endpoint e codice di firma |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | Le ultime 50 consegne con ogni tentativo, stato ed errore |

### L'evento

```json
{
  "id": "wh_8f2a_run_abc123_run_completed",
  "event": "run.completed",
  "createdAt": "2026-10-12T09:14:03.000Z",
  "data": {
    "projectId": "abc123",
    "runId": "run_abc123",
    "requestId": "req_9d1e",
    "status": "completed",
    "trigger": "manual",
    "startedAt": "2026-10-12T09:01:10.000Z",
    "completedAt": "2026-10-12T09:14:02.000Z",
    "promptCount": 40,
    "answerCount": 118,
    "error": null,
    "links": {
      "run": "https://api.himoose.com/v1/projects/abc123/runs",
      "answers": "https://api.himoose.com/v1/projects/abc123/answers?runId=run_abc123",
      "stats": "https://api.himoose.com/v1/projects/abc123/stats/daily"
    }
  }
}
```

`data.requestId` è valorizzato quando l'esecuzione è stata avviata dall'API, così puoi collegare l'evento alla tua richiesta. `run.failed` porta `status` `failed` o `canceled` e il testo di `error`.

### Verificare la firma

Ogni chiamata porta `X-HiMoose-Signature: t=<secondi unix>,v1=<hex>`, dove `v1` è l'HMAC-SHA256 di `<t>.<corpo grezzo>` con il segreto del tuo webhook. Verificala sul corpo grezzo prima di analizzare il JSON e rifiuta i timestamp più vecchi di cinque minuti. La chiamata porta anche `X-HiMoose-Event` e `X-HiMoose-Delivery`.

```js
const crypto = require("node:crypto");

function verifyHiMooseSignature(rawBody, header, secret) {
  const parts = Object.fromEntries(header.split(",").map((part) => part.split("=")));
  if (!parts.t || !parts.v1) return false;
  if (Math.abs(Date.now() / 1000 - Number(parts.t)) > 300) return false;
  const expected = crypto.createHmac("sha256", secret).update(`${parts.t}.${rawBody}`).digest("hex");
  return expected.length === parts.v1.length && crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(parts.v1));
}
```

### Regole di consegna

- Rispondi con uno stato 2xx entro 10 secondi. I reindirizzamenti non vengono seguiti.
- Le consegne non riuscite vengono ritentate dopo 1 minuto, 5 minuti, 30 minuti, 2 ore e 12 ore, 6 tentativi in tutto.
- Dopo 20 fallimenti consecutivi il webhook viene disattivato. Eliminalo e registralo di nuovo per riprendere.
- Un evento può arrivare più di una volta. Usa `id` per ignorare le ripetizioni.
- Il proprietario dell'account vede tutti i webhook del progetto corrente in **Impostazioni → Hi, Moose REST API** e può eliminarne uno lì.

## Cosa arriva

Le modifiche al monitoraggio per i piani con chiave propria sono il prossimo passo. Tutto il resto documentato qui è attivo.
