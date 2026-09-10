---
source_hash: 7e432cdd4918eeb01a120c373ca83181288da1c2c0b01d3aee18207e05092124
---
# Send Moose

## Wofür das gut ist

Send Moose ist der Ort, an dem Sie eine Aufgabe abgeben, statt sie selbst zu erledigen. Sie beschreiben die Arbeit in klarer Sprache („finde heraus, wer statt uns für Projektmanagement-Software empfohlen wird und warum", „prüfe, ob unsere Preisseite noch zu dem passt, was auf den Vergleichsseiten der Wettbewerber steht"), und Moose geht los und erledigt sie, mit dem Web und allem, was Hi, Moose über Ihr Projekt bereits weiß.

Das ist der Unterschied zwischen einem Chat, der Ihnen antwortet, und einem Agenten, der an die Arbeit geht. Der Chat ist ein Gespräch; Send Moose ist ein Auftrag, den Sie losschicken und zu dem Sie zurückkehren.

Sie finden ihn in der Seitenleiste unter **Send Moose**.

!!! warning "Send Moose ist experimentell"
    Es ist in der App und es funktioniert, aber es ist das Neueste und am wenigsten Gesetzte in Hi, Moose. Achten Sie auf die Qualität dessen, was zurückkommt, und in kostenpflichtigen Tarifen auf Ihren Tokenverbrauch: Scout und Skeptic laufen in der Cloud, selbst wenn Moose lokal arbeitet.

## Was Moose mitbringt

Ein allgemeiner Web-Agent fängt bei null an, und man muss ihm alles erklären. Moose kommt bereits mit Ihrem Projekt verbunden an:

| Er kann lesen | Was das bedeutet |
|---|---|
| Ihre Sichtbarkeitsdaten | Übersicht, Share of Voice, Wettbewerber, Themen, Prompts und was sich geändert hat |
| Ihren Website-Index | Gecrawlte Seiten, was sich dort geändert hat, interne Links und Ihren [Entity Graph](../features/entity-graph.md) |
| Ihre AEO-Historie | Frühere Audits und deren Details, Zitationskontext, Crawler-Zugang, Themenabdeckung |
| [Google Search Console](../integrations/google-search-console.md) | Ihre echten Such- und Seitendaten, iterativ abgefragt |
| Ihre [Bibliothek](../library/overview.md) | Briefs, Entwürfe, Key Points, FAQ und Audits, die Sie schon erstellt haben |
| Frühere Aufgaben | Was er in früheren Läufen dieses Projekts gefunden und entschieden hat |

Er kann außerdem mitten in einer Aufgabe eine [Sichtbarkeitsprüfung](../visibility/overview.md) oder ein [AEO-Audit](../features/aeo-audits.md) live ausführen, wenn die Antwort das erfordert, statt Ihnen zu sagen, Sie sollten es ausführen.

## Eine Aufgabe schicken

Beschreiben Sie die Arbeit und drücken Sie **Send Moose**. Zwei Optionen prägen den Ablauf:

- **Tiefe Arbeit**: Lassen Sie die Aufgabe Stunden dauern, wenn nötig: sehr viel mehr Seiten, sehr viel mehr Suchen, mehr Zwischenstände. Nutzen Sie das, wenn die Frage wirklich weit ist, nicht für eine kurze Recherche.
- **Dateien anhängen**: bis zu sechs Dateien pro Aufgabe, als Kontext, den er beim Arbeiten liest.

Sie können **Benachrichtige mich, wenn Moose fertig ist** anhaken und gehen. Die Aufgabe läuft weiter, ob Sie zusehen oder nicht und ob Sie auf dem Bildschirm bleiben oder nicht.

## Ihm bei der Arbeit zusehen

**Browser ansehen** öffnet die Browser-Instanz, die Moose gerade nutzt, sodass Sie die Seiten sehen, während er sie liest. **Übernehmen** gibt Ihnen den Browser, wenn er an etwas hängt, das Sie in einer Sekunde lösen können, etwa an einem Cookie-Banner oder einer Anmeldung, und **Zurück zur Aufgabe** gibt ihn zurück.

Sie können dieses Fenster jederzeit schließen. Moose arbeitet weiter.

## Moose, Scout und Skeptic

Im kostenlosen Tarif arbeitet Moose allein.

Kostenpflichtige Tarife stellen ihm zwei weitere Agenten zur Seite:

- **Scout** findet Blickwinkel, auf die Moose nicht gekommen ist.
- **Skeptic** hinterfragt die Belege, bevor sie in Ihr Ergebnis gelangen.

Sie können mitten in der Aufgabe im Thread mit jedem von ihnen sprechen: Moose etwas sagen, Scout um einen weiteren Blickwinkel bitten, Skeptic bitten, bei einer Behauptung nachzufassen. **Weitermachen** und **Fünf weitere Ergebnisse prüfen** verlängern einen Lauf, der an einer nützlichen Stelle stehengeblieben ist.

Scout und Skeptic laufen immer über OpenRouter in der Cloud, auch wenn Moose selbst auf einem lokalen Modell arbeitet. Sie kosten also Token.

## Wenn Moose Sie braucht

Zwei Dinge halten eine Aufgabe an und warten auf Sie, statt zu raten:

