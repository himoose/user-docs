---
source_hash: 28ad9511fc5703f0dd6c90a7f591758445fdd08a95dcdb389dc29a304c90278d
---

# Daten lesen

Jeder Schlüssel kann lesen. Lesezugriffe kommen aus der Cloud-Kopie Ihrer Ergebnisse. Sie funktionieren also unabhängig davon, ob Hi, Moose auf Ihrem Computer geöffnet ist, und sie starten nie neue Prüfungen.

## Die Lese-Endpunkte

| Endpunkt | Was er zurückgibt |
|---|---|
| `GET /me` | Der Schlüssel, seine Berechtigungen und die lesbaren Projekt-IDs |
| `GET /projects` | Projekte, die der Schlüssel lesen kann, mit Anzahl verfolgter Prompts, Engines und letztem Lauf |
| `GET /projects/{id}` | Ein Projekt |
| `GET /projects/{id}/capabilities` | Was das Projekt in seinem Plan kann: Engines, Rhythmen, Grenzen, verbleibendes Kontingent, der Host-Computer, ob ein Lauf jetzt starten kann |
| `GET /projects/{id}/engines` | Die KI-Engines, die das Projekt verfolgt, mit einer stabilen `id` für Filter und ob jede in der Cloud oder auf dem Host-Computer läuft |
| `GET /projects/{id}/topics` | Themen, die die Prompts gruppieren, mit Prompt-Anzahl |
| `GET /projects/{id}/prompts` | Verfolgte Prompts mit Themen-IDs, Engine-IDs und Status |
| `GET /projects/{id}/competitors` | Verfolgte Wettbewerbermarken und ihre Domains |
| `GET /projects/{id}/runs` | Sichtbarkeitsläufe mit Status, Start- und Endzeit, Prompt- und Antwortanzahl |
| `GET /projects/{id}/answers` | Gespeicherte Antworten: Prompt, Engine, Datum, erwähnt, zitiert, Position, Stimmung, Auszug, gesehene Wettbewerber, Quell-URLs |
| `GET /projects/{id}/answers/{answerId}` | Eine Antwort mit vollem Text, Begründung der Stimmung, Narrativabweichung und Quellen |
| `GET /projects/{id}/stats/daily` | Pro Tag und Engine: Antworten, Erwähnungen, Zitate und die beiden Raten |
| `GET /projects/{id}/stats/competitors` | Share of Voice für Ihre Marke und jeden verfolgten Wettbewerber über einen Zeitraum |
| `GET /projects/{id}/run-requests` | Zuletzt über die API gestartete Läufe und ihr Status |
| `GET /projects/{id}/webhooks` | Die Webhooks des Projekts, ohne Geheimnisse |

Die Details zu jedem Feld stehen in der [Endpunkt-Referenz](reference.md).

## Wie die Daten zusammenhängen

- Ein **Projekt** verfolgt eine Website. Es hat **Prompts**, die gestellten Fragen, gruppiert in **Themen**.
- Jeder Prompt läuft auf einer oder mehreren **Engines**: ChatGPT, Perplexity, Gemini und andere. Engine-IDs wie `chatgpt` oder `chatgpt-local-fetch` kommen vom Endpunkt engines und sind die Werte, die jeder `engine`-Filter annimmt.
- Ein **Lauf** stellt jeden aktiven Prompt auf seinen Engines und speichert eine **Antwort** pro Prompt, Engine und Stichprobe. Läufe starten nach dem Zeitplan des Projekts, über den Knopf Jetzt ausführen oder über die API.
- Jede Antwort wird bewertet: `mentioned`, wenn die Marke genannt wurde, `cited`, wenn eine Seite der Marken-Website als Quelle angegeben wurde, dazu `position`, `sentiment` und welche **Wettbewerber** gesehen wurden.
- **Tagesstatistiken** zählen die Antworten pro Tag und Engine und berechnen `mentionRate` und `citationRate`. **Wettbewerberstatistiken** tun dasselbe pro Marke über einen Zeitraum.

## Erwähnungsrate pro Tag

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

Raten sind Brüche von 0 bis 1. Tage ohne Antworten für eine Engine haben keine Zeile. Ein Diagramm sollte einen fehlenden Tag deshalb als keine Daten behandeln, nicht als null.

