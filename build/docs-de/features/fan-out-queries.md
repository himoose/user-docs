---
source_hash: 3b2a6720bd62d36c159ec05f39cfb8f6e59efa7a27d7e6054053a2fcb1d2c950
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/features/fan-out-queries/)

# Fan-out-Suchanfragen von ChatGPT

## Wofür das gut ist

Diese Funktion erfasst die einzelnen „Fan-out"-Suchen, die der Websuche-Schritt von OpenAI beim Beantworten Ihres Prompts ausgeführt hat, samt der zitierten Quellen und einer Vorschau der Antwort.

!!! info "Was das genau ist"
    Hi, Moose ruft die Responses-API von OpenAI mit aktiviertem Websuche-Werkzeug auf und liest anschließend die von diesem Lauf ausgeführten Suchen aus. Es ist keine Erfassung des Fan-outs im Endnutzerprodukt ChatGPT, das OpenAI nicht offenlegt. Was Sie erhalten, ist die nächstliegende verfügbare Annäherung: dieselbe Websuche-Schicht, angetrieben von derselben Modellfamilie, sodass die Anfrageerweiterung dem, was ChatGPT Search tut, sehr nahekommt. Behandeln Sie das als belastbares Signal, nicht als Mitschrift, und rechnen Sie mit gewissen Abweichungen zwischen zwei Läufen desselben Prompts.

!!! note "Verfügbarkeit"
    Diese Funktion führt im Hintergrund eine verwaltete Erfassung der OpenAI-Websuche-Spur aus und setzt daher einen **kostenpflichtigen verwalteten** Arbeitsbereich voraus. Das gilt auch in den BYOK-Tarifen: BYOK hält die eigentliche Modellausführung lokal, doch die Fan-out-Erfassung nutzt die verwaltete Infrastruktur von Hi, Moose, deren Betrieb uns Geld kostet. Sie ist deshalb weder in BYOK Free noch in BYOK Premium enthalten. Preview Mode enthält sie ebenfalls nicht.

## Wie Sie sie ausführen

1. Wählen Sie im [Chat](../chat/overview.md) den Schnellstart **ChatGPT-Fan-out-Abfragen erfassen** (oder bitten Sie direkt darum).
2. Geben Sie den Prompt ein, den Sie untersuchen möchten.
3. Hi, Moose erfasst die Antwort von ChatGPT und liefert:
    - Die einzelnen Fan-out-Suchanfragen, die ChatGPT ausgeführt hat.
    - Die zitierten Quellen.
    - Eine Vorschau der Antwort.

Hat OpenAI für einen bestimmten Lauf keine eigenständigen Fan-out-Suchanfragen offengelegt, zeigt Hi, Moose Ihnen dennoch die erfasste verwaltete Suchspur und die zitierten Quellen, statt ein leeres oder erfundenes Ergebnis zu präsentieren.

## Warum das wichtig ist

Fan-out-Suchanfragen legen die Anfrageerweiterung hinter einer webgestützten Antwort offen. Das hilft zu verstehen, welche konkreten Formulierungen Zitierungen auf Ihre Inhalte bringen oder eben nicht. Genau das fließt in das ein, was Sie in [Visibility](../visibility/overview.md) überwachen und in den [Content Briefs](content-briefs.md) planen.
