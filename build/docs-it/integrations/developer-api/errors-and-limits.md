---
source_hash: 85fe7ea99ed19540350085410907cba880592b989251ce17fdb81570b24829a2
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/integrations/developer-api/errors-and-limits/)


# Errori e limiti

## Errori

Gli errori usano il formato Problem Details (`application/problem+json`, RFC 9457) con un `code` stabile su cui puoi basare la logica del codice:

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/errors-and-limits/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

- `code` è il campo da controllare nel codice. Non cambia mai significato.
- `detail` è scritto per una persona e la formulazione può cambiare.
- `type` rimanda alla sezione della documentazione per quel tipo di errore.
- `requestId` identifica la richiesta. Citalo quando contatti il supporto. Viene inviato anche come intestazione `X-Request-Id` in ogni risposta.

Alcuni errori portano campi aggiuntivi, indicati nella tabella.

## Codici di errore

| Codice | Stato | Significato | Cosa fare |
|---|---|---|---|
| `invalid_key` | 401 | Manca l'intestazione `Authorization`, la chiave è nel formato sbagliato, oppure Hi, Moose non la conosce | Invia `Authorization: Bearer hmk_live_...`. Controlla che la chiave sia stata copiata per intero. |
| `key_revoked` | 401 | La chiave è stata revocata nelle Impostazioni | Crea una nuova chiave. |
| `key_expired` | 401 | La chiave ha superato la data di scadenza | Crea una nuova chiave. |
| `plan_required` | 403 | Il piano dell'account non include l'API | Passa a un piano a pagamento. |
| `insufficient_scope` | 403 | La chiave non ha il permesso per questa chiamata. Il corpo lo indica in `scope`. | Crea una chiave con quel permesso. |
| `not_found` | 404 | La risorsa non esiste, oppure la chiave non può leggerla. I due casi non vengono distinti. | Controlla l'id e l'accesso ai progetti della chiave. |
| `method_not_allowed` | 405 | L'endpoint esiste ma non con questo metodo | Vedi il [riferimento](reference.md). |
| `invalid_parameter` | 400 | Un parametro della query o un campo del corpo manca, è malformato o fuori intervallo. `detail` lo indica. | Correggi la richiesta. |
| `range_too_wide` | 400 | Da `from` a `to` passano più di 366 giorni | Chiedi un periodo più stretto. |
| `unsupported_filter_combination` | 400 | Filtri che non si possono combinare, per esempio `engine` con due tra `promptId`, `topicId` e `runId` | Togli un filtro. |
| `host_required` | 409 | Il progetto non ha un computer host scelto | Scegline uno in Hi, Moose in **Impostazioni → Hi, Moose MCP**. |
| `byok_not_supported` | 409 | In questo piano le impostazioni di monitoraggio vivono sul computer host, quindi l'API non può modificarle | Modificale in Hi, Moose su quel computer. |
| `plan_limit` | 409 | È stato raggiunto un limite del piano. Il corpo porta `limit`. | Controlla i limiti in `GET /projects/{id}/capabilities`. |
| `run_in_progress` | 409 | Una richiesta di esecuzione è già in coda, in attesa o in corso. Il corpo porta `requestId` e `requestStatus`. | Aspetta che finisca. |
| `insufficient_allowance` | 409 | L'esecuzione costerebbe più del credito rimanente. Il corpo porta `estimatedUnits`, `remainingUnits` e `periodEndsAt`. | Ricarica, oppure riduci prompt, motori o campioni. |
| `no_prompts` | 409 | Il progetto non ha alcun prompt monitorato con un motore | Aggiungi prima prompt e motori. |
| `rate_limited` | 429 | È stato raggiunto il limite al minuto o al giorno | Attendi i secondi indicati in `Retry-After`. |
| `daily_run_limit` | 429 | Il progetto ha fatto le sue 24 richieste di esecuzione per oggi | Riprova domani. |
| `internal` | 500 | Qualcosa è andato storto dal lato Hi, Moose | Riprova con backoff. Se persiste, contatta il supporto con il `requestId`. |

Un `502` o `503` senza corpo significa che l'API non ha raggiunto il suo backend. Riprova con backoff.

## Limiti di frequenza

| Limite | Valore |
|---|---|
| Per chiave | 300 richieste al minuto |
| Per account | 50.000 richieste al giorno |
| Richieste di esecuzione per progetto | 24 al giorno, una alla volta |
| Webhook per progetto | 5 |
| Righe per pagina | 200 |
| Periodo per richiesta | 366 giorni |

Oltre il limite l'API risponde `429 rate_limited` con un'intestazione `Retry-After`. Ogni risposta porta `RateLimit-Policy`, e le risposte riuscite portano `RateLimit` con il budget rimanente del giorno, secondo la bozza IETF sulle intestazioni di rate limit:

```
RateLimit-Policy: "per-minute";q=300;w=60, "per-day";q=50000;w=86400
RateLimit: "per-day";r=49871;t=61234
```

Il limite al minuto è contato per chiave all'edge ed è approssimativo; una breve raffica poco sopra il limite può passare. Il limite al giorno è contato per account su tutte le sue chiavi.

## Restare sotto i limiti

- **Metti in cache dalla tua parte.** Le statistiche giornaliere portano `Cache-Control: max-age=60`. Una dashboard che si aggiorna ogni minuto legge il riepilogo una volta al minuto per grafico, non una volta per visitatore.
- **Usa i riepiloghi.** Le statistiche giornaliere e quelle dei concorrenti sono costruite da una tabella di riepilogo. Disegna i grafici da quelle, e leggi le singole risposte solo quando qualcuno apre una riga.
- **Usa gli ETag.** Le risposte portano un `ETag`. Rimandalo in `If-None-Match` e un `304` costa quasi nulla.
- **Usa i webhook** invece di interrogare l'API per sapere se un'esecuzione è terminata. Vedi [Webhook](webhooks.md).
- **Fai backoff sul 429.** Attendi i secondi di `Retry-After`, poi riprova. Non riprovare subito.

## Id delle richieste

Ogni risposta porta `X-Request-Id`. Registralo accanto al tuo log delle richieste, così una segnalazione di problema può essere abbinata ai log di Hi, Moose. I corpi degli errori lo ripetono come `requestId`.
