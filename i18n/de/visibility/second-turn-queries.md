---
source_hash: bf06b2d4371815f46d4209e9c058c88a274ce098682e93731da1f9cafde41e72
---
# Second-Turn-Anfragen

## Wofür das gut ist

KI-Engines beenden eine Antwort oft damit, dass sie zur nächsten Frage einladen. Eine Second-Turn-Anfrage ist diese nächste Frage, vollständig ausformuliert, sodass sie für sich allein verständlich ist. Hi, Moose erfasst diese Anfragen während der Sichtbarkeitsläufe und zeigt sie im Reiter **Second-Turn-Anfragen** an, zusammen mit der Häufigkeit jeder Anfrage und der Angabe, ob Ihre Website sie abdeckt.

Eine Engine beendet eine Antwort zum Beispiel mit „Soll ich die beiden nebeneinander vergleichen?“. Die Second-Turn-Anfrage ist das, was eine Person eingeben würde, um zuzustimmen, etwa „Stehpult-Aufsätze und vollständige Stehschreibtische für ein kleines Heimbüro vergleichen“.

## Die Funktion einschalten

Öffnen Sie die [Visibility-Einstellungen](settings.md#second-turn-anfragen) und gehen Sie zum Abschnitt **Second-Turn-Anfragen**. Schalten Sie **Second-Turn-Anfragen erfassen** ein. Die Einstellung ist standardmäßig ausgeschaltet und wird für jedes Projekt einzeln eingeschaltet.

Solange die Einstellung ausgeschaltet ist, wird nichts erfasst, und der Reiter Second-Turn-Anfragen ist ausgeblendet.

Sie können die Einstellung in kostenpflichtigen verwalteten Tarifen, in BYOK Premium und in BYOK Agency einschalten. In Preview Mode und BYOK Free ist der Schalter ausgegraut und zeigt den Hinweis **In kostenpflichtigen Tarifen verfügbar**.

Mit dem Einschalten kommt für jede Antwort eines Laufs ein kleiner Modellaufruf hinzu. In kostenpflichtigen verwalteten Tarifen zählen diese Aufrufe zum Kontingent Ihres Tarifs. In BYOK Premium und BYOK Agency werden sie über Ihren OpenRouter-Schlüssel abgerechnet.

## Der Reiter Second-Turn-Anfragen

Der Reiter steht im Visibility-Dashboard direkt hinter **Chancen**. Er erscheint nur, wenn die Einstellung eingeschaltet ist. Er bleibt leer bis zum ersten Sichtbarkeitslauf nach dem Einschalten, weil Antworten aus früheren Läufen nicht verarbeitet werden.

Der Reiter richtet sich nach dem Zeitraum und den Filtern, die oben in Visibility gewählt sind. Eine Anfrage wird aufgeführt, wenn eine Antwort in diesem Zeitraum sie enthielt.

### Ansichten

- **Am häufigsten** ist die Standardansicht. Sie zeigt eine einzige Liste, geordnet nach der Zahl der Antworten, die die jeweilige Anfrage enthielten.
- **Nach Prompt** gruppiert die Anfragen unter dem überwachten Prompt, auf den sie jeweils folgten.

### Was eine Zeile zeigt

- Die Anfrage.
- **Antworten mit dieser Anfrage: N**, wobei N die Zahl der Antworten ist, die sie enthielten.
- Die Engines und das Thema.
- Das Ergebnis der [Website-Abdeckung](#website-abdeckung).
- **Details anzeigen** listet unter **Erscheint nach diesen Prompts** die Prompts auf, auf die die Anfrage folgte, jeweils mit einem Link **Antwort ansehen**. Dort stehen auch die Schlussworte der Engine.

## Wie neue Anfragen sortiert werden

Wenn eine neue Anfrage zum ersten Mal erscheint, prüft Hi, Moose, ob sie konkret genug ist und nah genug am Thema liegt, um verfolgt zu werden. Hi, Moose prüft außerdem, ob sie dasselbe bedeutet wie eine Anfrage, die bereits in der Liste steht. Anfragen mit derselben Bedeutung werden zusammen gezählt. Allgemeine Anfragen wie „Erzählen Sie mir mehr“ werden weggelassen.

Diese Sortierung findet beim Öffnen des Reiters statt. Wenn Sie ihn nach einem Lauf zum ersten Mal öffnen, zeigt der Reiter **Neue Anfragen werden sortiert: X von Y**.

## Website-Abdeckung

Jede Anfrage wird einmal mit den gecrawlten Seiten der Website Ihres Projekts abgeglichen. Die Zeile zeigt danach eines dieser Ergebnisse:

- **Auf der Website abgedeckt:** gefolgt von der Seite.
- **Auf der Website teilweise abgedeckt:** gefolgt von der Seite.
- **Auf der Website nicht abgedeckt**.

Die Abdeckung wird erneut geprüft, sobald ein neuer Crawl der Website abgeschlossen ist.

Die Prüfung setzt einen abgeschlossenen Crawl der Website auf Ihrem Gerät voraus, oder auf dem Gerät, das den Website-Index bereitstellt. Ohne abgeschlossenen Crawl zeigt die Zeile **Abdeckung der Website nicht geprüft**. In der Web-App ohne Desktop-Hostgerät wird die Abdeckung nicht geprüft.

## Schaltflächen in jeder Zeile

- **Zu getrackten Prompts hinzufügen** fügt die Anfrage als überwachten Prompt unter demselben Thema hinzu wie den Prompt, auf den sie folgte. Danach steht auf der Schaltfläche **Wird getrackt**.
- **Entwurf erstellen** wird angezeigt, wenn Ihre Website die Anfrage nicht abdeckt. Die Schaltfläche öffnet einen neuen Chat mit dem bereits ausgefüllten Formular für den [Content-Brief](../features/content-briefs.md).
- **Diese Seite aktualisieren** wird angezeigt, wenn Ihre Website die Anfrage teilweise abdeckt. Die Schaltfläche öffnet das Formular zur Inhaltsaktualisierung für diese Seite, mit der Anfrage als Ziel.
- **Verwerfen** blendet die Zeile aus. **Verworfene anzeigen** zeigt die verworfenen Zeilen wieder an, und **Wiederherstellen** bringt eine Zeile in die Liste zurück.

## Wann sich die Liste aktualisiert

Solange die Einstellung eingeschaltet ist, werden neue Anfragen bei jedem Sichtbarkeitslauf aus jeder Antwort erfasst. Sie werden sortiert, wenn Sie den Reiter das nächste Mal öffnen.

Da sich der Reiter nach dem gewählten Zeitraum richtet, wird eine Anfrage nicht mehr aufgeführt, wenn keine Antwort in diesem Zeitraum sie enthielt. Wählen Sie einen längeren Zeitraum, um sie wieder zu sehen.

## Teams und Tarife

In kostenpflichtigen verwalteten Tarifen werden die erfassten Anfragen, die verworfenen Anfragen und die Abdeckungsergebnisse mit der Cloud synchronisiert, sodass Teammitglieder dieselbe Liste sehen. In BYOK Premium und BYOK Agency bleibt alles auf Ihrem Gerät.

## Was nicht enthalten ist

- Die „Related“-Fragen von Perplexity und die „People also ask“-Fragen von Google werden nicht erfasst.
- Second-Turn-Anfragen sind nicht Teil des [PDF-Berichts](overview.md#exportieren).
- Second-Turn-Anfragen sind über die Werkzeuge von [Hi, Moose MCP](../integrations/hi-moose-mcp.md) nicht verfügbar.
