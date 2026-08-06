---
source_hash: 87a7b6f091685fae0a59b09ee8abe0ec965085647eb82bd29c1661777efb87ab
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/site-monitoring/overview/)

# Site Monitoring

## Wofür das gut ist

Hi, Moose führt ein lokales Abbild Ihrer Website: welche Seiten es gibt, was darauf steht und was sich seit dem letzten Mal geändert hat. Dieses Abbild speist drei Dinge: die Hinweise auf AEO-relevante Änderungen in Ihrer [Inbox](../inbox/overview.md), den semantischen Suchindex, mit dem Moose Fragen zu Ihrer eigenen Website beantwortet, und das Seiteninventar, auf das [Audits](../features/aeo-audits.md) und [Briefs](../features/content-briefs.md) zurückgreifen.

All das liegt unter **Einstellungen → Site Monitoring** und gilt jeweils für das aktuelle Projekt.

## Der geplante Crawl

Aktivieren Sie **Run weekly site crawl**, und Hi, Moose aktualisiert die überwachten Seiten wöchentlich und benachrichtigt Sie, wenn wesentliche Änderungen auftauchen. Wählen Sie Tag und Uhrzeit in Ihrer lokalen Zeit.

Manuelle Crawls bleiben in jedem Fall verfügbar. **Run crawl now** startet sofort einen vollständigen Crawl, dessen Fortschritt in der Statusleiste am unteren Fensterrand erscheint. Sie können einen laufenden Crawl **anhalten**; die bis dahin gefundenen Seiten bleiben erhalten, statt verworfen zu werden.

Bei großen Websites dauert das einige Minuten.

## Der Suchindex

Unter den Crawl-Bedienelementen liegt der **Search index**, der lokale semantische Index, mit dem Moose Fragen zu den Seiten Ihrer Website beantwortet. Er nennt die Anzahl indexierter Seiten, die daraus entstandenen Passagen und den Zeitpunkt der letzten Aktualisierung.

Indexiert wird auf Passagen-, nicht auf Seitenebene. Eine lange Seite wird zu vielen einzeln durchsuchbaren Passagen, und deshalb kann Moose einen bestimmten Absatz zitieren, statt Ihnen zu sagen, eine Seite handle „im Großen und Ganzen" von einem Thema.

- **Rebuild index** indexiert von Grund auf neu.
- Gibt es seit der letzten Aktualisierung neue oder geänderte Seiten, nennt Hi, Moose deren Anzahl. Sie werden beim nächsten Crawl indexiert, oder Sie bauen den Index sofort neu auf.

!!! note "Der Index ist ehrlich über das, was er nicht hat"
    Fragen Sie Moose nach einer Seite, die nicht indexiert wurde, sagt er das und verweist Sie auf einen Crawl, statt aus der URL der Seite Rückschlüsse zu ziehen.

## Überwachte Seiten

Die Seiten, die Hi, Moose auf AEO-relevante Änderungen prüft. Seiten, die durch die Website-Erkennung, durch [Google Search Console](../integrations/google-search-console.md) und durch [Sichtbarkeitsläufe](../visibility/overview.md) gefunden werden, erscheinen hier automatisch.

Sie können Seiten auch von Hand mit vollständiger URL hinzufügen, die Liste durchsuchen und filtern, seitenweise blättern und Seiten entfernen, die Sie nicht interessieren.

## Gesperrte Pfade

Crawls überspringen gesperrte Pfade und alles darunter, und passende Seiten werden aus der Überwachung entfernt.

Der Abgleich erfolgt über das Präfix eines Pfadsegments. `/results/` zu sperren erfasst `/results/` und sämtliche Unterpfade, aber **nicht** `/results-archive/`: Das Segment muss übereinstimmen, nicht bloß die Zeichenkette.

Das ist das richtige Mittel für Suchergebnisseiten, gefilterte Listenseiten, paginierte Archive und alles andere, was eine große Zahl nahezu identischer URLs erzeugt, die Sie lieber nicht crawlen, indexieren oder gemeldet bekommen möchten.

## Was in Ihrer Inbox landet

Ein Crawl erzeugt **eine einzige Zusammenfassung pro Lauf**, nicht einen Eintrag je geänderter Seite. Die Zusammenfassung öffnet sich zu einer Tabelle der geänderten Seiten mit der jeweiligen Änderung, einer Auswirkungsstufe und Aktionen je Seite.

Die Auswirkungsstufen sind **Critical**, **Notable**, **Low**, **Unreachable** und **Not reviewed**.

Zwei Einstellungen steuern das Rauschen:

- **Include informational AEO changes**: standardmäßig aus. Ist die Option an, erzeugen auch Änderungen mit geringer Auswirkung Inbox-Einträge.
- **OS notification minimum severity**: Nur Inbox-Einträge auf dieser Stufe oder darüber lösen eine Desktop-Benachrichtigung aus. Stellen Sie sie auf Info, wenn auch Änderungen mit geringer Auswirkung auf Betriebssystemebene erscheinen sollen.

## Moose fragen, was sich geändert hat

Die Zusammenfassung enthält die Aktion **Ask Moose about all of this**, die die vollständige Momentaufnahme des Crawls an den Chat übergibt und fragt, was am wichtigsten ist und womit Sie beginnen sollten. Einzelne Seiten haben ihre eigene Aktion **Ask Moose**, die nur die aufgezeichnete Änderung dieser Seite übergibt.

Beide beschränken sich auf die aufgezeichnete Momentaufnahme. Geht daraus nicht hervor, warum sich etwas geändert hat, ist Moose angewiesen, das zu sagen, statt einen Grund zu erfinden.

## Nicht erreichbare Seiten

Ist eine Seite oder die gesamte Website nicht erreichbar, wird das als eigene Änderungsart gemeldet, statt stillschweigend übergangen zu werden. Ein Ausfall der gesamten Website erzeugt einen einzigen Eintrag **Site unreachable** statt einer Meldung je Seite.
