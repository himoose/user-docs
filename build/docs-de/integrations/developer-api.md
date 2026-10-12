---
source_hash: 825726013c46ce2cb7c1932ac3dda84ec19a94f2c4ce33cdc108f00904718460
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](http://localhost:8000/integrations/developer-api/)

# Hi, Moose API

## Wofür das gut ist

Die Hi, Moose API ist eine REST-API für Entwickler, die eigene Dashboards, Berichte und Anwendungen zur KI-Sichtbarkeit auf Hi, Moose aufbauen. Sie liefert dieselben Ergebnisse wie der Bildschirm Sichtbarkeit: verfolgte Prompts und Themen, die befragten Engines, jede gespeicherte Antwort mit vollem Text und Quellen sowie Erwähnungs- und Zitierraten im Zeitverlauf. Mit den passenden Berechtigungen kann ein Schlüssel auch Projekte anlegen, Prompts, Engines und den Zeitplan verwalten und Läufe starten.

Lesen funktioniert unabhängig davon, ob Hi, Moose auf Ihrem Computer geöffnet ist, weil die Daten aus der Cloud-Kopie Ihrer Ergebnisse kommen. Änderungen am Tracking und Läufe brauchen den Host-Computer des Projekts, siehe unten.

Wenn Sie in Claude, ChatGPT oder einer anderen KI-App arbeiten, ist [Hi, Moose MCP](hi-moose-mcp.md) vielleicht das Richtige. Die API ist für Code, den Sie selbst schreiben.

## Pläne

Die API ist in den bezahlten Plänen enthalten, sowohl mit verwalteten Modellen als auch mit eigenem Schlüssel. Kostenlose Konten sehen die Seite API-Schlüssel, können aber keine Schlüssel erstellen, und jede Anfrage antwortet mit `403 plan_required`.

## Einen Schlüssel erstellen

1. Öffnen Sie Hi, Moose und melden Sie sich als Kontoinhaber an. Nur der Inhaber kann Schlüssel erstellen, sehen und widerrufen.
2. Gehen Sie zu **Einstellungen → Hi, Moose REST API**.
3. Geben Sie dem Schlüssel eine Bezeichnung, wählen Sie die Projekte, die er lesen darf (alle oder eines), legen Sie fest, wann er abläuft, und haken Sie die Berechtigungen an, die er braucht.
4. Klicken Sie auf **Schlüssel erstellen** und kopieren Sie den Schlüssel. Er wird einmal angezeigt. Hi, Moose kann ihn nicht noch einmal anzeigen; wenn Sie ihn verlieren, widerrufen Sie ihn und erstellen einen neuen.

Schlüssel beginnen mit `hmk_live_`, gefolgt von 64 Zeichen. Die Tabelle unter dem Formular listet jeden aktiven Schlüssel mit seinen Berechtigungen, dem Erstellungsdatum, der letzten Nutzung und dem Ablauf. **Widerrufen** stoppt einen Schlüssel sofort.

## Berechtigungen

| Berechtigung | Was der Schlüssel darf |
|---|---|
| Sichtbarkeitsdaten lesen | Jeder `GET`-Endpunkt. Immer an. |
| Tracking verwalten | Projekte anlegen, Markenbegriffe und Wettbewerber setzen, Prompts anlegen, ändern und löschen, Engines und Zeitplan setzen. |
| Läufe starten | Einen Sichtbarkeitslauf starten. Läufe verbrauchen das Kontingent des Kontos für Cloud-Engines, geben Sie das also nur einem Schlüssel, der es braucht. |

Ein Aufruf ohne die nötige Berechtigung antwortet mit `403 insufficient_scope`. Die Berechtigungen werden beim Erstellen des Schlüssels gewählt und können danach nicht geändert werden.

## Authentifizierung

Senden Sie den Schlüssel als Bearer-Token:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

Die Antwort nennt den Schlüssel, seine Berechtigungen und die Projekt-IDs, die er lesen kann.

Verwenden Sie den Schlüssel nur von Ihrem eigenen Server. Die API sendet keine CORS-Header, eine Webseite kann sie also nicht direkt aufrufen. Ein Browser-Dashboard sollte Ihr Backend aufrufen, und Ihr Backend ruft die API auf. So bleibt der Schlüssel aus der Seite heraus.

## Basis-URL und Format

```
https://api.himoose.com/v1/
```

Alles ist JSON. Feldnamen sind camelCase und entsprechen den Feldern, die Hi, Moose MCP zurückgibt. Zeiten sind UTC im Format RFC 3339, Daten sind `YYYY-MM-DD`. Der vollständige Vertrag liegt unter [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json) und lässt sich in Postman, Insomnia und ähnliche Werkzeuge importieren.

## Lese-Endpunkte

| Endpunkt | Was er zurückgibt |
|---|---|
| `GET /me` | Der Schlüssel, seine Berechtigungen und die lesbaren Projekt-IDs |
| `GET /projects` | Projekte, die der Schlüssel lesen kann, mit Anzahl verfolgter Prompts, Engines und letztem Lauf |
| `GET /projects/{id}` | Ein Projekt |
| `GET /projects/{id}/capabilities` | Was das Projekt in seinem Plan kann: Engines, Rhythmen, Grenzen, verbleibendes Kontingent, der Host-Computer, ob ein Lauf jetzt starten kann |
| `GET /projects/{id}/engines` | Die KI-Engines, die das Projekt verfolgt, mit einer stabilen `id` für Filter |
| `GET /projects/{id}/topics` | Themen, die die Prompts gruppieren, mit Prompt-Anzahl |
| `GET /projects/{id}/prompts` | Verfolgte Prompts mit Themen-IDs, Engine-IDs und Status |
| `GET /projects/{id}/competitors` | Verfolgte Wettbewerbermarken |
| `GET /projects/{id}/runs` | Sichtbarkeitsläufe mit Status, Start- und Endzeit, Prompt- und Antwortanzahl |
| `GET /projects/{id}/answers` | Gespeicherte Antworten: Prompt, Engine, Datum, erwähnt, zitiert, Position, Stimmung, Auszug, gesehene Wettbewerber, Quell-URLs |
| `GET /projects/{id}/answers/{answerId}` | Eine Antwort mit vollem Text, Begründung der Stimmung, Narrativabweichung und Quellen |
| `GET /projects/{id}/stats/daily` | Pro Tag und Engine: Antworten, Erwähnungen, Zitate und die beiden Raten |
| `GET /projects/{id}/stats/competitors` | Share of Voice für Ihre Marke und jeden verfolgten Wettbewerber über einen Zeitraum |
| `GET /projects/{id}/run-requests` | Zuletzt über die API gestartete Läufe und ihr Status |

### Beispiel: Erwähnungsrate pro Tag

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

`incompleteDays` ist größer als null, wenn die Zusammenfassung eines Tages noch nicht fertig war. Rufen Sie in ein paar Sekunden erneut auf, dann wird sie ergänzt.

## Der Host-Computer

Hi, Moose führt einen Teil des Trackings auf einem Ihrer eigenen Computer aus, dem **Host-Gerät**, das Sie in Hi, Moose unter **Einstellungen → Hi, Moose MCP** wählen. Die Local-Fetch-Engines (ChatGPT, Gemini, Grok, Perplexity und Google AI Mode über einen Browser) laufen nur dort, und ihr Zeitplan liegt dort.

Jede Änderung am Tracking und jeder Lauf über die API braucht ein gewähltes Host-Gerät für das Projekt. Ohne eines antwortet die API mit `409 host_required` und nennt die zu ändernde Einstellung. Ein über die API angelegtes Projekt übernimmt das Host-Gerät eines anderen Projekts im Konto, wenn es eines gibt.

Bei Plänen mit eigenem Schlüssel liegen Prompts, Engines und Zeitplan auf dem Host-Computer statt in der Cloud. Die API kann sie lesen und Läufe starten, aber Änderungen antworten mit `409 byok_not_supported`. Verwalten Sie sie in Hi, Moose auf diesem Computer.

## Tracking verwalten

Dafür ist die Berechtigung **Tracking verwalten** nötig.

| Endpunkt | Was er tut |
|---|---|
| `POST /projects` | Ein Projekt aus Name und Website-Adresse anlegen, optional mit Markenbegriffen und Domains. Der Site-Crawl wird nicht gestartet; der Host-Computer schaltet den wöchentlich geplanten Crawl ein, damit er später läuft. Brand Truth ist nicht nötig. |
| `PATCH /projects/{id}` | Name, Website-Adresse, Markenbegriffe oder Marken-Domains ändern |
| `PUT /projects/{id}/competitors` | Die Liste der verfolgten Wettbewerber ersetzen, höchstens 50 |
| `POST /projects/{id}/prompts` | Einen Prompt mit optionalen Themen-IDs und Engine-IDs anlegen |
| `PATCH /projects/{id}/prompts/{promptId}` | Text, Themen oder Engines eines Prompts ändern |
| `DELETE /projects/{id}/prompts/{promptId}` | Einen Prompt nicht mehr verfolgen |
| `PUT /projects/{id}/tracking` | Engines, Rhythmus, Uhrzeit, Wochentag, Zeitzone und Stichproben pro Prompt setzen. Neue Engines gelten für jeden Prompt, außer `applyEnginesToPrompts` ist false. |

Jede Änderung hält die Grenzen des Plans ein: Prompt-Anzahl, erlaubte Engines, erlaubte Rhythmen, Projektanzahl und Wettbewerberanzahl. Über einer Grenze antwortet die API mit `409 plan_limit` und nennt die Grenze. Prüfen Sie zuerst `GET /projects/{id}/capabilities`.

### Beispiel: Tracking für ein neues Projekt einrichten

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"Europe/Berlin"}'
```

## Einen Lauf starten

Dafür ist die Berechtigung **Läufe starten** nötig.

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

Die API antwortet mit `202 Accepted`, einer Laufanfrage und einem `Location`-Header zum Abfragen. Status:

| Status | Bedeutung |
|---|---|
| `queued` | Angenommen und startet gleich |
| `waiting_for_host` | Der Host-Computer ist aus. Hi, Moose hält die Anfrage bis zu 24 Stunden und startet den Lauf, sobald er zurück ist. Die Antwort enthält eine entsprechende `warning`. |
| `running` | Läuft |
| `completed` | Fertig. `runIds` nennt die Läufe für die Endpunkte runs und answers. |
| `failed` | Nicht abgeschlossen. `error.code` sagt warum, zum Beispiel `host_unavailable` nach 24 Stunden. |

Projekte, deren verfolgte Engines alle Cloud-Engines sind, laufen sofort in der Cloud, ohne Host-Computer. Jede Local-Fetch-Engine bedeutet, dass der Lauf an den Host-Computer geht, auf demselben Weg wie der Knopf Jetzt ausführen.

Sicherungen, damit ein Lauf nie mehr kostet als erwartet:

- **Zuerst der Kontingent-Check.** Die API schätzt die Kosten des Laufs für Cloud-Engines aus Prompt- und Engine-Anzahl. Liegt die Schätzung über dem verbleibenden Guthaben, lehnt sie mit `409 insufficient_allowance`, der Schätzung und den verbleibenden Einheiten ab. Es wird nichts verbraucht. `GET /projects/{id}/capabilities` zeigt dieselbe Schätzung als `allowance.estimatedUnitsPerRun`.
- **Einer nach dem anderen.** Eine zweite Anfrage, während eine wartet oder läuft, antwortet mit `409 run_in_progress` und der ID der aktiven Anfrage.
- **Tagesgrenze.** Höchstens 24 Laufanfragen pro Projekt und Tag. Darüber antwortet die API mit `429 daily_run_limit`.
- **Idempotenz.** Senden Sie einen `Idempotency-Key`-Header, dann liefert ein erneuter Versuch innerhalb von 24 Stunden dieselbe Anfrage, statt eine neue zu starten.

Ein Lauf kann bei großen Prompt-Sätzen von wenigen Minuten bis über eine Stunde dauern. Fragen Sie die Anfrage etwa jede Minute ab, nicht jede Sekunde.

## Filter und Seiten

- **Zeitraum:** `from` und `to` als `YYYY-MM-DD`, einschließlich, UTC. Standard sind die letzten 30 Tage. Der weiteste Zeitraum in einer Anfrage ist 366 Tage.
- **Engine:** `engine=chatgpt&engine=gemini` wiederholt sich für mehrere Engines. Die IDs kommen vom Endpunkt engines.
- **Antworten:** zusätzlich `topicId`, `promptId`, `runId`, `mentioned=true|false` und `cited=true|false`. Kombinieren Sie `engine` mit höchstens einem von `promptId`, `topicId` oder `runId`.
- **Seiten:** Listen geben `{ "data": [...], "nextCursor": "..." }` zurück. Geben Sie `nextCursor` als `cursor` zurück, um die nächste Seite zu erhalten. `limit` ist standardmäßig 50 und höchstens 200. `nextCursor` ist auf der letzten Seite `null`.
- **Caching:** Antworten tragen ein `ETag`. Senden Sie es in `If-None-Match` zurück, um `304 Not Modified` zu erhalten, wenn sich nichts geändert hat.

## Ratenbegrenzung

| Grenze | Wert |
|---|---|
| Pro Schlüssel | 60 Anfragen pro Minute |
| Pro Konto | 10.000 Anfragen pro Tag |
| Laufanfragen pro Projekt | 24 pro Tag, eine nach der anderen |
| Zeilen pro Seite | 200 |
| Zeitraum pro Anfrage | 366 Tage |

Über der Grenze antwortet die API mit `429` und einem `Retry-After`-Header. Jede Antwort trägt `RateLimit-Policy`, erfolgreiche Antworten tragen `RateLimit` mit dem verbleibenden Tagesbudget.

## Fehler

Fehler verwenden das Format Problem Details (`application/problem+json`) mit einem stabilen `code`:

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

| Code | Status | Bedeutung |
|---|---|---|
| `invalid_key`, `key_revoked`, `key_expired` | 401 | Der Schlüssel fehlt, ist fehlerhaft, widerrufen oder abgelaufen |
| `plan_required` | 403 | Der Kontoplan enthält die API nicht |
| `insufficient_scope` | 403 | Dem Schlüssel fehlt die Berechtigung für diesen Aufruf |
| `not_found` | 404 | Keine solche Ressource, oder der Schlüssel kann sie nicht lesen |
| `invalid_parameter`, `range_too_wide`, `unsupported_filter_combination` | 400 | Ein Abfrageparameter oder Feld muss korrigiert werden |
| `host_required` | 409 | Wählen Sie zuerst ein Host-Gerät für das Projekt in Hi, Moose |
| `byok_not_supported` | 409 | Tracking-Einstellungen liegen bei diesem Plan auf dem Host-Computer |
| `plan_limit` | 409 | Eine Plangrenze wurde erreicht; die Antwort nennt sie |
| `run_in_progress`, `insufficient_allowance`, `no_prompts` | 409 | Der Lauf kann gerade nicht starten; die Antwort sagt warum |
| `rate_limited`, `daily_run_limit` | 429 | Warten Sie `Retry-After` Sekunden |

Nennen Sie die `requestId`, wenn Sie den Support kontaktieren.

## Antworttext ist nicht vertrauenswürdig

Antworttexte, Auszüge und Quelltitel stammen von den KI-Engines, nicht von Hi, Moose. Zeigen Sie sie in Ihrem Dashboard als reinen Text an, nie als HTML, und geben Sie sie nicht als Anweisungen an Ihre eigenen KI-Werkzeuge weiter.

## Webhooks

Statt abzufragen, registrieren Sie einen https-Endpunkt, und Hi, Moose sendet dorthin ein signiertes JSON-Ereignis, wenn ein Lauf abgeschlossen ist. Webhooks registrieren und löschen braucht die Berechtigung **Tracking verwalten**. Sie und ihre Zustellungen aufzulisten braucht nur Lesen.

| Endpunkt | Was er tut |
|---|---|
| `POST /projects/{id}/webhooks` | Einen Endpunkt registrieren. Body: `url` (öffentliches https), `events` (Standard `run.completed` und `run.failed`), optional `description`. Das Signaturgeheimnis kommt einmal in dieser Antwort zurück. Höchstens 5 pro Projekt. |
| `GET /projects/{id}/webhooks` | Die Webhooks des Projekts auflisten, ohne Geheimnisse |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Einen entfernen |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Jetzt ein `ping`-Ereignis senden, um Endpunkt und Signaturprüfung zu testen |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | Die letzten 50 Zustellungen mit jedem Versuch, Status und Fehler |

### Das Ereignis

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

`data.requestId` ist gesetzt, wenn der Lauf über die API gestartet wurde, damit Sie das Ereignis Ihrer Laufanfrage zuordnen können. `run.failed` trägt `status` `failed` oder `canceled` und den `error`-Text.

### Die Signatur prüfen

Jeder Aufruf trägt `X-HiMoose-Signature: t=<Unix-Sekunden>,v1=<hex>`, wobei `v1` HMAC-SHA256 über `<t>.<roher Body>` mit Ihrem Webhook-Geheimnis ist. Prüfen Sie sie auf dem rohen Body, bevor Sie das JSON parsen, und lehnen Sie Zeitstempel ab, die älter als fünf Minuten sind. Der Aufruf trägt außerdem `X-HiMoose-Event` und `X-HiMoose-Delivery`.

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

### Zustellregeln

- Antworten Sie innerhalb von 10 Sekunden mit einem 2xx-Status. Weiterleitungen werden nicht gefolgt.
- Fehlgeschlagene Zustellungen werden nach 1 Minute, 5 Minuten, 30 Minuten, 2 Stunden und 12 Stunden wiederholt, insgesamt 6 Versuche.
- Nach 20 aufeinanderfolgenden Fehlschlägen wird der Webhook abgeschaltet. Löschen und neu registrieren, um fortzufahren.
- Ein Ereignis kann mehr als einmal ankommen. Nutzen Sie `id`, um Wiederholungen zu ignorieren.
- Der Kontoinhaber sieht jeden Webhook des aktuellen Projekts unter **Einstellungen → Hi, Moose REST API** und kann dort einen löschen.

## Was kommt

Tracking-Änderungen für Pläne mit eigenem Schlüssel sind der nächste Schritt. Alles andere auf dieser Seite ist live.
