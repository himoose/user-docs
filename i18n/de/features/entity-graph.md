---
source_hash: 1d8f1dffb939a9b3587c4b3a3f298386f6f202a5a02672b6b3dfd79bbccc2135
---
# Entity Graph

## Wofür das gut ist

Ein Entity Graph ist die Karte dessen, worum es auf Ihrer Website tatsächlich geht: die Personen, Produkte, Orte, Organisationen und Themen, die Ihre Seiten nennen, und wie diese Dinge zusammenhängen.

Das ist wichtig, weil Antwortmaschinen Ihre Website nicht als Liste von Seiten lesen. Sie lesen sie als eine Menge von Dingen und Beziehungen. Eine Website, die klar macht „wir sind dieses Unternehmen, wir machen diese Produkte, für diese Kunden, in dieser Kategorie", gibt einer Engine etwas, das sie abrufen und zitieren kann. Eine Website, auf der das mitgemeint, aber nie ausgesprochen wird, überlässt es dem Raten.

Der Entity Graph zeigt Ihnen, welche dieser Dinge Ihre Website bereits deutlich gemacht hat, welche dünn sind und womit eine Engine am Ende herausgehen würde.

Starten Sie ihn über **Werkzeuge → Entity Graph erstellen** oder fragen Sie einfach im [Chat](../chat/overview.md) danach.

## Bevor Sie einen bauen können

Der Graph entsteht aus Seiten, die Hi, Moose bereits gecrawlt hat. Das Projekt braucht also **eine Website und mindestens einen abgeschlossenen Crawl**. Gibt es noch keinen, sagt die Startkarte das und verlinkt Sie zu [Website-Monitoring](../site-monitoring/overview.md), um einen auszuführen.

Die Karte nennt die Grundlage: wie viele gecrawlte Seiten, und das Datum des letzten abgeschlossenen Crawls.

## Schnell oder vollständig

Zwei Tiefen:

- **Schnell**: nur strukturierte Daten. Liest das Schema-Markup, die Metadaten und die Seitenstruktur, die Ihre Website ohnehin veröffentlicht. Läuft sofort und kostet nichts.
- **Vollständig**: alles aus dem schnellen Modus, dazu ein KI-Durchgang, der Ihre wichtigsten Seiten liest und die Entitäten benennt, die nirgends ausgezeichnet sind. Dauert einige Minuten.

Im vollständigen Modus wählen Sie, wie viele Top-Seiten der KI-Durchgang lesen darf. Größere Läufe dauern länger, und in verwalteten Tarifen verbrauchen die Cloud-Modellaufrufe Ihr Monatskontingent. Der Durchgang läuft mit dem Modell, das im Modellmenü des Chats ausgewählt ist. Wählen Sie das Modell also zuerst, wenn Sie ein bestimmtes möchten: Ein geladenes lokales Modell hält alles auf Ihrem Rechner und kostenlos.

## Was zurückkommt

Der Graph berichtet:

- **Entitäten**: alles Gefundene, mit Typ, Aliasnamen, der Zahl der Seiten, auf denen es vorkommt, und einem **Salienz**-Wert dafür, wie zentral es für die Website ist.
- **Beziehungen**: wie diese Entitäten zusammenhängen, aufgeteilt in drei Arten:
    - **Benannt**: eine Beziehung, die Ihre strukturierten Daten oder der KI-Durchgang ausdrücklich aussprechen.
    - **Gemeinsame Seite**: zwei Entitäten, die immer wieder auf denselben Seiten auftauchen.
    - **Semantisch**: zwei Entitäten, die die Sprache als verwandt behandelt, auch wo nichts sie verknüpft.
- **Entitäten nach Typ**: die Aufschlüsselung, oft die nützlichste Einzelansicht. Eine Website, die Software verkauft und vierzig Personen neben drei Produkten zeigt, hat ein Erzählproblem, von dem man wissen sollte.

Eine Tabelle **Top-Entitäten** zeigt die wichtigsten mit Typ, Seitenzahl und Salienz. Der vollständige Satz lässt sich als **CSV** oder **PDF** exportieren; die Tabelle auf dem Bildschirm ist begrenzt und nennt, wie viele weitere die Exporte enthalten.

## Wenn der KI-Durchgang nicht läuft

Der vollständige Modus fällt zurück, statt zu scheitern. Kann der KI-Durchgang nicht laufen, erhalten Sie den Graphen trotzdem aus strukturierten Daten, gemeinsamen Seiten und semantischer Ähnlichkeit, und die Karte nennt den Grund:

- **Kein Modell verfügbar**: Laden Sie ein lokales Modell oder hinterlegen Sie einen OpenRouter-Schlüssel und bauen Sie dann im vollständigen Modus neu.
- **Nichts Neues zu lesen**: Alle infrage kommenden Seiten waren bereits in einem früheren Lauf analysiert.
- **Der Durchgang ist fehlgeschlagen**: Er konnte nicht abgeschlossen werden.
- **Kontingent aufgebraucht**: In verwalteten Tarifen endet der Durchgang mit Ihrem Monatskontingent, und der Graph enthält alles, was bis dahin analysiert wurde.

## Moose kann ihn wieder lesen

Sobald ein Graph existiert, kann der [Chat](../chat/tools-and-specialists.md) ihn direkt abfragen. Fragen Sie, bei welchen Entitäten Ihre Website am stärksten ist, was mit einem bestimmten Produkt verbunden ist oder was neben einem Thema fehlt, das Sie gewinnen wollen, und Moose liest den Graphen, statt neu zu crawlen oder zu raten.

Auch [Send Moose](../send-moose/overview.md) liest ihn, als Teil der Website-Intelligenz, die er zu einer Aufgabe mitbringt.

## Wie es weitergeht

- **[Website-Monitoring](../site-monitoring/overview.md)**: der Crawl, aus dem der Graph entsteht.
- **[Content Briefs](content-briefs.md)**: eine Lücke im Graphen in eine Seite verwandeln.
- **[AEO-Audits](aeo-audits.md)**: prüfen, ob eine einzelne Seite ihre Entitäten deutlich benennt.
