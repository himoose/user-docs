---
source_hash: b6472884da7df3e651f78be6893eb9896b38a6327a26378ca1d4cc26b2d0454e
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
- Wählen, gegen welche KI-Maschinen oder Modelle er läuft. **Modelle auswählen** öffnet eine Auswahl mit ChatGPT, Claude, Gemini, Grok, Perplexity, Google AI Mode, Google AI Overview und Bing Copilot (die Verfügbarkeit hängt von Ihrem Tarif ab und, bei Maschinen mit lokaler Abfrage, davon, dass die Desktop-App läuft).
- Den Prompt löschen.

Anders als bei einer einzigen kontoweiten Einstellung erfolgt die **Modellauswahl je Prompt**: Ein Prompt kann ausschließlich gegen ChatGPT und Gemini laufen, während ein anderer alle unterstützten Maschinen abdeckt. So verbrauchen Sie Ihr Kontingent nur für die Maschinen, die für diese konkrete Anfrage zählen.

## Diagnostic Prompts

**Diagnose-Prompts** ist eine reservierte, vom System verwaltete Kategorie, die sich aus Ihrem [Brand Truth Profile](../getting-started/context/brand-truth-profile.md) speist. Statt sie von Hand zu schreiben:

1. Klicken Sie auf **Aus Brand Truth generieren** (oder richten Sie zuerst Ihr Brand Truth Profile ein, falls noch nicht geschehen).
2. Hi, Moose schlägt Prompts vor, die gezielt darauf ausgelegt sind zu erkennen, wenn KI Ihre Kunden, Ihre Fähigkeiten oder Ihre Wettbewerber falsch beschreibt.
3. Prüfen Sie die Vorschläge in einem Dialog: Schalten Sie einzelne Prompts ein oder aus, ändern Sie die Formulierung oder entfernen Sie einen ganz, bevor Sie sie in die Überwachung übernehmen.
4. Der Dialog nennt vor der Bestätigung die geschätzten Kosten: Prompts × Modelle × Läufe pro Woche ≈ Gesamtläufe pro Woche.

Enthält Ihr Brand Truth Profile noch nicht genug Inhalt für sinnvolle Diagnose-Prompts, sagt Hi, Moose Ihnen das, statt generische Füllware zu erzeugen: Ergänzen Sie zuerst Kundenfragen, zentrale Fähigkeiten oder Wettbewerber in Ihrem Profil.

## Rein lokale Speicherung der Prompts

In den rein lokal arbeitenden BYOK-Tarifen werden Prompt-Kategorien, Prompt-Definitionen und Modellauswahlen auf Ihrem Gerät gespeichert statt in die Cloud synchronisiert.
