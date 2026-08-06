---
source_hash: b5d0a07f31228ccaaa2c18a76dddb8de404f3871f7b879591e111c89bae3e9c5
---
# Player und Einbettung

## Wofür das gut ist

Den eingebetteten Audio-Player an die Seite anpassen, auf der er stehen soll, und anschließend den Einbettungscode kopieren. Öffnen Sie das über **Player anpassen** bei einer fertigen Folge oder über die Einbettungsaktion im Reiter **Verlauf**.

## Player-Optionen

- **Design**: Dark, Light oder Auto. Auto folgt der Einstellung des jeweiligen Besuchergeräts.
- **Layout**: Full oder Compact.
- **Akzentfarbe**: ein beliebiger sechsstelliger Hexadezimalwert, etwa `#5688b0`.
- **Titel anzeigen**: Schalten Sie das aus, wenn die Einbettung unter Ihrer eigenen Überschrift steht.
- **Eigener Titel**: Leer lassen, um den Titel der Folge zu verwenden.
- **Transkriptions-Schaltfläche**: Blenden Sie die Transkriptionsumschaltung im Player ein oder aus.

Eine Live-Vorschau aktualisiert sich, während Sie Einstellungen ändern. Ist das Player-Skript während der Vorschau nicht erreichbar, zeigt die Vorschau schlichtes Markup; der kopierte Einbettungscode bleibt dennoch korrekt.

## Den Einbettungscode kopieren

Klicken Sie auf **Einbettungscode kopieren** und fügen Sie ihn in Ihre Seite ein.

- **WordPress**: in den HTML- oder Code-Block des Beitrags einfügen, oder das [Plugin Listen to This Article](https://wordpress.org/plugins/listen-to-this-article/) verwenden.
- **Webflow**: in ein Embed-Element einfügen.
- **Grav**: in den Seiteninhalt einfügen, wo rohes HTML erlaubt ist.

## Die Wiedergabe ist an die Domain gebunden

Erzeugtes Audio wird nur auf der Domain der Website Ihres Projekts und auf `himoose.com` abgespielt. Das ergibt sich aus dem Website-Feld des Projekts, und deshalb muss dieses Feld vor der Erzeugung ausgefüllt sein. Betten Sie den Player auf einer nicht freigegebenen Domain ein, wird die Wiedergabe verweigert.

## Agentur-Attribution

In Tarifen mit [White-Label-Branding](../agency/white-label.md) kann der eingebettete Player die Attribution Ihrer Agentur statt der von Hi, Moose tragen. Das stellen Sie unter **Einstellungen → Branding** ein:

- **Attribution der Audio-Einbettung**: der auf dem Player angezeigte Text. Leer lassen, um „Audio by" gefolgt vom Namen Ihrer Agentur zu verwenden.
- **Attributionslink**: eine vollständige `https://`-Adresse. Leer lassen, um Ihren Haupt-Markenlink zu übernehmen.

Die Attribution ist ein echter Link zurück auf Ihre Website von jeder Kundenseite, die den Player trägt, und genau darin liegt ihr Wert für Agenturen.

!!! warning "Die Attribution gilt für Code, der nach dem Speichern kopiert wurde"
    Eine Änderung des Brandings schreibt bereits platzierte Einbettungen nicht um. Kopieren Sie den Einbettungscode nach dem Speichern erneut, um die neue Attribution zu übernehmen.

## Warum das dem AEO hilft

Die Transkription fügt der Seite strukturierten, eigenen und crawlbaren Text hinzu. Das ist zusätzlicher echter Inhalt, den eine Antwortmaschine abrufen und zitieren kann, und er kann die Signale für Extrahierbarkeit und Vollständigkeit in einem [AEO Audit](../features/aeo-audits.md) stärken. Es ist für sich genommen kein bewerteter Faktor „hat Medien": Der Wert liegt in dem Text, den der Player mitbringt.
