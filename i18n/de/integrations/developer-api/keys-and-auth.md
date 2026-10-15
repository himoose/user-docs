---
source_hash: eef50f1fe484ff2af95068f006064217adac902f902e7159b98801260bb5cb9a
---

# Schlüssel und Authentifizierung

## Einen Schlüssel erstellen

1. Öffnen Sie Hi, Moose und melden Sie sich als Kontoinhaber an. Nur der Inhaber kann Schlüssel erstellen, sehen und widerrufen.
2. Gehen Sie zu **Einstellungen → Hi, Moose REST API**.
3. Geben Sie dem Schlüssel eine Bezeichnung, wählen Sie die Projekte, die er lesen darf (alle oder eines), legen Sie fest, wann er abläuft, und haken Sie die Berechtigungen an, die er braucht.
4. Klicken Sie auf **Schlüssel erstellen** und kopieren Sie den Schlüssel. Er wird einmal angezeigt. Hi, Moose kann ihn nicht noch einmal anzeigen; wenn Sie ihn verlieren, widerrufen Sie ihn und erstellen einen neuen.

Schlüssel beginnen mit `hmk_live_`, gefolgt von 64 Zeichen. Die Tabelle unter dem Formular listet jeden aktiven Schlüssel mit seinen Berechtigungen, dem Erstellungsdatum, der letzten Nutzung und dem Ablauf. **Widerrufen** stoppt einen Schlüssel sofort.

Hi, Moose speichert nur einen Hash des Schlüssels, so wie Passwörter gespeichert werden. Niemand bei Hi, Moose kann einen Schlüssel also nachträglich auslesen.

## Ein Schlüssel pro App

Erstellen Sie für jede App und jedes Skript einen eigenen Schlüssel mit einer Bezeichnung, die sagt, wofür er ist. Dann lässt sich ein Schlüssel widerrufen, ohne etwas anderes zu stören, und die Spalte **zuletzt verwendet** in den Einstellungen zeigt, welche App die Aufrufe gemacht hat.

## Berechtigungen

| Berechtigung | Was der Schlüssel darf |
|---|---|
| Sichtbarkeitsdaten lesen | Jeder `GET`-Endpunkt. Immer an. |
| Tracking verwalten | Projekte anlegen, Markenbegriffe und Wettbewerber setzen, Prompts anlegen, ändern und löschen, Engines und Zeitplan setzen, Webhooks registrieren und löschen. |
| Läufe starten | Einen Sichtbarkeitslauf starten. Läufe verbrauchen das Kontingent des Kontos für Cloud-Engines, geben Sie das also nur einem Schlüssel, der es braucht. |

Ein Aufruf ohne die nötige Berechtigung antwortet mit `403 insufficient_scope` und nennt die Berechtigung. Wählen Sie die Berechtigungen beim Erstellen des Schlüssels; danach lassen sie sich nicht ändern. Erstellen Sie stattdessen einen neuen Schlüssel.

In der API erscheinen die Berechtigungen als `visibility:read`, `tracking:write` und `runs:execute`, zum Beispiel in der Antwort von `GET /me`.

## Projektzugriff

Ein Schlüssel liest entweder jedes Projekt des Kontos oder ein Projekt, gewählt beim Erstellen des Schlüssels. Ein Projekt, das der Schlüssel nicht lesen darf, antwortet mit `404 not_found`, genau wie ein Projekt, das nicht existiert. So lässt sich mit einem Schlüssel nicht herausfinden, welche Projekte ein Konto hat.

## Authentifizierung

Senden Sie den Schlüssel bei jeder Anfrage als Bearer-Token im `Authorization`-Header:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

Die Antwort nennt den Schlüssel, seine Berechtigungen und die Projekt-IDs, die er lesen kann. Das ist ein guter erster Aufruf, um zu prüfen, ob ein Schlüssel funktioniert.

Eine Anfrage ohne Schlüssel oder mit einem fehlerhaften, widerrufenen oder abgelaufenen Schlüssel antwortet mit `401` und einem dieser Codes:

| Code | Bedeutung |
|---|---|
| `invalid_key` | Kein `Authorization`-Header, ein Schlüssel in falscher Form oder ein Schlüssel, den Hi, Moose nicht kennt |
| `key_revoked` | Der Schlüssel wurde in den Einstellungen widerrufen |
| `key_expired` | Der Schlüssel hat sein Ablaufdatum überschritten |

## Den Schlüssel auf Ihrem Server behalten

Verwenden Sie den Schlüssel nur von Ihrem eigenen Server. Die API sendet keine CORS-Header, eine Webseite kann sie also nicht direkt aufrufen. Ein Browser-Dashboard sollte Ihr Backend aufrufen, und Ihr Backend ruft die API auf. So bleibt der Schlüssel aus der Seite und aus dem Netzwerkprotokoll des Browsers heraus.

Speichern Sie den Schlüssel in einer Umgebungsvariable oder einem Secrets-Manager, nie in der Versionsverwaltung. Wenn ein Schlüssel nach außen gelangt, widerrufen Sie ihn in den Einstellungen und erstellen einen neuen. Das Widerrufen wirkt sofort.

## Ablauf

Ein Schlüssel kann nach 30, 90 oder 365 Tagen ablaufen, oder nie. Ein ablaufender Schlüssel ist der sicherere Standard für ein Skript, das ersetzt wird; ein nie ablaufender Schlüssel passt zu einem langlebigen Dashboard, dessen Schlüssel in einem Secrets-Manager liegt. Die Tabelle in den Einstellungen zeigt das Ablaufdatum jedes Schlüssels.
