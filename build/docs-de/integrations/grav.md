---
source_hash: 1d027fe8d7c0bf155818720c05a7777b1744c302a9ab057860377dc301df1947
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/integrations/grav/)

# Grav

## Wofür das gut ist

Eine produktive [Grav](https://getgrav.org)-Website über das Hi, Moose-Plugin für Grav verbinden, damit die Desktop-App Grav-Inhalte prüfen und Aktionen zum Anlegen, Aktualisieren, Veröffentlichen und Zurücknehmen direkt aus der Ferne ausführen kann.

## Das Plugin installieren

1. Öffnen Sie in der Desktop-App **Connections → Grav**, rufen Sie den Download-Link auf und laden Sie das ZIP-Archiv des Hi, Moose-Plugins herunter. Die aktuelle Version ist **0.1.1** und setzt Grav 1.7.0 oder höher voraus.
2. Öffnen Sie in Ihrer Grav-Verwaltung **Plugins**, laden Sie das ZIP hoch und schließen Sie die Installation ab.
3. Aktivieren Sie das Plugin und öffnen Sie dann dessen Einstellungen in der Grav-Verwaltung.
4. Kopieren Sie das dort angezeigte Verbindungspaket: Sie fügen es im nächsten Schritt in Hi, Moose ein.

## In Hi, Moose verbinden

1. Öffnen Sie **Connections** in der Desktop-App und wählen Sie Grav.
2. Geben Sie die URL Ihrer Grav-Website ein.
3. Lassen Sie die Konnektor-Route leer, sofern Ihr Grav-Plugin keine abweichende Route verwendet. Andernfalls nutzt Hi, Moose die Route aus dem Verbindungspaket oder greift auf `/himoose-connector` zurück.
4. Fügen Sie das aus dem Plugin kopierte Verbindungspaket ein und speichern Sie.
5. Klicken Sie auf **Test connector**, um die Verbindung gegen Ihre produktive Grav-Website zu prüfen.

## Verbindungsstatus

Nach dem Test meldet Hi, Moose einen von mehreren Zuständen: Der Konnektor ist noch nicht vollständig eingerichtet, er ist gespeichert, aber noch nicht geprüft, er hat geantwortet, doch entfernte Schreibaktionen sind nicht vollständig freigegeben (nur Lesen), er ist für Lese- und entfernte Schreibaktionen vollständig bereit, oder die letzte Prüfung ist fehlgeschlagen und die Website-Einstellungen oder die Plugin-Geheimnisse brauchen Aufmerksamkeit.

## Was die Verbindung leisten kann

Ist sie bereit, kann der Grav-Konnektor Inhalte auflisten, Rohinhalte lesen sowie Inhalte direkt anlegen, aktualisieren und veröffentlichen, und zwar über denselben vorbereiteten, überprüfbaren Weg, den [Entwürfe, Vorschau und Veröffentlichung](../features/drafts-and-publishing.md) auch für die anderen Verbindungen nutzen.

## Sicherheit

Die URL Ihrer Grav-Website und das Verbindungspaket werden lokal gespeichert und sind ausschließlich für den Hintergrundprozess der Desktop-App zugänglich; sie werden der Benutzeroberfläche niemals offengelegt.
