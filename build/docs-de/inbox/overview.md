---
source_hash: 9705deb0dc37b51cf84f956088049d0d7d87b416de55439c84ef17b2ef0d3d9c
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/inbox/overview/)

# Inbox

## Wofür das gut ist

Die Inbox ist der Ort, an dem Hi, Moose das nach oben holt, was Ihre Aufmerksamkeit verdient: geordnete Befunde, Audits und Veröffentlichungsereignisse, jeweils an ein echtes Artefakt gebunden statt an eine allgemeine Benachrichtigung. Sie verwandelt verstreute Signale (Stimmungsverschiebungen in der Sichtbarkeit, narrative Abweichungen, Ungenauigkeiten bei der Funktionsabdeckung, Ergebnisse von AEO Audits, Veröffentlichungsergebnisse und Freigabeanfragen) in eine einzige, priorisierte Arbeitsliste.

## Was in der Inbox erscheint

Jeder Eintrag der Inbox verweist auf etwas Konkretes, das Sie öffnen und bearbeiten können:

- **Sichtbarkeitssignale**: negative oder gemischte Stimmung in einer KI-Antwort, narrative Abweichung oder Ungenauigkeit bei der Funktionsabdeckung gegenüber Ihrem [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), oder ein abgeschlossener beziehungsweise fehlgeschlagener [Sichtbarkeitslauf](../visibility/overview.md).
- **Ergebnisse von AEO Audits**: ein abgeschlossener Audit oder ein Audit, dessen Maßnahmenplan eine Empfehlung mit hoher Priorität hervorgebracht hat.
- **Erkannte Änderungen an der Website**: eine einzige Zusammenfassung pro [Site-Monitoring](../site-monitoring/overview.md)-Crawl, die sich zu einer Tabelle aller geänderten Seiten mit ihrer Auswirkungsstufe öffnet. Nicht erreichbare Seiten und Ausfälle der gesamten Website werden als eigene Änderungsarten gemeldet.
- **Workflow-Berichte**: Ergebnisse eines [Workflow](../workflows/overview.md)-Laufs, etwa eine geplante Analyse, die neue Beiträge erzeugt oder eine Chance in der KI-Suche aufgezeigt hat.
- **Veröffentlichungsereignisse**: eine **fehlgeschlagene** Veröffentlichung oder eine Änderung, die auf Ihre Freigabe wartet. Erfolgreiche Veröffentlichungen erzeugen bewusst keinen Inbox-Eintrag mehr, denn eine Wand aus „hat geklappt"-Meldungen begräbt genau die Einträge, die Sie brauchen.
- **Eine Willkommensnachricht** von Moose nach Abschluss der Einrichtung, mit einem sinnvollen ersten Schritt.

Jeder Eintrag zeigt eine sinnvolle nächste Aktion, wo es angebracht ist: das Artefakt öffnen, einen Brief starten, einem Audit nachgehen, einen Entwurf durchsehen, eine Änderung freigeben oder einen fehlgeschlagenen Lauf wiederholen. So lesen Sie nicht bloß eine Benachrichtigung, sondern sind einen Klick vom Handeln entfernt.

Site-Monitoring-Zusammenfassungen enthalten zusätzlich die Aktion **Ask Moose about all of this**, die die Momentaufnahme des Crawls an den [Chat](../chat/overview.md) übergibt und fragt, womit Sie beginnen sollten.

## Die Inbox filtern

Zwei Filter bestimmen, was Sie sehen:

- **Status**: Standard ist **Active**, also alles, was nicht verworfen wurde (offene, laufende und erledigte Einträge). Wechseln Sie zu einem bestimmten Status oder zu **All**, um auch verworfene Einträge einzubeziehen, die Sie eventuell wieder aufgreifen möchten.
- **Schweregrad**: **Critical**, **Warning**, **Notice**, **Info** oder alle.

Einträge sind nach Datum gruppiert (etwa „Gestern", „Älter") mit einer Anzahl je Gruppe, damit Sie schnell sehen, wie viel auf Sie wartet. Umfangreiche Postfächer werden seitenweise geladen statt auf einmal.

**Alle als gelesen markieren** löscht die Kennzeichnung in Ihrer gesamten Inbox, nicht nur auf der angezeigten Seite.

!!! note "Die Inbox behält ihre 200 neuesten Einträge"
    Ältere werden automatisch entfernt. Die Inbox ist eine Arbeitsliste, kein Archiv: Alles Dauerhafte liegt in der [Library](../library/overview.md) oder in dem Artefakt, auf das der Eintrag verweist.

## Steuern, was Sie benachrichtigt

Klicken Sie auf **Notifications**, um Ihre projektbezogenen Benachrichtigungseinstellungen zu öffnen. Was die einzelnen Einstellungen bewirken, steht unter [Inbox-Benachrichtigungen](notifications.md).

## Verwaltet und BYOK

Die Inbox funktioniert gleich, ob Ihr Arbeitsbereich verwaltet oder BYOK ist: Einträge werden von der Seite geschrieben, die das zugrunde liegende Ereignis tatsächlich erzeugt hat (die Cloud bei verwalteten Workflows, der lokale Desktop-Prozess bei BYOK), und Sie sehen in beiden Fällen eine einheitliche Liste.
