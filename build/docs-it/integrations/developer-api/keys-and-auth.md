---
source_hash: eef50f1fe484ff2af95068f006064217adac902f902e7159b98801260bb5cb9a
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/integrations/developer-api/keys-and-auth/)


# Chiavi e autenticazione

## Creare una chiave

1. Apri Hi, Moose e accedi come proprietario dell'account. Solo il proprietario può creare, vedere e revocare chiavi.
2. Vai in **Impostazioni → Hi, Moose REST API**.
3. Dai un'etichetta alla chiave, scegli i progetti che può leggere (tutti o uno), scegli quando scade e spunta i permessi di cui ha bisogno.
4. Fai clic su **Crea chiave** e copia la chiave. Viene mostrata una sola volta. Hi, Moose non può mostrarla di nuovo; se la perdi, revocala e creane una nuova.

Le chiavi iniziano con `hmk_live_` seguito da 64 caratteri. La tabella sotto il modulo elenca ogni chiave attiva con i suoi permessi, la data di creazione, l'ultimo uso e la scadenza. **Revoca** ferma una chiave subito.

Hi, Moose conserva solo un hash della chiave, come si fa con le password, quindi nessuno in Hi, Moose può risalire a una chiave.

## Una chiave per app

Crea una chiave separata per ogni app o script, con un'etichetta che dice a cosa serve. Così una chiave si può revocare senza rompere nient'altro, e la colonna **ultimo uso** nelle Impostazioni mostra quale app ha fatto le chiamate.

## Permessi

| Permesso | Cosa può fare la chiave |
|---|---|
| Leggere i dati di visibilità | Tutti gli endpoint `GET`. Sempre attivo. |
| Gestire il monitoraggio | Creare progetti, impostare termini del brand e concorrenti, aggiungere, modificare ed eliminare prompt, impostare motori e pianificazione, registrare ed eliminare webhook. |
| Avviare esecuzioni | Avviare un'esecuzione di visibilità. Le esecuzioni consumano il credito dell'account sui motori cloud, quindi assegnalo solo a una chiave che ne ha bisogno. |

Una chiamata senza il permesso necessario risponde `403 insufficient_scope` e indica il permesso. I permessi si scelgono alla creazione della chiave e non si possono cambiare dopo. Crea una nuova chiave.

Nell'API i permessi compaiono come `visibility:read`, `tracking:write` e `runs:execute`, per esempio nella risposta di `GET /me`.

## Accesso ai progetti

Una chiave legge tutti i progetti dell'account oppure un solo progetto, a scelta alla creazione della chiave. Un progetto che la chiave non può leggere risponde `404 not_found`, come un progetto che non esiste, quindi una chiave non può essere usata per scoprire quali progetti ha un account.

## Autenticazione

Invia la chiave come token Bearer nell'intestazione `Authorization` a ogni richiesta:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

La risposta indica la chiave, i suoi permessi e gli id dei progetti che può leggere. È una buona prima chiamata per verificare che una chiave funzioni.

Una richiesta senza chiave, o con una chiave malformata, revocata o scaduta, risponde `401` con uno di questi codici:

| Codice | Significato |
|---|---|
| `invalid_key` | Manca l'intestazione `Authorization`, la chiave è nel formato sbagliato, oppure Hi, Moose non la conosce |
| `key_revoked` | La chiave è stata revocata nelle Impostazioni |
| `key_expired` | La chiave ha superato la data di scadenza |

## Tieni la chiave sul tuo server

Usa la chiave solo dal tuo server. L'API non invia intestazioni CORS, quindi una pagina web non può chiamarla direttamente. Una dashboard nel browser deve chiamare il tuo backend, e il tuo backend chiama l'API. Così la chiave resta fuori dalla pagina e fuori dal registro di rete del browser.

Conserva la chiave in una variabile d'ambiente o in un gestore di segreti, mai nel controllo di versione. Se una chiave finisce in mani sbagliate, revocala nelle Impostazioni e creane una nuova. La revoca ha effetto subito.

## Scadenza

Una chiave può scadere dopo 30, 90 o 365 giorni, oppure mai. Una chiave con scadenza è la scelta più sicura per uno script che verrà sostituito; una chiave senza scadenza va bene per una dashboard di lunga durata la cui chiave vive in un gestore di segreti. La tabella nelle Impostazioni mostra la data di scadenza di ogni chiave.
