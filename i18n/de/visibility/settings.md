---
source_hash: 185a9611ccdaef3c98b73cc4349bc1d586a1fa03b38212ecab7ffca94af54a21
---
# Visibility-Einstellungen

## Wofür das gut ist

Die Visibility-Einstellungen bestimmen, wie oft Hi, Moose die Sichtbarkeit prüft, welches Modell die Ergebnisse bewertet und welche Markenbegriffe und Domains in Ihre Kennzahlen einfließen. Prompts und Themen selbst liegen im [Prompt Manager](prompt-manager.md); auf diesem Bildschirm geht es um die Mechanik der Läufe.

## Zeitplan für Läufe

- **Häufigkeit**: täglich, an Werktagen, wöchentlich oder nur manuell.
- **Bevorzugte Laufzeit** und, bei wöchentlicher Häufigkeit, ein **Wochentag**. Läufe erfolgen in Ihrer lokalen Zeitzone.
- **Stichproben je Prompt**: Geplante Läufe können jeden Prompt mehrfach wiederholen und die Ergebnisse mitteln, um eine stabilere Sichtbarkeitsrate zu erhalten. Der manuelle Knopf **Run now** nutzt stets eine einzige Stichprobe. Ein höherer Wert vervielfacht den Tokenverbrauch entsprechend, und Hi, Moose weist Sie vor dem Speichern darauf hin.

!!! note "Geplante Läufe setzen voraus, dass dieses Gerät wach ist"
    Im **Preview Mode** und in den **BYOK**-Tarifen läuft die Zeitplanung lokal auf Ihrem Rechner: Ein geplanter Lauf kann nicht starten, während der Computer aus ist, im Ruhezustand liegt oder Hi, Moose vollständig beendet ist. Lassen Sie die App geöffnet (oder in die Taskleiste minimiert), damit geplante Läufe ausgeführt werden können. **Verwaltete Tarife** schalten einen durchgehend laufenden Cloud-Zeitplaner frei, der nicht davon abhängt, ob Ihr Gerät wach ist. Maschinen mit lokaler Abfrage setzen unabhängig vom Tarif weiterhin voraus, dass die App geöffnet ist, denn diese Prüfungen laufen von Ihrem Rechner aus.

## E-Mail-Benachrichtigungen

Aktivieren Sie **Scheduled visibility email reports**, um den Sichtbarkeitsbericht nach Abschluss geplanter Läufe per E-Mail zu erhalten. Dies ist eine persönliche Benachrichtigungseinstellung, getrennt von den [Benachrichtigungseinstellungen der Inbox](../inbox/notifications.md).

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

## Einrichtung wiederholen

Starten Sie den Einrichtungsassistenten für die Sichtbarkeit jederzeit erneut, um Ihre überwachte Domain, Ihre Prompts und Ihre Verfolgungseinstellungen von Grund auf zu aktualisieren.
