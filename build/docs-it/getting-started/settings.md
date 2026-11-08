---
source_hash: 0a9a56ce00908be9642b519b71a66ed53535f416da94c0f65e7bb741595259e0
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/getting-started/settings/)

# Impostazioni

## A cosa serve

Nelle Impostazioni gestisce il suo profilo, il suo piano, i suoi modelli, il suo team e il comportamento dell'app su questo computer. Sono organizzate in sezioni nella colonna di sinistra; alcune compaiono solo per il proprietario dell'account o nei piani a pagamento.

| Sezione | Contenuto |
|---|---|
| Generali | Dati del profilo e comportamento dell'app su questo computer |
| Utilizzo | Saldo di crediti e data di rinnovo |
| Account | E-mail, password, piano, chiave OpenRouter |
| IA locale | Download e attivazione del modello sul dispositivo |
| Team | Postazioni, inviti, ruoli |
| [Monitoraggio del sito](../site-monitoring/overview.md) | Pianificazione della scansione, indice di ricerca, pagine monitorate, percorsi bloccati |
| [Brand](../agency/white-label.md) | Report white label e attribuzione audio (solo piani a pagamento) |
| Accessi agli account | I siti in cui Moose ha effettuato l'accesso per le esecuzioni di visibilità e Send Moose |
| [Hi, Moose MCP](../integrations/hi-moose-mcp.md) | Dispositivo host, modello per le attività di scrittura, app collegate, lavori recenti |
| [API REST di Hi, Moose](../integrations/developer-api.md) | Chiavi API e webhook (solo proprietario) |
| Registri | Registri delle azioni ed esportazione CSV (solo proprietario) |
| Dati e backup | Backup e ripristino locali |
| Cronologia di visibilità | La copia locale delle sue risposte della ricerca IA e il suo limite di spazio |
| Risoluzione dei problemi | Cache, registro diagnostico, ripristino dei dati locali |

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

Scarichi e attivi un modello approvato sul dispositivo, come Gemma 4. Le risposte di un modello locale vengono generate sulla sua macchina, senza i modelli gestiti di Hi, Moose né la sua chiave OpenRouter, e l'uso è gratuito. Per impostazione predefinita, la chat usa un breve passaggio di instradamento nel cloud per scegliere lo strumento giusto per ogni messaggio, e per farlo invia il testo del messaggio a un servizio di instradamento cloud. Disattivi **Instradamento intelligente** in **Impostazioni → IA locale** perché anche quel passaggio resti sul suo dispositivo.

I modelli locali sono disponibili in tutti i piani e sono **necessari** in Preview Mode per gli [AEO audits](../features/aeo-audits.md) e per la valutazione della visibilità.

!!! note "La dimensione del contesto si adatta alla sua RAM"
    Hi, Moose dimensiona la finestra di contesto del modello in base alla memoria disponibile sulla sua macchina, perciò lo stesso modello usa una finestra più piccola su un portatile da 16 GB che su una workstation più capiente.

## Team

Inviti membri, ne consulti i ruoli e revochi gli accessi. I limiti di postazioni dipendono dal suo piano. Consulti [Gestione del team](team-management.md) per il percorso completo.

## Site Monitoring

Pianificazione della scansione, indice di ricerca locale, pagine monitorate e percorsi bloccati. È un'area ampia e ha una pagina dedicata: **[Monitoraggio del sito](../site-monitoring/overview.md)**.

Le connessioni a CMS e fonti dati sono un'altra cosa e si trovano nella schermata **Connessioni**, non nelle Impostazioni:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

Applichi il suo marchio ai report PDF esportati e ai player audio incorporati. Disponibile in tutti i piani a pagamento e modificabile dal titolare dell'abbonamento. Veda **[Personalizzazione white label](../agency/white-label.md)**.

## Accessi agli account

Moose usa un browser proprio per le esecuzioni di visibilità con interrogazione locale e per Send Moose. Questa sezione elenca i siti in cui può avere effettuato l'accesso, raggruppati in motori di risposta IA (ChatGPT, Google AI Mode e Gemini, Grok, Perplexity, Bing Copilot) e siti usati dagli agenti di Send Moose (Reddit, LinkedIn, X), ciascuno con l'indicazione **Accesso effettuato** o **Nessun accesso**. Apra un sito qui ed effettui l'accesso una volta; ogni esecuzione successiva riprende la sessione. Accedere elimina anche le verifiche «confermi di essere una persona» che i motori mostrano alle prime esecuzioni. Gli accessi restano su questo computer e non vanno mai nel cloud.

