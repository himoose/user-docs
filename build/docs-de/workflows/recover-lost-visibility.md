---
source_hash: 7907c08f25052f66801891d4fc6f24fe3bdcd307070021aede9005fe5995996b
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/workflows/recover-lost-visibility/)

# Verlorene Sichtbarkeit zurückgewinnen

## Wofür das gut ist

Das ist das Workflow-Rezept für **bestehende Inhalte**: Es beobachtet Ihre [Sichtbarkeitsergebnisse](../visibility/overview.md), und wenn etwas spürbar zurückgeht, ermittelt es automatisch, ob sich eine bestehende Seite korrigieren lässt oder ob neue Inhalte nötig sind, und bereitet die Arbeit zur Durchsicht vor.

## Den Workflow zusammenstellen

Der Workflow liest sich als ein einziger Satz, gebildet aus diesen Optionen:

> **Wenn** [der Share of Mentions fällt / der Share of Citations fällt / der Share of Mentions steigt / der Share of Citations steigt] **um** [einen Schwellenwert, 1 bis 99 Punkte] **für** [alle Themen / ein bestimmtes überwachtes Thema], ermittelt Hi, Moose die betroffenen Prompts und [bereitet eine inhaltliche Korrektur vor / benachrichtigt mich].

- **Auslöser**: welche Kennzahl beobachtet wird und ob Sie sich für Rückgänge oder Anstiege interessieren. Beachten Sie: Wählen Sie einen Auslöser für Anstiege, ist die einzige verfügbare Schlussaktion **benachrichtige mich**. Für Anstiege gibt es keinen Korrekturpfad, denn es gibt nichts zu reparieren.
- **Schwellenwert**: wie viele Punkte Veränderung als bedeutsam gelten sollen, damit übliches Rauschen den Workflow nicht auslöst.
- **Themenbereich**: den Workflow auf alles anwenden, was Sie überwachen, oder auf ein bestimmtes Thema begrenzen.
- **Schlussaktion**: **eine inhaltliche Korrektur vorbereiten** (weiter mit der Verzweigung unten) oder **benachrichtige mich** (erzeugt lediglich einen Inbox-Eintrag, ohne inhaltliche Maßnahme vorzubereiten).

## Wenn die Schlussaktion „eine inhaltliche Korrektur vorbereiten" lautet

Zwei weitere Optionen verzweigen danach, ob eine bestehende Seite passt:

- **Wenn passende Seiten vorhanden sind**: Wählen Sie, was Hi, Moose tun soll: **ein AEO Audit ausführen**, **FAQ und Schema erzeugen**, **Key Points erzeugen** oder **nichts**.
- **Wenn keine passende Seite vorhanden ist**: Wählen Sie zwischen **einen Brief und einen neuen Entwurf erstellen** oder **nichts**.

Diese Verzweigung ist der eigentliche Kern des Rezepts: Es empfiehlt nicht blind einen neuen Artikel, sobald die Sichtbarkeit sinkt. Es prüft zuerst, ob die Korrektur von etwas Vorhandenem der bessere Zug ist, und schlägt neue Inhalte nur vor, wenn nichts Bestehendes passt.

## Wie er ausgeführt wird

Dieser Workflow hat keinen Knopf für die manuelle Ausführung. Er wertet sich automatisch aus, sobald ein Sichtbarkeitslauf abgeschlossen ist, und vergleicht den zuletzt abgeschlossenen Lauf mit dem vorherigen. Löst er aus, landet das Ergebnis samt der betroffenen Prompts und der ergriffenen Maßnahme in Ihrer [Inbox](../inbox/overview.md), verknüpft mit der auslösenden Sichtbarkeitsveränderung.