- **Braucht Ihre Freigabe**: Moose will gleich eine Aktion auf einer echten Website auslösen, etwa einen Button in einem Formular drücken. Er zeigt Ihnen den genauen Button und wartet auf **Freigeben und fortfahren** oder **Nicht tun**.
- **Braucht Ihre Hilfe**: Er hängt an etwas, das nur Sie beantworten können. Tippen Sie eine Antwort, oder drücken Sie **Moose entscheiden lassen**, damit er selbst entscheidet.

Nichts wird irgendwo veröffentlicht, gesendet oder abgeschickt, ohne dass Sie es vorher freigeben. Das gilt auch für geplante Läufe.

## Das Ergebnis lesen

Eine abgeschlossene Aufgabe hat vier Reiter:

- **Ergebnis**: was er gefunden hat, ausformuliert.
- **Zusammenarbeit**: wie es lief und wer was beigetragen hat: Notizen von Scout, Einwände von Skeptic, wie oft Sie eingegriffen haben.
- **Quellen**: jede geöffnete Seite, mit den Belegen, die er daraus mitgenommen hat.
- **Aktivität**: der vollständige Lauf, filterbar nach Werkzeugen oder Agenten.

Von dort können Sie **In der Bibliothek speichern**, **Bericht herunterladen** oder im [Chat](../chat/overview.md) zum Ergebnis nachfragen. Dateien, die Moose während der Aufgabe gespeichert hat, erscheinen unter **Dateien, die Moose gespeichert hat**: öffnen, eine Kopie sichern oder im Ordner anzeigen. Er kann CSV-, Markdown-, Text-, PDF- und Word-Dateien speichern.

## Inhalte, die Moose erstellt

Moose kann im Rahmen einer Aufgabe echte Hi, Moose-Artefakte erzeugen, nicht nur eine geschriebene Antwort: einen **Content Brief**, einen **Entwurf**, **Key Points**, **FAQ** oder ein **AEO-Audit**. Sie landen wie alles andere in Ihrer [Bibliothek](../library/overview.md), und das Ergebnis der Aufgabe verlinkt direkt darauf.

## Eine Aufgabe nach Zeitplan ausführen

**Nach Zeitplan ausführen** macht aus einer einmaligen Aufgabe eine wiederkehrende: täglich, an Wochentagen, wöchentlich oder monatlich, zu einer oder mehreren Uhrzeiten.

Geplante Aufgaben erscheinen unter **Geplante Aufgaben** und lassen sich pausieren, fortsetzen oder löschen. Sie laufen unbeaufsichtigt: Moose trifft die kleinen Entscheidungen selbst und veröffentlicht oder sendet weiterhin nichts ohne Ihre Freigabe.

## Frühere Aufgaben

Jede Aufgabe bleibt unter **Frühere Aufgaben** erhalten, durchsuchbar und filterbar nach **Erledigt**, **Zurückgerufen**, **Nicht abgeschlossen** und **Blockiert**, gruppiert nach heute, früher diese Woche und davor. Aufgaben gehören zu dem Projekt, in dem sie ausgeführt wurden.

## Einstellungen

Die **Send-Moose-Einstellungen** werden je Projekt gespeichert:

- **Moose-LLM**: Automatisch nutzt das größte installierte lokale Modell oder das Cloud-Modell Ihres Tarifs, wenn lokale KI aus ist. Sie können auch ein bestimmtes Modell festlegen.
- **Scout-LLM** und **Skeptic-LLM**: nur in kostenpflichtigen Tarifen, standardmäßig Gemma 4 31B.
- **Inhaltsmodell**: welches Modell die Briefs, Entwürfe und FAQ schreibt, die er erstellt. Standardmäßig dasselbe, das Moose nutzt.
- **Suchmaschine**: womit er sucht.

Alles, was mit **Verbraucht Token** gekennzeichnet ist, läuft über OpenRouter in der Cloud statt auf Ihrem Rechner. Aufgaben mit tiefer Arbeit laufen am längsten und kosten daher am meisten.

## Was es braucht

- **Ein lokales Modell oder einen kostenpflichtigen Tarif.** Moose denkt auf einem Gemma-Modell, das auf Ihrem Rechner läuft. Laden Sie es einmal über den Hinweis auf dem Bildschirm herunter, und Aufgaben kosten Sie nichts. Kostenpflichtige Tarife können ihn stattdessen auf ein Cloud-Modell setzen. Haben Sie lokale KI ausgeschaltet und sind im kostenlosen Tarif, sagt Send Moose das und bietet an, sie wieder einzuschalten.
- **Eine Website am Projekt**, für Aufgaben rund um Ihre eigene Website, Marke oder Wettbewerber. Allgemeine Web-Aufgaben funktionieren auch ohne.

## Wie es weitergeht

- **[Chat](../chat/overview.md)**: für Arbeit, die Sie Zug um Zug steuern statt abgeben wollen.
- **[Workflows](../workflows/overview.md)**: für ein festes Rezept, das auf einen Auslöser hin läuft, statt einer offenen Aufgabe.
- **[Bibliothek](../library/overview.md)**: wo die Berichte und Inhalte einer Aufgabe aufbewahrt werden.
