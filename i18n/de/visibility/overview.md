---
source_hash: 1dc177bd9d47a042bd000ba0afbc51f44bad29916bc4af372cc495b526aa80e3
---
# Visibility

## Wofür das gut ist

Das Visibility-Dashboard zeigt, wie sich Ihre Marke in der KI-Suche tatsächlich schlägt: welche Anfragen Kundinnen und Kunden nutzen, um Sie zu finden, ob Ihre Marke in die engere Wahl kommt und ob KI-Maschinen sie zutreffend beschreiben. Es ist die zentrale Ansicht für die Schritte **überwachen** und **erkennen** des [zentralen Operator-Kreislaufs](../index.md#der-zentrale-operator-kreislauf).

Das Dashboard hat sieben Reiter:

| Reiter | Welche Frage er beantwortet |
|---|---|
| **Übersicht** | Wie stehe ich da? |
| **[Chancen](#chancen)** | Woran sollte ich arbeiten? |
| **[Wettbewerb](competitors.md)** | Wie stehe ich im Vergleich zu ihnen da? |
| **Erwähnungen** | Welche Marken werden in diesen Antworten genannt? |
| **Zitationen** | Auf welche Quellen stützen sich die Engines tatsächlich? |
| **Themen & Engines** | Wo genau bin ich stark oder schwach? |
| **Prompts** | Was ist bei jedem einzelnen Prompt passiert? |

## Kennzahlen

Jeder Lauf meldet für den gewählten Zeitraum einige Hauptkennzahlen:

- **Anteil der Erwähnungen**: wie oft Ihre Marke über die überwachten Prompts und Maschinen hinweg erwähnt wird.
- **Share of Citations**: wie oft Ihre Domain tatsächlich als Quelle zitiert wird.
- **Stimmung**: der durchschnittliche Ton (positiv, gemischt, neutral, negativ) der Erwähnungen.
- **Durchschnittliche Position**: wo Ihre Marke typischerweise landet, wenn sie in einer Liste oder Rangfolge auftaucht. Zeigt **Not enough data**, solange es zu wenige positionierte Erwähnungen für einen Durchschnitt gibt.
- **Narrativ-Abweichung**: ob KI-Antworten von Ihrer beabsichtigten Positionierung abweichen.
- **Feature-Parität**: ob KI-Antworten zutreffend wiedergeben, was Sie anbieten.

Narrative Drift und Feature Parity zeigen **Nicht bewertet** mit einem Einrichtungslink an, solange Sie Ihr Brand Truth Profile nicht ausgefüllt haben. Diese beiden Kennzahlen sind erst aussagekräftig, wenn Hi, Moose weiß, was über Ihre Marke zutrifft, um es vergleichen zu können. Siehe [Brand Truth Profile](../getting-started/context/brand-truth-profile.md).

!!! note "Fehlgeschlagene Beobachtungen werden ausgeschlossen, nicht als Abwesenheit gewertet"
    War eine Maschine nicht verfügbar oder eine Anfrage fehlgeschlagen, bleibt diese Beobachtung aus allen Kennzahlen heraus, statt als „Ihre Marke wurde nicht erwähnt" bewertet zu werden. Ein Lauf mit Verbindungsproblemen berichtet über weniger Beobachtungen, statt einen erfundenen Rückgang zu melden. Die Ansicht je Prompt kennzeichnet sie als **Antwort nicht verfügbar** und nennt die Anzahl der ausgeschlossenen Beobachtungen.

## Filter und Zeitraum

- Filtern Sie nach **Thema**, **KI-Engine**, **Prompt** (Mehrfachauswahl mit Suche), **Seite**, **Sentiment**, **Narrativ** oder **Feature-Parität**, oder setzen Sie alle Filter auf einmal zurück.
- Der Filter **Seite** grenzt auf bestimmte URLs ein und lässt sich nach Pfad durchsuchen. Er zeigt korrekt auch die Maschinen, in denen die URL **nicht** zitiert wurde: Sie sehen also ebenso, wo eine Seite fehlt, wie dort, wo sie auftaucht.
- Legen Sie unter **Zeitraum** einen Datumsbereich fest und klicken Sie auf **Anwenden**, oder klicken Sie auf **Vergleichen**, um einen früheren Zeitraum oder den vorherigen Lauf zu überlagern.

## Verlauf über die Zeit

Das Verlaufsdiagramm stellt **Erwähnungen**, **Citations**, **Positiv %** oder die durchschnittliche Position in Intervallen von **Tag**, **Woche** oder **Monat** dar, aufgeschlüsselt nach KI-Maschine oder mit **Alle Modelle** zusammengefasst, damit Sie erkennen, ob eine bestimmte Maschine die Zahlen bewegt.

## Detail je Prompt

Unter dem Diagramm:

- **Erwähnungsrate** schlüsselt die Ergebnisse nach Maschine auf und zeigt, welche Sie erwähnt haben und welche nicht.
- **Meistzitierte Seiten** zeigt, welche Ihrer URLs zitiert werden und von welchen Maschinen.
- **Aufschlüsselung auf Prompt-Ebene** klappt jeden überwachten Prompt auf, um die einzelnen Ergebnisse je Maschine zu sehen, einschließlich der vollständigen KI-Antwort und der Begründung zu Stimmung, Narrativ und Funktionsabdeckung.

Jeder Prompt enthält einen Link **im Chat untersuchen**, der die genauen Beobachtungsdaten an Moose übergibt und um eine Empfehlung bittet, ob der nächste Schritt ein [AEO Audit](../features/aeo-audits.md) einer bestehenden Seite oder ein neuer [Content-Brief mit Entwurf](../features/content-briefs.md) sein sollte.

## Der Reiter Übersicht

Die Übersicht beginnt mit einer geschriebenen Zusammenfassung des aktuellen Ausschnitts: einige Absätze, die sagen, wo Sie stehen, was sich bewegt hat und was einen Blick wert ist, in Sätzen statt in Zahlen. Sie entsteht aus demselben Datenblatt, das auch der Bericht nutzt, und mit **Zusammenfassung neu schreiben** lassen Sie sie neu formulieren. Ist kein Modell verfügbar, das sie schreiben kann, greift die Übersicht auf eine direkt aus den Zahlen gebaute Fassung zurück und sagt das auch.

Unter der Zusammenfassung stehen zwei Blöcke:

- **Wo Sie stehen**: Ihr Share of Voice, die Erwähnungsrate über die gelesenen Antworten, Zitationen, der durchschnittliche Rang, wenn Sie genannt werden, und die Erwähnungsrate je Engine, mit dem gesamten Feld der verfolgten Marken daneben.
- **Beschreibt die KI Sie zutreffend?**: Positionierungsabgleich, Tonaufschlüsselung und eine Liste **prüfenswerter Antworten**: die konkreten Antworten, in denen eine Engine eine Fähigkeit falsch dargestellt hat oder von Ihrer Positionierung abgewichen ist. Jede öffnet die Antwort oder springt im Reiter Prompts dorthin.

## Chancen

Der Reiter **Chancen** macht aus den verfolgten Ergebnissen eine priorisierte Arbeitsliste. Jede Zeile ist eine Sache, die zu beheben ist: eine einzeilige Überschrift, die betroffenen Prompts und KI-Engines, Ihr Anteil gegenüber dem stärksten Rivalen und eine Zeile **Nächster Schritt:**, die den ersten Schritt nennt.

Die Zeilen entstehen nur aus den Prompts, die Sie verfolgen, aus den zehn neuesten Läufen je Engine. Der Zeitraumfilter oben ändert die Liste nicht, und [stillgelegte Prompts](prompt-manager.md#einen-prompt-stilllegen) bleiben außen vor.

Jede Zeile trägt:

- **Eine Aktionsart.** **Abdeckung schaffen**, wenn keine Ihrer Seiten einen Prompt beantwortet, bei dem die Engines Sie nie nennen. **Eine Seite verbessern**, wenn Ihre Seite existiert, aber verliert. **Aufnahme erreichen**, wenn eine von den Engines zitierte Drittseite Sie aufführen könnte. **Die Beschreibung korrigieren**, wenn eine Antwort Ihrem Brand Truth Profile widerspricht. **Eine Veränderung untersuchen**, wenn eine Engine aufgehört hat, Sie zu nennen oder zu zitieren. **Den Vorsprung halten**, wenn Sie vorn liegen und das bleiben sollten.
- **Eine Priorität.** Hoch, Mittel oder Niedrig, abhängig davon, wie viele Prompt-und-Engine-Paare die Lücke betrifft, wie beständig sie über die Läufe bestand, ob ein verfolgter Wettbewerber vor Ihnen liegt und ob die Lösung auf einer Seite liegt, die Sie kontrollieren.
- **Eine Verlässlichkeit.** Belastbar, Richtungsweisend oder Prüfung nötig, abhängig davon, in wie vielen Läufen die Lücke zu sehen war und wie oft sie zwischen Läufen gekippt ist.
- **Einen Aufwand.** Klein, Mittel oder Groß, von neuem Inhalt, der zu recherchieren und zu schreiben ist, bis zu einer einzeiligen Änderung in Ihrem Brand Truth Profile.

Klicken Sie auf eine Zeile, um sie zu öffnen. Das Detail zeigt, was passiert, welche Schritte zu tun sind und welche Belege hinter der Zeile stehen: das Raster aus Prompts und Engines mit den Stellen, an denen Sie fehlten, genannt oder zitiert wurden, die markierten Antworten, die Wettbewerber vor Ihnen, die konkurrierenden Seiten, die die Engines zitieren, Ihre eigene passende Seite mit einem etwaigen früheren Audit und was sich gegenüber dem vorherigen Zeitraum geändert hat.

Aus dem Detail starten Sie die Arbeit: **Brief erstellen**, **Seite prüfen**, **Pitch entwerfen** an die Website, die Sie aufnehmen könnte, **Brand Truth aktualisieren**, **Korrekturanfrage entwerfen** oder **Antworten prüfen**. Brief und Audit öffnen sich mit den Prompts und Seiten der Zeile bereits ausgefüllt, und das Ergebnis wird mit der Zeile verknüpft, deren Status auf **Brief fertig**, **Entwurf fertig** oder **Audit fertig** wechselt.

Zeilen haben einen Status. **Als erledigt markieren**, **Verwerfen** oder **Zurückstellen** um eine Anzahl Tage, **Zuweisen** an ein Teammitglied und **Notiz hinzufügen** gibt es in jeder Zeile. Eine geschlossene Zeile ist ausgeblendet, bis Sie geschlossene Zeilen einblenden, und sie kommt als **Durch neue Belege wieder geöffnet** zurück, wenn spätere Läufe die Lücke erneut zeigen. Filtern Sie die Liste nach Aktion, Priorität, Verlässlichkeit, Status, Engine oder Thema, und nutzen Sie **Nach Excel exportieren** für die gesamte Liste mit den Belegspalten.

Eine verbundene MCP-App erhält dieselbe Liste in derselben Reihenfolge über [visibility_list_opportunities](../integrations/hi-moose-mcp/tools.md#visibility_list_opportunities).

## Erwähnungen

Der Reiter **Erwähnungen** ist die vollständige Liste jeder Marke, jedes Produkts und jeder Website, die die Engines in den Antworten des aktuellen Ausschnitts genannt haben - nicht nur Sie und Ihre verfolgten Wettbewerber, sondern alle, die aufgetaucht sind.

Jede Zeile zeigt, in wie vielen Antworten die Marke genannt wurde, das als Prozentsatz der Antworten im Ausschnitt, ihren Anteil an allen Erwähnungen, ihren durchschnittlichen Rang unter den in einer Antwort genannten Marken und ihr häufigstes Sentiment-Urteil. Fahren Sie über einen Sentiment-Wert für die Aufschlüsselung positiv/gemischt/neutral/negativ und über eine Spaltenüberschrift für ihre genaue Definition.

Über der Tabelle zeichnet ein **Verlauf der Erwähnungspräsenz** die meistgenannten Marken und Sie über die Zeit.

Hier finden Sie die Wettbewerber, von denen Sie nichts wussten. Marken werden vom Scoring-Modell aus dem Antworttext gelesen, die Liste bringt also Namen zum Vorschein, die Sie nie in Ihr Tracking aufgenommen haben.

## Zitationen

Der Reiter **Zitationen** ist dieselbe Idee für Quellen: jede Domain und jede Seite, die die Engines im aktuellen Ausschnitt zitiert haben.

Wechseln Sie zwischen **Nach Domain** und **Nach Seiten-URL**, und filtern Sie auf **Alle** oder **Weder Sie noch ein Wettbewerber**, um die Drittquellen zu sehen, die die Antworten prägen. Jede Quelle ist kategorisiert: Ihre Marke, Wettbewerber, Social, Bewertungsseite, Publikation, Nachschlagewerk, Entwickler oder Sonstiges.

Die Spalten sind:

| Spalte | Was sie bedeutet |
|---|---|
| **Zitierte Prompts** | In wie vielen Antworten diese Domain oder URL zitiert wurde |
| **Präsenz %** | Das als Anteil an den Antworten im Ausschnitt |
| **Anzahl Zitationen** | Wie oft insgesamt zitiert, Wiederholungen mitgezählt |
| **Sichtbarkeit %** | Ihr Anteil an allen Zitationen im Ausschnitt |
| **Durchschn. Rang** | Ihre durchschnittliche Position in den Zitationslisten der Engines |
| **Veränderung** | Bewegung gegenüber dem Vergleichszeitraum oder dem vorherigen Lauf |

**Details** in einer Zeile listet die dahinterliegenden Seiten und die Prompts, für die jede Seite zitiert wurde. Jede Domain in der Tabelle lässt sich mit **Als Wettbewerber verfolgen** direkt zu Ihren verfolgten Wettbewerbern hinzufügen, sodass ein hier entdeckter Name ohne erneutes Tippen in den [Share of Voice](competitors.md) einfließt.

Beide Tabellen lassen sich als CSV herunterladen.

!!! note "Engines, die nicht im Web nachsehen, liefern keine Zitationen"
    Zitationen stammen von Engines, die beim Antworten das Web abrufen. Ein lokales Modell oder eine Engine, die allein aus ihrem Training antwortet, liefert keine - eine leere Tabelle unter einem engen Filter bedeutet also nicht zwangsläufig ein Problem mit Ihrer Website.

## Topics & Engines

Dieser Reiter schlüsselt die Leistung auf zwei Arten auf:

- **Erwähnungsrate nach Thema**: wie oft jede Marke in den KI-Antworten zu jedem Thema auftaucht.
- **Verlauf der Erwähnungsrate nach Thema**: dasselbe, aufgeschlüsselt über die Zeit.
- **Erwähnungsrate nach Plattform**: eine Heatmap, wie oft jede Marke im Zeitraum in den Antworten jeder Plattform auftaucht.

Die Themen stammen aus Ihren Prompt-Kategorien. Sind Ihre Prompts nicht kategorisiert, fordert dieser Reiter Sie auf, sie im [Prompt Manager](prompt-manager.md) zu ordnen, statt ein leeres Diagramm anzuzeigen.

## Exportieren

**Exportieren** bietet zwei Formate:

- **CSV-Tabelle**: alle Ergebnisse der aktuellen Ansicht, für Excel oder Google Sheets.
- **PDF-Managementbericht**: ein vollständiger Bericht in dreizehn Abschnitten zur aktuellen Ansicht, geschrieben, um ihn jemandem zu geben, der nicht im Raum war.

Der Bericht beginnt mit einer geschriebenen Darstellung statt einer Diagrammflut und arbeitet dann durch: wo Sie stehen, ob die KI Sie zutreffend beschreibt, die Bewegung im Zeitraum, Engine für Engine, wo die KI Sie zitiert, Fragen, die Wettbewerber gewinnen, wofür Wettbewerber zitiert werden, das gesamte Feld, in KI-Antworten genannte Marken, von der KI zitierte Domains, Erwähnungsrate je Engine, Erwähnungsrate je Thema und einen Schlussabschnitt, der erklärt, wie jede Kennzahl zu lesen ist.

Exporte berücksichtigen Ihre aktiven Filter, und das Deckblatt des PDF nennt die angewendeten Filter, damit ein Bericht nicht mit einem Gesamtbild des Kontos verwechselt werden kann. In kostenpflichtigen Tarifen trägt das PDF Ihr [White-Label-Branding](../agency/white-label.md), sofern Sie es eingerichtet haben.

## Sichtbarkeitsprüfungen ausführen

Klicken Sie auf **Jetzt ausführen** für eine Prüfung auf Abruf. Das Verhalten hängt von Ihrem [Tarif](../getting-started/account-modes.md) ab:

- **Preview Mode** führt lokale Abfragen direkt von Ihrem Gerät gegen die öffentlichen KI-Suchoberflächen aus. Hi, Moose bittet Sie zuvor um Bestätigung, denn Prüfungen in schneller Folge können dort vorübergehende Sperren wegen Anfragelimits auslösen. Die Bewertung von Stimmung, Narrativ und Abdeckung benötigt ein aktiviertes lokales Gemma-4-Modell; ohne dieses werden diese Prüfungen übersprungen.
- **BYOK-Tarife** laufen lokal mit Ihrem eigenen OpenRouter-Schlüssel.
- **Verwaltete Tarife** laufen über die Infrastruktur von Hi, Moose. Reicht das Kontingent Ihres Arbeitsbereichs in diesem Monat für den aktuellen Zeitplan nicht aus, pausieren geplante Läufe, bis Sie den Tarif wechseln, Ihre [Laufhäufigkeit](settings.md#zeitplan-fur-laufe) anpassen oder sich das Kontingent zurücksetzt. Hi, Moose nennt Ihnen, wie viele Einheiten nötig sind und wie viele verbleiben.

Sie können einen Lauf vorzeitig beenden, und Läufe, die von einem App-Update unterbrochen werden, setzen fort, statt verloren zu gehen.

## Wie viel Historie aufbewahrt wird

Jede Beobachtung, die ein Lauf erzeugt, wird lokal archiviert, damit Verläufe, Vergleiche und die Tabellen Erwähnungen und Zitationen weiter zurückblicken können als nur auf die letzten Läufe. Das Archiv hält bis zu **400 Tage** je Arbeitsbereich und bis zu 200.000 Beobachtungen; jenseits einer der beiden Grenzen fallen die ältesten Zeilen weg.

In kostenpflichtigen verwalteten Tarifen synchronisieren auch Sichtbarkeitsläufe, die auf Ihrem Rechner laufen, ihre Ergebnisse in die Cloud, sodass Teammitglieder dieselbe Historie sehen wie Sie und nicht nur die Läufe, die auf ihrem eigenen Gerät stattgefunden haben.

## Wie es weitergeht

- **[Wettbewerber und Share of Voice](competitors.md)**: Wettbewerbsposition, Wettbewerberzitierungen und Lücken.
- **[Prompt Manager](prompt-manager.md)**: die überwachten Prompts hinzufügen, ordnen und kategorisieren.
- **[Visibility-Einstellungen](settings.md)**: Zeitplan für Läufe, Bewertungsmodell, Wettbewerberverfolgung, sekundäre Markenbegriffe und Domains sowie Standardmodelle.
