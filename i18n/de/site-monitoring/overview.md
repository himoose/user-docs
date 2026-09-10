---
source_hash: 29ee2dfc08c9390fc91d11ea66fc96fc6fef4439d84b5f28508c2afbf8f0c1d3
---
# Website-Monitoring

## Wofür das gut ist

Hi, Moose führt ein lokales Abbild Ihrer Website: welche Seiten es gibt, was darauf steht und was sich seit dem letzten Mal geändert hat. Dieses Abbild speist vier Dinge: die Hinweise auf AEO-relevante Änderungen in Ihrer [Inbox](../inbox/overview.md), den semantischen Suchindex, mit dem Moose Fragen zu Ihrer eigenen Website beantwortet, das Seiteninventar, auf das [Audits](../features/aeo-audits.md) und [Briefs](../features/content-briefs.md) zurückgreifen, und den [Entity Graph](../features/entity-graph.md), der abbildet, worum es auf Ihrer Website geht.

All das liegt unter **Einstellungen → Website-Monitoring** und gilt jeweils für das aktuelle Projekt.

## Der geplante Crawl

Aktivieren Sie **Wöchentlichen Website-Crawl ausführen**, und Hi, Moose aktualisiert die überwachten Seiten wöchentlich und benachrichtigt Sie, wenn wesentliche Änderungen auftauchen. Wählen Sie Tag und Uhrzeit in Ihrer lokalen Zeit.

Manuelle Crawls bleiben in jedem Fall verfügbar. **Crawl jetzt ausführen** startet sofort einen vollständigen Crawl, dessen Fortschritt in der Statusleiste am unteren Fensterrand erscheint. Sie können einen laufenden Crawl **pausieren**, **fortsetzen** oder **stoppen**; die bis dahin gefundenen Seiten bleiben erhalten, statt verworfen zu werden.

Bei großen Websites dauert das einige Minuten.

### Der Crawler findet sein eigenes Tempo

Jede Website hat eine Geschwindigkeit, in der sie sich bequem lesen lässt, und die ist bei einer statischen Site auf einem CDN eine andere als bei einem datenbankgestützten Shop auf Shared Hosting. Hi, Moose rät sie nicht aus einer Einstellung, sondern findet sie heraus.

Der Crawl beginnt behutsam, wird schneller, solange Seiten zügig zurückkommen, und nimmt sich zurück, sobald die Website Anstrengung zeigt: langsamere Antwortzeiten oder eine Antwort mit Ratenbegrenzung oder Serverauslastung. Dann meldet die Statusleiste **Wird langsamer, um zur Website zu passen**, und der Crawl läuft im langsameren Tempo weiter, statt den Server zu überfahren oder aufzugeben.

Praktisch heißt das: Inventare kommen vollständig zurück. Ein Crawl, der auf halber Strecke ratenbegrenzt wurde, lieferte ein Teilbild Ihrer Website, und damit wurde auch alles darauf Aufbauende unvollständig: der Suchindex, die Audits, die Briefs.

Konfigurieren müssen Sie davon nichts.

## Der Suchindex

Unter den Crawl-Bedienelementen liegt der **Suchindex**, der lokale semantische Index, mit dem Moose Fragen zu den Seiten Ihrer Website beantwortet. Er nennt die Anzahl indexierter Seiten, die daraus entstandenen Passagen und den Zeitpunkt der letzten Aktualisierung.

Indexiert wird auf Passagen-, nicht auf Seitenebene. Eine lange Seite wird zu vielen einzeln durchsuchbaren Passagen, und deshalb kann Moose einen bestimmten Absatz zitieren, statt Ihnen zu sagen, eine Seite handle „im Großen und Ganzen" von einem Thema.

- **Index neu aufbauen** indexiert von Grund auf neu.
- Gibt es seit der letzten Aktualisierung neue oder geänderte Seiten, nennt Hi, Moose deren Anzahl. Sie werden beim nächsten Crawl indexiert, oder Sie bauen den Index sofort neu auf.

!!! note "Der Index ist ehrlich über das, was er nicht hat"
    Fragen Sie Moose nach einer Seite, die nicht indexiert wurde, sagt er das und verweist Sie auf einen Crawl, statt aus der URL der Seite Rückschlüsse zu ziehen.

## Überwachte Seiten

