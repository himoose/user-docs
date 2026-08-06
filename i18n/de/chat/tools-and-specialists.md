---
source_hash: 6b12d8d972a33f212f60d823c287d184f083cfb60d8934f6b9ac8571ceb3c32e
---
# Chat-Werkzeuge und Spezialisten

## Wofür das gut ist

Über das bloße Eintippen einer Anfrage hinaus bietet Ihnen das Eingabefeld des Chats mehrere Wege, das zu formen, was Hi, Moose mit Ihrer Nachricht anstellt: Kontext anhängen, einen Spezialisten wählen, um das Gespräch zu fokussieren, oder einen Schnellstart auslösen.

## Anhänge

Klicken Sie auf die Anhang-Schaltfläche im Eingabefeld, um Ihrer Nachricht Kontext hinzuzufügen:

- **Datei oder Bild hochladen**: `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg` und `.png`. Tabellen werden in lesbaren Text überführt, sodass Sie Moose eine Arbeitsmappe übergeben und nach deren Inhalt fragen können.
- **Bildschirmfoto aufnehmen**: Wählen Sie einen Bildschirm oder ein Fenster und ziehen Sie dann genau den Bereich auf, den Sie senden möchten. Unter macOS müssen Sie Hi, Moose bei der ersten Nutzung Zugriff auf die Bildschirmaufnahme gewähren.
- **Aus der Library hinzufügen**: Hängen Sie ein gespeichertes [Library](../library/overview.md)-Artefakt an (einen Brief, einen Entwurf, Key Points oder FAQ), statt es erneut einzufügen.
- **Vektordatenbank der Website**: Hängen Sie die indexierte Website Ihres Projekts an, damit Moose aus Ihren echten Seiten antwortet und nicht aus dem, was er dort vermutet. Den Index bauen Sie unter [Site Monitoring](../site-monitoring/overview.md) auf.

## Werkzeuge, die Moose einsetzen kann

Der Chat beschränkt sich nicht auf Texterzeugung. Im Verlauf eines Gesprächs kann Moose Werkzeuge in Ihrem Auftrag einsetzen und zeigt Ihnen, wenn er das tut.

| Werkzeug | Funktion |
|---|---|
| Websuche | Live-Ergebnisse, in Tarifen mit Websuche im Chat |
| Seite lesen | Eine bestimmte URL abrufen |
| Suche im Website-Index | Aus Ihren eigenen indexierten Seiten antworten |
| Search Console | Ihre verbundenen [Search-Console](../integrations/google-search-console.md)-Daten abfragen |
| Sofortige Markenprüfung | Eine Anfrage in fünf KI-Maschinen prüfen, siehe [Sofortprüfung der Marke](../tools/instant-brand-check.md) |
| Abdeckungsprüfung | Feststellen, ob Ihre Website ein Thema bereits abdeckt |
| Bilderzeugung | Ein Bild für einen Entwurf erstellen |
| Hilfe zur App | Sie zur passenden Dokumentation oder zum Support führen |

Der Einsatz von Werkzeugen funktioniert in verwalteten Tarifen, BYOK-Tarifen und mit lokalen Gemma-4-Modellen gleichermaßen.

!!! note "Fragen zur Search Console werden agentisch beantwortet"
    Moose fragt Ihre Search-Console-Daten schrittweise ab, statt einen festen Bericht auszuführen. Stellen Sie eine vage Frage, grenzt er sie über mehrere Abfragen ein, um sie zu beantworten, statt einen allgemeinen Datenauszug zurückzugeben.

## Spezialisten

Spezialisten sind fokussierte Einstiegspunkte zu demselben Hauptoperator. Es sind weder eigene Werkzeuge noch getrennte Gedächtnisse, sondern lediglich eine Möglichkeit, das Gespräch auf eine bestimmte Aufgabe auszurichten. Öffnen Sie die Spezialistenauswahl, um einen zu wählen:

- **Content-Brief-Spezialist**: einen knappen Brief mit Struktur und nächsten Schritten erstellen.
- **Google-Search-Console-Spezialist**: Moose zu Ihren verbundenen [Google-Search-Console](../integrations/google-search-console.md)-Daten befragen. Dieser Spezialist benötigt ein verbundenes Search-Console-Konto oder eine gespeicherte Property für das aktive Projekt, bevor er aus Ihren eigenen Daten antworten kann.
- **Audio-Spezialist**: eine Anfrage in ein sauberes Sprechskript verwandeln.
- **Entwurfs-Spezialist**: Entwurfsinhalte erzeugen, die zur Durchsicht und Bearbeitung bereit sind.
- **FAQ-Spezialist**: knappe FAQ rund um die wertvollsten Fragen verfassen.
- **Key-Points-Spezialist**: zuerst die wichtigsten Erkenntnisse herausarbeiten.

Ist ein Spezialist aktiv, erscheint seine Kennzeichnung am Gespräch, und Sie können sie jederzeit entfernen, um zum allgemeinen Chat zurückzukehren.

### Eigene Spezialisten

Sie können auch einen eigenen lokalen Spezialisten anlegen: Geben Sie ihm einen Namen und eine Zusammenfassung der Aufgaben, die er übernehmen soll, und wählen Sie dann, auf welche Teile Ihres Kontexts er zugreifen darf: Projektkontext, Markenprofil, Website-Kontext, Chatverlauf, entwurfsorientierte Ausgabe oder Ausgabe im Markdown-Format. Eigene Spezialisten lassen sich auch importieren, wenn jemand einen mit Ihnen teilt.

## Schnellstarts

Das Eingabefeld bietet Schnellstarts mit einem Klick für häufige Aufgaben, darunter:

- [Ein AEO Audit ausführen](../features/aeo-audits.md)
- [Einen recherchegestützten Content-Brief erstellen](../features/content-briefs.md)
- [Recherchegestützte FAQ erstellen](../features/faq-generator.md)
- [Optimierte Key Points erzeugen](../features/key-points.md)
- [Einen Blogbeitrags-Entwurf erstellen](../features/blog-post-draft.md)
- [Einen Glossarbeitrag erstellen](../features/glossary-post.md)
- [Landingpage-Inhalte erstellen](../features/landing-page-content.md)
- [Produktseiten-Inhalte erstellen](../features/product-page-content.md)
- [Grounding-Suchanfragen von Google AI Mode zu einem Prompt erfassen](../features/grounding-queries.md)
- [Fan-out-Suchanfragen von ChatGPT zu einem Prompt erfassen](../features/fan-out-queries.md)
- [Textinhalte in Audio verwandeln](../audio/overview.md)

Dieselbe Auswahl steht im **[Tools-Menü](../tools/overview.md)** der oberen Leiste zur Verfügung, nach Aufgabe gruppiert und durchsuchbar.

Die Schnellstarts für Grounding- und Fan-out-Suchanfragen zeigen Ihnen die Suchen, die eine webgestützte KI-Maschine beim Beantworten eines Prompts ausgeführt hat, samt der zitierten Quellen. Beide funktionieren über einen verwalteten Aufruf an Gemini oder OpenAI, dessen ausgeführte Suchen anschließend ausgelesen werden. Sie sind damit eine nahe Annäherung an das, was AI Mode und ChatGPT Search tun, und keine Aufzeichnung dieser Produkte selbst. Da dieser Aufruf auf unserer Infrastruktur läuft, setzen beide einen **kostenpflichtigen verwalteten Arbeitsbereich** voraus, und das gilt auch in BYOK-Tarifen, denn der Erfassungsschritt nutzt die verwaltete Infrastruktur von Hi, Moose und nicht Ihren lokalen Schlüssel.

Der Audio-Schnellstart öffnet den Bildschirm [Audio](../audio/overview.md) in der Desktop-App. Früher führte er in die alte Web-App; das ist nicht mehr der Fall.