L'indicazione è una stima basata sui cookie di ogni sito. Se un'esecuzione le chiede ancora di accedere, apra il sito qui e acceda di nuovo.

Per Send Moose si può aggiungere una casella di **posta web**, così Moose può leggere i link di conferma mentre lavora a un incarico. Non invia, non risponde, non elimina e non cambia mai le impostazioni. Usi una casella creata per Moose e tenga separata la sua posta personale.

## Hi, Moose MCP

Colleghi Claude, ChatGPT o qualsiasi altra app MCP al suo account Hi, Moose, scelga il dispositivo host che esegue il lavoro, scelga il **modello per le attività di scrittura** e consulti le app collegate e i lavori recenti. Veda **[Hi, Moose MCP](../integrations/hi-moose-mcp.md)**.

## API REST di Hi, Moose

Questa sezione compare solo per il proprietario dell'account. Crei e revochi le chiavi API che leggono i suoi dati di visibilità salvati dalle sue dashboard e dai suoi report, scelga cosa può fare ogni chiave (leggere i dati di visibilità, gestire il monitoraggio, avviare esecuzioni) e consulti o rimuova i webhook registrati per il progetto. Veda **[API di Hi, Moose](../integrations/developer-api.md)**.

## Logs

Registri delle azioni del progetto corrente, con tipo, utente, data, stato e metadati di ogni azione registrata. Nei piani gestiti i registri condivisi del team si sincronizzano accanto ai suoi locali.

**Esporta CSV** li scarica. L'esportazione dei registri delle azioni del team è riservata ai titolari di spazi di lavoro gestiti a pagamento.

## Data & Backup

Crei un backup compresso `.hmbk` della sua cronologia sul dispositivo e lo importi in seguito per ripristinarla.

**I backup comprendono** i record del database locale e le pianificazioni di visibilità BYOK salvate, così i suoi brief, audit, anteprime, la cronologia di site monitoring, lo stato dell'Inbox e gli altri artefatti di lavoro non riservati restano trasferibili.

**I backup non comprendono** lo stato di accesso, le credenziali dei connettori, le chiavi API, i file dei modelli locali o gli allegati.

!!! warning "L'importazione sovrascrive i dati locali in modo permanente"
    Un'importazione sostituisce i dati locali di Hi, Moose di questo dispositivo con il contenuto del backup. La finestra di conferma le indica quanti record verranno ripristinati e quando è stato creato il backup. Riavvii l'app subito dopo, perché tutte le schermate si ricarichino dai dati ripristinati.

Le importazioni accettano soltanto file `.hmbk` esportati dall'app desktop di Hi, Moose.

## Cronologia di visibilità

Hi, Moose conserva su questo computer una copia delle sue risposte della ricerca IA, così la pagina Visibility può mostrare qualsiasi periodo senza scaricarlo di nuovo. Questa sezione mostra quanto spazio occupa la copia del progetto corrente e le date che copre, e un **limite di spazio**: quando la copia supera quella dimensione, i giorni più vecchi vengono rimossi solo da questo computer e tornano dal cloud quando sceglie un periodo che li richiede. Nei piani senza copia nel cloud nulla viene rimosso automaticamente; faccia invece un backup delle risposte in Dati e backup.

## Troubleshooting

Tre strumenti di ripristino. Tutti agiscono solo sullo stato locale del desktop e non toccano mai i dati in cloud.

**Svuotare la cache temporanea**: cancella la cache HTTP, i service worker e altri stati eliminabili. Mantiene il suo accesso e la cronologia di lavoro locale. Provi prima questo.

**Registro diagnostico**: Hi, Moose tiene un piccolo registro degli errori su questo dispositivo. **Apri la cartella dei registri** la porta lì; se il supporto glielo chiede, invii il file `main-errors.log`. Il registro resta sul suo dispositivo, a meno che non decida di condividerlo.

**Ripristinare i dati locali dell'app**: rimuove in modo permanente artefatti, brief, anteprime, cronologia della visibilità e altri stati di lavoro locali dal dispositivo. L'operazione non è reversibile. Il suo accesso e le credenziali salvate dei connettori restano invariati.
