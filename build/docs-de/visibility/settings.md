---
source_hash: 0bf4df4be6bc4ecf9f90b0973d78ad5121f1c5f07aa1f1c11b5f4615df894dae
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/visibility/settings/)

# Visibility-Einstellungen

## Wofür das gut ist

Die Visibility-Einstellungen bestimmen, wie oft Hi, Moose die Sichtbarkeit prüft, welches Modell die Ergebnisse bewertet und welche Markenbegriffe und Domains in Ihre Kennzahlen einfließen. Prompts und Themen selbst liegen im [Prompt Manager](prompt-manager.md); auf diesem Bildschirm geht es um die Mechanik der Läufe.

## Zeitplan für Läufe

- **Häufigkeit**: täglich, an Werktagen, wöchentlich oder nur manuell.
- **Bevorzugte Laufzeit** und, bei wöchentlicher Häufigkeit, ein **Wochentag**. Läufe erfolgen in Ihrer lokalen Zeitzone.
- **Stichproben je Prompt**: Geplante Läufe können jeden Prompt mehrfach wiederholen und die Ergebnisse mitteln, um eine stabilere Sichtbarkeitsrate zu erhalten. Der manuelle Knopf **Jetzt ausführen** nutzt stets eine einzige Stichprobe. Ein höherer Wert vervielfacht den Tokenverbrauch entsprechend, und Hi, Moose weist Sie vor dem Speichern darauf hin.

!!! note "Geplante Läufe setzen voraus, dass dieses Gerät wach ist"
    Im **Preview Mode** und in den **BYOK**-Tarifen läuft die Zeitplanung lokal auf Ihrem Rechner: Ein geplanter Lauf kann nicht starten, während der Computer aus ist, im Ruhezustand liegt oder Hi, Moose vollständig beendet ist. Lassen Sie die App geöffnet (oder in die Taskleiste minimiert), damit geplante Läufe ausgeführt werden können. **Verwaltete Tarife** schalten einen durchgehend laufenden Cloud-Zeitplaner frei, der nicht davon abhängt, ob Ihr Gerät wach ist. Maschinen mit lokaler Abfrage setzen unabhängig vom Tarif weiterhin voraus, dass die App geöffnet ist, denn diese Prüfungen laufen von Ihrem Rechner aus.

!!! note "Cloud-Läufe decken jeden Prompt auf jeder Engine ab"
    Ein geplanter Cloud-Lauf prüft jeden Ihrer überwachten Prompts gegen jede Engine, die Sie dafür ausgewählt haben, in einem Durchgang. Es gibt keine Stichprobe Ihrer Promptliste je Lauf, die Zahlen eines geplanten Laufs decken also den gesamten Satz ab und nicht nur einen Ausschnitt.

## E-Mail-Benachrichtigungen

Aktivieren Sie **Geplante Sichtbarkeits-Berichte per E-Mail**, um den Sichtbarkeitsbericht nach Abschluss geplanter Läufe per E-Mail zu erhalten. Dies ist eine persönliche Benachrichtigungseinstellung, getrennt von den [Benachrichtigungseinstellungen der Inbox](../inbox/notifications.md).

## Sekundäre Markenbegriffe und Domains

- **Sekundäre Markenbegriffe**: alternative Formulierungen oder Schreibvarianten Ihrer Marke, die ebenfalls als Erwähnung zählen sollen.
- **Sekundäre Domains**: weitere Domains, die für dieses Projekt neben Ihrer Hauptdomain als gültige Markenzitierung zählen sollen.

## Wettbewerberverfolgung

Fügen Sie die Marken hinzu, mit denen dieses Projekt verglichen wird. Jeder Wettbewerber benötigt einen Namen und optional eine Website.

Wenn eine KI-Antwort einen davon erwähnt oder zitiert, fließt das in [Share of Voice, Wettbewerberzitierungen und Lücken](competitors.md) ein.

