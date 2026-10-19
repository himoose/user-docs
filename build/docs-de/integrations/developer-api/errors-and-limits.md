---
source_hash: 85fe7ea99ed19540350085410907cba880592b989251ce17fdb81570b24829a2
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](http://localhost:8000/integrations/developer-api/errors-and-limits/)


# Fehler und Grenzen

## Fehler

Fehler verwenden das Format Problem Details (`application/problem+json`, RFC 9457) mit einem stabilen `code`, nach dem Sie im Code verzweigen können:

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

- `code` ist das Feld, das Sie im Code prüfen. Seine Bedeutung ändert sich nie.
- `detail` ist für Menschen geschrieben und kann im Wortlaut wechseln.
- `type` verlinkt auf den Doku-Abschnitt zu dieser Art von Fehler.
- `requestId` identifiziert die Anfrage. Nennen Sie sie, wenn Sie den Support kontaktieren. Sie wird auch als Header `X-Request-Id` mit jeder Antwort gesendet.

Manche Fehler tragen zusätzliche Felder, die in der Tabelle genannt sind.

## Fehlercodes

| Code | Status | Bedeutung | Was tun |
|---|---|---|---|
| `invalid_key` | 401 | Kein `Authorization`-Header, ein Schlüssel in falscher Form oder ein Schlüssel, den Hi, Moose nicht kennt | Senden Sie `Authorization: Bearer hmk_live_...`. Prüfen Sie, ob der Schlüssel vollständig kopiert wurde. |
| `key_revoked` | 401 | Der Schlüssel wurde in den Einstellungen widerrufen | Erstellen Sie einen neuen Schlüssel. |
| `key_expired` | 401 | Der Schlüssel hat sein Ablaufdatum überschritten | Erstellen Sie einen neuen Schlüssel. |
| `plan_required` | 403 | Der Kontoplan enthält die API nicht | Wechseln Sie zu einem bezahlten Plan. |
| `insufficient_scope` | 403 | Dem Schlüssel fehlt die Berechtigung für diesen Aufruf. Der Body nennt sie in `scope`. | Erstellen Sie einen Schlüssel mit dieser Berechtigung. |
| `not_found` | 404 | Keine solche Ressource, oder der Schlüssel kann sie nicht lesen. Die beiden Fälle werden nicht unterschieden. | Prüfen Sie die ID und den Projektzugriff des Schlüssels. |
| `method_not_allowed` | 405 | Der Endpunkt existiert, aber nicht mit dieser Methode | Siehe die [Referenz](reference.md). |
| `invalid_parameter` | 400 | Ein Abfrageparameter oder Body-Feld fehlt, ist fehlerhaft oder außerhalb des erlaubten Bereichs. `detail` nennt es. | Korrigieren Sie die Anfrage. |
| `range_too_wide` | 400 | `from` bis `to` umfasst mehr als 366 Tage | Fragen Sie einen engeren Zeitraum ab. |
| `unsupported_filter_combination` | 400 | Filter, die sich nicht kombinieren lassen, zum Beispiel `engine` mit zwei von `promptId`, `topicId` und `runId` | Lassen Sie einen Filter weg. |
| `host_required` | 409 | Für das Projekt ist kein Host-Computer gewählt | Wählen Sie einen in Hi, Moose unter **Einstellungen → Hi, Moose MCP**. |
| `byok_not_supported` | 409 | Bei diesem Plan liegen die Tracking-Einstellungen auf dem Host-Computer, die API kann sie also nicht ändern | Ändern Sie sie in Hi, Moose auf diesem Computer. |
| `plan_limit` | 409 | Eine Plangrenze wurde erreicht. Der Body trägt `limit`. | Prüfen Sie `GET /projects/{id}/capabilities` für die Grenzen. |
| `run_in_progress` | 409 | Eine Laufanfrage steht schon in der Warteschlange, wartet oder läuft. Der Body trägt `requestId` und `requestStatus`. | Warten Sie, bis sie fertig ist. |
| `insufficient_allowance` | 409 | Der Lauf würde mehr kosten als das verbleibende Kontingent. Der Body trägt `estimatedUnits`, `remainingUnits` und `periodEndsAt`. | Laden Sie auf, oder reduzieren Sie Prompts, Engines oder Stichproben. |
| `no_prompts` | 409 | Das Projekt hat keinen verfolgten Prompt mit einer Engine | Legen Sie zuerst Prompts und Engines an. |
| `rate_limited` | 429 | Die Minuten- oder Tagesgrenze wurde erreicht | Warten Sie `Retry-After` Sekunden. |
| `daily_run_limit` | 429 | Das Projekt hat seine 24 Laufanfragen für heute gestellt | Versuchen Sie es morgen. |
| `internal` | 500 | Auf der Seite von Hi, Moose ist etwas fehlgeschlagen | Wiederholen Sie mit Backoff. Bleibt es bestehen, kontaktieren Sie den Support mit der `requestId`. |

Ein `502` oder `503` ohne Body bedeutet, dass die API ihr Backend nicht erreichen konnte. Wiederholen Sie mit Backoff.

## Ratenbegrenzung

| Grenze | Wert |
|---|---|
| Pro Schlüssel | 300 Anfragen pro Minute |
| Pro Konto | 50.000 Anfragen pro Tag |
| Laufanfragen pro Projekt | 24 pro Tag, eine nach der anderen |
| Webhooks pro Projekt | 5 |
| Zeilen pro Seite | 200 |
| Zeitraum pro Anfrage | 366 Tage |

Über der Grenze antwortet die API mit `429 rate_limited` und einem `Retry-After`-Header. Jede Antwort trägt `RateLimit-Policy`, erfolgreiche Antworten tragen `RateLimit` mit dem verbleibenden Tagesbudget, nach dem IETF-Entwurf für Rate-Limit-Header:

```
RateLimit-Policy: "per-minute";q=300;w=60, "per-day";q=50000;w=86400
RateLimit: "per-day";r=49871;t=61234
```

Die Minutengrenze wird pro Schlüssel am Edge gezählt und ist ungefähr; ein kurzer Schub etwas darüber kann durchgehen. Die Tagesgrenze wird pro Konto über alle seine Schlüssel gezählt.

## Unter den Grenzen bleiben

- **Cachen Sie auf Ihrer Seite.** Tagesstatistiken tragen `Cache-Control: max-age=60`. Ein Dashboard, das jede Minute aktualisiert, liest die Zusammenfassung einmal pro Minute und Diagramm, nicht einmal pro Betrachter.
- **Nutzen Sie die Zusammenfassungen.** Tagesstatistiken und Wettbewerberstatistiken werden aus einer Zusammenfassungstabelle gebaut. Zeichnen Sie Diagramme daraus, und lesen Sie einzelne Antworten nur, wenn jemand eine Zeile öffnet.
- **Nutzen Sie ETags.** Antworten tragen ein `ETag`. Senden Sie es in `If-None-Match` zurück, und ein `304` kostet fast nichts.
- **Nutzen Sie Webhooks**, statt auf das Ende eines Laufs zu pollen. Siehe [Webhooks](webhooks.md).
- **Warten Sie bei 429.** Schlafen Sie `Retry-After` Sekunden, dann wiederholen Sie. Wiederholen Sie nicht sofort.

## Anfrage-IDs

Jede Antwort trägt `X-Request-Id`. Protokollieren Sie sie neben Ihrem eigenen Anfrageprotokoll, damit sich eine Problemmeldung den Logs von Hi, Moose zuordnen lässt. Fehler-Bodies wiederholen sie als `requestId`.
