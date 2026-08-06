---
source_hash: a8e831ea98a893f4158e5124991eae0686f8eb64e2448fe9541f8444c4680099
---
# AEO Audits

## Wofür das gut ist

Ein AEO Audit (Prüfung der Optimierung für Antwortmaschinen) bewertet, wie gut eine Seite darauf vorbereitet ist, von KI-Systemen wie ChatGPT, Google AI Overviews, Perplexity und Gemini verstanden, abgerufen und zitiert zu werden, und liefert Ihnen anschließend einen priorisierten, belegbasierten Maßnahmenplan zur Verbesserung.

Das ersetzt vereinzelte „AEO-Tipps" durch ein dauerhaftes, vergleichbares Artefakt: Jedes Audit erzeugt eine Bewertungsübersicht und einen Maßnahmenplan, die Sie erneut aufrufen können, und spätere Audits derselben Seite zeigen, ob Ihre Änderungen die Bewertung tatsächlich bewegt haben.

## Was bewertet wird

Die Gesamtbewertung ist eine gewichtete Zusammensetzung aus acht Kategorien, jeweils von 0 bis 100 bewertet:

1. **Freshness**: Signale für Aktualität und Pflege.
2. **Structure**: Überschriften, Listen, Tabellen und Absätze, die eine Antwortmaschine auswerten kann.
3. **Semantic Clarity**: wie eng der Inhalt zu Ihrer Zielanfrage und deren Absicht passt.
4. **Extractability**: wie leicht eine Antwortmaschine eine Definition, einen Fakt oder eine Kernaussage herausziehen kann.
5. **Citation Potential**: Signale für Zuschreibung und Quellenarbeit, ermittelt aus den externen Referenzlinks der Seite.
6. **Comprehensiveness**: Abdeckung der Unterthemen, die Menschen und Antwortmaschinen bei dieser Anfrage erwarten.
7. **Trust Signals**: Stimmigkeit, Konkretheit und Differenziertheit der Aussagen in der Art, wie die Seite Zuschreibung und Quellen darstellt. Diese Kategorie prüft Aussagen nicht gegen externe Quellen: Sie misst, wie gut belegt und wie konkret die eigenen Aussagen der Seite sind.
8. **Answer Readiness**: eine direkte Antwort nahe am Seitenanfang, ein Gedanke pro Block, klare Verweissprache (kein vages „dies/es/sie") und einheitliche Benennung von Entitäten. Die Bewertung berücksichtigt die Sprache für Englisch, Deutsch, Spanisch, Französisch, Italienisch und Portugiesisch.

Das Audit erfasst außerdem Signale zu Engagement, Entity Recognition und Media Enrichment, auch wenn diese weder in die Gesamtbewertung einfließen noch in der Bewertungsübersicht erscheinen.

## Prüfungen zu Infrastruktur und Abrufbarkeit

Neben der inhaltlichen Bewertung prüft jedes Audit, ob eine Antwortmaschine die Seite überhaupt abrufen kann:

- **Zugang für KI-Crawler**: prüft die robots.txt-Regeln für jeden der spezifischen KI-Crawler-Bezeichner von OpenAI, Anthropic, Perplexity, Google und Bing (Trainings-, Indexierungs- und Live-Abruf-Crawler jeweils getrennt, denn eine Website kann den einen sperren und den anderen zulassen). Ein gesperrter Abruf- oder Indexierungs-Crawler wird als kritisch gekennzeichnet; ein gesperrter Live-Abruf-Agent hat mittlere Priorität; eine reine Trainingssperre wird als legitime, neutrale Entscheidung vermerkt, die Zitierungen nicht beeinflusst.
- **Serverseitiges Rendern und Erkennung clientseitig gerenderter Hüllen**: Die meisten KI-Crawler führen kein JavaScript aus. Erscheinen die wesentlichen Inhalte einer Seite erst nach clientseitigem Rendern, wird das als kritischer, hervorgehobener Befund gekennzeichnet und nicht als technische Randnotiz, denn es ist ein Abrufproblem, das jeder inhaltlichen Optimierung vorausgeht.
- **Abrufhygiene**: prüft eine Stichprobe interner Links auf tote Links und Weiterleitungsketten.
- **Vorhandensein im Bing-Index**: prüft, ob die Seite bei Bing indexiert zu sein scheint, denn Microsoft Copilot und Teile der ChatGPT-Suche stützen sich auf den Bing-Index. Die Urteile sind bewusst zurückhaltend: Ein nicht eindeutiges Ergebnis wird als nicht eindeutig gemeldet statt geraten, und das Urteil „nicht gelistet" erscheint nur, wenn die Prüfung dafür ein belastbares Signal hat.

## Externer Kontext und Abdeckung

- **Zitierlandschaft**: Läuft eine Live-Recherche, meldet das Audit, welche Domains eine Antwortmaschine für die Zielanfrage tatsächlich zitiert hat, ob die geprüfte Website darunter ist und ob Drittquellen (Community-Seiten, Bewertungsportale, Wikipedia, YouTube) die Antwort dominieren. Das wird als Kontext ausgewiesen, den Sie durch Bearbeiten Ihrer eigenen Seite kaum beeinflussen können, und fließt nicht in die Bewertung ein.
- **Ihr eigener Sichtbarkeitsverlauf**: Wurde die geprüfte URL in Ihren jüngsten [Sichtbarkeitsläufen](../visibility/overview.md) zitiert, bezieht das Audit das ein, damit die Empfehlungen berücksichtigen, wie sich die Seite in KI-Antworten bereits schlägt, statt sie als Unbekannte zu behandeln. Fehlgeschlagene Läufe bleiben dabei außen vor, damit ein Ausfall nicht als Fehlen von Zitierungen gelesen wird.
- **Fan-out-Abdeckung**: gleicht die Seite mit verwandten Anfragen ab, zu denen eine Antwortmaschine die ursprüngliche Anfrage erweitern könnte (Fragen aus „Ähnliche Fragen", verwandte Suchen, sekundäre Suchbegriffe). Werden mehrere davon auf der Seite nicht behandelt, wird daraus eine konkrete Empfehlung, diese verwandten Fragen abzudecken.

## Belegstufen bei Empfehlungen

Jedes Problem und jede Empfehlung ist danach gekennzeichnet, wie belastbar die zugrunde liegende Evidenz ist:

- **Proven**: Abrufvoraussetzungen mit starker empirischer Grundlage (Crawler-Zugang, serverseitiges Rendern, funktionierende Links, Indexierung durch Suchmaschinen).
- **Directional**: gestützt auf breit angelegte Beobachtungsforschung, aber ohne Garantie (Antwort zuerst platzieren, Aktualität, strukturelle Klarheit).
- **Best-practice**: plausibel und günstig umzusetzen, aber ohne Nachweis, dass sie KI-Zitierungen bewegen (Statistiken, Zitate oder zusätzlicher Feinschliff bei den Quellen).

Das Audit empfiehlt weder Schema-/JSON-LD-Markup noch `llms.txt`-Dateien noch Keyword-Stuffing als Mittel zur Verbesserung von KI-Zitierungen, da die aktuelle Forschung es nicht rechtfertigt, sie als Hebel für Zitierungen zu behandeln.

## Wie viele Empfehlungen Sie erhalten

Die Anzahl der Empfehlungen richtet sich danach, wie viele echte Probleme gefunden werden, gewichtet mit der Gesamtbewertung der Seite: Eine Seite mit echten Problemen erhält mehr Empfehlungen, eine bereits gut bewertete weniger, manchmal gar keine. Die Anzahl wird nie künstlich aufgefüllt, um eine feste Zielgröße zu erreichen.

## Ein Audit ausführen

1. Geben Sie eine produktive URL an oder fügen Sie einen Entwurf ein, dazu die Zielanfrage, mit der jemand diesen Inhalt finden würde.
2. Hi, Moose erstellt eine abgegrenzte Momentaufnahme von Inhalt und Struktur der Seite und verwendet dabei die statische Fassung (ohne JavaScript-Rendering) als Hauptbeleg, denn sie kommt dem am nächsten, was die meisten KI-Crawler tatsächlich sehen.
3. Wo es hilfreich ist, sammelt Hi, Moose echte Belege aus Antwortmaschinen oder Zitierungen zur Zielanfrage.
4. Verfügt Ihr Projekt über eine verbundene [Google-Search-Console](../integrations/google-search-console.md)-Property für diese URL, fließen Ihre eigenen Suchdaten in die Priorisierung und in die Vorsicht der Empfehlungen ein. Die zugrunde liegende AEO-Bewertung ändert sich dadurch nicht.
5. Hi, Moose bewertet die Seite, legt eine Referenz an (oder prüft gegen eine frühere Referenz) und setzt das Audit zu einem dauerhaften Artefakt mit ausdrücklichem Maßnahmenplan zusammen.

## Verbesserung überprüfen

Da jedes Audit als Referenz gespeichert wird, erzeugt ein erneutes Audit derselben Seite nach Änderungen ein **Prüfergebnis**, das zeigt, ob sich die Bewertung tatsächlich verbessert hat, und nicht bloß, ob Sie etwas bearbeitet haben.

## Integrität

AEO Audits erfinden niemals Belege. Kann Hi, Moose die Belege nicht sammeln oder einen Bewertungsschritt nicht wirklich abschließen, schlägt das Audit ausdrücklich fehl und nennt den Grund, statt eine Vermutung als fertiges Ergebnis auszugeben. Lassen sich Live-Recherche und Wettbewerbsanalyse bei einem kostenpflichtigen verwalteten Audit nicht abschließen, wird das Audit dennoch mit den vorhandenen Seitenbelegen fertiggestellt, samt ausdrücklichem Hinweis, dass für diesen Lauf keine Live-Recherche verfügbar war.

## Berechtigungen je Tarif

- **Preview Mode (kostenlos)** führt Audits auf einem aktivierten lokalen Gemma-4-Modell aus. Ein kostenloses monatliches Kontingent für Cloud-Audits gibt es nicht mehr: Richten Sie ein [lokales Modell](../getting-started/settings.md#local-model) ein, und Audits sind kostenfrei, so oft Sie möchten.
- **BYOK-Tarife** führen Audits lokal mit Ihrem eigenen OpenRouter-Schlüssel aus.
- **Verwaltete Tarife** nutzen die verwalteten Modelle von Hi, Moose über das übliche Guthaben Ihres Kontos. Eine gesonderte Währung „Audit-Guthaben" gibt es nicht.

## Nächste Schritte nach einem Audit

Der Maßnahmenplan eines Audits führt direkt in andere Funktionen: einen [Content-Brief](content-briefs.md) erstellen, eine [Änderung samt Vorschau](drafts-and-publishing.md) vorbereiten oder FAQ beziehungsweise Key Points ergänzen. Das Audit ist damit ein Ausgangspunkt zum Handeln und nicht bloß ein Bericht.
