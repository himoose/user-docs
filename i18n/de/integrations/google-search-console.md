---
source_hash: 07b1b5e8bf746dc48362fa004a86b7566ef960fafcbe265cebb6ecd32d7aff91
---
# Google Search Console

## Wofür das gut ist

Google Search Console verbinden, damit Hi, Moose Ihre eigenen Google-Suchdaten (Impressionen, Klicks und Suchanfragen) in dieselbe lokale Belegbasis holt, die auch [Visibility](../visibility/overview.md), die [AEO Audits](../features/aeo-audits.md) und die [Content Briefs](../features/content-briefs.md) nutzen.

!!! note "Verfügbarkeit"
    Die Verbindung zur Google Search Console ist in allen kostenpflichtigen Tarifen enthalten: BYOK Premium, BYOK Agency und allen verwalteten Tarifen. In BYOK Free und Preview Mode ist sie nicht enthalten. Siehe [Kontotypen und Tarife](../getting-started/account-modes.md).

## Warum das lokal bleibt

Der Zugriff auf die Search Console erfordert die OAuth-Zugangsdaten Ihres Google-Kontos, und Hi, Moose behandelt sie bewusst als sensibel: Die Autorisierung läuft in Ihrem Browser, und die daraus entstehenden Token werden **ausschließlich auf Ihrem Rechner** gespeichert. Die Cloud-Dienste von Hi, Moose erhalten für diese Verbindung niemals Ihre Google-Zugriffstoken, Aktualisierungstoken oder Client-Geheimnisse: Die Desktop-App ist das Einzige, was in Ihrem Auftrag mit der Google Search Console spricht.

## Eine Verbindung einrichten

1. Öffnen Sie **Verbindungen** in der Desktop-App und wählen Sie Google Search Console.
2. Erteilen Sie den Zugriff in Ihrem Browser.
3. Binden Sie eine Search-Console-Property an das aktive [Projekt](../getting-started/projects.md).

## Was Sie damit tun können

- Eine lokale Momentaufnahme der Seiten- und Anfrageleistung der gebundenen Property abrufen.
- Die jüngste Momentaufnahme mit einem früheren Zeitfenster vergleichen, um wesentliche Veränderungen zu erkennen.
- Ihre Search-Console-Daten direkt im Chat abfragen. Moose fragt sie agentisch ab und grenzt eine vage Frage über mehrere Abfragen ein, statt einen festen Bericht auszuführen. Das Modell versteht Ihre Frage, doch die Desktop-App prüft und führt jede zugrunde liegende Abfrage lokal aus, sodass Ihre Daten und die Hoheit über die Token auf dem Gerät bleiben.
- Search-Console-Belege in die Sichtbarkeitsdiagnose einfließen lassen und danach priorisieren, welche Seiten einen Content-Brief oder ein AEO Audit verdienen.

## Wo die Daten liegen

Search-Console-Daten, die in Hi, Moose einfließen, werden **lokal auf Ihrem Gerät** gespeichert, nicht in der Cloud von Hi, Moose. Sie sind Teil Ihrer lokalen Belegbasis und in einer [lokalen Sicherung](../getting-started/settings.md#data-backup) enthalten, statt zwischen Rechnern synchronisiert zu werden.

## Aktueller Umfang

Diese Verbindung ist in Version 1 schreibgeschützt: Hi, Moose schreibt nicht in die Search Console zurück. Derzeit lässt sich je Projekt eine Property binden.

Search Console setzt einen kostenpflichtigen Tarif voraus. In Preview Mode und BYOK Free ist sie nicht enthalten.

!!! note "Aktualisieren Sie die App, wenn die Verbindung unter Windows fehlschlägt"
    Windows-Installationsprogramme vor Version 0.3.245 wurden ohne die für die Verbindung nötigen Google-Zugangsdaten ausgeliefert, sodass das Verbinden in der installierten App stets fehlschlug. Ein Update behebt das.
