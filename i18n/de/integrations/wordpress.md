---
source_hash: 57477f3edd7e63b53a23c12a7676c0c723e2f37903e1f4aa75a613f296e8277b
---
# WordPress

## Wofür das gut ist

Eine WordPress-Website mit Hi, Moose verbinden, damit die Desktop-App Inhaltsänderungen direkt vorbereiten und anwenden kann (FAQ, Key Points, briefbasierte Entwürfe und Empfehlungen aus AEO Audits), mit einem Vorschau- und einem Freigabeschritt, bevor etwas live geht.

## Wie die Verbindung funktioniert

Die Desktop-App ist die aktive Seite dieser Verbindung: Sie ermittelt den Zielbeitrag, holt dessen aktuellen Inhalt, baut die vorgeschlagene Änderung lokal auf und ruft die REST-Endpunkte Ihrer WordPress-Website direkt über HTTPS auf, um die Änderung vorzubereiten. Ihre WordPress-Website bleibt passiv: Sie stellt einen Endpunkt bereit, der auf Aufrufe wartet, und muss sich niemals von sich aus bei Hi, Moose melden.

Das bedeutet:

- Ihr Website-Token und Ihre Verbindungsdaten liegen nie bei der Benutzeroberfläche, sondern ausschließlich beim Hintergrundprozess der Desktop-App.
- In den BYOK-Tarifen laufen die Schritte mit lokalem Modell, die bei der Vorbereitung einer Änderung anfallen (etwa das Auffinden des genauen zu ersetzenden Inhaltsabschnitts), mit Ihrem eigenen OpenRouter-Schlüssel und nicht über einen von Hi, Moose gehosteten Aufruf.

## Eine Verbindung einrichten

1. Öffnen Sie **Connections** in der Desktop-App und wählen Sie WordPress.
2. Laden Sie das Konnektor-Plugin herunter, installieren Sie es in Ihrer WordPress-Verwaltung und fügen Sie dort Ihre Website-URL sowie den API-Schlüssel dieses Projekts in die Plugin-Einstellungen ein.
3. Speichern Sie zurück in Hi, Moose die Verbindung und prüfen Sie, dass der Konnektor einen erfolgreichen Ping von Ihrer Website meldet.

## Umgebungen

Jede WordPress-Installation, die Sie verbinden (Produktion, Staging oder beides), ist eine eigene **Umgebung** mit eigenem Website-Token und eigenem HMAC-Geheimnis, vollständig voneinander getrennt. Wählen Sie, welche Umgebung das Standardziel für neue Änderungen ist, und wechseln Sie jederzeit zwischen ihnen. Liegt eine Staging-Website hinter einer HTTP-Basic-Authentifizierung, können Sie diese Zugangsdaten eigens für diese Umgebung hinterlegen, damit Hi, Moose sie erreicht.

## Patches

Jede WordPress-Änderung, ob aus den [FAQ](../features/faq-generator.md), den [Key Points](../features/key-points.md), einem [Entwurf](../features/drafts-and-publishing.md) oder einer von Ihnen selbst angelegten manuellen Textersetzung, wird als **Patch** geführt: ein lokaler Registereintrag je Umgebung mit eigenem Status.

Ein Patch durchläuft ausdrückliche Zustände: **Draft**, **Staged**, **Applied**, **Discarded**, **Rolled back** oder **Failed**. Aus der Patch-Liste heraus können Sie:

- Einen Patch zur Vorschau auf Ihrer WordPress-Website **vorbereiten**.
- Einen vorbereiteten Patch **anwenden**, um ihn live zu schalten.
- Einen Patch **verwerfen**, den Sie nicht nutzen möchten.
- Einen angewendeten Patch **zurücknehmen**.
- Einen Patch in eine andere Umgebung **übernehmen** (etwa von Staging nach Produktion), um ihn dort erneut zur Durchsicht vorzubereiten.

Haben Sie einen Entwurf einmal übergeben, merkt Hi, Moose sich das, sodass Sie denselben nicht versehentlich mehrfach übergeben.

## Plugin Listen to this Article

Das eigenständige WordPress-Plugin **Listen to This Article** bettet den Audio-Player und die Transkription ein, die [Audio](../audio/overview.md) in der Desktop-App erzeugt. Installieren Sie es über [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/), oder fügen Sie den Einbettungscode direkt in Ihren Beitrag ein. Siehe [Player und Einbettung](../audio/player-and-embed.md).

## Voraussetzungen

- WordPress 6.0 oder höher, mit Administratorzugang, um die Verbindung auf Ihrer Website einzurichten.
- Ein in der Desktop-App eingerichtetes Projekt.
