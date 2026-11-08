---
source_hash: 0a9a56ce00908be9642b519b71a66ed53535f416da94c0f65e7bb741595259e0
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/getting-started/settings/)

# Einstellungen

## Wofür das gut ist

In den Einstellungen verwalten Sie Ihr Profil, Ihren Tarif, Ihre Modelle, Ihr Team und das Verhalten der App auf diesem Rechner. Sie sind in Bereiche in der linken Spalte gegliedert; einige erscheinen nur für den Kontoinhaber oder in kostenpflichtigen Tarifen.

| Bereich | Inhalt |
|---|---|
| Allgemein | Profildaten und App-Verhalten auf diesem Rechner |
| Nutzung | Guthabenstand und Zurücksetzungsdatum |
| Konto | E-Mail, Passwort, Tarif, OpenRouter-Schlüssel |
| Lokale KI | Herunterladen und Aktivieren des Modells auf dem Gerät |
| Team | Sitzplätze, Einladungen, Rollen |
| [Website-Monitoring](../site-monitoring/overview.md) | Crawl-Zeitplan, Suchindex, überwachte Seiten, gesperrte Pfade |
| [Branding](../agency/white-label.md) | White-Label-Berichte und Audio-Attribution (nur kostenpflichtige Tarife) |
| Konto-Anmeldungen | Die Websites, bei denen Moose für Sichtbarkeitsläufe und Send Moose angemeldet ist |
| [Hi, Moose MCP](../integrations/hi-moose-mcp.md) | Host-Gerät, Modell für Schreibaufgaben, verbundene Apps, letzte Aufträge |
| [Hi, Moose REST API](../integrations/developer-api.md) | API-Schlüssel und Webhooks (nur Inhaber) |
| Protokolle | Aktionsprotokolle und CSV-Export (nur Inhaber) |
| Daten & Backup | Lokale Sicherung und Wiederherstellung |
| Sichtbarkeitsverlauf | Die lokale Kopie Ihrer KI-Suchantworten und ihr Speicherbudget |
| Fehlerbehebung | Cache, Diagnoseprotokoll, Zurücksetzen lokaler Daten |

## General

**Profildaten**: Ihr bevorzugter Name, Ihre Funktion und Ihr Standort. Sie personalisieren die App und machen die Zuordnung gemeinsamer Arbeit klarer.

**App-Verhalten** steuert, wie Hi, Moose auf diesem Rechner läuft:

- **Hi, Moose bei der Anmeldung starten**: Nach einem Neustart öffnet sich die App unauffällig im Hintergrund, damit geplante Arbeit weiterläuft. Sie können das Fenster jederzeit über die Taskleiste oder die Menüleiste öffnen.
- **Anonyme Nutzungsstatistiken teilen**: Sendet anonyme, aggregierte Ereignisse (welche Funktionen laufen, App-Version, Fehler), damit wir das Produkt verbessern können. Niemals übertragen werden Ihre Inhalte, Ihre Prompts, Ihre Schlüssel oder die von Ihnen analysierten Websites, und Ihre IP-Adresse wird verworfen. Sie können die Option jederzeit deaktivieren.

## Usage

In verwalteten Tarifen sehen Sie hier Ihr Guthaben und den verbleibenden Rest des Monats.

!!! note "Der Monat richtet sich nach UTC"
    Das Guthaben wird zu Beginn jedes Monats in UTC zurückgesetzt, nicht in Ihrer Zeitzone. Die Einstellungen zeigen Ihnen das entsprechende Datum bei Ihnen vor Ort, weshalb es spät am letzten Tag des Monats so wirken kann, als sei die Zurücksetzung zu früh erfolgt.

BYOK-Tarife verbrauchen für die Inferenz kein Hi, Moose-Guthaben, da die Erzeugung mit Ihrem eigenen Schlüssel läuft. Die Modellkosten gehen direkt an OpenRouter.

## Konto

- Ändern Sie Ihre E-Mail-Adresse, bestätigen Sie sie und setzen Sie Ihr Passwort zurück, sofern Sie ein Konto mit E-Mail und Passwort nutzen. Google-Konten werden über Google verwaltet.
- Änderungen der E-Mail-Adresse werden erst wirksam, nachdem Sie sie über einen Link bestätigt haben; anschließend wird Ihre Sitzung in der App aktualisiert.
- Sehen Sie Ihren aktuellen Tarif ein und wechseln Sie ihn. Siehe [Kontotypen und Tarife](account-modes.md).

### Ihren OpenRouter-API-Schlüssel hinterlegen

