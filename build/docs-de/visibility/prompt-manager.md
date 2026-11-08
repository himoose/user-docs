---
source_hash: 52e4fc142ac45ba9ec93251b7b681cb95c1e09d409fef443f88b56ac8cbebaa7
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/visibility/prompt-manager/)

# Prompt Manager

## Wofür das gut ist

Im Prompt Manager erstellen und ordnen Sie die tatsächlichen Anfragen, die Hi, Moose gegen KI-Maschinen prüft: die Prompts, die Ihre Kundinnen und Kunden realistischerweise eintippen oder stellen würden.

## Prompts über Kategorien ordnen

Prompts werden in Kategorien gruppiert, die in der Filterliste links erscheinen: **Alle Prompts**, **Ohne Kategorie** und alle von Ihnen angelegten eigenen Kategorien (etwa nach Thema oder Kampagne). Eine neue Kategorie legen Sie über das Feld am Ende der Liste an. Arbeitsbereiche im kostenlosen Tarif sind auf 5 Kategorien begrenzt.

## Einen Prompt anlegen und bearbeiten

Geben Sie einen neuen Prompt ein und fügen Sie ihn einer Kategorie hinzu. Für jeden Prompt können Sie:

- Den Prompt-Text bearbeiten.
- Wählen, gegen welche KI-Engines er läuft. **Modelle auswählen** öffnet eine Auswahl mit allen Engines, die Ihr Tarif verfolgen kann, API- und Local-fetch-Varianten gleichermaßen (siehe [die Engines, die Sie verfolgen können](settings.md#die-engines-die-sie-verfolgen-konnen)). Local-fetch-Engines brauchen eine geöffnete Desktop-App, wenn der Lauf ausgeführt wird.
- Den Prompt stilllegen (siehe unten).
- Den Prompt löschen.

Anders als bei einer einzigen kontoweiten Einstellung erfolgt die **Modellauswahl je Prompt**: Ein Prompt kann ausschließlich gegen ChatGPT und Gemini laufen, während ein anderer alle unterstützten Maschinen abdeckt. So verbrauchen Sie Ihr Kontingent nur für die Maschinen, die für diese konkrete Anfrage zählen.

## Mehrere Prompts finden und auswählen

**Prompts durchsuchen** filtert die Liste nach Text. Haken Sie mehrere Prompts an, und die Werkzeugleiste bietet **Kategorien zuweisen**, **Modelle zuweisen**, **Ausgewählte stilllegen** und **Ausgewählte löschen**, sodass eine Änderung an vielen Prompts in einem Schritt gespeichert wird statt Prompt für Prompt. Löschen können Sie nur Prompts, die Sie selbst angelegt haben, es sei denn, Sie sind Team-Inhaber.

## Einen Prompt stilllegen

Legen Sie einen Prompt still, wenn er veraltet ist, seine Historie aber erhalten bleiben soll, zum Beispiel ein Prompt, der das letzte Jahr nennt. Ein stillgelegter Prompt:

- behält alle bisherigen Ergebnisse, sodass Verläufe und Berichte sie weiterhin enthalten;
- bleibt bei neuen Läufen außen vor, kostet also nichts;
- bleibt in der Liste der [Chancen](overview.md#chancen) außen vor.

Stillgelegte Prompts stehen im Abschnitt **Stillgelegte Prompts** der Filterliste, jeweils mit dem Datum der Stilllegung, und **Wiederherstellen** nimmt einen wieder in die Verfolgung auf. Einen neuen Prompt mit demselben Text wie ein stillgelegter anzulegen bewirkt nichts; stellen Sie ihn stattdessen wieder her. **Löschen** nimmt einen Prompt ebenfalls aus der künftigen Verfolgung und behält die historischen Laufdaten für Berichte, lässt sich aber nicht rückgängig machen.

## Diagnostic Prompts

**Diagnose-Prompts** ist eine reservierte, vom System verwaltete Kategorie, die sich aus Ihrem [Brand Truth Profile](../getting-started/context/brand-truth-profile.md) speist. Statt sie von Hand zu schreiben:

1. Klicken Sie auf **Aus Brand Truth generieren** (oder richten Sie zuerst Ihr Brand Truth Profile ein, falls noch nicht geschehen).
2. Hi, Moose schlägt Prompts vor, die gezielt darauf ausgelegt sind zu erkennen, wenn KI Ihre Kunden, Ihre Fähigkeiten oder Ihre Wettbewerber falsch beschreibt.
3. Prüfen Sie die Vorschläge in einem Dialog: Schalten Sie einzelne Prompts ein oder aus, ändern Sie die Formulierung oder entfernen Sie einen ganz, bevor Sie sie in die Überwachung übernehmen.
4. Der Dialog nennt vor der Bestätigung die geschätzten Kosten: Prompts × Modelle × Läufe pro Woche ≈ Gesamtläufe pro Woche.

Enthält Ihr Brand Truth Profile noch nicht genug Inhalt für sinnvolle Diagnose-Prompts, sagt Hi, Moose Ihnen das, statt generische Füllware zu erzeugen: Ergänzen Sie zuerst Kundenfragen, zentrale Fähigkeiten oder Wettbewerber in Ihrem Profil.

## Rein lokale Speicherung der Prompts

In den rein lokal arbeitenden BYOK-Tarifen werden Prompt-Kategorien, Prompt-Definitionen und Modellauswahlen auf Ihrem Gerät gespeichert statt in die Cloud synchronisiert.
