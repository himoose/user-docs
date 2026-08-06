---
source_hash: 90bb543cefb714f7fdb6facb1f7799b751aff22949ece082264e7713b4992995
---
# Modellauswahl

## Wofür das gut ist

Jeder Chat läuft mit einem bestimmten KI-Modell, und über die Modellauswahl sehen und wechseln Sie, welches Sie gerade nutzen, einschließlich lokaler Modelle auf dem Gerät.

## Ein Modell wählen

Öffnen Sie die Modellauswahl, um die in Ihrem [Tarif](../getting-started/account-modes.md) verfügbaren Modelle zu sehen. Jede Option trägt Kennzeichnungen, damit Sie vor dem Wechsel wissen, was Sie bekommen:

- **Free** / **HiMoose Cloud** / **Paid or BYOK**: welche Tarife dieses Modell nutzen können.
- **Speed: Slow / Average / Very Fast**: ein grober Eindruck der Antwortzeit.
- **Local**: läuft vollständig auf Ihrem Gerät (siehe unten).
- Eine **Multiplikator-Kennzeichnung** bei teureren Modellen, die zeigt, wie viel mehr sie von Ihrem Guthaben verbrauchen als die Standardoption.

Das Angebot folgt dem, was die Modellanbieter veröffentlichen, und umfasst derzeit die Familien Claude, GPT, Gemini und Gemma. Ist ein Modell in Ihrem Tarif nicht verfügbar, sagt Hi, Moose Ihnen das direkt, statt stillschweigend auf ein anderes auszuweichen.

## Lokale Modelle

Zugelassene lokale Modelle wie Googles Gemma 4 laufen **vollständig auf Ihrem Rechner**. Keine Token verbraucht, kein Umweg über die Cloud, und keine Daten verlassen Ihr Gerät. Wenn Sie zum ersten Mal ein lokales Modell wählen, führt Hi, Moose Sie durch die Einrichtung.

Nach Download und Aktivierung sind lokale Antworten auf Apple Silicon schnell. Auf Macs mit Intel-Prozessor läuft das Modell auf der CPU und ist deutlich langsamer als Cloud-Modelle; Hi, Moose weist Sie darauf hin, bevor Sie den Download starten.

Lokale Modelle sind keine abgespeckte Variante. Gemma 4 unterstützt den Aufruf von Werkzeugen, sodass die [Chat-Werkzeuge](tools-and-specialists.md) auf einem lokalen Modell genauso funktionieren wie in der Cloud.

!!! note "Preview Mode ist auf ein lokales Modell angewiesen"
    Im kostenlosen Tarif funktionieren [AEO Audits](../features/aeo-audits.md) und die Sichtbarkeitsbewertung nur mit einem aktivierten lokalen Modell. Das ist der wichtigste Grund, früh eines einzurichten.

## Teurere Modelle

Manche Modelle verbrauchen deutlich mehr von Ihrem Guthaben als die Standardoption. Wählen Sie eines davon, fragt Hi, Moose zuvor nach und nennt ungefähr, um welchen Faktor mehr Token anfallen, damit Sie Ihr Guthaben nicht versehentlich aufbrauchen.

Die teuersten Modelle sind an den Tarif gebunden. Enthält Ihrer sie nicht, erscheinen sie als nicht verfügbar statt ausgeblendet.

## Fundierung durch Websuche

Der Chat kann seine Antworten für das laufende Gespräch auf Live-Suchergebnisse stützen. Das steht in BYOK Premium, BYOK Agency und allen verwalteten Tarifen zur Verfügung. In BYOK Free und Preview Mode ist es nicht enthalten.

## Sprache

Der Chat folgt einer Spracheinstellung, sodass Sie in einer anderen Sprache arbeiten können als der, in der die App-Oberfläche erscheint.

## Wenn ein Modell nicht genutzt werden kann

Statt einer Antwort kann eine Meldung erscheinen, wenn:

- das gewählte Modell vorübergehend nicht verfügbar ist (versuchen Sie ein anderes),
- das Modell in Ihrem Tarif nicht zugelassen ist (wählen Sie eines, das enthalten ist), oder
- ein Bild an ein Modell angehängt wurde, das keine Bildeingabe unterstützt. Hi, Moose nennt ein Modell, das es kann, und bietet den Wechsel an.

## Wie das mit BYOK zusammenhängt

In BYOK-Tarifen bestimmt die Modellauswahl, welches Modell Ihr eigener OpenRouter-Schlüssel aufruft. Die Inferenz läuft weiterhin lokal in der Desktop-App. Unter [Kontotypen und Tarife](../getting-started/account-modes.md) sehen Sie, wie sich der Modellzugang je Tarif unterscheidet.

Ihr OpenRouter-Schlüssel wird pro Konto und nicht pro Gerät gespeichert. Haben Sie noch keinen hinterlegt, fragt Hi, Moose beim ersten Bedarf danach, statt stillschweigend zu scheitern.
