---
source_hash: 807f4fd0f8157bf27491590b13dd7b2b18f5cb12dd648c025f2c46cabf3ea0ed
---
# Kontotypen und Tarife

Hi, Moose führt KI-Arbeit auf zwei Arten aus: mit Ihrem eigenen OpenRouter-Schlüssel (BYOK) oder mit den verwalteten Modellen von Hi, Moose. Diese Entscheidung, nicht der Preis, ist die eigentliche Weggabelung. Alles Weitere sind Projektanzahl, Sitzplätze und die Höhe des monatlichen Guthabens.

Die Tarife sind im Bildschirm **Upgrade** in zwei Reitern gruppiert: **Startup** und **Enterprise & Agenturen**.

## Die zwei Wege, KI auszuführen

### BYOK: eigenen Schlüssel mitbringen

Sie stellen einen [OpenRouter](https://openrouter.ai)-API-Schlüssel bereit, und die Modellaufrufe laufen **aus der Desktop-App heraus auf Ihrem Rechner** mit diesem Schlüssel. Hi, Moose leitet BYOK-Inferenz niemals über eigene Server, Ihr Schlüssel und Ihre Prompts bleiben also lokal.

Daran ändert auch ein kostenpflichtiger BYOK-Tarif nichts. Sie zahlen für mehr Arbeitsmöglichkeiten (Projekte, Sitzplätze, Gedächtnis, Workflows, Search Console), nicht dafür, dass Hi, Moose Ihre Modellaufrufe ausführt. Die Modellkosten gehen direkt an OpenRouter, und es gibt keinen Hi, Moose-Tokenzähler, den Sie im Auge behalten müssten.

### Verwaltet: Hi, Moose führt die Modelle aus

Kein API-Schlüssel. Die verwalteten Modelle von Hi, Moose übernehmen die Arbeit, und Sie verbrauchen ein monatliches **Guthaben**. Ein Zähler statt mehrerer. Die Unterstützung lokaler Modelle bleibt in jedem verwalteten Tarif als optionale Möglichkeit auf dem Gerät bestehen.

## Startup-Tarife

### Preview Mode (kostenlos)

Preview Mode ist die kostenlose Art, Hi, Moose auszuprobieren. Er ist wirklich lokal: 1 Projekt, 1 Sitzplatz, lokale Speicherung und Sichtbarkeitsläufe, die die öffentlichen KI-Suchoberflächen direkt von Ihrem Gerät aus abfragen.

- 1 Projekt, 1 Benutzersitzplatz
- Nur kostenlose und lokale LLMs
- Lokale Sichtbarkeitsläufe
- Kontextspeicherung und -abruf, Brand Voice und Styleguide
- Verbindungen: WordPress, Webflow, Grav
- Eingeschränkte Live-Such- und Wettbewerbsdaten, eingeschränkte KI-Qualität, eingeschränkte Exportoptionen

!!! warning "Preview Mode benötigt ein lokales Modell für Bewertung und Audits"
    Preview Mode enthält kein Cloud-KI-Kontingent. [AEO Audits](../features/aeo-audits.md) sowie die Bewertung von Stimmung, Narrativ und Funktionsabdeckung in [Sichtbarkeitsläufen](../visibility/overview.md) funktionieren erst, wenn Sie unter **Einstellungen → Local Model** ein lokales Gemma-4-Modell aktiviert haben. Solange keines aktiv ist, werden diese Prüfungen übersprungen statt in der Cloud ausgeführt.

### BYOK Free

Die kostenlose Art, mit Ihrem eigenen Schlüssel zu arbeiten. Derselbe Zuschnitt mit 1 Projekt und 1 Sitzplatz wie Preview Mode, aber mit Zugriff auf alle von OpenRouter angebotenen Modelle statt nur auf die kostenlosen.

- 1 Projekt, 1 Benutzersitzplatz
- Ihr eigener OpenRouter-Schlüssel, unbegrenzte Token
- Alle LLMs, einschließlich lokaler Modelle
- Sichtbarkeitsläufe ausschließlich lokal
- Verbindungen: WordPress, Webflow, Grav
- Eingeschränkte Kontextspeicherung und -abruf, eingeschränkte [Library](../library/overview.md)
- Keine Websuche im Chat, keine Workflows, keine Google Search Console

### BYOK Premium: 39 USD pro Monat oder 390 USD pro Jahr

Der vollwertige lokale Tarif und der Punkt, an dem Teamsitzplätze und der Zeitplaner freigeschaltet werden.

- 3 Projekte, zusätzliche Projekte für je 10 USD pro Monat
- Bis zu 10 Teamsitzplätze
- Vollständige Sichtbarkeitsläufe mit eigenem Zeitplaner
- Websuche aus dem Chat heraus
- Vollständige Kontextspeicherung und -abruf, vollständige [Library](../library/overview.md)
- [Workflows](../workflows/overview.md)
- Brand Voice, Styleguide und [Brand Truth Profile](context/brand-truth-profile.md)
- Verbindungen: WordPress, Webflow, Grav, [Google Search Console](../integrations/google-search-console.md)
- 15 [Audioerzeugungen](../audio/overview.md) pro Monat

### Verwaltete Tarife

Alle drei laufen mit den Modellen von Hi, Moose und enthalten unbegrenzte Teamsitzplätze, unbegrenzte Audioerzeugungen, Administrationsprotokolle mit Export sowie lokale und Cloud-Speicherung.

| Tarif | Preis | Projekte | Monatliches Guthaben | Modelle |
|---|---|---|---|---|
| Standard | 79 USD/Monat oder 849 USD/Jahr | 3 | 1.700.000 | Standardmodelle, dazu lokale |
| Professional | 129 USD/Monat oder 1.389 USD/Jahr | 5 | 3.000.000 | Alle Modelle, dazu lokale |
| Premium | 249 USD/Monat oder 2.689 USD/Jahr | 10 | 6.000.000 | Alle Modelle, dazu lokale |

## Enterprise- und Agenturtarife

### BYOK Agency: 149 USD pro Monat oder 1.490 USD pro Jahr

BYOK Premium im Agenturmaßstab. Dasselbe lokale Prinzip und derselbe Funktionsumfang, ausgelegt auf die Betreuung vieler Kunden.

- 25 Projekte, zusätzliche Projekte für je 10 USD pro Monat
- Bis zu 25 Teamsitzplätze
- 15 Audioerzeugungen pro Monat
- [White-Label-Branding](../agency/white-label.md) für Berichte und Audio-Einbettungen, wie in allen kostenpflichtigen Tarifen

### Verwaltete Agenturtarife

| Tarif | Preis | Projekte | Monatliches Guthaben | Speicherung |
|---|---|---|---|---|
| Agent Core | 449 USD/Monat oder 4.849 USD/Jahr | 25 | 15.000.000 | Team-Cloud |
| Agent Studio | 999 USD/Monat oder 10.789 USD/Jahr | 75 | 40.000.000 | Team-Cloud |
| Agent Scale | 1.999 USD/Monat oder 21.589 USD/Jahr | Unbegrenzt | 120.000.000 | Team-Cloud |

## Kurzvergleich

| | Preview Mode | BYOK Free | BYOK Premium | BYOK Agency | Verwaltete Tarife |
|---|---|---|---|---|---|
| Eigener API-Schlüssel nötig | Nein | Ja | Ja | Ja | Nein |
| Wo die Inferenz läuft | Auf Ihrem Gerät | Auf Ihrem Gerät | Auf Ihrem Gerät | Auf Ihrem Gerät | Hi, Moose-Cloud (lokal optional) |
| Projekte | 1 | 1 | 3 | 25 | 3 bis unbegrenzt |
| Teamsitzplätze | 1 | 1 | 10 | 25 | Unbegrenzt |
| Websuche im Chat | Nein | Nein | Ja | Ja | Ja |
| [Workflows](../workflows/overview.md) | Nein | Nein | Ja | Ja | Ja |
| [Google Search Console](../integrations/google-search-console.md) | Nein | Nein | Ja | Ja | Ja |
| [Audio](../audio/overview.md) | Nein | Nein | 15 pro Monat | 15 pro Monat | Unbegrenzt |
| [White-Label-Branding](../agency/white-label.md) | Nein | Nein | Ja | Ja | Ja |

## Sitzplätze, Projekte und Guthaben

**Zusätzliche Projekte** kosten in jedem kostenpflichtigen Tarif 10 USD pro Monat und Projekt. Sie fügen sie unter **Upgrade → Zusätzliche Projekte** hinzu oder entfernen sie dort.

**Sitzplätze** sind die eigentliche Grenze zwischen kostenlos und kostenpflichtig. Preview Mode und BYOK Free sind auf die Kontoinhaberin oder den Kontoinhaber beschränkt. BYOK Premium erlaubt bis zu 10, BYOK Agency bis zu 25, und die verwalteten Tarife sind unbegrenzt, weil alle Mitglieder aus dem Guthaben der Inhaberin oder des Inhabers schöpfen.

**Guthabenaufstockungen** stehen in verwalteten Tarifen zur Verfügung, wenn Ihnen mitten im Monat das Guthaben ausgeht:

- 500.000 Einheiten für 25 USD
- 2.500.000 Einheiten für 100 USD

Aufstockungen sind Einmalkäufe, keine Abonnements. Sie werden erst verbraucht, wenn Ihr Monatsguthaben aufgebraucht ist, und verfallen nie.

!!! note "Audio-Wiedergaben werden separat abgerechnet"
    Jeder Tarif mit Audio enthält zusätzlich die ersten 10.000 Wiedergaben kontoweit. Darüber hinaus werden Wiedergaben mit 5,00 USD je 10.000 pro Monat berechnet. In verwalteten Tarifen belastet auch die *Erzeugung* von Audio Ihr Guthaben.

## Gutscheine

Wenn Sie einen Rabattcode haben, geben Sie ihn beim Bezahlvorgang im Bildschirm **Upgrade** ein.

## Tarif wechseln

Sie können den Tarif jederzeit unter **Einstellungen → Konto** oder im Bildschirm **Upgrade** wechseln. Wenn Sie von einem verwalteten Tarif zu einem BYOK-Tarif wechseln, hinterlegen Sie zuerst Ihren OpenRouter-API-Schlüssel. Hi, Moose prüft den Schlüssel, bevor das KI-Routing darauf umgestellt wird.

Ihr OpenRouter-Schlüssel wird pro Konto und nicht pro Gerät gespeichert und begleitet Sie daher zu einer neuen Installation.
