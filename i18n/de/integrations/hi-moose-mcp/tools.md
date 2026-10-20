---
source_hash: 9f28cef13a975ad78da4716aa179f501b7552d5e70ee5517e47c8582b3e9d005
---

# Werkzeug-Referenz

Jedes Werkzeug, das Hi, Moose MCP einer verbundenen App anbietet, mit dem, was es braucht und was zurückkommt. Sie rufen Werkzeuge nicht selbst auf: Die App wählt das Werkzeug anhand Ihrer Anfrage. Diese Seite sagt Ihnen, was Sie anfragen können und was Sie erwarten dürfen.

Jedes Werkzeug außer `list_projects` und `get_result` braucht ein **Projekt**, mit dem Namen, der in Hi, Moose angezeigt wird. Nennen Sie den Projektnamen in Ihrer Anfrage, wenn Sie mehr als ein Projekt haben, zum Beispiel „für das Projekt Acme“.

## Wie lange etwas dauert

| Werkzeug | Übliche Dauer |
|---|---|
| Projekte, Briefings, Entwürfe auflisten | Wenige Sekunden |
| Site-Abdeckung prüfen | Unter einer Minute |
| Sichtbarkeitsfrage, eine Antwort lesen | Wenige Sekunden |
| Chancenliste | Wenige Sekunden bis eine Minute |
| Content-Briefing, Entwurf, FAQs, Kernaussagen, Beitragsbild | Ein bis drei Minuten |
| AEO-Audit | Zwei bis vier Minuten |
| Inhaltsaktualisierung | Drei bis sechs Minuten |
| Interne Links | Etwa eine Minute |
| Audio-Episode | 5 Minuten für kurz, 9 für standard, 15 für ausführlich |

Dauert ein Werkzeug länger, als die App wartet, antwortet es mit „läuft noch“ und einer Auftrags-ID. Die App holt die fertige Arbeit dann mit `get_result` ab; bitten Sie sie, erneut nachzusehen, falls sie es nicht tut.

## Projekte und Library

### list_projects

Listet die Hi, Moose-Projekte, an denen Sie arbeiten können. Jedes andere Werkzeug braucht ein Projekt, die App ruft das also meist zuerst auf.

Fragen Sie: „Liste meine Hi, Moose-Projekte auf.“

### list_briefs

Listet die in der Library gespeicherten Content-Briefings eines Projekts, neueste zuerst, bis zu 50. Nutzen Sie es, wenn Sie sich auf ein früher erstelltes Briefing beziehen.

Fragen Sie: „Zeige die gespeicherten Briefings für Acme.“

### list_drafts

Listet die in der Library gespeicherten Entwürfe eines Projekts, neueste zuerst, bis zu 50.

Fragen Sie: „Welche Entwürfe habe ich in Acme?“

### get_result

Holt Arbeit ab, die ein anderes Werkzeug gestartet hat, per Auftrags-ID. Wartet bis zu einer Minute auf den Abschluss. Die App ruft das von selbst auf; Sie brauchen es nur, wenn die App sagt, die Arbeit laufe noch, und Sie sie erneut nachsehen lassen wollen.

## Site-Abdeckung

### check_site_coverage

Prüft den letzten Crawl Ihrer Website auf Seiten, die ein oder mehrere Themen schon abdecken.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| topics | ja | Eine bis fünfzehn kurze Formulierungen, etwa „SBOM-Erstellung für Python“ |
| parentTopic | nein | Das übergeordnete Thema, zu dem die Themen gehören, zur Bewertung teilweiser Abdeckung |

Für jedes Thema antwortet es mit **covered**, **partial**, **uncovered** oder **unknown**, mit den nächstliegenden Seiten-URLs als Beleg und dem Datum des geprüften Crawls. Unknown heißt, dass die Prüfung für dieses Thema nicht laufen konnte, nicht, dass die Website es nicht hat.

Fragen Sie: „Deckt unsere Website SCA vs. SAST schon ab?“

## Content

