---
source_hash: 638e427715918eeab4249561f6f095b46f57a8531e8ee857a78f4e07d0941c4e
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](http://localhost:8000/integrations/developer-api/tracking-and-runs/)


# Tracking und Läufe

Zu ändern, was Hi, Moose verfolgt, braucht die Berechtigung **Tracking verwalten**. Einen Lauf zu starten braucht die Berechtigung **Läufe starten**. Beide werden beim Erstellen des Schlüssels gewählt, siehe [Schlüssel und Authentifizierung](keys-and-auth.md#permissions).

## Der Host-Computer

Hi, Moose führt einen Teil des Trackings auf einem Ihrer eigenen Computer aus, dem **Host-Gerät**, das Sie in Hi, Moose unter **Einstellungen → Hi, Moose MCP** wählen. Die Local-Fetch-Engines (ChatGPT, Gemini, Grok, Perplexity und Google AI Mode über einen Browser) laufen nur dort, und ihr Zeitplan liegt dort.

Jede Änderung am Tracking und jeder Lauf über die API braucht ein gewähltes Host-Gerät für das Projekt. Ohne eines antwortet die API mit `409 host_required` und nennt die zu ändernde Einstellung. Ein über die API angelegtes Projekt übernimmt das Host-Gerät eines anderen Projekts im Konto, wenn es eines gibt.

Nach einer Tracking-Änderung übergibt die API dem Host-Computer einen kurzen Auftrag, die neuen Einstellungen zu übernehmen. Der Host erledigt das innerhalb einer Minute, solange Hi, Moose dort geöffnet ist, oder beim nächsten Öffnen. Lesezugriffe zeigen die neuen Einstellungen in jedem Fall sofort.

Bei Plänen mit eigenem Schlüssel liegen Prompts, Engines und Zeitplan auf dem Host-Computer statt in der Cloud. Die API kann sie lesen und Läufe starten, aber Änderungen antworten mit `409 byok_not_supported`. Verwalten Sie sie in Hi, Moose auf diesem Computer.

`GET /projects/{id}/capabilities` sagt Ihnen vor dem Schreiben: den Plan, die erlaubten Engines und Rhythmen, die Grenzen, den Host-Computer und ob er online ist, und ob ein Lauf jetzt starten könnte.

## Tracking verwalten

| Endpunkt | Was er tut |
|---|---|
| `POST /projects` | Ein Projekt aus Name und Website-Adresse anlegen, optional mit Markenbegriffen und Domains. Der Site-Crawl wird nicht gestartet; der Host-Computer schaltet den wöchentlich geplanten Crawl ein, damit er später läuft. Brand Truth ist nicht nötig. |
| `PATCH /projects/{id}` | Name, Website-Adresse, Markenbegriffe oder Marken-Domains ändern |
| `PUT /projects/{id}/competitors` | Die Liste der verfolgten Wettbewerber ersetzen, höchstens 50 |
| `POST /projects/{id}/prompts` | Einen Prompt mit optionalen Themen-IDs und Engine-IDs anlegen |
| `PATCH /projects/{id}/prompts/{promptId}` | Text, Themen oder Engines eines Prompts ändern oder einen pausierten fortsetzen |
| `DELETE /projects/{id}/prompts/{promptId}` | Einen Prompt nicht mehr verfolgen. Seine gespeicherten Antworten bleiben erhalten. |
| `PUT /projects/{id}/tracking` | Standard-Engines, Rhythmus, Uhrzeit, Wochentag, Zeitzone und Stichproben pro Prompt setzen |

Jede Änderung hält die Grenzen des Plans ein: Prompt-Anzahl, erlaubte Engines, erlaubte Rhythmen, Projektanzahl und Wettbewerberanzahl. Über einer Grenze antwortet die API mit `409 plan_limit` und nennt die Grenze im Body.

### Engines auf Prompts

Jeder Prompt hat seine eigene Liste von Engines. `PUT /projects/{id}/tracking` mit `engineIds` setzt den Standard für später angelegte Prompts und lässt jeden bestehenden Prompt, wie er ist. Um die Engines bestehender Prompts zu ändern, senden Sie entweder `applyEnginesToPrompts: true` im selben Aufruf, was die neue Liste auf jeden Prompt im Projekt setzt, oder ändern Sie Prompts einzeln mit `PATCH /projects/{id}/prompts/{promptId}`.

Ein Prompt ohne Engines bleibt erhalten, wird in Läufen aber übersprungen. `POST /projects/{id}/prompts` ohne `engineIds` gibt dem neuen Prompt die Standard-Engines des Projekts.

### Ersetzen heißt ersetzen

`PUT /projects/{id}/competitors` ersetzt die ganze Liste. Senden Sie die vollständige Liste, die Sie behalten wollen, nicht nur die Ergänzungen. Eine leere Liste entfernt jeden Wettbewerber. Dasselbe gilt für `brandTerms` und `brandDomains` bei `PATCH /projects/{id}`.

### Beispiel: Tracking für ein neues Projekt einrichten

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

Wer die Engines setzt, bevor er Prompts anlegt, gibt jedem neuen Prompt diese Engines als Standard.

### Zeitplan

| Feld | Werte |
|---|---|
| `cadence` | `manual` (Zeitplan aus), `daily`, `weekdays`, `weekly` |
| `timeOfDay` | `HH:MM` in der Zeitzone des Projekts |
| `weeklyDay` | `monday` bis `sunday`, verwendet von `weekly` |
| `timezone` | Ein IANA-Name wie `Europe/Berlin` |
| `samplesPerPrompt` | Wie oft jeder Prompt pro Engine in einem Lauf gestellt wird. Mehr Stichproben kosten mehr Kontingent. |

Der Plan entscheidet, welche Rhythmen erlaubt sind; der Endpunkt capabilities listet sie.

## Einen Lauf starten

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

Die API antwortet mit `202 Accepted`, einer Laufanfrage und einem `Location`-Header zum Abfragen:

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

| Status | Bedeutung |
|---|---|
| `queued` | Angenommen und startet gleich |
| `waiting_for_host` | Der Host-Computer ist aus. Hi, Moose hält die Anfrage bis zu 24 Stunden und startet den Lauf, sobald er zurück ist. Die Antwort enthält eine entsprechende `warning`. |
| `running` | Läuft |
| `completed` | Fertig. `runIds` nennt die Läufe für die Endpunkte runs und answers. |
| `failed` | Nicht abgeschlossen. `error.code` sagt warum, zum Beispiel `host_unavailable` nach 24 Stunden. |
| `canceled` | Aus Hi, Moose gestoppt, bevor er fertig war |

`mode` sagt, wo der Lauf läuft. Projekte, deren verfolgte Engines alle Cloud-Engines sind, laufen sofort in der Cloud, ohne Host-Computer. Jede Local-Fetch-Engine bedeutet, dass der Lauf an den Host-Computer geht, auf demselben Weg wie der Knopf Jetzt ausführen. In beiden Fällen braucht das Projekt einen gewählten Host-Computer.

### Sicherungen

Damit ein Lauf nie mehr kostet als erwartet:

- **Zuerst der Kontingent-Check.** Die API schätzt die Kosten des Laufs für Cloud-Engines aus Prompt- und Engine-Anzahl. Liegt die Schätzung über dem verbleibenden Guthaben, lehnt sie mit `409 insufficient_allowance`, der Schätzung und den verbleibenden Einheiten ab. Es wird nichts verbraucht. `GET /projects/{id}/capabilities` zeigt dieselbe Schätzung als `allowance.estimatedUnitsPerRun`.
- **Einer nach dem anderen.** Eine zweite Anfrage, während eine in der Warteschlange steht, wartet oder läuft, antwortet mit `409 run_in_progress` und der ID der aktiven Anfrage.
- **Tagesgrenze.** Höchstens 24 Laufanfragen pro Projekt und Tag. Darüber antwortet die API mit `429 daily_run_limit`.
- **Idempotenz.** Senden Sie einen `Idempotency-Key`-Header, dann liefert ein erneuter Versuch innerhalb von 24 Stunden dieselbe Anfrage mit `200` und `replayed: true`, statt einen weiteren Lauf zu starten.
- **Etwas zum Ausführen.** Ein Projekt ohne Prompt mit einer Engine antwortet mit `409 no_prompts`.

### Einen Lauf verfolgen

Fragen Sie `GET /projects/{id}/run-requests/{requestId}` etwa einmal pro Minute ab. Ein Lauf kann bei großen Prompt-Sätzen von wenigen Minuten bis über eine Stunde dauern. Sobald `status` auf `completed` steht, enthält `runIds` den Lauf zum Lesen:

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?runId=RUN_ID" \
  -H "Authorization: Bearer hmk_live_..."
```

Um das Abfragen zu vermeiden, registrieren Sie einen [Webhook](webhooks.md). Das Ereignis `run.completed` trägt die `requestId`, damit Sie es Ihrer Anfrage zuordnen können.

Über die API gestartete Läufe erscheinen in Hi, Moose wie jeder andere Lauf, und in der Tabelle **Letzte Agenten-Aufträge** unter **Einstellungen → Hi, Moose MCP** mit der Bezeichnung des Schlüssels.
