---
source_hash: f262de43811a037ebe40f0f411828409a4bc1eda0f592f12d08358e5530d41e6
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/integrations/hi-moose-mcp/security/)


# Sicherheit und Datenverarbeitung

Diese Seite richtet sich an die Personen, die einen Connector prüfen, bevor ein Team ihn verbindet. Sie beschreibt, wie Hi, Moose MCP heute arbeitet, in der Reihenfolge, in der eine Sicherheitsprüfung üblicherweise fragt. Zuletzt am 2026-10-19 gegen den laufenden Server geprüft.

## Kurze Antworten

| Frage | Antwort |
|---|---|
| Wer betreibt den Server? | Hi, Moose, der Hersteller der App. Kein Dritter. |
| Kann sich die Werkzeugliste nach dem Verbinden ändern? | Nein. Werkzeuge sind fester Code. Die genaue Liste ist mit einem Hash unter [mcp.himoose.com/tools.json](https://mcp.himoose.com/tools.json) veröffentlicht. |
| Wie melden sich Personen an? | OAuth 2.1, der Standardablauf für Remote-MCP, mit ihrem bestehenden Hi, Moose-Konto. Keine API-Schlüssel. |
| Wie lange gelten Tokens? | Zugriffstokens eine Stunde. Refresh-Tokens laufen nach 30 Tagen ohne Nutzung ab, höchstens nach 90 Tagen. |
| Können wir den Zugriff entziehen? | Ja, pro App, in Hi, Moose unter **Einstellungen → Hi, Moose MCP**. |
| Was kann eine verbundene App ändern? | Inhaltsarbeit und Lesezugriffe innerhalb der Projekte des angemeldeten Kontos. Sie kann nicht veröffentlichen, nichts löschen und weder Einstellungen noch Teammitglieder noch das Tracking ändern. |
| Erreicht sie etwas außerhalb von Hi, Moose? | Nein. Sie sieht nie die Chats, Dateien, Repositories oder anderen Connectors der App, aus der sie genutzt wird. |
| Wo läuft die Arbeit? | In der Hi, Moose-App auf einem Gerät Ihrer Wahl, dem Host-Gerät. |
| Wird fremder Text in Ergebnissen markiert? | Ja. Seitenpassagen und Antworten von KI-Suchmaschinen kommen zwischen Markierungen zurück, die sie als Daten kennzeichnen, nicht als Anweisungen. |
| Wo melden wir ein Problem? | [legal@himoose.com](mailto:legal@himoose.com) oder die [Kontaktseite](https://himoose.com/de/contact/). |

## Wer den Server betreibt

Hi, Moose MCP wird von Hi, Moose gebaut und betrieben. Es ist der einzige MCP-Server, der ein Hi, Moose-Konto erreicht, und kein Community- oder Drittanbieter-Server. Die Serveradresse lautet:

```text
https://mcp.himoose.com/mcp
```

Der Server selbst ist klein. Er übernimmt Anmeldung und Tokens, bietet die Werkzeugliste an und reicht jede Anfrage an die Cloud von Hi, Moose weiter, die sie an das Host-Gerät übergibt. Die Arbeit, etwa den Site-Crawl lesen oder ein Briefing schreiben, läuft in der Hi, Moose-App auf diesem Gerät, genauso wie wenn jemand in der App auf den Knopf klickt.

## Die Werkzeugliste ist veröffentlicht und ändert sich nicht

Ein MCP-Server kann grundsätzlich seine Werkzeugbeschreibungen ändern, nachdem Sie sich verbunden haben, oder darin Anweisungen für den KI-Agenten verstecken. OWASP nennt das Tool Poisoning.

Die Werkzeuge von Hi, Moose MCP sind fester Code im Server. Namen, Beschreibungen und Eingabeschemata ändern sich zwischen Aufrufen nicht, und es werden nie Nutzerinhalte hineingeschrieben. Ein neues Werkzeug bedeutet eine neue Serverversion.

Die genaue Liste, die der Server ausliefert, ist veröffentlicht unter:

```text
https://mcp.himoose.com/tools.json
```

Sie enthält die Serverversion, das Datum der letzten Änderung der Werkzeugliste, die Anzahl der Werkzeuge, den vollständigen Text jedes Werkzeugs, den Anweisungstext, den der Server dem Agenten gibt, und einen SHA-256-Hash. Der Hash deckt das kompakte JSON der Felder `instructions` und `tools` ab, Sie können ihn also aus der Datei neu berechnen oder mit dem vergleichen, was Ihr MCP-Client erhalten hat. Halten Sie den Hash in Ihren Prüfnotizen fest und vergleichen Sie ihn regelmäßig. Derselbe Hash ist der `ETag`-Header der Datei.

Bevor sich jemand anmeldet, zeigt die Einwilligungsseite dieselbe Werkzeugliste in einfachen Worten, unter „Diese App wird können“ und „Sie wird nicht können“.

## Anmeldung und Tokens

Jeder Client durchläuft denselben Ablauf: Claude im Web, die Claude-Desktop-App, Claude Code, ChatGPT und jede andere MCP-App. Es gibt keine Abkürzung, kein geteiltes Token und keinen API-Schlüssel.

- OAuth 2.1, wie es die aktuelle MCP-Autorisierungsspezifikation beschreibt: Protected Resource Metadata (RFC 9728) mit einer `WWW-Authenticate`-Aufforderung, Authorization Server Metadata (RFC 8414), PKCE für jeden Client verpflichtend, Resource Indicators (RFC 8707), damit ein Token für diesen Server nicht anderswo wiederverwendet werden kann, Dynamic Client Registration (RFC 7591) und Client ID Metadata Documents sowie Token-Widerruf (RFC 7009).
- Die Anmeldung erfolgt auf `console.himoose.com` mit dem bestehenden Hi, Moose-Konto der Person, per E-Mail und Passwort oder mit Google. Die MCP-App sieht das Passwort nie. Hi, Moose MCP erfährt nur Konto-ID und E-Mail und welche Projekte das Konto sehen kann.
- Die Einwilligungsseite nennt die App, die anfragt. Wenn die App ihre Identität veröffentlicht, zeigt die Seite ihre Herausgeber-Domain. Wenn nicht, steht dort „Name nicht verifiziert“.
- Zugriffstokens gelten eine Stunde. Refresh-Tokens gelten höchstens 90 Tage und laufen nach 30 Tagen ohne Nutzung ab. Tokens, Codes und Geheimnisse werden nur als Hashes gespeichert.
- Eine Verbindung gehört einer Person. Teammitglieder verbinden sich mit ihren eigenen Konten.

Um eine App zu trennen, öffnen Sie Hi, Moose und gehen zu **Einstellungen → Hi, Moose MCP**. Die Tabelle **Verbundene Apps** listet jede im Konto angemeldete App mit Herausgeber-Domain und Verbindungszeitpunkt. **Zugriff entziehen** meldet diese App innerhalb einer Minute ab. Die App kann sich nur über eine erneute Anmeldung wieder verbinden.

## Was eine verbundene App kann und nicht kann

Alles, was eine verbundene App kann, steht in der [Einrichtungsanleitung](../hi-moose-mcp.md) und wird in der [Werkzeug-Referenz](tools.md) Werkzeug für Werkzeug beschrieben. Es ist Inhalts- und Recherchearbeit innerhalb der Projekte des Kontos: Briefings, Entwürfe, Bilder, FAQs, Kernaussagen, AEO-Audits, Pläne für interne Links, Audio-Episoden, Abdeckungsprüfungen und Lesezugriffe auf gespeicherte KI-Suchergebnisse.

Sie kann nicht:

- Auf einer Website veröffentlichen oder dort etwas ändern
- Etwas löschen
- Einstellungen, Teammitglieder, Abrechnung oder das Host-Gerät ändern
- Ändern, was Hi, Moose verfolgt, oder einen Sichtbarkeitslauf starten
- Ein anderes Konto erreichen als das angemeldete
- Irgendetwas in der App erreichen, aus der sie genutzt wird: keine Chats, Dateien, Repositories, kein Gedächtnis, keine anderen Connectors

Jede Anfrage nennt ein Projekt. Bevor Arbeit beginnt, prüft Hi, Moose, dass das angemeldete Konto Zugriff auf dieses Projekt hat. Eine Anfrage für ein Projekt, das das Konto nicht sehen kann, schlägt sofort fehl.

## Wo die Arbeit läuft und welche Daten sich bewegen

Hi, Moose MCP hat nie eine Kopie des Site-Crawls, des Brand-Truth-Profils oder der Library. Diese liegen in der Hi, Moose-App auf dem Host-Gerät, dem einen Computer oder Server, den Sie in den Einstellungen wählen. Der Host führt jeden Auftrag so aus, wie die App ihn über einen Knopf ausführt.

So verläuft eine Anfrage:

1. Die MCP-App sendet den Werkzeugnamen und die Eingabe an den Server.
2. Der Server prüft das Token und bittet die Cloud von Hi, Moose, einen Auftragsdatensatz für das Projekt anzulegen. Die Cloud prüft den Projektzugriff und schreibt den Datensatz.
3. Das Host-Gerät, das Aufträge für seine Projekte beobachtet, nimmt den Auftrag auf und führt ihn aus.
4. Der Host schreibt das Ergebnis in den Auftragsdatensatz und speichert es in der Library. Der Server gibt das Ergebnis an die MCP-App zurück.

Was das für Ihre Daten bedeutet:

- Anfrage und Ergebnis laufen als Auftragsdatensatz durch die Cloud von Hi, Moose (Google Cloud, Region USA). Der Datensatz bleibt beim Projekt, damit die Tabelle **Letzte Agenten-Aufträge** in den Einstellungen zeigen kann, was angefragt wurde, von welcher App und welchem Konto, und ob es abgeschlossen ist.
- Erzeugte Bilder werden im Hi, Moose-Cloud-Speicher des Kontos abgelegt und als Link zurückgegeben.
- Modellaufrufe nutzen denselben Weg wie die App: die verwalteten Modelle Ihres Tarifs, Ihre eigenen Modellschlüssel, falls Sie welche hinterlegt haben, oder ein lokales Modell, falls Sie eines betreiben. Eine MCP-App zu verbinden ändert nicht, welche Modelle Ihre Inhalte sehen.
- Die eigenen Protokolle des Servers halten den Werkzeugnamen, die Dauer des Aufrufs und ob der Client gestreamt hat. Sie halten nie die Eingabe oder das Ergebnis fest.

## Fremder Text in Ergebnissen

Manche Ergebnisse enthalten Text, den Hi, Moose nicht geschrieben hat: Passagen von Seiten Ihrer Website, aus einer Seite zitierten Ankertext, kurze Auszüge dessen, was eine KI-Suchmaschine geantwortet hat, oder den vollständigen Text einer gespeicherten Antwort. Solcher Text könnte Anweisungen enthalten, die sich an einen KI-Agenten richten. OWASP nennt das indirekte Prompt-Injection.

Jedes Ergebnis mit fremdem Text markiert ihn. Der Text kommt zwischen einer Start- und einer Endmarkierung zurück, davor eine Zeile, die die Herkunft nennt und festhält, dass alles zwischen den Markierungen Daten sind, keine Anweisungen. Die strukturierte Form desselben Ergebnisses trägt ein Feld `dataNotice`, das dasselbe sagt. Das gilt für `check_site_coverage`, `run_aeo_audit`, `find_internal_links`, `visibility_check_topic`, `visibility_get_answer` und `visibility_list_opportunities`.

Briefings, Entwürfe, FAQs, Kernaussagen und Audio-Skripte schreibt Hi, Moose für Sie. Die Recherche dahinter wird auf dem Host-Gerät gelesen und nicht an den Agenten durchgereicht.

Markierungen helfen einem Agenten, den Text als Daten zu behandeln. Sie machen einen Agenten nicht immun gegen Anweisungen in Inhalten, die er liest, und kein Werkzeuganbieter kann das versprechen. Halten Sie die Berechtigungen des Agenten, den Sie verbinden, so eng, wie seine Aufgabe es verlangt, wie bei jedem anderen Connector.

## Ein Sicherheitsproblem melden

Schreiben Sie an [legal@himoose.com](mailto:legal@himoose.com) oder nutzen Sie die [Kontaktseite](https://himoose.com/de/contact/). Sagen Sie uns, was Sie gefunden haben und wie es sich nachstellen lässt. Wir beantworten jede Meldung und sagen Ihnen, was wir geändert haben.
