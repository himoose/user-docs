---
source_hash: f262de43811a037ebe40f0f411828409a4bc1eda0f592f12d08358e5530d41e6
---

# Sicurezza e trattamento dei dati

Questa pagina è per le persone che esaminano un connettore prima che un team lo colleghi. Descrive come funziona oggi Hi, Moose MCP, nell'ordine in cui di solito chiede una revisione di sicurezza. Ultima verifica sul server in produzione: 2026-10-19.

## Risposte brevi

| Domanda | Risposta |
|---|---|
| Chi gestisce il server? | Hi, Moose, il produttore dell'app. Non una terza parte. |
| L'elenco degli strumenti può cambiare dopo il collegamento? | No. Gli strumenti sono codice fisso. L'elenco esatto è pubblicato con un hash su [mcp.himoose.com/tools.json](https://mcp.himoose.com/tools.json). |
| Come accedono le persone? | OAuth 2.1, il flusso standard per MCP remoto, con il loro account Hi, Moose esistente. Nessuna chiave API. |
| Quanto durano i token? | I token di accesso un'ora. I token di aggiornamento scadono dopo 30 giorni senza uso, al massimo 90 giorni. |
| Possiamo revocare l'accesso? | Sì, per app, in Hi, Moose sotto **Impostazioni → Hi, Moose MCP**. |
| Cosa può cambiare un'app collegata? | Lavoro sui contenuti e letture dentro i progetti dell'account collegato. Non può pubblicare, eliminare, né cambiare impostazioni, membri del team o tracciamento. |
| Raggiunge qualcosa fuori da Hi, Moose? | No. Non vede mai le chat, i file, i repository o gli altri connettori dell'app da cui viene usata. |
| Dove viene eseguito il lavoro? | Nell'app Hi, Moose su un dispositivo che scegli tu, il dispositivo host. |
| Il testo esterno nei risultati è contrassegnato? | Sì. I passaggi di pagine e le risposte dei motori di IA tornano tra marcatori etichettati come dati, non istruzioni. |
| Dove segnaliamo un problema? | [legal@himoose.com](mailto:legal@himoose.com), oppure la [pagina dei contatti](https://himoose.com/it/contact/). |

## Chi gestisce il server

Hi, Moose MCP è costruito e gestito da Hi, Moose. È l'unico server MCP che raggiunge un account Hi, Moose, e non è un server della community né di terze parti. L'indirizzo del server è:

```text
https://mcp.himoose.com/mcp
```

Il server in sé è piccolo. Gestisce l'accesso e i token, offre l'elenco degli strumenti e passa ogni richiesta al cloud di Hi, Moose, che la consegna al dispositivo host. Il lavoro, come leggere la scansione del sito o scrivere un brief, viene eseguito nell'app Hi, Moose su quel dispositivo, allo stesso modo di quando qualcuno preme il pulsante nell'app.

## L'elenco degli strumenti è pubblicato e non cambia

Un server MCP può, in linea di principio, cambiare le descrizioni dei suoi strumenti dopo il collegamento, o nascondervi istruzioni per l'agente di IA. OWASP lo chiama avvelenamento degli strumenti (tool poisoning).

Gli strumenti di Hi, Moose MCP sono codice fisso nel server. Nomi, descrizioni e schemi di input non cambiano tra una chiamata e l'altra, e non vi viene mai scritto contenuto dell'utente. Un nuovo strumento significa una nuova versione del server.

L'elenco esatto che il server fornisce è pubblicato su:

```text
https://mcp.himoose.com/tools.json
```

Contiene la versione del server, la data dell'ultima modifica all'elenco, il numero di strumenti, il testo completo di ogni strumento, il testo di istruzioni che il server dà all'agente e un hash SHA-256. L'hash copre il JSON compatto dei campi `instructions` e `tools`, quindi puoi ricalcolarlo dal file o confrontarlo con ciò che ha ricevuto il tuo client MCP. Annota l'hash nelle tue note di revisione e confrontalo con regolarità. Lo stesso hash è l'header `ETag` del file.

Prima che qualcuno acceda, la pagina di consenso mostra lo stesso elenco di strumenti in parole semplici, sotto "Questa app potrà" e "Non potrà".

## Accesso e token

Ogni client segue lo stesso flusso: Claude sul web, l'app desktop di Claude, Claude Code, ChatGPT e qualsiasi altra app MCP. Non ci sono scorciatoie, token condivisi né chiavi API.

- OAuth 2.1 come lo descrive l'attuale specifica di autorizzazione MCP: metadati della risorsa protetta (RFC 9728) con una sfida `WWW-Authenticate`, metadati del server di autorizzazione (RFC 8414), PKCE obbligatorio per ogni client, indicatori di risorsa (RFC 8707) perché un token per questo server non possa essere riutilizzato altrove, registrazione dinamica dei client (RFC 7591) e Client ID Metadata Documents, e revoca dei token (RFC 7009).
- L'accesso avviene su `console.himoose.com`, con l'account Hi, Moose esistente della persona, via email e password o con Google. L'app MCP non vede mai la password. Hi, Moose MCP apprende solo l'id e l'email dell'account, e quali progetti l'account può vedere.
- La pagina di consenso nomina l'app che chiede l'accesso. Quando l'app pubblica la propria identità, la pagina mostra il suo dominio editore. Quando non lo fa, la pagina dice "Nome non verificato".
- I token di accesso durano un'ora. I token di aggiornamento durano al massimo 90 giorni e scadono dopo 30 giorni senza uso. Token, codici e segreti sono conservati solo come hash.
- Un collegamento appartiene a una persona. I membri del team si collegano con i propri account.

Per scollegare un'app, apri Hi, Moose e vai in **Impostazioni → Hi, Moose MCP**. La tabella **App collegate** elenca ogni app con accesso all'account, con il dominio editore e l'ora del collegamento. **Revoca** disconnette quell'app entro un minuto. L'app può ricollegarsi solo ripassando dall'accesso.

## Cosa può e cosa non può fare un'app collegata

Tutto ciò che un'app collegata può fare è elencato nella [guida alla configurazione](../hi-moose-mcp.md) e descritto strumento per strumento nel [riferimento degli strumenti](tools.md). È lavoro di contenuto e ricerca dentro i progetti dell'account: brief, bozze, immagini, FAQ, punti chiave, audit AEO, piani di link interni, episodi audio, verifiche di copertura e letture dei risultati di ricerca IA archiviati.

Non può:

- Pubblicare su un sito web, né cambiarvi nulla
- Eliminare nulla
- Cambiare impostazioni, membri del team, fatturazione o il dispositivo host
- Cambiare ciò che Hi, Moose traccia, né avviare un'esecuzione di visibilità
- Raggiungere un account diverso da quello che ha effettuato l'accesso
- Raggiungere qualsiasi cosa nell'app da cui viene usata: né chat, né file, né repository, né memoria, né altri connettori

Ogni richiesta nomina un progetto. Prima che inizi qualsiasi lavoro, Hi, Moose verifica che l'account collegato abbia accesso a quel progetto. Una richiesta per un progetto che l'account non può vedere fallisce subito.

## Dove viene eseguito il lavoro e quali dati si muovono

Hi, Moose MCP non ha mai una copia della scansione del sito, del profilo Brand Truth o della Library. Questi vivono nell'app Hi, Moose sul dispositivo host, l'unico computer o server che scegli nelle Impostazioni. L'host esegue ogni lavoro allo stesso modo in cui l'app lo esegue da un pulsante.

Ecco il percorso di una richiesta:

1. L'app MCP invia al server il nome dello strumento e il suo input.
2. Il server verifica il token e chiede al cloud di Hi, Moose di creare un record di lavoro per il progetto. Il cloud verifica l'accesso al progetto e scrive il record.
3. Il dispositivo host, che osserva i lavori dei suoi progetti, prende il lavoro e lo esegue.
4. L'host scrive il risultato nel record di lavoro e lo salva nella Library. Il server restituisce il risultato all'app MCP.

Cosa significa per i tuoi dati:

- La richiesta e il risultato passano per il cloud di Hi, Moose (Google Cloud, regione Stati Uniti) come record di lavoro. Il record resta con il progetto perché la tabella **Lavori recenti degli agenti** nelle Impostazioni possa mostrare cosa è stato chiesto, da quale app e account, e se è finito.
- Le immagini generate sono conservate nello spazio cloud Hi, Moose dell'account e restituite come link.
- Le chiamate ai modelli usano lo stesso percorso dell'app: i modelli gestiti del tuo piano, le tue chiavi di modello se le hai portate, o un modello locale se ne esegui uno. Collegare un'app MCP non cambia quali modelli vedono i tuoi contenuti.
- I log del server stesso conservano il nome dello strumento, la durata della chiamata e se il client ha usato lo streaming. Non conservano mai l'input né il risultato.

## Testo esterno nei risultati

Alcuni risultati contengono testo che Hi, Moose non ha scritto: passaggi di pagine del tuo sito, testo di ancoraggio citato da una pagina, brevi estratti di ciò che ha risposto un motore di IA, o il testo completo di una risposta archiviata. Un testo così potrebbe contenere istruzioni rivolte a un agente di IA. OWASP lo chiama prompt injection indiretta.

Ogni risultato che contiene testo esterno lo contrassegna. Il testo torna tra un marcatore di inizio e uno di fine, preceduto da una riga che ne indica la provenienza e dice che tutto ciò che sta tra i marcatori sono dati, non istruzioni. La forma strutturata dello stesso risultato porta un campo `dataNotice` che dice la stessa cosa. Vale per `check_site_coverage`, `run_aeo_audit`, `find_internal_links`, `visibility_check_topic`, `visibility_get_answer` e `visibility_list_opportunities`.

Brief, bozze, FAQ, punti chiave e copioni audio sono scritti da Hi, Moose per te. La ricerca alle loro spalle viene letta sul dispositivo host e non viene passata all'agente.

I marcatori aiutano un agente a trattare il testo come dati. Non rendono un agente immune alle istruzioni nei contenuti che legge, e nessun fornitore di strumenti può prometterlo. Mantieni i permessi dell'agente che colleghi stretti quanto richiede il suo compito, come faresti con qualsiasi connettore.

## Segnalare un problema di sicurezza

Scrivi a [legal@himoose.com](mailto:legal@himoose.com) o usa la [pagina dei contatti](https://himoose.com/it/contact/). Dicci cosa hai trovato e come riprodurlo. Rispondiamo a ogni segnalazione e ti diremo cosa abbiamo cambiato.