### create_content_brief

Erstellt ein suchbasiertes Content-Briefing: Ziel, Zielgruppe, Begründung, Keyword-Gruppen, empfohlene Struktur und Vorgaben, gestützt auf Live-Suchergebnisse, Ihren Site-Crawl, Markenrichtlinien und Brand Truth.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| topic | ja | Das Thema, die Frage oder der Arbeitstitel, bis zu 400 Zeichen |
| targetUrl | nein | Die Seite Ihrer Website, für die das Briefing ist |
| templateType | nein | Die Art des Inhalts: „Blog post“, „Landing page“, „Comparison page“, „Guide“ |
| guidance | nein | Anderswo festgelegte Anforderungen: Blickwinkel, Pflichtpunkte, Tonalität. Bis zu 4.000 Zeichen. |

Gibt das Briefing als Text zurück plus eine Briefing-ID, die das Entwurfs-Werkzeug nutzt. Wird in der Library gespeichert.

Fragen Sie: „Schreibe ein Content-Briefing für einen Leitfaden zur SBOM-Erstellung für Python-Teams.“

### create_draft

Schreibt einen veröffentlichungsreifen ersten Entwurf aus einem Briefing, in der Stimme Ihrer Marke, gestützt auf das Briefing, Brand Truth und Markenrichtlinien, mit internen Links aus Ihrem Site-Crawl und einem Feinschliff.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| briefId | eines von beiden | Ein in Hi, Moose erstelltes Briefing |
| brief | eines von beiden | Ein anderswo geschriebenes Briefing, als Text, bis zu 60.000 Zeichen |
| briefTitle | nein | Der Arbeitstitel, wenn ein Briefing als Text übergeben wird |
| templateType | nein | Die Art des Inhalts, wenn ein Briefing als Text übergeben wird |
| guidance | nein | Zusätzliche Anforderungen, bis zu 4.000 Zeichen |

Gibt den Entwurf als Text zurück plus eine Entwurfs-ID. Wird in der Library gespeichert.

Fragen Sie: „Schreibe den Artikel aus diesem Briefing.“ oder „Hier ist ein Briefing, das ich geschrieben habe, entwirf es für Acme: ...“

### refresh_content

Aktualisiert Inhalte, die Sie bereits haben. Hi, Moose liest den aktuellen Inhalt, ermittelt die Suchanfrage, auf die er abzielt (oder nutzt die von Ihnen genannte), führt dieselbe Live-Recherche wie für ein Content-Briefing zu dieser Anfrage durch und vergleicht beides: was noch funktioniert, was veraltet wirkt, welche Fakten zu aktualisieren sind, was die rankenden und zitierten Seiten abdecken und Ihr Inhalt nicht, und welche Fragen Suchende stellen, die er nicht beantwortet.

| Eingabe | Erforderlich | Bedeutung |
|---|---|---|
| url | eine von dreien | Die veröffentlichte Seite. Am besten, denn dann vergleicht Hi, Moose genau das, was online ist. |
| draftId | eine von dreien | Ein gespeicherter Entwurf |
| content | eine von dreien | Der aktuelle Inhalt als Text, bis zu 60.000 Zeichen |
| title | nein | Der Titel, wenn Sie den Inhalt als Text übergeben |
| targetQuery | nein | Die Frage oder Suchanfrage, die der aktualisierte Inhalt gewinnen soll, bis zu 200 Zeichen. Ohne Angabe ermittelt Hi, Moose die Hauptanfrage aus dem Inhalt und nennt sie im Ergebnis. |
| templateType | nein | Die Art des Inhalts, etwa „Blogbeitrag“ oder „Landingpage“ |
| guidance | nein | Vorgaben für die Aktualisierung: Abschnitte, die bleiben sollen, Punkte, die dazukommen sollen, Tonalität. Bis zu 4.000 Zeichen. |