Die Seiten, die Hi, Moose auf AEO-relevante Änderungen prüft. Seiten, die durch die Website-Erkennung, durch [Google Search Console](../integrations/google-search-console.md) und durch [Sichtbarkeitsläufe](../visibility/overview.md) gefunden werden, erscheinen hier automatisch.

Sie können Seiten auch von Hand mit vollständiger URL hinzufügen, die Liste durchsuchen und filtern, seitenweise blättern und Seiten entfernen, die Sie nicht interessieren.
Überwachte Seiten sind auf die eigene Domain des Projekts festgelegt. Subdomains davon sind in Ordnung, eine fremde Domain wird abgelehnt, damit sich die Überwachung eines Projekts nicht unbemerkt mit den Seiten eines anderen füllt.

## Gesperrte Pfade

Crawls überspringen gesperrte Pfade und alles darunter, und passende Seiten werden aus der Überwachung entfernt.

Der Abgleich erfolgt über das Präfix eines Pfadsegments. `/results/` zu sperren erfasst `/results/` und sämtliche Unterpfade, aber **nicht** `/results-archive/`: Das Segment muss übereinstimmen, nicht bloß die Zeichenkette.

Das ist das richtige Mittel für Suchergebnisseiten, gefilterte Listenseiten, paginierte Archive und alles andere, was eine große Zahl nahezu identischer URLs erzeugt, die Sie lieber nicht crawlen, indexieren oder gemeldet bekommen möchten.

## Wie alt ist jede Seite

Während des Crawls liest Hi, Moose die Veröffentlichungs- und Änderungsdaten, die Ihre Seiten angeben (in ihren strukturierten Daten, ihren Metadaten und ihren `<time>`-Elementen), und hält sie bei der Seite fest.

Das ist wichtig, weil Aktualität eines der Kriterien ist, die Antwortmaschinen abwägen, wenn sie entscheiden, welcher Quelle sie bei einer Frage mit sich änderndem Stand vertrauen. Eine Seite, die nichts darüber sagt, wann sie geschrieben wurde, kann dieses Argument nicht führen. Ihre [AEO-Audits](../features/aeo-audits.md) verwenden diese Daten in ihrer Aktualitätsbewertung, und dort sehen Sie das Ergebnis.

Gibt eine Seite nirgends ein Datum an, ist genau das schon ein Befund, auf den sich reagieren lässt.

## Was in Ihrer Inbox landet

Ein Crawl erzeugt **eine einzige Zusammenfassung pro Lauf**, nicht einen Eintrag je geänderter Seite. Die Zusammenfassung öffnet sich zu einer Tabelle der geänderten Seiten mit der jeweiligen Änderung, einer Auswirkungsstufe und Aktionen je Seite.

Die Auswirkungsstufen sind **Kritisch**, **Erheblich**, **Gering**, **Nicht erreichbar** und **Nicht geprüft**.

Zwei Einstellungen steuern das Rauschen:

- **Informative AEO-Änderungen einbeziehen**: standardmäßig aus. Ist die Option an, erzeugen auch Änderungen mit geringer Auswirkung Inbox-Einträge.
- **Mindest-Schweregrad für Betriebssystem-Benachrichtigungen**: Nur Inbox-Einträge auf dieser Stufe oder darüber lösen eine Desktop-Benachrichtigung aus. Stellen Sie sie auf Info, wenn auch Änderungen mit geringer Auswirkung auf Betriebssystemebene erscheinen sollen.

## Moose fragen, was sich geändert hat

Die Zusammenfassung enthält die Aktion **Moose zu all dem fragen**, die die vollständige Momentaufnahme des Crawls an den Chat übergibt und fragt, was am wichtigsten ist und womit Sie beginnen sollten. Einzelne Seiten haben ihre eigene Aktion **Moose fragen**, die nur die aufgezeichnete Änderung dieser Seite übergibt.

Beide beschränken sich auf die aufgezeichnete Momentaufnahme. Geht daraus nicht hervor, warum sich etwas geändert hat, ist Moose angewiesen, das zu sagen, statt einen Grund zu erfinden.

## Nicht erreichbare Seiten

Ist eine Seite oder die gesamte Website nicht erreichbar, wird das als eigene Änderungsart gemeldet, statt stillschweigend übergangen zu werden. Ein Ausfall der gesamten Website erzeugt einen einzigen Eintrag **Website nicht erreichbar** statt einer Meldung je Seite.
