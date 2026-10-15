---
source_hash: 44a098b9f501f2117290c2037c5635c5aa9f250b49d72a34e103dba9d3cb8b5b
---

# Fehlerbehebung

Was tun, wenn Hi, Moose MCP nicht so antwortet, wie Sie erwarten. Die meisten Probleme hängen mit dem Host-Gerät zusammen: dem Computer, auf dem Hi, Moose geöffnet bleibt und die Arbeit ausführt.

## „Das Host-Gerät für dieses Projekt hat sich nicht gemeldet“

Der als Host-Gerät gewählte Computer ist aus, im Ruhezustand, offline, oder Hi, Moose ist dort geschlossen oder abgemeldet.

1. Öffnen Sie Hi, Moose auf diesem Computer und melden Sie sich an.
2. Warten Sie eine Minute und fragen Sie erneut. Der Host meldet sich alle paar Minuten, solange Hi, Moose geöffnet ist.
3. Ist der Computer dauerhaft weg, wählen Sie unter **Einstellungen → Hi, Moose MCP** einen anderen. Nur der Kontoinhaber kann das Host-Gerät ändern.

Aufträge warten bis zu 15 Minuten auf das Host-Gerät. Danach laufen sie ab und die App erhält eine entsprechende Meldung; fragen Sie erneut, sobald der Host zurück ist.

## „Dieses Projekt hat kein Host-Gerät“

Für das Projekt hat noch niemand ein Host-Gerät gewählt. Öffnen Sie Hi, Moose auf dem Computer, der die Arbeit ausführen soll, gehen Sie zu **Einstellungen → Hi, Moose MCP** und wählen Sie ihn. Jedes Projekt hat sein eigenes Host-Gerät, ein neues Projekt braucht also ebenfalls eines.

## Die App sagt, die Arbeit laufe noch

Briefings, Entwürfe, Audits und Audio dauern Minuten, und manche Apps hören auf zu warten, bevor die Arbeit fertig ist. Bitten Sie die App, erneut nachzusehen; sie holt das Ergebnis mit der Auftrags-ID ab, die sie erhalten hat. Die Arbeit wird auch in Ihrer [Library](../../library/overview.md) in Hi, Moose gespeichert, es geht also nichts verloren, wenn der Chat weitergeht.

Audio dauert am längsten: etwa 5 Minuten für eine kurze Episode, 9 für standard und 15 für ausführlich. Das Host-Gerät arbeitet währenddessen an nichts anderem, eine zweite Anfrage wartet also dahinter.

## Die App hat das falsche Projekt gewählt

Werkzeuge nehmen das Projekt nach Name. Nennen Sie ihn in der Anfrage, zum Beispiel „für das Projekt Acme“, oder bitten Sie die App, zuerst die Projekte aufzulisten und dann zu wählen. Haben zwei Projekte ähnliche Namen, verwenden Sie genau den, der in Hi, Moose angezeigt wird.

## Der Connector verbindet sich nicht

- **Die Anmeldeseite öffnet sich nie.** Prüfen Sie, ob die Serveradresse `https://mcp.himoose.com/mcp` lautet, ohne angehängte Zeichen, und ob die App OAuth verwendet, nicht einen API-Schlüssel.
- **Der Anmeldecode ist abgelaufen.** Der Code gilt zwei Minuten. Starten Sie die Verbindung aus der App erneut.
- **Claude Team oder Enterprise.** Ein Owner muss den Connector für die Organisation hinzufügen, bevor Mitglieder sich verbinden können.
- **ChatGPT.** Eigene MCP-Server brauchen einen Bezahlplan, und in Business- und Enterprise-Workspaces muss ein Owner eigene Connectors eventuell zuerst erlauben oder den Entwicklermodus einschalten. Menünamen ändern sich; siehe [In ChatGPT verbinden](../hi-moose-mcp.md#connect-in-chatgpt).

## Die App war verbunden und ist es jetzt nicht mehr

Der Zugriff läuft nach 30 Tagen ohne Nutzung von selbst ab, und der Kontoinhaber kann einer App unter **Einstellungen → Hi, Moose MCP** den Zugriff entziehen. Verbinden Sie sich aus der App erneut.

## Ergebnisse wirken veraltet

- **Site-Abdeckung und interne Links** lesen den letzten Crawl Ihrer Website und nennen sein Datum. Seiten, die seitdem veröffentlicht wurden, sind nicht enthalten. Starten Sie einen Crawl in Hi, Moose und fragen Sie erneut.
- **Sichtbarkeit und Chancen** lesen nur gespeicherte Ergebnisse und führen nie neue Prüfungen aus. Sie umfassen die verfolgten Prompts auf den verfolgten Engines über den in der Antwort genannten Zeitraum. Um ein neues Thema zu sehen, legen Sie auf dem Bildschirm Sichtbarkeit einen Prompt dafür an und lassen Sie einen Lauf stattfinden.

## Etwas ist gelaufen, das Sie nicht erwartet haben

Die Tabelle **Letzte Agenten-Aufträge** unter **Einstellungen → Hi, Moose MCP** listet jeden Auftrag: was angefragt wurde, von welcher App, wann, und ob er fertig wurde. Aufträge laufen unter dem Konto, das auf dem Host-Gerät angemeldet ist, eine verbundene App kann also nur die Library dieses Kontos lesen und beschreiben.

## Immer noch nicht weiter

Schreiben Sie dem Support mit dem Projektnamen, der verwendeten App, dem ungefähren Zeitpunkt und dem, was die App gesagt hat. Die Tabelle der Agenten-Aufträge hilft ebenfalls.