Liefert zwei Dinge, beide in der Library gespeichert: ein Aktualisierungs-Briefing (den Vergleich, eine Änderungsliste und ein vollständiges Content-Briefing für die aktualisierte Fassung) und einen überarbeiteten Entwurf, der Struktur, Tonfall und Links beibehält und die Änderungen umsetzt. Laden Sie das Briefing aus der Library als PDF, Word oder Markdown herunter, wenn Sie die Aktualisierung intern begründen müssen.

Fragen Sie: „Aktualisiere https://acme.example/guides/sbom.“ oder „Dieser Artikel ist zwei Jahre alt, aktualisiere ihn für ‚SBOM-Tools‘: ...“

### create_featured_image

Erstellt ein Beitragsbild für einen Artikel, 1200 mal 630, in Ihrem gespeicherten Bildstil, wenn einer festgelegt ist.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| draftId | eines von beiden | Ein in Hi, Moose erstellter Entwurf |
| title und summary | eines von beiden | Der Artikeltitel und eine kurze Zusammenfassung, bis zu 6.000 Zeichen, wenn es keinen Entwurf gibt |
| styleIntent | nein | Ein Wunsch für dieses eine Bild: Stimmung, Szene, Farben. Der gespeicherte Stil gilt weiterhin. |

Gibt das Bild und einen Link zur PNG zurück. Die Datei wird auch auf dem Host-Gerät gespeichert.

Fragen Sie: „Erstelle ein Beitragsbild für diesen Entwurf, Abendlicht, keine Personen.“

### create_faqs

Schreibt häufig gestellte Fragen mit Antworten für einen Inhalt, in der Stimme Ihrer Marke, plus FAQPage-Schema-Markup zum Einfügen in die Seite. Bei bezahlten Konten werden die Fragen zuerst aus echtem Suchverhalten recherchiert.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| draftId | eines von beiden | Ein gespeicherter Entwurf |
| url | eines von beiden | Eine veröffentlichte Seite Ihrer Website |
| guidance | nein | Zielgruppe, Fragen, die vorkommen müssen, Tonalität. Bis zu 4.000 Zeichen. |

Fragen Sie: „Schreibe FAQs für https://acme.example/guides/sbom.“

### create_key_points

Schreibt die Kernaussagen eines Inhalts: kurze, zitierfähige Aussagen in der Stimme Ihrer Marke, die Answer Engines übernehmen können.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| draftId | eines von beiden | Ein gespeicherter Entwurf |
| url | eines von beiden | Eine veröffentlichte Seite Ihrer Website |
| guidance | nein | Zielgruppe, Punkte, die vorkommen müssen, Tonalität. Bis zu 4.000 Zeichen. |

Fragen Sie: „Gib mir Kernaussagen für den Entwurf des SBOM-Leitfadens.“

## Audits und Links

### run_aeo_audit

Führt ein Audit zur Answer Engine Optimization für einen Inhalt aus: eine Bewertung von 100, Bewertungen je Kategorie (Struktur, Extrahierbarkeit, Zitierpotenzial, Vertrauenssignale, Aktualität, Antwortbereitschaft und mehr), die gefundenen Probleme und konkrete Änderungen mit Textvorschlägen.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| url | eines von dreien | Eine Live-Seite. Am besten, weil technische Prüfungen wie der Zugriff für KI-Crawler und Seitendaten nur auf einer Live-Seite laufen. |
| draftId | eines von dreien | Ein gespeicherter Entwurf |
| content | eines von dreien | Der Inhalt als Text, für eine Seite, die noch nicht live ist. Bis zu 50.000 Zeichen. |
| targetQuery | nein | Die Frage oder der Suchprompt, den der Inhalt gewinnen soll, bis zu 200 Zeichen. Ohne Angabe leitet Hi, Moose einen ab. |

Bei bezahlten Konten werden Belege aus der Live-Suche einbezogen.

Fragen Sie: „Prüfe https://acme.example/guides/sbom für die Suchanfrage ‚SBOM generation tools‘.“

### find_internal_links

