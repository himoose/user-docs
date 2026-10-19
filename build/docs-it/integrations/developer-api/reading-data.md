---
source_hash: 28ad9511fc5703f0dd6c90a7f591758445fdd08a95dcdb389dc29a304c90278d
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](http://localhost:8000/integrations/developer-api/reading-data/)


# Leggere i dati

Ogni chiave può leggere. Le letture arrivano dalla copia cloud dei tuoi risultati, quindi funzionano sia che Hi, Moose sia aperto sul tuo computer sia che non lo sia, e non avviano mai nuove verifiche.

## Gli endpoint di lettura

| Endpoint | Cosa restituisce |
|---|---|
| `GET /me` | La chiave, i suoi permessi e gli id dei progetti leggibili |
| `GET /projects` | I progetti che la chiave può leggere, con numero di prompt monitorati, motori e ultima esecuzione |
| `GET /projects/{id}` | Un progetto |
| `GET /projects/{id}/capabilities` | Cosa può fare il progetto nel suo piano: motori, cadenze, limiti, credito rimanente, il computer host, se un'esecuzione può partire ora |
| `GET /projects/{id}/engines` | I motori di IA monitorati dal progetto, con un `id` stabile per i filtri e se ognuno gira nel cloud o sul computer host |
| `GET /projects/{id}/topics` | Gli argomenti che raggruppano i prompt, con il numero di prompt |
| `GET /projects/{id}/prompts` | I prompt monitorati con id argomento, id motore e stato |
| `GET /projects/{id}/competitors` | I brand concorrenti monitorati e i loro domini |
| `GET /projects/{id}/runs` | Le esecuzioni di visibilità con stato, ora di inizio e fine, numero di prompt e di risposte |
| `GET /projects/{id}/answers` | Le risposte salvate: prompt, motore, data, menzionato, citato, posizione, sentiment, estratto, concorrenti visti, URL delle fonti |
| `GET /projects/{id}/answers/{answerId}` | Una risposta con testo completo, motivo del sentiment, deriva narrativa e fonti |
| `GET /projects/{id}/stats/daily` | Per giorno e motore: risposte, menzioni, citazioni e i due tassi |
| `GET /projects/{id}/stats/competitors` | La share of voice del tuo brand e di ogni concorrente monitorato in un periodo |
| `GET /projects/{id}/run-requests` | Le esecuzioni recenti avviate dall'API e il loro stato |
| `GET /projects/{id}/webhooks` | I webhook del progetto, senza segreti |

Il dettaglio campo per campo di ognuno è nel [riferimento degli endpoint](reference.md).

## Come si collegano i dati

- Un **progetto** monitora un sito. Ha dei **prompt**, le domande poste, raggruppati in **argomenti**.
- Ogni prompt gira su uno o più **motori**: ChatGPT, Perplexity, Gemini e altri. Gli id dei motori come `chatgpt` o `chatgpt-local-fetch` arrivano dall'endpoint engines e sono i valori accettati da ogni filtro `engine`.
- Un'**esecuzione** interroga ogni prompt attivo sui suoi motori e salva una **risposta** per prompt, motore e campione. Le esecuzioni partono dalla pianificazione del progetto, dal pulsante Esegui ora o dall'API.
- Ogni risposta viene valutata: `mentioned` quando il brand è stato nominato, `cited` quando una pagina del sito del brand è stata indicata come fonte, più `position`, `sentiment` e quali **concorrenti** sono stati visti.
- Le **statistiche giornaliere** contano le risposte per giorno e motore e calcolano `mentionRate` e `citationRate`. Le **statistiche dei concorrenti** fanno lo stesso per brand in un periodo.

## Tasso di menzione per giorno

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

I tassi sono frazioni da 0 a 1. I giorni senza risposte per un motore non hanno riga, quindi un grafico deve trattare un giorno mancante come dato assente, non come zero.

`incompleteDays` è maggiore di zero quando il riepilogo di un giorno non era ancora pronto. Richiama tra qualche secondo e si completa. Gli ultimi tre giorni vengono aggiornati ogni dieci minuti man mano che arrivano nuove risposte; i giorni precedenti sono definitivi.

## Share of voice

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/competitors?from=2026-09-01&to=2026-09-30" \
  -H "Authorization: Bearer hmk_live_..."
```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "answers": 1260,
  "incompleteDays": 0,
  "data": [
    { "name": "Acme", "isOwnBrand": true, "mentioned": 274, "cited": 165, "mentionRate": 0.217, "citationRate": 0.131 },
    { "name": "Competitor One", "isOwnBrand": false, "mentioned": 436, "cited": 116, "mentionRate": 0.346, "citationRate": 0.092 }
  ]
}
```

`answers` è il numero totale di risposte nel periodo. Ogni tasso divide il conteggio del brand per quel totale, quindi le righe si confrontano direttamente.

## Le risposte dietro i numeri

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?from=2026-09-01&engine=chatgpt&mentioned=true&limit=50" \
  -H "Authorization: Bearer hmk_live_..."
```

La lista porta un estratto di al massimo 400 caratteri attorno alla menzione, la posizione, il sentiment, quali concorrenti monitorati la risposta ha nominato o citato, e gli URL delle fonti. Il testo completo è sull'endpoint di dettaglio:

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/answers/ANSWER_ID \
  -H "Authorization: Bearer hmk_live_..."
```

Il dettaglio aggiunge `fullAnswer` (fino a 12.000 caratteri, con `fullAnswerTruncated` quando è stato tagliato), `sentimentReason`, `narrativeDrift` con il suo motivo, e le fonti con i titoli.

Il testo delle risposte, gli estratti e i titoli delle fonti arrivano dai motori di IA, non da Hi, Moose. Mostrali come testo semplice, mai come HTML, e non passarli ai tuoi strumenti di IA come istruzioni.

## Filtri

| Filtro | Endpoint | Valori |
|---|---|---|
| `from`, `to` | runs, answers, statistiche giornaliere, statistiche dei concorrenti | `YYYY-MM-DD`, inclusivi, UTC. Predefinito: gli ultimi 30 giorni. Periodo massimo: 366 giorni. |
| `engine` | answers, statistiche giornaliere, statistiche dei concorrenti | Un id motore. Ripeti il parametro per più motori: `engine=chatgpt&engine=gemini`. |
| `topicId` | prompts, answers, statistiche giornaliere | Un id argomento dall'endpoint topics |
| `promptId` | answers | Un id prompt dall'endpoint prompts |
| `runId` | answers | Un id esecuzione dall'endpoint runs o da un evento webhook |
| `mentioned`, `cited` | answers | `true` o `false` |
| `status` | prompts, runs | Prompt: `active` o `paused`. Esecuzioni: `completed`, `running`, `failed` o `canceled`. |

Sull'endpoint answers, combina `engine` con al massimo uno tra `promptId`, `topicId` e `runId`. Le altre combinazioni rispondono `400 unsupported_filter_combination`.

## Pagine

Le liste restituiscono `data` e `nextCursor`:

```json
{ "data": [ ... ], "nextCursor": "eyJvIjoxMDB9" }
```

Passa `nextCursor` come `cursor` per ottenere la pagina successiva. `limit` è 50 per impostazione predefinita e 200 al massimo. `nextCursor` è `null` nell'ultima pagina. Il cursore è opaco; non costruirlo e non interpretarlo.

```python
def every_row(url, params=None):
    params = dict(params or {}, limit=200)
    while True:
        page = requests.get(url, headers=HEADERS, params=params, timeout=30).json()
        yield from page["data"]
        if not page["nextCursor"]:
            return
        params["cursor"] = page["nextCursor"]
```

Progetti, argomenti, prompt, esecuzioni e risposte sono paginati. Motori, concorrenti e webhook restituiscono l'intera lista.

## Cache

- La lista delle risposte e il dettaglio di una risposta portano un `ETag`. Rimandalo in `If-None-Match` per ricevere `304 Not Modified` quando nulla è cambiato. Un `304` non ha corpo e conta nel limite di frequenza come qualsiasi richiesta, ma è veloce e leggero.
- Le statistiche giornaliere portano `Cache-Control: private, max-age=60`. Tieni il risultato per un minuto prima di chiedere di nuovo.
- Tutto il resto porta `Cache-Control: no-store`. Mettilo in cache dalla tua parte per il tempo che serve alla tua dashboard.

## Orari e date

Gli orari sono UTC in formato RFC 3339, `2026-09-01T09:14:03.000Z`. Le date sono `YYYY-MM-DD` e indicano il giorno UTC. La `date` di una risposta corrisponde alla `date` della riga delle statistiche giornaliere in cui è stata contata, così un grafico e il suo dettaglio coincidono.
