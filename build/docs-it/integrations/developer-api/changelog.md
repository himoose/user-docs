---
source_hash: 422edf700d29e3ee080f114ca1c4fbdc3f92677eb196cdf636fdac1f0e5e4cad
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/integrations/developer-api/changelog/)


# Changelog

La versione del contratto è in `info.version` di [openapi.json](https://api.himoose.com/v1/openapi.json) e nell'intestazione del [riferimento degli endpoint](reference.md). L'URL di base resta `/v1` per ogni versione elencata qui; una modifica incompatibile riceverebbe un nuovo URL di base e un lungo preavviso.

## 1.2.1, 2026-10-15

Prima versione pubblica.

- **Lettura:** progetti, motori, argomenti, prompt, concorrenti, esecuzioni, risposte con testo completo, statistiche giornaliere, statistiche dei concorrenti e capabilities.
- **Gestione del monitoraggio:** creare e modificare progetti, sostituire i concorrenti, aggiungere, modificare ed eliminare prompt, impostare motori e pianificazione.
- **Esecuzioni:** avviare un'esecuzione con verifica del credito, una alla volta, 24 al giorno, con chiavi di idempotenza e uno stato da interrogare.
- **Webhook:** eventi `run.completed` e `run.failed` con firme HMAC, nuovi tentativi e un registro delle consegne.
- **Limiti:** 300 richieste al minuto per chiave, 50.000 al giorno per account.
- `PUT /projects/{id}/tracking` con `engineIds` cambia solo i motori predefiniti. I prompt esistenti mantengono i propri motori salvo che `applyEnginesToPrompts` sia `true`.

## In programma

- Modifiche al monitoraggio nei piani con chiave propria, le cui impostazioni oggi vivono sul computer host.
- Opportunità, la coda di lavoro in ordine di priorità della scheda Opportunità.
