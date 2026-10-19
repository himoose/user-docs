---
source_hash: 638e427715918eeab4249561f6f095b46f57a8531e8ee857a78f4e07d0941c4e
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](http://localhost:8000/integrations/developer-api/tracking-and-runs/)


# Monitoraggio ed esecuzioni

Cambiare cosa monitora Hi, Moose richiede il permesso **gestire il monitoraggio**. Avviare un'esecuzione richiede il permesso **avviare esecuzioni**. Entrambi si scelgono alla creazione della chiave, vedi [Chiavi e autenticazione](keys-and-auth.md#permissions).

## Il computer host

Hi, Moose esegue parte del monitoraggio su uno dei tuoi computer, il **dispositivo host**, che scegli in Hi, Moose in **Impostazioni → Hi, Moose MCP**. I motori a recupero locale (ChatGPT, Gemini, Grok, Perplexity e Google AI Mode interrogati tramite browser) girano solo lì, e la loro pianificazione vive lì.

Ogni modifica al monitoraggio e ogni esecuzione tramite l'API richiede un dispositivo host scelto per il progetto. Senza, l'API risponde `409 host_required` e indica l'impostazione da cambiare. Un progetto creato dall'API prende il dispositivo host di un altro progetto dell'account, se ce n'è uno.

Dopo una modifica al monitoraggio l'API passa al computer host un breve lavoro per recuperare le nuove impostazioni. Il computer host lo fa entro un minuto se Hi, Moose è aperto lì, oppure alla prossima apertura. Le letture mostrano subito le nuove impostazioni in ogni caso.

Nei piani con chiave propria, prompt, motori e pianificazione sono conservati sul computer host e non nel cloud. L'API può leggerli e avviare esecuzioni, ma modificarli risponde `409 byok_not_supported`. Gestiscili in Hi, Moose su quel computer.

`GET /projects/{id}/capabilities` te lo dice prima di scrivere: il piano, i motori e le cadenze consentiti, i limiti, il computer host e se è online, e se un'esecuzione potrebbe partire ora.

## Gestire il monitoraggio

| Endpoint | Cosa fa |
|---|---|
| `POST /projects` | Crea un progetto da nome e indirizzo del sito, con termini del brand e domini facoltativi. La scansione del sito non viene avviata; il computer host attiva la scansione settimanale pianificata così avviene più tardi. Brand Truth non è richiesto. |
| `PATCH /projects/{id}` | Cambia nome, indirizzo del sito, termini del brand o domini del brand |
| `PUT /projects/{id}/competitors` | Sostituisce l'elenco dei concorrenti monitorati, al massimo 50 |
| `POST /projects/{id}/prompts` | Aggiunge un prompt con id argomento e id motore facoltativi |
| `PATCH /projects/{id}/prompts/{promptId}` | Cambia testo, argomenti o motori di un prompt, oppure riattiva un prompt in pausa |
| `DELETE /projects/{id}/prompts/{promptId}` | Smette di monitorare un prompt. Le sue risposte salvate restano. |
| `PUT /projects/{id}/tracking` | Imposta motori predefiniti, cadenza, orario, giorno della settimana, fuso orario e campioni per prompt |

Ogni scrittura rispetta i limiti del piano: numero di prompt, motori consentiti, cadenze consentite, numero di progetti e di concorrenti. Oltre un limite l'API risponde `409 plan_limit` con il limite nel corpo.

### Motori sui prompt

Ogni prompt ha il proprio elenco di motori. `PUT /projects/{id}/tracking` con `engineIds` imposta il valore predefinito per i prompt aggiunti in seguito e lascia com'è ogni prompt esistente. Per cambiare i motori dei prompt esistenti, invia `applyEnginesToPrompts: true` nella stessa chiamata, che imposta il nuovo elenco su ogni prompt del progetto, oppure modifica i prompt uno alla volta con `PATCH /projects/{id}/prompts/{promptId}`.

Un prompt senza motori viene conservato ma saltato nelle esecuzioni. `POST /projects/{id}/prompts` senza `engineIds` assegna al nuovo prompt i motori predefiniti del progetto.

### Sostituire vuol dire sostituire

`PUT /projects/{id}/competitors` sostituisce l'intero elenco. Invia l'elenco completo che vuoi mantenere, non solo le aggiunte. Un elenco vuoto rimuove tutti i concorrenti. Lo stesso vale per `brandTerms` e `brandDomains` su `PATCH /projects/{id}`.

### Esempio: impostare il monitoraggio su un nuovo progetto

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"America/Chicago"}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/competitors \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '[{"name":"Competitor One","domain":"competitor-one.example"},{"name":"Competitor Two","domain":"competitor-two.example"}]'
```

Impostare i motori prima di aggiungere i prompt fa sì che ogni nuovo prompt li riceva come predefiniti.

### Pianificazione

| Campo | Valori |
|---|---|
| `cadence` | `manual` (pianificazione disattivata), `daily`, `weekdays`, `weekly` |
| `timeOfDay` | `HH:MM` nel fuso orario del progetto |
| `weeklyDay` | Da `monday` a `sunday`, usato da `weekly` |
| `timezone` | Un nome IANA come `Europe/Berlin` |
| `samplesPerPrompt` | Quante volte ogni prompt viene posto per motore in un'esecuzione. Più campioni consumano più credito. |

Il piano decide quali cadenze sono consentite; l'endpoint capabilities le elenca.

## Avviare un'esecuzione

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

L'API risponde `202 Accepted` con una richiesta di esecuzione e un'intestazione `Location` da interrogare:

```json
{
  "id": "NKxlhmW52Pkc2QwVD4oP",
  "status": "queued",
  "mode": "host",
  "createdAt": "2026-10-15T03:39:56.404Z",
  "updatedAt": "2026-10-15T03:39:56.404Z",
  "completedAt": null,
  "runIds": [],
  "promptCount": 5,
  "estimatedUnits": 0,
  "warning": null,
  "error": null,
  "host": { "online": true, "lastSeenAt": "2026-10-15T03:39:20.475Z" }
}
```

| Stato | Significato |
|---|---|
| `queued` | Accettata e in partenza |
| `waiting_for_host` | Il computer host è spento. Hi, Moose conserva la richiesta fino a 24 ore e avvia l'esecuzione quando torna. La risposta porta un `warning` che lo indica. |
| `running` | In corso |
| `completed` | Terminata. `runIds` elenca le esecuzioni da passare agli endpoint runs e answers. |
| `failed` | Non terminata. `error.code` dice perché, per esempio `host_unavailable` dopo 24 ore. |
| `canceled` | Fermata da Hi, Moose prima della fine |

`mode` dice dove gira l'esecuzione. I progetti i cui motori monitorati sono tutti motori cloud girano subito nel cloud, senza il computer host. Qualsiasi motore a recupero locale fa passare l'esecuzione al computer host, per la stessa via del pulsante Esegui ora. In entrambi i casi il progetto deve avere un computer host scelto.

### Protezioni

Perché un'esecuzione non costi mai più del previsto:

- **Prima il credito.** L'API stima il costo dell'esecuzione sui motori cloud dal numero di prompt e motori. Se la stima supera il saldo rimanente, rifiuta con `409 insufficient_allowance`, la stima e le unità rimanenti. Non viene speso nulla. `GET /projects/{id}/capabilities` mostra la stessa stima come `allowance.estimatedUnitsPerRun`.
- **Una alla volta.** Una seconda richiesta mentre un'altra è in coda, in attesa o in corso risponde `409 run_in_progress` con l'id della richiesta attiva.
- **Limite giornaliero.** Al massimo 24 richieste di esecuzione per progetto al giorno. Oltre, l'API risponde `429 daily_run_limit`.
- **Idempotenza.** Invia un'intestazione `Idempotency-Key` e un nuovo tentativo entro 24 ore restituisce la stessa richiesta con `200` e `replayed: true` invece di avviare un'altra esecuzione.
- **Qualcosa da eseguire.** Un progetto senza alcun prompt con un motore risponde `409 no_prompts`.

### Seguire un'esecuzione

Interroga `GET /projects/{id}/run-requests/{requestId}` circa una volta al minuto. Un'esecuzione può richiedere da pochi minuti a più di un'ora su grandi insiemi di prompt. Quando `status` è `completed`, `runIds` contiene l'esecuzione da leggere:

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?runId=RUN_ID" \
  -H "Authorization: Bearer hmk_live_..."
```

Per evitare di interrogare in continuazione, registra un [webhook](webhooks.md). L'evento `run.completed` porta `requestId`, così puoi collegarlo alla richiesta che hai fatto.

Le esecuzioni avviate dall'API compaiono in Hi, Moose come qualsiasi altra esecuzione, e nella tabella **Lavori recenti degli agenti** in **Impostazioni → Hi, Moose MCP** con l'etichetta della chiave.