`incompleteDays` ist größer als null, wenn die Zusammenfassung eines Tages noch nicht fertig war. Rufen Sie in ein paar Sekunden erneut auf, dann wird sie ergänzt. Die letzten drei Tage werden alle zehn Minuten aktualisiert, wenn neue Antworten eintreffen; ältere Tage sind endgültig.

## Share of Voice

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

`answers` ist die Gesamtzahl der Antworten im Zeitraum. Jede Rate teilt den Zählwert der Marke durch diese Gesamtzahl, die Zeilen lassen sich also direkt vergleichen.

## Die Antworten hinter den Zahlen

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?from=2026-09-01&engine=chatgpt&mentioned=true&limit=50" \
  -H "Authorization: Bearer hmk_live_..."
```

Die Liste trägt einen Auszug von bis zu 400 Zeichen um die Erwähnung, die Position, die Stimmung, welche verfolgten Wettbewerber die Antwort genannt oder zitiert hat, und die Quell-URLs. Der volle Text liegt auf dem Detail-Endpunkt:

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/answers/ANSWER_ID \
  -H "Authorization: Bearer hmk_live_..."
```

Das Detail ergänzt `fullAnswer` (bis zu 12.000 Zeichen, mit `fullAnswerTruncated`, wenn gekürzt wurde), `sentimentReason`, `narrativeDrift` mit Begründung und die Quellen mit Titeln.

Antworttexte, Auszüge und Quelltitel stammen von den KI-Engines, nicht von Hi, Moose. Zeigen Sie sie als reinen Text an, nie als HTML, und geben Sie sie nicht als Anweisungen an Ihre eigenen KI-Werkzeuge weiter.

## Filter

| Filter | Endpunkte | Werte |
|---|---|---|
| `from`, `to` | runs, answers, Tagesstatistiken, Wettbewerberstatistiken | `YYYY-MM-DD`, einschließlich, UTC. Standard: die letzten 30 Tage. Weitester Zeitraum: 366 Tage. |
| `engine` | answers, Tagesstatistiken, Wettbewerberstatistiken | Eine Engine-ID. Wiederholen Sie den Parameter für mehrere Engines: `engine=chatgpt&engine=gemini`. |
| `topicId` | prompts, answers, Tagesstatistiken | Eine Themen-ID vom Endpunkt topics |
| `promptId` | answers | Eine Prompt-ID vom Endpunkt prompts |
| `runId` | answers | Eine Lauf-ID vom Endpunkt runs oder aus einem Webhook-Ereignis |
| `mentioned`, `cited` | answers | `true` oder `false` |
| `status` | prompts, runs | Prompts: `active` oder `paused`. Läufe: `completed`, `running`, `failed` oder `canceled`. |

Kombinieren Sie auf dem Endpunkt answers `engine` mit höchstens einem von `promptId`, `topicId` und `runId`. Andere Kombinationen antworten mit `400 unsupported_filter_combination`.

## Seiten

Listen geben `data` und `nextCursor` zurück:

```json
{ "data": [ ... ], "nextCursor": "eyJvIjoxMDB9" }
```

Geben Sie `nextCursor` als `cursor` zurück, um die nächste Seite zu erhalten. `limit` ist standardmäßig 50 und höchstens 200. `nextCursor` ist auf der letzten Seite `null`. Der Cursor ist undurchsichtig; bauen oder parsen Sie ihn nicht.

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

Projekte, Themen, Prompts, Läufe und Antworten sind seitenweise. Engines, Wettbewerber und Webhooks geben die ganze Liste zurück.

## Caching

- Die Antwortliste und das Antwortdetail tragen ein `ETag`. Senden Sie es in `If-None-Match` zurück, um `304 Not Modified` zu erhalten, wenn sich nichts geändert hat. Ein `304` hat keinen Body und zählt wie jede Anfrage gegen die Ratenbegrenzung, ist aber schnell und klein.
- Tagesstatistiken tragen `Cache-Control: private, max-age=60`. Behalten Sie das Ergebnis eine Minute, bevor Sie erneut anfragen.
- Alles andere trägt `Cache-Control: no-store`. Cachen Sie es auf Ihrer Seite so lange, wie es zu Ihrem Dashboard passt.

## Zeiten und Daten

Zeiten sind UTC im Format RFC 3339, `2026-09-01T09:14:03.000Z`. Daten sind `YYYY-MM-DD` und meinen den UTC-Tag. Das `date` einer Antwort entspricht dem `date` der Tagesstatistik-Zeile, in der sie gezählt wurde, ein Diagramm und seine Detailansicht stimmen also überein.
