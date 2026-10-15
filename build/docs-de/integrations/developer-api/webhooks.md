---
source_hash: 6467de19290f42e43d33241a37345989dbd6267011d89947d750f7e073ea66e2
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/integrations/developer-api/webhooks/)


# Webhooks

Statt abzufragen, registrieren Sie einen https-Endpunkt, und Hi, Moose sendet dorthin ein signiertes JSON-Ereignis, wenn ein Lauf abgeschlossen ist. Webhooks registrieren, testen und löschen braucht die Berechtigung **Tracking verwalten**. Sie und ihre Zustellungen aufzulisten braucht nur Lesen.

## Endpunkte

| Endpunkt | Was er tut |
|---|---|
| `POST /projects/{id}/webhooks` | Einen Endpunkt registrieren. Body: `url` (öffentliches https), `events` (Standard `run.completed` und `run.failed`), optional `description`. Das Signaturgeheimnis kommt einmal in dieser Antwort zurück. Höchstens 5 pro Projekt. |
| `GET /projects/{id}/webhooks` | Die Webhooks des Projekts auflisten, ohne Geheimnisse |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Einen entfernen |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Jetzt ein `ping`-Ereignis senden, um Endpunkt und Signaturprüfung zu testen |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | Die letzten 50 Zustellungen mit jedem Versuch, Status und Fehler |

## Einen registrieren

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

Speichern Sie `secret` neben Ihrem Schlüssel. Es wird nur in dieser Antwort angezeigt. Die URL muss öffentlich sein und https verwenden; private Adressen, localhost und reines http werden mit `400 invalid_parameter` abgelehnt.

Senden Sie sich dann einen Ping:

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/test \
  -H "Authorization: Bearer hmk_live_..."
```

Die Antwort ist der Zustellungsdatensatz, und der Endpunkt deliveries zeigt den Versuch mit dem HTTP-Status, den Ihr Endpunkt geantwortet hat.

## Das Ereignis

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

| Ereignis | Wann |
|---|---|
| `run.completed` | Ein Lauf ist abgeschlossen und seine Antworten sind gespeichert. Geplante Läufe, Läufe über den Knopf Jetzt ausführen und Läufe über die API zählen alle. |
| `run.failed` | Ein Lauf endete mit `status` `failed` oder `canceled`. `data.error` sagt warum. |
| `ping` | Gesendet vom Test-Endpunkt. `data` trägt die Projekt-ID und eine Nachricht. |

`data.requestId` ist gesetzt, wenn der Lauf über die API gestartet wurde, damit Sie das Ereignis Ihrer Laufanfrage zuordnen können. Bei geplanten Läufen und in Hi, Moose gestarteten Läufen ist es `null`.

Das Ereignis ist ein Signal, nicht die Daten. Folgen Sie bei `run.completed` dem Link `data.links.answers` oder aktualisieren Sie Ihre Tagesstatistiken. Die Tageszusammenfassungen für die Tage des Laufs werden innerhalb von zehn Minuten nach Abschluss neu gebaut; `incompleteDays` in der Statistik-Antwort sagt, wenn sie noch nicht fertig sind.

## Header

| Header | Wert |
|---|---|
| `X-HiMoose-Signature` | `t=<unix seconds>,v1=<hex>`, siehe unten |
| `X-HiMoose-Event` | Der Name des Ereignisses |
| `X-HiMoose-Delivery` | Die Zustellungs-ID, dieselbe wie auf dem Endpunkt deliveries |
| `User-Agent` | `HiMoose-Webhooks/1.0` |
| `Content-Type` | `application/json` |

## Die Signatur prüfen

`v1` ist HMAC-SHA256 über `<t>.<raw body>` mit Ihrem Webhook-Geheimnis, als Hex-String in Kleinbuchstaben. Prüfen Sie sie auf dem rohen Request-Body, bevor Sie das JSON parsen, vergleichen Sie in konstanter Zeit, und lehnen Sie Zeitstempel ab, die älter als fünf Minuten sind.

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

Die meisten Web-Frameworks parsen JSON, bevor Ihr Code läuft. Achten Sie darauf, die Bytes so zu signieren, wie sie ankamen, nicht eine neu serialisierte Kopie, sonst passt die Signatur nicht.

## Zustellregeln

- Antworten Sie innerhalb von 10 Sekunden mit einem 2xx-Status. Erledigen Sie die Arbeit nach dem Antworten, nicht davor. Weiterleitungen werden nicht gefolgt.
- Fehlgeschlagene Zustellungen werden nach 1 Minute, 5 Minuten, 30 Minuten, 2 Stunden und 12 Stunden wiederholt, insgesamt 6 Versuche. Eine Zustellung ist `pending`, solange Wiederholungen übrig sind, `delivered` nach einem 2xx, `failed` nach dem letzten Versuch.
- Nach 20 aufeinanderfolgenden Fehlschlägen wird der Webhook abgeschaltet, `active` wird false, und es werden keine Ereignisse mehr gesendet. Löschen und neu registrieren, um fortzufahren.
- Ein Ereignis kann mehr als einmal ankommen. Nutzen Sie `id`, um Wiederholungen zu ignorieren.
- Ereignisse eines Projekts können in falscher Reihenfolge ankommen, wenn eine Wiederholung im Spiel ist. Nutzen Sie `createdAt`, wenn die Reihenfolge wichtig ist.

## Zustellungen ansehen

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/deliveries \
  -H "Authorization: Bearer hmk_live_..."
```

Jede Zustellung listet jeden Versuch mit Zeitpunkt, dem HTTP-Status, den Ihr Endpunkt geantwortet hat, der Dauer und einem etwaigen Fehler. Wenn sich ein Endpunkt falsch verhält, ist das der erste Ort zum Nachsehen.

Der Kontoinhaber sieht jeden Webhook des aktuellen Projekts unter **Einstellungen → Hi, Moose REST API** mit dem Status seiner letzten Zustellung und kann dort einen löschen.
