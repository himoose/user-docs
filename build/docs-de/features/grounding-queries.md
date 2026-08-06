---
source_hash: 3856622231055de776fe82082345666ad4d8429b9d735111e9d399831a122f47
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/features/grounding-queries/)

# Grounding-Suchanfragen von AI Mode

## Wofür das gut ist

Diese Funktion zeigt Ihnen die Google-Suchen, die Gemini beim Fundieren seiner Antwort auf einen Prompt ausgeführt hat, samt der zitierten Quellen und der fundierten Antwort selbst.

!!! info "Was das genau ist"
    Hi, Moose bittet die Gemini-API, Ihren Prompt mit aktivierter Google-Such-Fundierung zu beantworten, und liest anschließend die Liste der Suchen aus, die das Modell abgesetzt hat. Es ist keine Aufzeichnung des AI Mode für Endnutzer von Google. AI Mode ist eine eigene Oberfläche, die ihre internen Anfragen niemandem offenlegt. Was Sie erhalten, ist die nächstliegende verfügbare Annäherung: derselbe Suchindex, dieselbe Modellfamilie und Formulierungen, die dem, was AI Mode erzeugt, sehr nahekommen. Behandeln Sie das als belastbares Signal, nicht als Mitschrift, und rechnen Sie mit gewissen Abweichungen zwischen zwei Läufen desselben Prompts.

!!! note "Verfügbarkeit"
    Diese Funktion führt im Hintergrund einen verwalteten Fundierungsaufruf an Gemini aus und setzt daher einen **kostenpflichtigen verwalteten** Arbeitsbereich voraus. Das gilt auch in den BYOK-Tarifen: BYOK hält die eigentliche Chat-Erzeugung lokal, doch das Erfassen der Grounding-Suchanfragen nutzt die verwaltete Infrastruktur von Hi, Moose, deren Betrieb uns Geld kostet. Es ist deshalb weder in BYOK Free noch in BYOK Premium enthalten. Preview Mode enthält es ebenfalls nicht.

## Wie Sie sie ausführen

1. Wählen Sie im [Chat](../chat/overview.md) den Schnellstart **Capture AI Mode grounding queries** (oder bitten Sie direkt darum).
2. Geben Sie den Prompt ein, den Sie untersuchen möchten.
3. Hi, Moose prüft die Grounding-Suchanfragen von Gemini zu diesem Prompt und liefert:
    - Die von Gemini tatsächlich verwendeten Grounding-Suchanfragen.
    - Die zitierten Quellen.
    - Die fundierte Antwort selbst.

## Warum das wichtig ist

Grounding-Suchanfragen zeigen Ihnen, wie eine Antwortmaschine aus einem einzigen Prompt eine ganze Reihe echter Suchen macht. Das hilft zu verstehen, warum Ihre Seite aufgegriffen wird oder nicht, und deckt Anfragevarianten auf, die Sie derzeit weder in [Visibility](../visibility/overview.md) noch im [Prompt Manager](../visibility/prompt-manager.md) überwachen.

## Wenn ein Lauf fehlschlägt

Kann Hi, Moose zu einem Prompt keine echten Grounding-Suchanfragen sammeln, sagt er das, statt eine Vermutung zu präsentieren. Versuchen Sie es gleich noch einmal, oder prüfen Sie, ob im Arbeitsbereich ein verwaltetes Abonnement aktiv ist.
