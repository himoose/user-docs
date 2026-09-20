---
source_hash: a5f6ba4ca639882531f721cd6d5669ca1865f2c242b18c3fa8bbfa39f0ddb815
---
# Modellauswahl

## Wofür das gut ist

Jeder Chat läuft mit einem bestimmten KI-Modell, und über die Modellauswahl sehen und wechseln Sie, welches Sie gerade nutzen, einschließlich lokaler Modelle auf dem Gerät.

## Ein Modell wählen

Öffnen Sie die Modellauswahl, um die in Ihrem [Tarif](../getting-started/account-modes.md) verfügbaren Modelle zu sehen. Jede Option trägt Kennzeichnungen, damit Sie vor dem Wechsel wissen, was Sie bekommen:

- **Kostenlos** / **HiMoose Cloud** / **Bezahlt oder BYOK**: welche Tarife dieses Modell nutzen können.
- **Speed: Slow / Average / Very Fast**: ein grober Eindruck der Antwortzeit.
- **Lokal**: das Modell läuft auf Ihrem Gerät (siehe unten).
- Eine **Multiplikator-Kennzeichnung** bei teureren Modellen, die zeigt, wie viel mehr sie von Ihrem Guthaben verbrauchen als die Standardoption.

Das Angebot folgt dem, was die Modellanbieter veröffentlichen. Derzeit umfasst es die Familien Claude, GPT, Gemini, Gemma, Grok, DeepSeek, GLM, Kimi, Llama, Muse, Nemotron, Step und Trinity, darunter mehrere kostenlose Optionen und die lokalen Gemma-Varianten. Ist ein Modell in Ihrem Tarif nicht verfügbar, sagt Hi, Moose Ihnen das direkt, statt stillschweigend auf ein anderes auszuweichen.

Die Liste ändert sich, während Anbieter Modelle einführen und abkündigen. Betrachten Sie daher die Auswahl in der App als die aktuelle Antwort, nicht diese Seite.

## Lokale Modelle

Zugelassene lokale Modelle wie Googles Gemma 4 laufen **auf Ihrem Rechner**, und ihre Antworten entstehen dort. Keine Token verbraucht. Standardmäßig sendet ein kurzer Routing-Schritt den Text Ihrer Nachricht an einen Cloud-Dienst, der das passende Werkzeug dafür wählt. Das haben Sie in der Hand: Schalten Sie **Intelligentes Routing** unter **Einstellungen → Lokale KI** ab, dann bleibt auch dieser Schritt auf Ihrem Gerät. Wenn Sie zum ersten Mal ein lokales Modell wählen, führt Hi, Moose Sie durch die Einrichtung.

Nach Download und Aktivierung sind lokale Antworten auf Apple Silicon schnell. Auf Macs mit Intel-Prozessor läuft das Modell auf der CPU und ist deutlich langsamer als Cloud-Modelle; Hi, Moose weist Sie darauf hin, bevor Sie den Download starten.

Lokale Modelle sind keine abgespeckte Variante. Gemma 4 unterstützt den Aufruf von Werkzeugen, sodass die [Chat-Werkzeuge](tools-and-specialists.md) auf einem lokalen Modell genauso funktionieren wie in der Cloud.

!!! note "Preview Mode ist auf ein lokales Modell angewiesen"
    Im kostenlosen Tarif funktionieren [AEO Audits](../features/aeo-audits.md) und die Sichtbarkeitsbewertung nur mit einem aktivierten lokalen Modell. Das ist der wichtigste Grund, früh eines einzurichten.

## Teurere Modelle

Manche Modelle verbrauchen deutlich mehr von Ihrem Guthaben als die Standardoption. Wählen Sie eines davon, fragt Hi, Moose zuvor nach und nennt ungefähr, um welchen Faktor mehr Token anfallen, damit Sie Ihr Guthaben nicht versehentlich aufbrauchen.

Die teuersten Modelle sind an den Tarif gebunden. Enthält Ihrer sie nicht, erscheinen sie als nicht verfügbar statt ausgeblendet.

## Fundierung durch Websuche

Der Chat kann seine Antworten für das laufende Gespräch auf Live-Suchergebnisse stützen. Das steht in BYOK Premium, BYOK Agency und allen verwalteten Tarifen zur Verfügung. In BYOK Free und Preview Mode ist es nicht enthalten.

In verwalteten Tarifen kostet jede Websuche **500 Credits** zusätzlich zum Tokenverbrauch des Modells selbst, weil die Suche über einen kostenpflichtigen Anbieter läuft und für uns nicht gratis ist. Ein Gespräch, das mehrfach sucht, macht sich entsprechend auf Ihrem Guthaben bemerkbar. In BYOK-Tarifen wird die Suche wie jeder andere Aufruf über Ihren eigenen OpenRouter-Schlüssel abgerechnet.

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
