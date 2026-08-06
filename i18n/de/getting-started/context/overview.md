---
source_hash: 05fae21b2ec70be5a8bae1ca0e58f085c9da2140a80bae1dc2e083051aeffb43
---
# Context

## Wofür das gut ist

**Kontext** ist die Fundamentschicht in der linken Navigation der Desktop-App. Es ist der gemeinsame Arbeitskontext Ihres aktuellen Projekts: die Informationen, die der Operator, der Chat und alle Erzeugungsfunktionen wiederverwenden, statt bei jeder Anfrage bei null anzufangen.

Context besteht aus drei getrennten Teilen:

| | Geltungsbereich | Wofür er da ist |
|---|---|---|
| **[Brand Voice](brand-voice.md)** | Pro Projekt | Wie Ihre Marke klingen soll: Tonfall, Zielgruppe, Werte, Terminologie. Prägt den Schreibstil von allem, was Hi, Moose erzeugt. |
| **[Brand Truth Profile](brand-truth-profile.md)** | Pro Projekt | Eine maschinenlesbare Quelle der Wahrheit darüber, was Ihr Unternehmen wirklich ist, verkauft und bedient. Dient dazu zu erkennen, wenn KI-Antworten dies verzerren oder davon abweichen. |
| **[Über Sie](about-you.md)** | Pro Gerät, nicht pro Projekt | Notizen über Sie persönlich: Ihre Funktion, Ihre Ziele und Ihre Arbeitsweise, damit der Chat die Person kennt und nicht nur die Marke. |

## Warum es drei getrennte Artefakte sind

Brand Voice und Brand Truth Profile beantworten unterschiedliche Fragen, auch wenn beide Ihre Marke beschreiben:

- **Brand Voice** beantwortet „Wie soll das klingen?": Tonfall, Stil, bevorzugtes Vokabular. Es ist eine gestalterische und stilistische Richtschnur für erzeugte Inhalte.
- **Brand Truth Profile** beantwortet „Was stimmt über uns?": kanonische Beschreibung, idealer Kunde, Angebote, Wettbewerber und die konkreten Punkte, bei denen KI häufig danebenliegt. Es ist eine sachliche Referenz zum Erkennen von Verzerrungen, kein Styleguide.

**Über Sie** unterscheidet sich von beiden: Es geht überhaupt nicht um die Marke. Es ist persönlicher Kontext über **Sie**, die Person, die die App nutzt, lokal auf Ihrem Gerät gespeichert statt an ein Projekt gebunden. Er begleitet Sie deshalb durch alle Projekte, statt bei jedem Wechsel des Arbeitsbereichs zurückgesetzt zu werden.

## Wo Context genutzt wird

- **Brand Voice** wird wiederverwendet in [Content Briefs](../../features/content-briefs.md), im [FAQ-Generator](../../features/faq-generator.md), im [Key-Points-Extraktor](../../features/key-points.md), bei [Entwürfen, Vorschau und Veröffentlichung](../../features/drafts-and-publishing.md) und in den Empfehlungen der [AEO Audits](../../features/aeo-audits.md).
- **Brand Truth Profile** wird während der [Visibility](../../visibility/overview.md)-Läufe wiederverwendet, wo Hi, Moose prüft, ob die Antwort einer KI-Maschine über Ihre Marke zu Ihrer kanonischen Beschreibung, Ihren Angeboten, Ihren Wettbewerbern und bekannten Verzerrungsmustern passt.
- **Über Sie** wird im [Chat](../../chat/overview.md) wiederverwendet, damit Antworten Ihre Funktion, Ihre Ziele und Ihren bevorzugten Kommunikationsstil berücksichtigen.

## Wie Sie es ausfüllen

Jedes Artefakt zeigt an, wie viele Felder Sie ausgefüllt haben, und blendet eine kurze Vorschau ein, sobald Sie etwas hinzufügen. Alle Felder aller drei Artefakte sind optional: Hi, Moose arbeitet auch mit unvollständigem Kontext und wird präziser, je mehr Sie ergänzen.

Speziell bei der Brand Voice müssen Sie nicht jedes Feld von Hand ausfüllen: Eine Funktion zum **automatischen Ausfüllen** kann die Website Ihres Projekts lokal crawlen und Werte für leere Felder vorschlagen.

## Lokale Speicherung und Cloud-Synchronisierung

Standardmäßig werden Brand Voice und Brand Truth Profile **lokal für das aktuelle Projekt** gespeichert, und Über Sie wird **lokal auf Ihrem Gerät** gespeichert. Die Cloud-Synchronisierung, die Brand Voice und Brand Truth Profile sichert und im Team teilt, steht in **allen kostenpflichtigen Tarifen** zur Verfügung, einschließlich der kostenpflichtigen BYOK-Tarife. Preview Mode und BYOK Free bleiben rein lokal; ein Wechsel in einen höheren Tarif aktiviert die Synchronisierung, sodass Ihr Team dieselbe Grundlage teilt und diese geschützt ist, falls Ihrem Rechner etwas zustößt.

!!! note "In den BYOK-Tarifen"
    Das Crawlen des Markenkontexts (der Schritt zum automatischen Ausfüllen) und die Brand-Truth-Analyse laufen lokal in der Desktop-App. Hi, Moose muss die Inhalte Ihrer Website nicht auf eigenen Servern sehen, um diesen Kontext aufzubauen oder zu nutzen.
