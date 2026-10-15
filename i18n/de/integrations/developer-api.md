---
source_hash: 85052baa431b76ba0d9c99312dbc2fdf61031a24075e6841f48c0662cc8c5cdb
---

# Hi, Moose API

## Wofür das gut ist

Die Hi, Moose API ist eine REST-API für Entwickler, die eigene Dashboards, Berichte und Anwendungen zur KI-Sichtbarkeit auf Hi, Moose aufbauen. Sie liefert dieselben Ergebnisse wie der Bildschirm Sichtbarkeit: verfolgte Prompts und Themen, die befragten Engines, jede gespeicherte Antwort mit vollem Text und Quellen sowie Erwähnungs- und Zitierraten im Zeitverlauf. Mit den passenden Berechtigungen kann ein Schlüssel auch Projekte anlegen, Prompts, Engines und den Zeitplan verwalten, Läufe starten und einen signierten Webhook-Aufruf erhalten, wenn ein Lauf abgeschlossen ist.

Lesen funktioniert unabhängig davon, ob Hi, Moose auf Ihrem Computer geöffnet ist, weil die Daten aus der Cloud-Kopie Ihrer Ergebnisse kommen. Änderungen am Tracking und Läufe brauchen den Host-Computer des Projekts, erklärt unter [Tracking und Läufe](developer-api/tracking-and-runs.md).

Wenn Sie in Claude, ChatGPT oder einer anderen KI-App arbeiten, ist [Hi, Moose MCP](hi-moose-mcp.md) vielleicht das Richtige. Die API ist für Code, den Sie selbst schreiben.

## Seiten

| Seite | Inhalt |
|---|---|
| [Schnellstart](developer-api/quickstart.md) | Ein Schlüssel, ein erster Aufruf und ein Diagramm der Erwähnungsrate pro Tag, in curl, Python und JavaScript |
| [Schlüssel und Authentifizierung](developer-api/keys-and-auth.md) | Schlüssel erstellen und widerrufen, Berechtigungen, der Bearer-Header, den Schlüssel aus dem Browser heraushalten |
| [Daten lesen](developer-api/reading-data.md) | Projekte, Prompts, Läufe, Antworten und Statistiken, mit Filtern, Seiten und Caching |
| [Tracking und Läufe](developer-api/tracking-and-runs.md) | Der Host-Computer, Projekte und Prompts anlegen, Engines und Zeitplan, Läufe starten |
| [Webhooks](developer-api/webhooks.md) | Signierte Ereignisse, wenn ein Lauf abgeschlossen ist, Signaturprüfung, Wiederholungen |
| [Fehler und Grenzen](developer-api/errors-and-limits.md) | Das Fehlerformat, jeder Fehlercode, Ratenbegrenzung |
| [Endpunkt-Referenz](developer-api/reference.md) | Jeder Endpunkt mit Parametern, Feldern und einem Beispiel, aus dem Vertrag erzeugt |
| [Changelog](developer-api/changelog.md) | Was sich in jeder Vertragsversion geändert hat |

## Pläne

Die API ist in den bezahlten Plänen enthalten, sowohl mit verwalteten Modellen als auch mit eigenem Schlüssel. Kostenlose Konten sehen die Seite API-Schlüssel, können aber keine Schlüssel erstellen, und jede Anfrage antwortet mit `403 plan_required`.

## Auf einen Blick

```
https://api.himoose.com/v1/
```

- **Authentifizierung:** ein API-Schlüssel, gesendet als Bearer-Token. Schlüssel erstellt der Kontoinhaber in Hi, Moose unter **Einstellungen → Hi, Moose REST API**.
- **Format:** JSON in beide Richtungen. Feldnamen sind camelCase. Zeiten sind UTC im Format RFC 3339, Daten sind `YYYY-MM-DD`.
- **Vertrag:** [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json), OpenAPI 3.1. Er lässt sich in Postman, Insomnia, Bruno und Code-Generatoren importieren, und die [Endpunkt-Referenz](developer-api/reference.md) wird daraus erzeugt.
- **Berechtigungen:** jeder Schlüssel kann lesen. **Tracking verwalten** und **Läufe starten** werden beim Erstellen des Schlüssels gewählt.
- **Grenzen:** 300 Anfragen pro Minute und Schlüssel sowie 50.000 pro Tag und Konto. Siehe [Fehler und Grenzen](developer-api/errors-and-limits.md).
- **Kein CORS:** rufen Sie die API von Ihrem eigenen Server auf, nie aus einer Webseite.

## Woher die Daten kommen

Hi, Moose stellt jeden verfolgten Prompt auf jeder verfolgten Engine, nach Zeitplan oder wenn jemand einen Lauf startet. Jede Antwort wird gespeichert und bewertet: Wurde die Marke genannt, wurde eine Seite ihrer Website zitiert, wo erschien sie, welche Stimmung hatte die Antwort, welche Wettbewerber wurden gesehen. Die API liest diese gespeicherten Antworten und die daraus gebauten Tageszusammenfassungen. Sie führt beim Lesen nie neue Prüfungen aus, Lesen ist also schnell und kostet nichts.

Manche Engines laufen in der Cloud. Andere, die Local-Fetch-Engines, laufen über einen Browser auf einem Ihrer eigenen Computer. Beide Arten speichern ihre Antworten am selben Ort, die API zeigt sie also zusammen.

## Antworttext ist nicht vertrauenswürdig

Antworttexte, Auszüge und Quelltitel stammen von den KI-Engines, nicht von Hi, Moose. Zeigen Sie sie in Ihrem Dashboard als reinen Text an, nie als HTML, und geben Sie sie nicht als Anweisungen an Ihre eigenen KI-Werkzeuge weiter.

## Was kommt

Tracking-Änderungen für Pläne mit eigenem Schlüssel sind der nächste Schritt. Alles, was hier dokumentiert ist, ist live.
