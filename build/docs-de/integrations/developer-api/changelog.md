---
source_hash: 422edf700d29e3ee080f114ca1c4fbdc3f92677eb196cdf636fdac1f0e5e4cad
---
!!! note "Maschinell übersetzt"
    Diese Seite wurde von einer KI übersetzt. Maßgeblich ist die englische Fassung.

    [Auf Englisch lesen](https://himoose.com/docs/integrations/developer-api/changelog/)


# Changelog

Die Vertragsversion steht in `info.version` der [openapi.json](https://api.himoose.com/v1/openapi.json) und in der Überschrift der [Endpunkt-Referenz](reference.md). Die Basis-URL bleibt für jede hier gelistete Version `/v1`; eine inkompatible Änderung bekäme eine neue Basis-URL und eine lange Vorankündigung.

## 1.2.1, 2026-10-15

Erste öffentliche Version.

- **Lesen:** Projekte, Engines, Themen, Prompts, Wettbewerber, Läufe, Antworten mit vollem Text, Tagesstatistiken, Wettbewerberstatistiken und capabilities.
- **Tracking verwalten:** Projekte anlegen und ändern, Wettbewerber ersetzen, Prompts anlegen, ändern und löschen, Engines und Zeitplan setzen.
- **Läufe:** einen Lauf mit Kontingent-Check starten, einer nach dem anderen, 24 pro Tag, mit Idempotenz-Schlüsseln und einem abfragbaren Status.
- **Webhooks:** Ereignisse `run.completed` und `run.failed` mit HMAC-Signaturen, Wiederholungen und einem Zustellungsprotokoll.
- **Grenzen:** 300 Anfragen pro Minute und Schlüssel, 50.000 pro Tag und Konto.
- `PUT /projects/{id}/tracking` mit `engineIds` ändert nur die Standard-Engines. Bestehende Prompts behalten ihre Engines, außer `applyEnginesToPrompts` ist `true`.

## Geplant

- Tracking-Änderungen bei Plänen mit eigenem Schlüssel, deren Einstellungen heute auf dem Host-Computer liegen.
- Chancen, die priorisierte Arbeitsliste aus dem Tab Chancen.