Plant interne Links für einen Inhalt anhand des Crawls Ihrer eigenen Website. Gibt zwei Listen zurück: Seiten, auf die dieser Inhalt verlinken sollte, jeweils mit dem zu verwendenden Ankertext, und bestehende Seiten, die einen Link auf diesen Inhalt setzen sollten, jeweils mit dem Ankertext für diese Seite. Seiten, die in eine der beiden Richtungen schon verlinkt sind, werden ausgelassen.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| url | eines von dreien | Eine Seite Ihrer Website, live |
| draftId | eines von dreien | Ein gespeicherter Entwurf |
| content | eines von dreien | Der Inhalt als Text, bis zu 50.000 Zeichen |
| title | nein | Der Titel, wenn der Inhalt als Text übergeben wird |

Die Ergebnisse umfassen die bisher gecrawlten Seiten und nennen das Crawl-Datum. Seiten, die seit dem letzten Crawl veröffentlicht wurden, sind nicht enthalten.

Fragen Sie: „Plane interne Links für den Entwurf des SBOM-Leitfadens.“

## KI-Suchsichtbarkeit

### visibility_check_topic

Beantwortet „Erscheinen wir in der KI-Suche zu X?“ aus den Sichtbarkeitsergebnissen, die Hi, Moose gespeichert hat. Stellen Sie die Frage in Ihren eigenen Worten; Hi, Moose ordnet sie den verfolgten Prompts zu, in jeder Sprache.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| question | ja | Das Thema oder die Frage, bis zu 400 Zeichen |
| lookbackDays | nein | Wie viele Tage gespeicherter Ergebnisse gelesen werden. Standard 90. |
| engine | nein | Nur diese Engine, nach Name, etwa „ChatGPT“ |

Gibt je Engine zurück, ob die Marke im letzten Lauf und in einem früheren Lauf erwähnt oder zitiert wurde, die Erwähnungs- und Zitierraten über den Zeitraum, einen kurzen Auszug aus der letzten Antwort, in der die Marke erschien, die zugeordneten Prompts und andere gesehene Marken. Jeder Auszug trägt eine Antwort-ID für das nächste Werkzeug. Die Ergebnisse umfassen nur die verfolgten Prompts auf den verfolgten Engines, nie die gesamte KI-Suche. Es liest gespeicherte Ergebnisse und führt nie neue Prüfungen aus.

Fragen Sie: „Erscheinen wir in der KI-Suche zu SBOM-Erstellung?“

### visibility_get_answer

Holt eine gespeicherte Antwort per Antwort-ID: den Prompt, die Engine, das Datum, ob die Marke erwähnt oder zitiert wurde, die von der Engine gelisteten Quellen, die Notizen der Bewertung und den vollständigen Antworttext. Der Text ist das, was die Engine damals geschrieben hat.

Fragen Sie: „Zeige mir die vollständige ChatGPT-Antwort aus diesem Ergebnis.“

### visibility_list_opportunities

Gibt die priorisierte Arbeitsliste zurück, die Hi, Moose aus gespeicherten Sichtbarkeitsergebnissen baut, dieselben Zeilen wie der Tab Chancen. Jede Zeile nennt die genaue Lücke, den nächsten Schritt in einem Satz, die Priorität mit ihren Gründen, wie beständig die Lücke über Läufe hinweg war, den Aufwand, den vom Team gesetzten Status und eine Chancen-ID.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| lookbackDays | nein | Tage gespeicherter Ergebnisse, die gelesen werden. Standard 7, wie im Tab Chancen. Höchstens 90. |
| limit | nein | Zurückgegebene Zeilen, beste zuerst. Standard 10, höchstens 25. |
| action | nein | Nur eine Art von Zeile: `create-coverage`, `improve-page`, `earn-inclusion`, `correct-description` oder `investigate-change` |
| priority | nein | `high`, `medium` oder `low` |
| includeClosed | nein | Auch Zeilen zurückgeben, die als erledigt, verworfen oder zurückgestellt markiert sind. Standard false. |
| opportunityId | nein | Eine ID aus einem früheren Ergebnis. Gibt statt der Liste die vollständigen Belege für diese eine Zeile zurück. |