In BYOK-Tarifen hinterlegen Sie hier Ihren [OpenRouter](https://openrouter.ai)-Schlüssel. Hi, Moose prüft den Schlüssel, bevor das KI-Routing darauf umgestellt wird. Nach dem Hinterlegen gilt:

- KI-Funktionen laufen lokal in der Desktop-App mit Ihrem Schlüssel
- Sie wählen, welche unterstützten Modelle für Chat und Erzeugung genutzt werden
- Ihr Schlüssel und Ihre Prompts gelangen für die BYOK-Inferenz niemals über die Server von Hi, Moose

Der Schlüssel wird pro Konto und nicht pro Gerät gespeichert und begleitet Sie daher zu einer neuen Installation.

## Local Model

Laden Sie ein zugelassenes Modell auf das Gerät und aktivieren Sie es, etwa Gemma 4. Antworten eines lokalen Modells entstehen auf Ihrem Rechner, ohne die verwalteten Modelle von Hi, Moose und ohne Ihren OpenRouter-Schlüssel, und die Nutzung ist kostenfrei. Standardmäßig nutzt der Chat einen kurzen Cloud-Routing-Schritt, um für jede Nachricht das passende Werkzeug zu wählen, und sendet dafür den Text der Nachricht an einen Cloud-Routing-Dienst. Schalten Sie **Intelligentes Routing** unter **Einstellungen → Lokale KI** ab, damit auch dieser Schritt auf Ihrem Gerät bleibt.

Lokale Modelle stehen in allen Tarifen zur Verfügung und sind im Preview Mode **erforderlich** für [AEO Audits](../features/aeo-audits.md) und die Sichtbarkeitsbewertung.

!!! note "Die Kontextgröße richtet sich nach Ihrem Arbeitsspeicher"
    Hi, Moose bemisst das Kontextfenster des Modells nach dem verfügbaren Speicher Ihres Rechners. Dasselbe Modell nutzt daher auf einem Notebook mit 16 GB ein kleineres Fenster als auf einer größeren Workstation.

## Team

Laden Sie Mitglieder ein, sehen Sie deren Rollen ein und entziehen Sie Zugriffe. Die Sitzplatzgrenzen hängen von Ihrem Tarif ab. Den vollständigen Ablauf finden Sie unter [Teamverwaltung](team-management.md).

## Site Monitoring

Crawl-Zeitplan, lokaler Suchindex, überwachte Seiten und gesperrte Pfade. Das ist ein umfangreicher Bereich mit einer eigenen Seite: **[Website-Monitoring](../site-monitoring/overview.md)**.

Verbindungen zu CMS und Datenquellen sind davon getrennt und liegen im Bildschirm **Verbindungen**, nicht in den Einstellungen:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

Versehen Sie exportierte PDF-Berichte und eingebettete Audio-Player mit Ihrer eigenen Marke. In allen kostenpflichtigen Tarifen verfügbar und von der Inhaberin oder dem Inhaber des Abonnements bearbeitbar. Siehe **[White-Label-Branding](../agency/white-label.md)**.

## Konto-Anmeldungen

Moose nutzt für Local-fetch-Sichtbarkeitsläufe und für Send Moose einen eigenen Browser. Dieser Bereich listet die Websites, bei denen er angemeldet sein kann, gruppiert in KI-Antwortmaschinen (ChatGPT, Google AI Mode und Gemini, Grok, Perplexity, Bing Copilot) und Websites, die die Send-Moose-Agenten nutzen (Reddit, LinkedIn, X), jeweils mit dem Hinweis **Angemeldet** oder **Nicht angemeldet**. Öffnen Sie eine Website hier und melden Sie sich einmal an; jeder spätere Lauf übernimmt die Sitzung. Die Anmeldung beendet auch die „Bestätigen Sie, dass Sie ein Mensch sind“-Prüfungen, die Engines bei ersten Läufen zeigen. Die Anmeldungen bleiben auf diesem Rechner und gehen nie in die Cloud.

Der Hinweis ist eine Schätzung anhand der Cookies jeder Website. Verlangt ein Lauf weiterhin eine Anmeldung, öffnen Sie die Website hier und melden Sie sich erneut an.

Für Send Moose lässt sich ein **Webmail**-Postfach hinzufügen, damit Moose Bestätigungslinks lesen kann, während er an einem Auftrag arbeitet. Er sendet, antwortet, löscht oder ändert nie Einstellungen. Verwenden Sie ein für Moose angelegtes Postfach und halten Sie Ihr persönliches Postfach getrennt.

## Hi, Moose MCP

Verbinden Sie Claude, ChatGPT oder jede andere MCP-App mit Ihrem Hi, Moose-Konto, wählen Sie das Host-Gerät, das die Arbeit ausführt, wählen Sie das **Modell für Schreibaufgaben** und sehen Sie verbundene Apps und letzte Aufträge. Siehe **[Hi, Moose MCP](../integrations/hi-moose-mcp.md)**.

## Hi, Moose REST API

Dieser Bereich erscheint nur für den Kontoinhaber. Erstellen und widerrufen Sie die API-Schlüssel, die Ihre gespeicherten Sichtbarkeitsdaten aus Ihren eigenen Dashboards und Berichten lesen, legen Sie fest, was jeder Schlüssel darf (Sichtbarkeitsdaten lesen, Verfolgung verwalten, Läufe starten), und sehen oder entfernen Sie die für das Projekt registrierten Webhooks. Siehe **[Hi, Moose API](../integrations/developer-api.md)**.

## Logs

Aktionsprotokolle des aktuellen Projekts mit Typ, Benutzer, Datum, Status und Metadaten jeder aufgezeichneten Aktion. In verwalteten Tarifen werden die geteilten Teamprotokolle neben Ihren lokalen synchronisiert.

**Export CSV** lädt sie herunter. Der Export der Team-Aktionsprotokolle ist Inhaberinnen und Inhabern kostenpflichtiger verwalteter Arbeitsbereiche vorbehalten.

## Data & Backup

Erstellen Sie eine komprimierte `.hmbk`-Sicherung Ihres Verlaufs auf dem Gerät und importieren Sie sie später zur Wiederherstellung.

**Sicherungen enthalten** die Einträge der lokalen Datenbank und gespeicherte BYOK-Sichtbarkeitszeitpläne, sodass Ihre Briefs, Audits, Vorschauen, der Site-Monitoring-Verlauf, der Inbox-Status und weitere nicht vertrauliche Arbeitsartefakte portabel bleiben.

**Sicherungen enthalten nicht** den Anmeldestatus, Zugangsdaten von Konnektoren, API-Schlüssel, lokale Modelldateien oder Dateianhänge.

!!! warning "Ein Import überschreibt lokale Daten dauerhaft"
    Ein Import ersetzt die lokalen Hi, Moose-Daten dieses Geräts durch den Inhalt der Sicherung. Der Bestätigungsdialog nennt Ihnen, wie viele Einträge wiederhergestellt werden und wann die Sicherung erstellt wurde. Starten Sie die App anschließend neu, damit alle Bildschirme aus den wiederhergestellten Daten neu laden.

Importe akzeptieren ausschließlich `.hmbk`-Dateien, die von der Hi, Moose-Desktop-App exportiert wurden.

## Sichtbarkeitsverlauf

Hi, Moose bewahrt auf diesem Rechner eine Kopie Ihrer KI-Suchantworten auf, damit die Visibility-Seite jeden Zeitraum anzeigen kann, ohne ihn erneut herunterzuladen. Dieser Bereich zeigt, wie viel Platz die Kopie des aktuellen Projekts belegt und welche Daten sie abdeckt, sowie ein **Speicherbudget**: Überschreitet die Kopie diese Größe, werden die ältesten Tage nur von diesem Rechner entfernt und kommen aus der Cloud zurück, wenn Sie einen Zeitraum wählen, der sie braucht. In Tarifen ohne Cloud-Kopie wird nichts automatisch entfernt; sichern Sie die Antworten stattdessen unter Daten & Backup.

## Troubleshooting

Drei Wiederherstellungswerkzeuge. Alle betreffen ausschließlich den lokalen Desktop-Zustand und rühren niemals an Cloud-Daten.

**Temporären Cache leeren**: Löscht den HTTP-Cache, Service Worker und andere verzichtbare Zustände. Anmeldung und lokaler Arbeitsverlauf bleiben erhalten. Probieren Sie das zuerst.

**Diagnoseprotokoll**: Hi, Moose führt auf diesem Gerät ein kleines Fehlerprotokoll. **Protokollordner öffnen** bringt Sie dorthin; wenn der Support danach fragt, senden Sie die Datei `main-errors.log`. Das Protokoll bleibt auf Ihrem Gerät, sofern Sie es nicht selbst weitergeben.

**Lokale App-Daten zurücksetzen**: Entfernt dauerhaft Artefakte, Briefs, Vorschauen, den Sichtbarkeitsverlauf und weitere lokale Arbeitszustände vom Gerät. Das lässt sich nicht rückgängig machen. Ihre Anmeldung und gespeicherte Konnektor-Zugangsdaten bleiben bestehen.
