---
source_hash: d13fbe0e44e283bca3759e24ae06c4632b5ccb20e66f5806145543eb82fe5f65
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/features/drafts-and-publishing/)

# Entwürfe, Vorschau und Veröffentlichung

## Wofür das gut ist

Hi, Moose hört nicht bei der Empfehlung auf: Die Plattform begleitet Sie von einem Brief oder einer Änderungsidee bis zur veröffentlichten Änderung, mit einem Vorschau- und einem Freigabeschritt dazwischen und einer Aufzeichnung dessen, was geschehen ist.

## Draft Studio

Im Draft Studio werden Entwürfe geschrieben und verfeinert. Die Entwurfserzeugung ist darauf ausgelegt, auf einem [Content-Brief](content-briefs.md) aufzubauen, statt als blinder Textaufbläher zu arbeiten: Erfordert eine Aufgabe strukturierte Planung, erstellt oder bestätigt Hi, Moose zuerst den Brief und schreibt dann daraus. Das Draft Studio unterstützt außerdem das direkte Bearbeiten langer Texte.

### Inhaltstypen

Die Entwurfserzeugung folgt denselben Vorlagentypen, die beim [Erstellen eines Content-Briefs](content-briefs.md#einen-brief-erstellen) zur Verfügung stehen. Vier davon haben einen eigenen Schnellstart im Chat, jeweils mit eigener Struktur: [Blogbeitrags-Entwurf](blog-post-draft.md), [Glossarbeitrag](glossary-post.md), [Landingpage-Inhalte](landing-page-content.md) und [Produktseiten-Inhalte](product-page-content.md). Die Vorlage für Lösungsseiten steht ebenfalls beim Erstellen eines Briefs zur Verfügung, allerdings ohne eigenen Schnellstart.

Alle Vorlagen durchlaufen denselben Ablauf mit vorangehendem Brief; nur die Struktur unterscheidet sich. Ein Entwurf für eine Landingpage wird also anders geplant und geformt als ein Blogbeitrag, obwohl beide von einem [Content-Brief](content-briefs.md) ausgehen.

Wenn Sie um einen Beitrag bitten und Hi, Moose einen Brief erzeugt, geht er weiter und erzeugt den Entwurf, statt innezuhalten und darauf zu warten, dass Sie erneut fragen.

### Interne Verlinkung

Neue Entwürfe werden mit Ihrer indexierten Website abgeglichen, und passende interne Links werden dort eingefügt, wo sie wirklich hingehören. Das setzt einen aufgebauten [Suchindex](../site-monitoring/overview.md) voraus: Ohne ihn gibt es nichts zu verlinken, und Hi, Moose erfindet keine Links.

## Eine Änderung vorbereiten

Ob sie aus einem briefbasierten Entwurf, aus [FAQ](faq-generator.md), aus [Key Points](key-points.md) oder aus einer Empfehlung eines [AEO Audits](aeo-audits.md) stammt: Eine vorgeschlagene Änderung wird als **Änderungsvorschlag** vorbereitet, als dauerhaftes Artefakt und nicht als bloßer Chattext, bevor irgendetwas Ihre produktive Website berührt.

## Vorschau

Bevor Sie etwas freigeben, kann Hi, Moose eine Vorschau der vorbereiteten Änderung erzeugen, damit Sie sehen, wie sie auf der echten Seite aussehen wird. Für Änderungen, die jemand anders durchsehen soll, kann Hi, Moose einen signierten, ablaufenden Freigabelink erzeugen, sodass eine Kollegin oder eine Kundin die Änderung ohne Zugang zur Desktop-App prüfen kann.

## Freigeben und veröffentlichen

- **Freigeben**: eine vorbereitete Änderung ausdrücklich annehmen, bevor sie veröffentlicht werden kann. Vorschau und Veröffentlichung sind stets getrennte Schritte; einen Entwurf oder eine Vorschau zu erzeugen gilt nie für sich allein als „erledigt".
- **Veröffentlichen**: Nach der Freigabe veröffentlicht Hi, Moose die Änderung über die jeweilige Verbindung ([WordPress](../integrations/wordpress.md), [Webflow](../integrations/webflow.md) oder [Grav](../integrations/grav.md)) und hält fest, was wann und warum veröffentlicht wurde.

### Verhalten je CMS

**WordPress**: Entwürfe lassen sich an eine verbundene Website als vorbereitete Entwürfe übergeben, statt direkt live zu gehen, und der Veröffentlichungsablauf richtet sich danach, ob das Ziel bereits vorbereitet oder veröffentlicht ist. Haben Sie einen Entwurf einmal übergeben, merkt Hi, Moose sich das, sodass Sie denselben nicht versehentlich mehrfach übergeben.

**Webflow**: Beim Veröffentlichen in eine Collection werden zuerst deren übrige Pflichtfelder geladen und Sie werden gebeten, sie auszufüllen, damit eine Veröffentlichung nicht mitten im Ablauf an einem Feld scheitert, das Sie nicht sehen konnten.

Eine fehlgeschlagene Veröffentlichung landet in Ihrer [Inbox](../inbox/overview.md). Eine erfolgreiche bewusst nicht.

## Work Queue

In der Work Queue sammeln sich vorbereitete Änderungen, ausstehende Vorschauen und Einträge, die auf Ihre Freigabe warten, damit nichts allein in einem Chatprotokoll liegen bleibt und in Vergessenheit gerät.

## Library und Verlauf

- Die **[Library](../library/overview.md)** bewahrt die dauerhaften Artefakte auf, die Sie erzeugt haben (Briefs, Entwürfe, FAQ-Sätze, Key Points, AEO Audits), damit Sie sie wiederfinden und weiterverwenden können, statt sie neu zu erzeugen.
- **[Chats (Verlauf)](../chat/chats-history.md)** ist der Verlauf Ihrer gespeicherten Chatsitzungen: ein früheres Gespräch erneut öffnen, umbenennen oder löschen. Das ist ein Gesprächsverlauf, kein Protokoll von Veröffentlichungen oder Sichtbarkeitsergebnissen; ein eigener Nachweis, der veröffentlichte Änderungen mit dem auslösenden Sichtbarkeitssignal verknüpft, ist geplant, aber noch nicht gebaut.

## Warum das zählt

Dieser Weg aus Vorschau, Freigabe und Veröffentlichung macht aus einer Empfehlung eine abgeschlossene, nachvollziehbare Handlung. Ein Ablauf, der nur Ratschläge hervorbringt, ist unvollständig; ein Ablauf, der in einer geprüften, freigegebenen und veröffentlichten Änderung endet, verknüpft mit dem ursprünglichen Sichtbarkeitssignal, ist der eigentliche Sinn von Hi, Moose.