Diese Liste wird mit Ihrem [Brand Truth Profile](../getting-started/context/brand-truth-profile.md) geteilt: An beiden Stellen hinzugefügte Wettbewerber erscheinen jeweils auch am anderen Ort. Die Zahl der in Sichtbarkeitsläufen verfolgten Wettbewerber ist begrenzt: Der Bildschirm nennt die Obergrenze und weist Sie darauf hin, wenn Ihre Liste sie überschreitet, damit Sie wissen, dass nur die ersten verfolgt werden.

## Bewertungsmodell

Wählen Sie das Modell, mit dem Hi, Moose Stimmung, narrative Abweichung und Funktionsabdeckung bewertet, nachdem eine Antwort erfasst wurde:

- Die **automatische Voreinstellung** richtet sich nach Ihrem Tarif:
    - **Preview Mode** nutzt ein aktiviertes lokales Gemma-4-Modell. Die Bewertung wird übersprungen, solange keines installiert und aktiv ist (Einstellungen → Local Model).
    - **BYOK-Tarife** bewerten mit Ihrem eigenen OpenRouter-Schlüssel.
    - **Verwaltete Tarife** bewerten über das verwaltete Modell-Routing von Hi, Moose (die Bewertung durch lokale Modelle gilt weiterhin, wo sie unterstützt wird).
- Sie können statt der automatischen Voreinstellung auch ein bestimmtes Modell wählen.

Die kostenlosen Modelle von OpenRouter werden nicht mehr als Bewertungsoption angeboten. Sie waren bei der strukturierten Bewertung so unzuverlässig, dass die Ergebnisse eine Auswertung nicht wert waren.

## Standardmodelle für neue Prompts

Wählen Sie, welche Maschinen vorausgewählt sind, wenn Sie im [Prompt Manager](prompt-manager.md) einen neuen Prompt anlegen; die Auswahl lässt sich anschließend je Prompt ändern. Modelle mit der Kennzeichnung **Paid** setzen einen kostenpflichtigen oder BYOK-Tarif voraus; Preview Mode ist auf Modelle mit lokaler Abfrage beschränkt. Jedes hier angehakte Modell fließt bei ausgeführten Sichtbarkeitsläufen in den Tokenverbrauch ein.

### Die Engines, die Sie verfolgen können

| Engine | Wie sie läuft | Tarif |
|---|---|---|
| ChatGPT | API | Alle |
| ChatGPT (local fetch) | Von Ihrem Rechner | Alle |
| Claude | API | Alle |
| Gemini | API | Alle |
| Grok | API | Alle |
| Grok (local fetch) | Von Ihrem Rechner | Alle |
| Perplexity | API | Alle |
| Perplexity (local fetch) | Von Ihrem Rechner | Alle |
| Google AI Mode (local fetch) | Von Ihrem Rechner | Alle |
| Google Search AI Overview (local fetch) | Von Ihrem Rechner | Alle |
| Google AI Mode | API | Kostenpflichtig |
| Google AI Overviews | API | Kostenpflichtig |
| Bing Copilot | API | Kostenpflichtig |
| DeepSeek | API | Kostenpflichtig |
| Meta AI | API | Kostenpflichtig |

**DeepSeek** und **Meta AI** sind standardmäßig aus. Sie lohnen sich, wenn Ihre Kategorie in den Märkten, in denen diese beiden stark sind, echte Relevanz hat; ist das nicht der Fall, hält das Ausschalten die Kosten pro Lauf niedrig.

**Local-fetch**-Engines lesen die öffentliche KI-Suchoberfläche von Ihrem eigenen Rechner, statt eine API aufzurufen. Sie kosten keine Token, brauchen aber in jedem Tarif eine geöffnete Desktop-App, wenn der Lauf ausgeführt wird.

## Einrichtung wiederholen

Starten Sie den Einrichtungsassistenten für die Sichtbarkeit jederzeit erneut, um Ihre überwachte Domain, Ihre Prompts und Ihre Verfolgungseinstellungen von Grund auf zu aktualisieren.
