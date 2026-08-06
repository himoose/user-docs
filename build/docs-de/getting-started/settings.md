---
source_hash: f081840e659e67696268902173c5c0f26e8413e1debac31049488ad42cb5c005
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/getting-started/settings/)

# Einstellungen

## Wofür das gut ist

In den Einstellungen verwalten Sie Ihr Profil, Ihren Tarif, Ihre Modelle, Ihr Team und das Verhalten der App auf diesem Rechner. Sie sind in zehn Bereiche in der linken Spalte gegliedert.

| Bereich | Inhalt |
|---|---|
| General | Profildaten und App-Verhalten auf diesem Rechner |
| Usage | Guthabenstand und Zurücksetzungsdatum |
| Konto | E-Mail, Passwort, Tarif, OpenRouter-Schlüssel |
| Local Model | Herunterladen und Aktivieren des Modells auf dem Gerät |
| Team | Sitzplätze, Einladungen, Rollen |
| [Site Monitoring](../site-monitoring/overview.md) | Crawl-Zeitplan, Suchindex, überwachte Seiten, gesperrte Pfade |
| [Branding](../agency/white-label.md) | White-Label-Berichte und Audio-Attribution (nur kostenpflichtige Tarife) |
| Logs | Aktionsprotokolle und CSV-Export |
| Data & Backup | Lokale Sicherung und Wiederherstellung |
| Troubleshooting | Cache, Diagnoseprotokoll, Zurücksetzen lokaler Daten |

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

Laden Sie ein zugelassenes Modell auf das Gerät und aktivieren Sie es, etwa Gemma 4. Die lokale Ausführung nutzt weder die Modelle von Hi, Moose noch Ihren OpenRouter-Schlüssel: Sie läuft vollständig auf Ihrem Rechner und ist kostenfrei.

Lokale Modelle stehen in allen Tarifen zur Verfügung und sind im Preview Mode **erforderlich** für [AEO Audits](../features/aeo-audits.md) und die Sichtbarkeitsbewertung.

!!! note "Die Kontextgröße richtet sich nach Ihrem Arbeitsspeicher"
    Hi, Moose bemisst das Kontextfenster des Modells nach dem verfügbaren Speicher Ihres Rechners. Dasselbe Modell nutzt daher auf einem Notebook mit 16 GB ein kleineres Fenster als auf einer größeren Workstation.

## Team

Laden Sie Mitglieder ein, sehen Sie deren Rollen ein und entziehen Sie Zugriffe. Die Sitzplatzgrenzen hängen von Ihrem Tarif ab. Den vollständigen Ablauf finden Sie unter [Teamverwaltung](team-management.md).

## Site Monitoring

Crawl-Zeitplan, lokaler Suchindex, überwachte Seiten und gesperrte Pfade. Das ist ein umfangreicher Bereich mit einer eigenen Seite: **[Site Monitoring](../site-monitoring/overview.md)**.

Verbindungen zu CMS und Datenquellen sind davon getrennt und liegen im Bildschirm **Connections**, nicht in den Einstellungen:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

Versehen Sie exportierte PDF-Berichte und eingebettete Audio-Player mit Ihrer eigenen Marke. In allen kostenpflichtigen Tarifen verfügbar und von der Inhaberin oder dem Inhaber des Abonnements bearbeitbar. Siehe **[White-Label-Branding](../agency/white-label.md)**.

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

## Troubleshooting

Drei Wiederherstellungswerkzeuge. Alle betreffen ausschließlich den lokalen Desktop-Zustand und rühren niemals an Cloud-Daten.

**Temporären Cache leeren**: Löscht den HTTP-Cache, Service Worker und andere verzichtbare Zustände. Anmeldung und lokaler Arbeitsverlauf bleiben erhalten. Probieren Sie das zuerst.

**Diagnoseprotokoll**: Hi, Moose führt auf diesem Gerät ein kleines Fehlerprotokoll. **Protokollordner öffnen** bringt Sie dorthin; wenn der Support danach fragt, senden Sie die Datei `main-errors.log`. Das Protokoll bleibt auf Ihrem Gerät, sofern Sie es nicht selbst weitergeben.

**Lokale App-Daten zurücksetzen**: Entfernt dauerhaft Artefakte, Briefs, Vorschauen, den Sichtbarkeitsverlauf und weitere lokale Arbeitszustände vom Gerät. Das lässt sich nicht rückgängig machen. Ihre Anmeldung und gespeicherte Konnektor-Zugangsdaten bleiben bestehen.
