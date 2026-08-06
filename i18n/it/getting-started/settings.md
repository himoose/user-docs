---
source_hash: f081840e659e67696268902173c5c0f26e8413e1debac31049488ad42cb5c005
---
# Impostazioni

## A cosa serve

Nelle Impostazioni gestisce il suo profilo, il suo piano, i suoi modelli, il suo team e il comportamento dell'app su questo computer. Sono organizzate in dieci sezioni nella colonna di sinistra.

| Sezione | Contenuto |
|---|---|
| General | Dati del profilo e comportamento dell'app su questo computer |
| Usage | Saldo di crediti e data di rinnovo |
| Account | E-mail, password, piano, chiave OpenRouter |
| Local Model | Download e attivazione del modello sul dispositivo |
| Team | Postazioni, inviti, ruoli |
| [Site Monitoring](../site-monitoring/overview.md) | Pianificazione della scansione, indice di ricerca, pagine monitorate, percorsi bloccati |
| [Branding](../agency/white-label.md) | Report white label e attribuzione audio (solo piani a pagamento) |
| Logs | Registri delle azioni ed esportazione CSV |
| Data & Backup | Backup e ripristino locali |
| Troubleshooting | Cache, registro diagnostico, ripristino dei dati locali |

## General

**Dati del profilo**: il suo nome preferito, il suo ruolo e la sua posizione. Servono a personalizzare l'app e a rendere più chiara l'attribuzione del lavoro condiviso.

**Comportamento dell'app** governa come Hi, Moose funziona su questo computer:

- **Avviare Hi, Moose all'accesso**: dopo un riavvio l'app si apre discretamente in background, così il lavoro pianificato continua. Può aprire la finestra in qualsiasi momento dalla barra delle applicazioni o dalla barra dei menu.
- **Condividere statistiche d'uso anonime**: invia eventi anonimi e aggregati (quali funzioni vengono usate, versione dell'app, errori) perché possiamo migliorare il prodotto. Non invia mai i suoi contenuti, i suoi prompt, le sue chiavi o i siti che analizza, e il suo indirizzo IP viene scartato. Può disattivarla quando vuole.

## Usage

Nei piani gestiti qui vede il suo saldo di crediti e quanto resta per il mese.

!!! note "Il mese si calcola in UTC"
    I crediti si rinnovano all'inizio di ogni mese in UTC, non nel suo fuso orario. Le Impostazioni le mostrano la data corrispondente da lei, perciò a tarda ora dell'ultimo giorno del mese può sembrare che il rinnovo sia arrivato in anticipo.

I piani BYOK non consumano crediti di Hi, Moose per l'inferenza, poiché la generazione avviene con la sua chiave. Il costo dei modelli va direttamente a OpenRouter.

## Account

- Aggiorni il suo indirizzo e-mail, lo verifichi e reimposti la password sugli account con e-mail e password. Gli account Google si gestiscono tramite Google.
- Le modifiche dell'indirizzo e-mail attendono la sua conferma tramite un link prima di avere effetto, e poi la sua sessione nell'app viene aggiornata.
- Consulti il suo piano attuale e lo cambi. Veda [Tipi di account e piani](account-modes.md).

### Inserire la sua chiave API di OpenRouter

Nei piani BYOK inserisca qui la sua chiave di [OpenRouter](https://openrouter.ai). Hi, Moose verifica la chiave prima di spostarvi l'instradamento dell'IA. Una volta inserita:

- Le funzioni di IA girano in locale nell'app desktop con la sua chiave
- Lei sceglie quali modelli supportati usare per chat e generazione
- La sua chiave e i suoi prompt non passano mai per i server di Hi, Moose nell'inferenza BYOK

La chiave viene salvata per account e non per dispositivo, quindi la accompagna in una nuova installazione.

## Local Model

Scarichi e attivi un modello approvato sul dispositivo, come Gemma 4. L'esecuzione locale non usa né i modelli di Hi, Moose né la sua chiave OpenRouter: avviene interamente sulla sua macchina ed è gratuita.

I modelli locali sono disponibili in tutti i piani e sono **necessari** in Preview Mode per gli [AEO audits](../features/aeo-audits.md) e per la valutazione della visibilità.

!!! note "La dimensione del contesto si adatta alla sua RAM"
    Hi, Moose dimensiona la finestra di contesto del modello in base alla memoria disponibile sulla sua macchina, perciò lo stesso modello usa una finestra più piccola su un portatile da 16 GB che su una workstation più capiente.

## Team

Inviti membri, ne consulti i ruoli e revochi gli accessi. I limiti di postazioni dipendono dal suo piano. Consulti [Gestione del team](team-management.md) per il percorso completo.

## Site Monitoring

Pianificazione della scansione, indice di ricerca locale, pagine monitorate e percorsi bloccati. È un'area ampia e ha una pagina dedicata: **[Site Monitoring](../site-monitoring/overview.md)**.

Le connessioni a CMS e fonti dati sono un'altra cosa e si trovano nella schermata **Connections**, non nelle Impostazioni:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

Applichi il suo marchio ai report PDF esportati e ai player audio incorporati. Disponibile in tutti i piani a pagamento e modificabile dal titolare dell'abbonamento. Veda **[Personalizzazione white label](../agency/white-label.md)**.

## Logs

Registri delle azioni del progetto corrente, con tipo, utente, data, stato e metadati di ogni azione registrata. Nei piani gestiti i registri condivisi del team si sincronizzano accanto ai suoi locali.

**Export CSV** li scarica. L'esportazione dei registri delle azioni del team è riservata ai titolari di spazi di lavoro gestiti a pagamento.

## Data & Backup

Crei un backup compresso `.hmbk` della sua cronologia sul dispositivo e lo importi in seguito per ripristinarla.

**I backup comprendono** i record del database locale e le pianificazioni di visibilità BYOK salvate, così i suoi brief, audit, anteprime, la cronologia di site monitoring, lo stato dell'Inbox e gli altri artefatti di lavoro non riservati restano trasferibili.

**I backup non comprendono** lo stato di accesso, le credenziali dei connettori, le chiavi API, i file dei modelli locali o gli allegati.

!!! warning "L'importazione sovrascrive i dati locali in modo permanente"
    Un'importazione sostituisce i dati locali di Hi, Moose di questo dispositivo con il contenuto del backup. La finestra di conferma le indica quanti record verranno ripristinati e quando è stato creato il backup. Riavvii l'app subito dopo, perché tutte le schermate si ricarichino dai dati ripristinati.

Le importazioni accettano soltanto file `.hmbk` esportati dall'app desktop di Hi, Moose.

## Troubleshooting

Tre strumenti di ripristino. Tutti agiscono solo sullo stato locale del desktop e non toccano mai i dati in cloud.

**Svuotare la cache temporanea**: cancella la cache HTTP, i service worker e altri stati eliminabili. Mantiene il suo accesso e la cronologia di lavoro locale. Provi prima questo.

**Registro diagnostico**: Hi, Moose tiene un piccolo registro degli errori su questo dispositivo. **Apri la cartella dei registri** la porta lì; se il supporto glielo chiede, invii il file `main-errors.log`. Il registro resta sul suo dispositivo, a meno che non decida di condividerlo.

**Ripristinare i dati locali dell'app**: rimuove in modo permanente artefatti, brief, anteprime, cronologia della visibilità e altri stati di lavoro locali dal dispositivo. L'operazione non è reversibile. Il suo accesso e le credenziali salvate dei connettori restano invariati.