Die fünf Arten von Zeilen: **create-coverage** (keine Ihrer Seiten beantwortet einen Prompt, den Wettbewerber gewinnen), **improve-page** (eine Ihrer Seiten wird zitiert oder ist der nächstliegende Treffer, aber die Marke fehlt oder liegt hinten), **earn-inclusion** (eine Drittseite, die die Engines zitieren, nennt Wettbewerber, aber nicht Sie), **correct-description** (Antworten wiederholen eine Aussage über die Marke, die geprüft werden muss) und **investigate-change** (die Marke wurde früher genannt oder zitiert und jetzt nicht mehr).

Fragen Sie: „Woran sollen wir diese Woche für die KI-Suche arbeiten?“ und dann „Zeige mir die Belege für die erste.“

## Audio

### create_audio

Erstellt eine Episode „Diesen Artikel anhören“: ein gesprochenes Gespräch mit zwei Stimmen über den Inhalt, als MP3 gerendert und von Hi, Moose gehostet, plus das HTML-Snippet für den einbettbaren Player.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| url | eines von dreien | Eine Live-Seite |
| draftId | eines von dreien | Ein gespeicherter Entwurf |
| content und title | eines von dreien | Der Artikel als Text, 1.200 bis 200.000 Zeichen, mit seinem Titel |
| length | nein | `short` (etwa 4 Minuten), `standard` oder `deep`. Standard short. |
| hostVoice, guestVoice | nein | Zwei verschiedene Stimmen. Standard Sulafat und Fenrir. |
| language | nein | Sprache der Erzählung. Standard: die Sprache des Inhalts. |
| focus | nein | Worauf sich das Gespräch konzentrieren soll, bis zu 500 Zeichen |
| theme, layout, color, showTitle, customTitle, showTranscript, hideAttribution | nein | Das Aussehen des Players, siehe unten |

Auf der [Audio-Einstellungsseite](https://himoose.com/hi-moose-mcp/audio/) können Sie jede Stimme anhören, Länge, Sprache und das Aussehen des Players wählen und eine Einstellungszeile kopieren, die Sie in den Chat einfügen. Während die Episode rendert, arbeitet das Host-Gerät an nichts anderem. Sagt das Ergebnis, die Episode rendere noch, holt das nächste Werkzeug sie ein paar Minuten später ab.

Fragen Sie: „Mach aus https://acme.example/guides/sbom eine Audio-Episode, kurz, mit Zephyr und Charon.“

### get_audio_embed

Gibt das Player-Snippet für eine vorhandene Episode zurück, mit neuem Aussehen, wenn Player-Felder übergeben werden. Das Audio wird nicht neu gerendert. Auch der Weg, eine Episode abzuholen, die noch gerendert wurde.

| Eingabe | Pflicht | Bedeutung |
|---|---|---|
| audioId | ja | Die ID der Episode |
| theme | nein | `dark`, `light` oder `auto`. Standard dark. |
| layout | nein | `full` oder `compact`. Standard full. |
| color | nein | Akzentfarbe als Hex, zum Beispiel `#5688b0` |
| showTitle, customTitle | nein | Eine Titelzeile anzeigen oder einen eigenen Titel setzen |
| showTranscript | nein | Den Transkript-Knopf anzeigen. Standard true. |
| hideAttribution | nein | Die Zeile „Audio by Hi, Moose“ ausblenden. Nur in bezahlten Plänen. |

Fragen Sie: „Gib mir den kompakten hellen Player für diese Episode.“

## Was die Werkzeuge nicht können

Sie können keine Einstellungen oder Teammitglieder ändern, nicht ändern, was Hi, Moose verfolgt, keine Sichtbarkeitsläufe starten und nichts löschen. Für Dashboards und Automatisierung nutzen Sie die [Hi, Moose API](../developer-api.md).
