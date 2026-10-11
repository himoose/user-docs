---
source_hash: 5b66e35e4cc4b5ac9c7567edd481631bcbd56d2ff1ca7f0d3e2f1b0c1fbbd5c3
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/integrations/hi-moose-mcp/)

# Hi, Moose MCP

## Wofür das gut ist

Mit Hi, Moose MCP können die KI-Apps, in denen Sie schon arbeiten, Hi, Moose nutzen. Fügen Sie es als MCP-Connector in Claude, ChatGPT oder jeder anderen App hinzu, die MCP mit Anmeldung unterstützt, melden Sie sich mit Ihrem Hi, Moose-Konto an und fordern Sie Hi, Moose-Arbeit direkt aus dieser App an. MCP (Model Context Protocol) ist der Standard, über den diese Apps externe Werkzeuge anbinden.

Die Arbeit läuft auf einem Ihrer eigenen Geräte, dem **Host-Gerät**, auf dem Hi, Moose geöffnet und angemeldet bleibt. Ergebnisse gehen an die App zurück und werden in Ihrer [Library](../library/overview.md) gespeichert.

## Was eine verbundene App kann

Mit den aktuellen Werkzeugen kann eine verbundene App:

- Ihre Hi, Moose-Projekte auflisten
- Die in Ihrer Library gespeicherten Briefings und Entwürfe auflisten
- Prüfen, ob Ihre Website ein Thema schon abdeckt, mit den passenden Seiten und dem Datum des geprüften Crawls
- Ein Content-Briefing erstellen
- Einen Entwurf aus einem Briefing schreiben
- Ein Beitragsbild erstellen
- FAQs mit FAQPage-Schema für einen gespeicherten Entwurf oder eine Seite Ihrer Website schreiben
- Kernaussagen für einen gespeicherten Entwurf oder eine Seite Ihrer Website schreiben
- Ein AEO-Audit für eine Live-Seite, einen gespeicherten Entwurf oder eingefügten Text ausführen, mit Bewertungen, Problemen und Korrekturvorschlägen
- Fertige Arbeit abholen

Sie kann keine Einstellungen oder Teammitglieder ändern und nichts löschen. Weitere Werkzeuge folgen.

## Bevor Sie beginnen

1. Öffnen Sie Hi, Moose auf dem Gerät, das die Arbeit ausführen soll, und melden Sie sich an.
2. Gehen Sie zu **Einstellungen → Hi, Moose MCP** und wählen Sie dieses Gerät als Host-Gerät für das Projekt. Nur der Kontoinhaber kann das Host-Gerät wählen.
3. Kopieren Sie die dort angezeigte Serveradresse:

```
https://mcp.himoose.com/mcp
```

## In Claude verbinden

In Claude.ai und der Claude-Desktop-App:

1. Öffnen Sie **Einstellungen → Connectors** (auch erreichbar unter claude.ai/customize/connectors).
2. Wählen Sie **Benutzerdefinierten Connector hinzufügen**, fügen Sie die Serveradresse ein und klicken Sie auf **Hinzufügen**. Die OAuth-Client-Felder bleiben leer.
3. Klicken Sie neben Hi, Moose MCP auf **Verbinden**. Eine Hi, Moose-Seite öffnet sich, zeigt, was die App können wird, und bittet Sie, sich mit Ihrem Hi, Moose-Konto anzumelden.
4. Starten Sie einen neuen Chat und fragen Sie zum Beispiel: „Liste meine Hi, Moose-Projekte auf“.

In Team- und Enterprise-Plänen fügt zuerst ein Owner den Connector für die Organisation hinzu, danach verbindet sich jedes Mitglied einzeln.

In Claude Code:

```
claude mcp add --transport http himoose https://mcp.himoose.com/mcp
```

Führen Sie dann in Claude Code `/mcp` aus und folgen Sie der Anmeldung.

## In ChatGPT verbinden

ChatGPT unterstützt eigene MCP-Server in den Bezahlplänen. Die Menünamen ändern sich gelegentlich; das ist der aktuelle Weg.

1. Öffnen Sie **Einstellungen → Apps** (in manchen Versionen **Connectors**). In Business- und Enterprise-Workspaces muss ein Owner eigene Connectors eventuell zuerst erlauben.
2. Wählen Sie **Hinzufügen** und dann **Eigenen MCP-Server erstellen**. Ältere Versionen zeigen stattdessen **MCP-App erstellen** und brauchen vorher eventuell den **Entwicklermodus** in den erweiterten Einstellungen.
3. Fügen Sie die Serveradresse ein, wählen Sie **OAuth** als Authentifizierung und speichern Sie.
4. Melden Sie sich auf der Seite, die sich öffnet, mit Ihrem Hi, Moose-Konto an.
5. Schalten Sie den Connector in einem Chat für dieses Gespräch ein und fordern Sie Hi, Moose-Arbeit an.

## Andere Apps

Jede App, die einen entfernten MCP-Server mit OAuth-Anmeldung hinzufügen kann, funktioniert genauso: Serveradresse hinzufügen, mit dem Hi, Moose-Konto anmelden, loslegen.

## So läuft eine Anfrage

1. Die App schickt Ihre Anfrage an Hi, Moose MCP.
2. Hi, Moose MCP übergibt sie an das Host-Gerät, das die Arbeit mit dem Crawl, Brand Truth und der Recherche des Projekts ausführt.
3. Das Ergebnis geht an die App zurück und wird in Ihrer Library gespeichert.

Ein Briefing, ein Entwurf, ein Bild, ein FAQ-Satz oder eine Liste von Kernaussagen dauert ein bis drei Minuten, ein AEO-Audit zwei bis vier. Sagt die App, die Arbeit laufe noch, bitten Sie sie, erneut nachzusehen; sie holt das Ergebnis ab, sobald es fertig ist. Ist das Host-Gerät aus oder abgemeldet, erhält die App eine entsprechende Meldung.

Aufträge laufen unter dem Konto, das auf dem Host-Gerät angemeldet ist. Die Library, die sie lesen und beschreiben, ist also die Library dieses Kontos. Die Tabelle **Letzte Agenten-Aufträge** in den Einstellungen zeigt, was angefragt wurde, von welcher App, und ob es fertig wurde.

## Eine App trennen

Gehen Sie zu **Einstellungen → Hi, Moose MCP**. Die Tabelle **Verbundene Apps** listet jede App, die bei Ihrem Konto angemeldet ist. **Zugriff entziehen** meldet diese App ab. Das kann bis zu einer Minute dauern, und die App kann sich später wieder verbinden. Der Zugriff läuft außerdem nach 30 Tagen ohne Nutzung von selbst ab.
