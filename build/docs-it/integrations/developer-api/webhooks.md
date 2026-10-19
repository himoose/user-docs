---
source_hash: 6467de19290f42e43d33241a37345989dbd6267011d89947d750f7e073ea66e2
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/integrations/developer-api/webhooks/)


# Webhook

Invece di interrogare l'API, registra un endpoint https e Hi, Moose vi invia un evento JSON firmato quando un'esecuzione termina. Registrare, testare ed eliminare webhook richiede il permesso **gestire il monitoraggio**. Elencarli, con le loro consegne, richiede solo la lettura.

## Endpoint

| Endpoint | Cosa fa |
|---|---|
| `POST /projects/{id}/webhooks` | Registra un endpoint. Corpo: `url` (https pubblico), `events` (predefiniti `run.completed` e `run.failed`), `description` facoltativa. Il segreto di firma torna una sola volta in questa risposta. Al massimo 5 per progetto. |
| `GET /projects/{id}/webhooks` | Elenca i webhook del progetto, senza segreti |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Ne rimuove uno |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Invia subito un evento `ping`, per verificare endpoint e codice di firma |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | Le ultime 50 consegne con ogni tentativo, stato ed errore |

## Registrarne uno

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"url":"https://reports.acme.example/himoose","description":"Nightly dashboard refresh"}'
```

```json
{
  "id": "BGXhe1dlOnmy36j6rRTa",
  "url": "https://reports.acme.example/himoose",
  "events": ["run.completed", "run.failed"],
  "description": "Nightly dashboard refresh",
  "active": true,
  "createdAt": "2026-10-15T03:20:10.000Z",
  "secret": "whsec_..."
}
```

Conserva `secret` accanto alla tua chiave. Viene mostrato solo in questa risposta. L'URL deve essere pubblico e usare https; indirizzi privati, localhost e http semplice vengono rifiutati con `400 invalid_parameter`.

Poi inviati un ping:

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/test \
  -H "Authorization: Bearer hmk_live_..."
```

La risposta è il record di consegna, e l'endpoint deliveries mostra il tentativo con lo stato HTTP con cui ha risposto il tuo endpoint.

## L'evento

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

| Evento | Quando |
|---|---|
| `run.completed` | Un'esecuzione è terminata e le sue risposte sono salvate. Contano le esecuzioni pianificate, quelle dal pulsante Esegui ora e quelle dall'API. |
| `run.failed` | Un'esecuzione è finita con `status` `failed` o `canceled`. `data.error` dice perché. |
| `ping` | Inviato dall'endpoint di test. `data` porta l'id del progetto e un messaggio. |

`data.requestId` è valorizzato quando l'esecuzione è stata avviata dall'API, così puoi collegare l'evento alla tua richiesta di esecuzione. È `null` per le esecuzioni pianificate e per quelle avviate in Hi, Moose.

L'evento è un segnale, non i dati. Su `run.completed`, segui `data.links.answers` oppure aggiorna le tue statistiche giornaliere. I riepiloghi giornalieri dei giorni dell'esecuzione vengono ricostruiti entro dieci minuti dalla fine dell'esecuzione; `incompleteDays` nella risposta delle statistiche indica quando non sono ancora pronti.

## Intestazioni

| Intestazione | Valore |
|---|---|
| `X-HiMoose-Signature` | `t=<unix seconds>,v1=<hex>`, vedi sotto |
| `X-HiMoose-Event` | Il nome dell'evento |
| `X-HiMoose-Delivery` | L'id della consegna, lo stesso dell'endpoint deliveries |
| `User-Agent` | `HiMoose-Webhooks/1.0` |
| `Content-Type` | `application/json` |

## Verificare la firma

`v1` è l'HMAC-SHA256 di `<t>.<raw body>` con il segreto del tuo webhook, come stringa esadecimale minuscola. Verificala sul corpo grezzo della richiesta prima di analizzare il JSON, confronta in tempo costante e rifiuta i timestamp più vecchi di cinque minuti.

=== "JavaScript"

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

=== "Python"

    ```python
    import hashlib
    import hmac
    import time

    def verify_himoose_signature(raw_body: bytes, header: str, secret: str) -> bool:
        parts = dict(part.split("=", 1) for part in header.split(",") if "=" in part)
        if "t" not in parts or "v1" not in parts:
            return False
        if abs(time.time() - int(parts["t"])) > 300:
            return False
        expected = hmac.new(secret.encode(), f"{parts['t']}.".encode() + raw_body, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, parts["v1"])
    ```

La maggior parte dei framework web analizza il JSON prima che giri il tuo codice. Assicurati di firmare i byte così come ricevuti, non una copia riserializzata, altrimenti la firma non corrisponderà.

## Regole di consegna

- Rispondi con uno stato 2xx entro 10 secondi. Fai il lavoro dopo aver risposto, non prima. I reindirizzamenti non vengono seguiti.
- Le consegne non riuscite vengono ritentate dopo 1 minuto, 5 minuti, 30 minuti, 2 ore e 12 ore, 6 tentativi in tutto. Una consegna è `pending` finché restano tentativi, `delivered` dopo un 2xx, `failed` dopo l'ultimo tentativo.
- Dopo 20 fallimenti consecutivi il webhook viene disattivato, `active` diventa false e non vengono più inviati eventi. Eliminalo e registralo di nuovo per riprendere.
- Un evento può arrivare più di una volta. Usa `id` per ignorare le ripetizioni.
- Gli eventi di un progetto possono arrivare fuori ordine quando c'è di mezzo un nuovo tentativo. Usa `createdAt` se l'ordine conta.

## Vedere le consegne

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/deliveries \
  -H "Authorization: Bearer hmk_live_..."
```

Ogni consegna elenca tutti i tentativi con l'ora, lo stato HTTP con cui ha risposto il tuo endpoint, quanto ha impiegato ed eventuali errori. Quando un endpoint si comporta male, questo è il primo posto dove guardare.

Il proprietario dell'account vede tutti i webhook del progetto corrente in **Impostazioni → Hi, Moose REST API** con lo stato dell'ultima consegna, e può eliminarne uno lì.
