---
source_hash: 07b1b5e8bf746dc48362fa004a86b7566ef960fafcbe265cebb6ecd32d7aff91
---
# Google Search Console

## A cosa serve

Collegare Google Search Console perché Hi, Moose possa portare i suoi dati di rendimento della ricerca Google (impressioni, clic e query) nella stessa base locale di evidenze usata da [Visibility](../visibility/overview.md), dagli [AEO audits](../features/aeo-audits.md) e dai [brief di contenuto](../features/content-briefs.md).

!!! note "Disponibilità"
    La connessione a Google Search Console è compresa in tutti i piani a pagamento: BYOK Premium, BYOK Agency e tutti i piani gestiti. Non è compresa in BYOK Free né in Preview Mode. Veda [Tipi di account e piani](../getting-started/account-modes.md).

## Perché resta in locale

L'accesso a Search Console richiede le credenziali OAuth del suo account Google, e Hi, Moose le tratta come sensibili per scelta progettuale: l'autorizzazione avviene nel suo browser e i token che ne derivano vengono salvati **soltanto sulla sua macchina**. I servizi cloud di Hi, Moose non ricevono mai i suoi token di accesso, i token di aggiornamento o i segreti client di Google per questa connessione: l'app desktop è l'unica cosa che dialoga con Google Search Console per suo conto.

## Configurare una connessione

1. Apra **Connessioni** nell'app desktop e scelga Google Search Console.
2. Autorizzi l'accesso nel suo browser.
3. Colleghi una proprietà di Search Console al [progetto](../getting-started/projects.md) attivo.

## Che cosa può farci

- Ottenere un'istantanea locale del rendimento di pagine e query per la proprietà collegata.
- Confrontare l'ultima istantanea con una finestra precedente per cogliere i cambiamenti significativi.
- Interrogare i suoi dati di Search Console direttamente nella chat. Moose li interroga in modo agentico, restringendo il campo attraverso più query per rispondere a una domanda vaga, invece di eseguire un report fisso. Il modello interpreta la sua domanda, ma è l'app desktop a validare ed eseguire in locale ciascuna query sottostante, così i suoi dati e la custodia dei token restano sul dispositivo.
- Far confluire le evidenze di Search Console nella diagnosi della visibilità e nella scelta di quali pagine meritino un brief di contenuto o un AEO audit.

## Dove risiedono i dati

I dati di Search Console portati in Hi, Moose vengono salvati **in locale sul suo dispositivo**, non nel cloud di Hi, Moose. Fanno parte della sua base locale di evidenze e sono inclusi in un [backup locale](../getting-started/settings.md#data-backup) anziché sincronizzati tra macchine.

## Ambito attuale

Questa connessione è in sola lettura nella versione 1: Hi, Moose non scrive nulla in Search Console. Per ora si può collegare una proprietà per progetto.

Search Console richiede un piano a pagamento. Non è compresa in Preview Mode né in BYOK Free.

!!! note "Aggiorni l'app se la connessione fallisce su Windows"
    I programmi di installazione per Windows precedenti alla versione 0.3.245 venivano distribuiti senza le credenziali Google necessarie alla connessione, perciò il collegamento falliva sempre nell'app installata. L'aggiornamento risolve il problema.
