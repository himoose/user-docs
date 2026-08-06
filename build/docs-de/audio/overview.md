---
source_hash: 3de48b1823942dd1ca44b6be6cf581f170fdffe9e0e850d467f3322e9e89f1a8
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/audio/overview/)

# Audio

## Wofür das gut ist

Einen Artikel in ein Gespräch mit zwei Stimmen verwandeln und anschließend die MP3-Datei herunterladen oder den Player auf Ihrer Website einbetten. Der Player bringt eine Transkription mit, die der Seite echten, eigenen und crawlbaren Text hinzufügt: Inhalt, den eine Antwortmaschine abrufen kann.

Audio liegt in der Desktop-App unter **Audio** in der Seitenleiste und ist in drei Reiter geteilt: **Generate**, **History** und **Analytics**.

!!! note "Audio ist aus der früheren Web-App umgezogen"
    Die Audioerzeugung lag früher unter `app.himoose.com` als „Listen to this Article". Sie ist jetzt vollständig Teil der Desktop-App, mit projektbezogener Abgrenzung, Hörstatistiken und einer Player-Anpassung, die es in der Webfassung nicht gab.

## Bevor Sie beginnen

Hinterlegen Sie zuerst die Website des Projekts. Die Wiedergabe ist auf Ihre Projektdomain und `himoose.com` beschränkt, Hi, Moose muss die Domain also kennen, bevor überhaupt etwas erzeugt wird. Ist sie nicht hinterlegt, zeigt der Reiter Generate statt des Editors den Hinweis **Set website**.

Die Verfügbarkeit von Audio hängt von Ihrem [Tarif](../getting-started/account-modes.md) ab: BYOK Premium und BYOK Agency enthalten 15 Erzeugungen pro Monat, verwaltete Tarife sind unbegrenzt, und die kostenlosen Tarife enthalten kein Audio.

## Eine Quelle wählen

Drei Wege, Inhalte einzubringen:

- **Artikel-URL**: Fügen Sie eine veröffentlichte URL ein und klicken Sie auf **Fetch**. Hi, Moose extrahiert den Inhalt und zeigt Domain, Wortzahl und geschätzte Lesezeit. Der Artikel muss öffentlich erreichbar sein, nicht hinter einer Anmeldung oder Bezahlschranke.
- **Text einfügen**: Geben Sie der Folge einen Titel und fügen Sie das Skript oder den Artikeltext direkt ein.
- **Datei hochladen**: Legen Sie eine `.txt`-, `.md`-, `.docx`-, `.doc`- oder `.pdf`-Datei ab. Die Datei wird auf Ihrem Gerät gelesen, und ihr Text landet im Einfüge-Ablauf.

## Das Gespräch formen

**Focus** (optional) lenkt, worauf das Gespräch vertiefend eingeht. Es gibt Vorschläge für die üblichen Blickwinkel: zentrale Erkenntnisse, für Einsteiger erklären, dem Argument widersprechen, für wen das relevant ist.

**Length** legt die angestrebte Laufzeit fest:

| Länge | Zeit | Ungefähres Skript |
|---|---|---|
| Short | 4-5 Min. | ~700 Wörter |
| Standard | 8-10 Min. | ~1.400 Wörter |
| Deep dive | 15-18 Min. | ~2.600 Wörter |

**Language** folgt standardmäßig der Sprache des Artikels. Ändern Sie die Einstellung, um Skript und Stimmen zugleich umzustellen.

**Voices** kommen als Paarungen aus Gastgeber und Gast, mit drei Voreinstellungen (warm und neugierig, ruhig und analytisch, hell und skeptisch) oder einer selbst gewählten Paarung.

## Erweiterte Regieanweisungen

Optional, und alles, was Sie leer lassen, folgt dem Artikel und der Stimmpaarung. Sieben Felder stehen zur Verfügung: Regie für Gastgeber, Regie für Gast, Szene, Stil, Tempo, Akzent und zusätzlicher Kontext.

- **Szene**: Studiointerview, Kamingespräch, Podiumsdiskussion, Hörertelefonat, Gespräch im Gehen
- **Stil**: erklärend, Streitgespräch, erzählend, Interview, locker
- **Tempo**: langsamer, natürlich, schneller
- **Akzent**: amerikanisch (neutral), britisch, australisch, irisch, indisch oder international neutral

Jedes dieser Felder lässt sich durch eine eigene Beschreibung in Ihren Worten ersetzen.

**Zusätzlicher Kontext** ist für das gedacht, was der Artikel nicht sagt: wie ein Produktname auszusprechen ist, welche Aussagen zu vermeiden sind, wer das Publikum ist.

!!! warning "Kontext lenkt den Ton, nicht die Fakten"
    Hi, Moose erfindet keine Fakten, um einer Anweisung zu genügen. Zusätzlicher Kontext verändert Rahmung und Vortrag; er fügt keine Belege hinzu, die nicht in der Quelle stehen.

Haben Sie Einstellungen gefunden, die Ihnen zusagen, übernimmt **Save as project default** sie für die nächste Folge dieses Projekts.

## Erzeugen

Klicken Sie auf **Generate audio**. Der Editor nennt vorab eine geschätzte Renderzeit. Die Erzeugung läuft im Hintergrund, Sie können den Bildschirm also verlassen und weiterarbeiten: Die fertige Folge erscheint in der Liste **Recents** der Seitenleiste, und ein Klick öffnet sie direkt.

Ist sie fertig, erhalten Sie:

- Einen Player mit Suchlauf, 15-Sekunden-Sprüngen vor und zurück sowie Abspielgeschwindigkeit
- **Download MP3**
- **Share**, um den Audiolink zu kopieren
- Die vollständige **Transkription**, mit Anzahl der Sprechwechsel und Wörter, samt Kopierschaltfläche
- **Embed on your site**, beschrieben unter [Player und Einbettung](player-and-embed.md)
- **Regenerate with edits** und **Edit settings**, um die Regie anzupassen und erneut zu erzeugen

## History

Der Reiter **History** listet jede Folge des aktuellen Projekts mit Länge, Erstellungsdatum und Status. Folgen sind projektbezogen abgegrenzt: Ein Projektwechsel ändert also, was Sie sehen.

- Folgen nach Namen durchsuchen
- Nach **All**, **Ready** oder **Needs attention** filtern
- Abspielen, herunterladen, die Einbettungsoptionen öffnen oder die vollständige Folge öffnen
- Eine fehlgeschlagene Folge **erneut versuchen**

Die Status lauten Ready, Processing, Playing, Failed und Canceled.

## Wie es weitergeht

- **[Player und Einbettung](player-and-embed.md)**: Design, Layout, Akzentfarbe und Einbettungscode.
- **[Hörstatistiken](analytics.md)**: was geschieht, sobald der Player auf einer Seite steht.
