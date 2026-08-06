---
source_hash: 40b089c8c06f81c797410e131c0f51ee08f0beba3baaaf1ad18b0794a101df1a
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/visibility/overview/)

# Visibility

## Wofür das gut ist

Das Visibility-Dashboard zeigt, wie sich Ihre Marke in der KI-Suche tatsächlich schlägt: welche Anfragen Kundinnen und Kunden nutzen, um Sie zu finden, ob Ihre Marke in die engere Wahl kommt und ob KI-Maschinen sie zutreffend beschreiben. Es ist die zentrale Ansicht für die Schritte **überwachen** und **erkennen** des [zentralen Operator-Kreislaufs](../index.md#der-zentrale-operator-kreislauf).

Das Dashboard hat drei Reiter:

| Reiter | Welche Frage er beantwortet |
|---|---|
| **Overview** | Wie stehe ich da? |
| **[Competition](competitors.md)** | Wie stehe ich im Vergleich zu ihnen da? |
| **Topics & Engines** | Wo genau bin ich stark oder schwach? |

## Kennzahlen

Jeder Lauf meldet für den gewählten Zeitraum einige Hauptkennzahlen:

- **Share of Mentions**: wie oft Ihre Marke über die überwachten Prompts und Maschinen hinweg erwähnt wird.
- **Share of Citations**: wie oft Ihre Domain tatsächlich als Quelle zitiert wird.
- **Stimmung**: der durchschnittliche Ton (positiv, gemischt, neutral, negativ) der Erwähnungen.
- **Durchschnittliche Position**: wo Ihre Marke typischerweise landet, wenn sie in einer Liste oder Rangfolge auftaucht. Zeigt **Not enough data**, solange es zu wenige positionierte Erwähnungen für einen Durchschnitt gibt.
- **Narrative Drift**: ob KI-Antworten von Ihrer beabsichtigten Positionierung abweichen.
- **Feature Parity**: ob KI-Antworten zutreffend wiedergeben, was Sie anbieten.

Narrative Drift und Feature Parity zeigen **Not scored** mit einem Einrichtungslink an, solange Sie Ihr Brand Truth Profile nicht ausgefüllt haben. Diese beiden Kennzahlen sind erst aussagekräftig, wenn Hi, Moose weiß, was über Ihre Marke zutrifft, um es vergleichen zu können. Siehe [Brand Truth Profile](../getting-started/context/brand-truth-profile.md).

!!! note "Fehlgeschlagene Beobachtungen werden ausgeschlossen, nicht als Abwesenheit gewertet"
    War eine Maschine nicht verfügbar oder eine Anfrage fehlgeschlagen, bleibt diese Beobachtung aus allen Kennzahlen heraus, statt als „Ihre Marke wurde nicht erwähnt" bewertet zu werden. Ein Lauf mit Verbindungsproblemen berichtet über weniger Beobachtungen, statt einen erfundenen Rückgang zu melden. Die Ansicht je Prompt kennzeichnet sie als **Response unavailable** und nennt die Anzahl der ausgeschlossenen Beobachtungen.

## Filter und Zeitraum

- Filtern Sie nach **Topic**, **AI Engine**, **Prompt** (Mehrfachauswahl mit Suche), **Page**, **Sentiment**, **Narrative** oder **Feature Parity**, oder setzen Sie alle Filter auf einmal zurück.
- Der Filter **Page** grenzt auf bestimmte URLs ein und lässt sich nach Pfad durchsuchen. Er zeigt korrekt auch die Maschinen, in denen die URL **nicht** zitiert wurde: Sie sehen also ebenso, wo eine Seite fehlt, wie dort, wo sie auftaucht.
- Legen Sie unter **Period** einen Datumsbereich fest und klicken Sie auf **Apply**, oder klicken Sie auf **Compare**, um einen früheren Zeitraum oder den vorherigen Lauf zu überlagern.

## Verlauf über die Zeit

Das Verlaufsdiagramm stellt **Mentions**, **Citations**, **Positive %** oder die durchschnittliche Position in Intervallen von **Tag**, **Woche** oder **Monat** dar, aufgeschlüsselt nach KI-Maschine oder mit **All models** zusammengefasst, damit Sie erkennen, ob eine bestimmte Maschine die Zahlen bewegt.

## Detail je Prompt

Unter dem Diagramm:

- **Mention Rate** schlüsselt die Ergebnisse nach Maschine auf und zeigt, welche Sie erwähnt haben und welche nicht.
- **Top Cited Pages** zeigt, welche Ihrer URLs zitiert werden und von welchen Maschinen.
- **Prompt-Level Breakdown** klappt jeden überwachten Prompt auf, um die einzelnen Ergebnisse je Maschine zu sehen, einschließlich der vollständigen KI-Antwort und der Begründung zu Stimmung, Narrativ und Funktionsabdeckung.

Jeder Prompt enthält einen Link **im Chat untersuchen**, der die genauen Beobachtungsdaten an Moose übergibt und um eine Empfehlung bittet, ob der nächste Schritt ein [AEO Audit](../features/aeo-audits.md) einer bestehenden Seite oder ein neuer [Content-Brief mit Entwurf](../features/content-briefs.md) sein sollte.

## Topics & Engines

Dieser Reiter schlüsselt die Leistung auf zwei Arten auf:

- **Mention Rate by Topic**: wie oft jede Marke in den KI-Antworten zu jedem Thema auftaucht.
- **Mention Rate Trend by Topic**: dasselbe, aufgeschlüsselt über die Zeit.
- **Mention Rate by Platform**: eine Heatmap, wie oft jede Marke im Zeitraum in den Antworten jeder Plattform auftaucht.

Die Themen stammen aus Ihren Prompt-Kategorien. Sind Ihre Prompts nicht kategorisiert, fordert dieser Reiter Sie auf, sie im [Prompt Manager](prompt-manager.md) zu ordnen, statt ein leeres Diagramm anzuzeigen.

## Exportieren

**Export** bietet zwei Formate:

- **CSV spreadsheet**: alle Ergebnisse der aktuellen Ansicht, für Excel oder Google Sheets.
- **PDF executive report**: ein druckfertiger Bericht der aktuellen Ansicht, samt der Wettbewerbsdiagramme und -daten aus dem Reiter Competition.

Exporte berücksichtigen Ihre aktiven Filter, und das Deckblatt des PDF nennt die angewendeten Filter, damit ein Bericht nicht mit einem Gesamtbild des Kontos verwechselt werden kann. In kostenpflichtigen Tarifen trägt das PDF Ihr [White-Label-Branding](../agency/white-label.md), sofern Sie es eingerichtet haben.

## Sichtbarkeitsprüfungen ausführen

Klicken Sie auf **Run now** für eine Prüfung auf Abruf. Das Verhalten hängt von Ihrem [Tarif](../getting-started/account-modes.md) ab:

- **Preview Mode** führt lokale Abfragen direkt von Ihrem Gerät gegen die öffentlichen KI-Suchoberflächen aus. Hi, Moose bittet Sie zuvor um Bestätigung, denn Prüfungen in schneller Folge können dort vorübergehende Sperren wegen Anfragelimits auslösen. Die Bewertung von Stimmung, Narrativ und Abdeckung benötigt ein aktiviertes lokales Gemma-4-Modell; ohne dieses werden diese Prüfungen übersprungen.
- **BYOK-Tarife** laufen lokal mit Ihrem eigenen OpenRouter-Schlüssel.
- **Verwaltete Tarife** laufen über die Infrastruktur von Hi, Moose. Reicht das Kontingent Ihres Arbeitsbereichs in diesem Monat für den aktuellen Zeitplan nicht aus, pausieren geplante Läufe, bis Sie den Tarif wechseln, Ihre [Laufhäufigkeit](settings.md#zeitplan-fur-laufe) anpassen oder sich das Kontingent zurücksetzt. Hi, Moose nennt Ihnen, wie viele Einheiten nötig sind und wie viele verbleiben.

Sie können einen Lauf vorzeitig beenden, und Läufe, die von einem App-Update unterbrochen werden, setzen fort, statt verloren zu gehen.

## Wie es weitergeht

- **[Wettbewerber und Share of Voice](competitors.md)**: Wettbewerbsposition, Wettbewerberzitierungen und Lücken.
- **[Prompt Manager](prompt-manager.md)**: die überwachten Prompts hinzufügen, ordnen und kategorisieren.
- **[Visibility-Einstellungen](settings.md)**: Zeitplan für Läufe, Bewertungsmodell, Wettbewerberverfolgung, sekundäre Markenbegriffe und Domains sowie Standardmodelle.
