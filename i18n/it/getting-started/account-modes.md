---
source_hash: 807f4fd0f8157bf27491590b13dd7b2b18f5cb12dd648c025f2c46cabf3ea0ed
---
# Tipi di account e piani

Hi, Moose esegue il lavoro di IA in due modi: con la sua chiave OpenRouter (BYOK) oppure con i modelli gestiti di Hi, Moose. È questa scelta, non il prezzo, il vero bivio. Tutto il resto è numero di progetti, postazioni e quantità di credito mensile.

I piani sono raggruppati in due schede nella schermata **Upgrade**: **Startup** ed **Enterprise & Agencies**.

## I due modi di eseguire l'IA

### BYOK: porti la sua chiave

Lei fornisce una chiave API di [OpenRouter](https://openrouter.ai) e le chiamate ai modelli vengono eseguite **dall'app desktop, sulla sua macchina**, con quella chiave. Hi, Moose non instrada mai l'inferenza BYOK attraverso i propri server, quindi la sua chiave e i suoi prompt restano in locale.

Pagare un piano BYOK non cambia questo. Lei paga per maggiori capacità di lavoro (progetti, postazioni, memoria, workflows, Search Console), non perché Hi, Moose esegua le sue chiamate ai modelli. Il costo dei modelli va direttamente a OpenRouter e non c'è alcun contatore di token di Hi, Moose da sorvegliare.

### Gestito: i modelli li esegue Hi, Moose

Nessuna chiave API. Il lavoro lo svolgono i modelli gestiti di Hi, Moose e lei consuma un saldo mensile di **crediti**. Un solo contatore, non diversi. Il supporto ai modelli locali resta disponibile come opzione sul dispositivo in tutti i piani gestiti.

## Piani Startup

### Preview Mode (gratuito)

Preview Mode è il modo gratuito di provare Hi, Moose. È davvero locale: 1 progetto, 1 postazione, archiviazione locale ed esecuzioni di visibilità che interrogano le superfici pubbliche di ricerca con IA direttamente dal suo dispositivo.

- 1 progetto, 1 postazione utente
- Solo LLM gratuiti e locali
- Esecuzioni di visibilità locali
- Archiviazione e richiamo del contesto, Brand Voice e guida di stile
- Connessioni: WordPress, Webflow, Grav
- Dati di ricerca in tempo reale e sui concorrenti limitati, qualità dell'IA limitata, opzioni di esportazione limitate

!!! warning "Preview Mode richiede un modello locale per punteggi e audit"
    Preview Mode non comprende alcuna dotazione di IA in cloud. Gli [AEO audits](../features/aeo-audits.md) e la valutazione di sentiment, narrativa e copertura funzionale nelle [esecuzioni di visibilità](../visibility/overview.md) funzionano solo dopo che ha attivato un modello locale Gemma 4 in **Impostazioni → Local Model**. Finché non ce n'è uno attivo, questi controlli vengono saltati anziché eseguiti in cloud.

### BYOK Free

Il modo gratuito di lavorare con la sua chiave. Stessa struttura da 1 progetto e 1 postazione di Preview Mode, ma con accesso a tutti i modelli offerti da OpenRouter e non solo a quelli gratuiti.

- 1 progetto, 1 postazione utente
- La sua chiave OpenRouter, token illimitati
- Tutti gli LLM, compresi i modelli locali
- Esecuzioni di visibilità solo in locale
- Connessioni: WordPress, Webflow, Grav
- Archiviazione e richiamo del contesto limitati, [Library](../library/overview.md) limitata
- Niente ricerca web nella chat, niente Workflows, niente Google Search Console

### BYOK Premium: 39 USD al mese o 390 USD all'anno

Il piano locale completo, e il punto in cui si sbloccano le postazioni del team e la pianificazione.

- 3 progetti, più progetti aggiuntivi a 10 USD al mese ciascuno
- Fino a 10 postazioni del team
- Esecuzioni di visibilità complete con pianificazione personalizzata
- Ricerca web dalla chat
- Archiviazione e richiamo del contesto completi, [Library](../library/overview.md) completa
- [Workflows](../workflows/overview.md)
- Brand Voice, guida di stile e [Brand Truth Profile](context/brand-truth-profile.md)
- Connessioni: WordPress, Webflow, Grav, [Google Search Console](../integrations/google-search-console.md)
- 15 [generazioni audio](../audio/overview.md) al mese

### Piani gestiti

Tutti e tre funzionano con i modelli di Hi, Moose e comprendono postazioni del team illimitate, generazioni audio illimitate, registri di amministrazione con esportazione e archiviazione locale e in cloud.

| Piano | Prezzo | Progetti | Crediti mensili | Modelli |
|---|---|---|---|---|
| Standard | 79 USD/mese o 849 USD/anno | 3 | 1.700.000 | Modelli standard, più quelli locali |
| Professional | 129 USD/mese o 1.389 USD/anno | 5 | 3.000.000 | Tutti i modelli, più quelli locali |
| Premium | 249 USD/mese o 2.689 USD/anno | 10 | 6.000.000 | Tutti i modelli, più quelli locali |

## Piani Enterprise e per agenzie

### BYOK Agency: 149 USD al mese o 1.490 USD all'anno

BYOK Premium su scala di agenzia. Lo stesso funzionamento locale e lo stesso insieme di funzioni, dimensionati per seguire molti clienti.

- 25 progetti, più progetti aggiuntivi a 10 USD al mese ciascuno
- Fino a 25 postazioni del team
- 15 generazioni audio al mese
- [Personalizzazione white label](../agency/white-label.md) su report e incorporamenti audio, come in tutti i piani a pagamento

### Piani gestiti per agenzie

| Piano | Prezzo | Progetti | Crediti mensili | Archiviazione |
|---|---|---|---|---|
| Agent Core | 449 USD/mese o 4.849 USD/anno | 25 | 15.000.000 | Cloud del team |
| Agent Studio | 999 USD/mese o 10.789 USD/anno | 75 | 40.000.000 | Cloud del team |
| Agent Scale | 1.999 USD/mese o 21.589 USD/anno | Illimitati | 120.000.000 | Cloud del team |

## Confronto rapido

| | Preview Mode | BYOK Free | BYOK Premium | BYOK Agency | Piani gestiti |
|---|---|---|---|---|---|
| Serve una chiave API propria | No | Sì | Sì | Sì | No |
| Dove viene eseguita l'inferenza | Sul suo dispositivo | Sul suo dispositivo | Sul suo dispositivo | Sul suo dispositivo | Cloud di Hi, Moose (locale opzionale) |
| Progetti | 1 | 1 | 3 | 25 | Da 3 a illimitati |
| Postazioni del team | 1 | 1 | 10 | 25 | Illimitate |
| Ricerca web nella chat | No | No | Sì | Sì | Sì |
| [Workflows](../workflows/overview.md) | No | No | Sì | Sì | Sì |
| [Google Search Console](../integrations/google-search-console.md) | No | No | Sì | Sì | Sì |
| [Audio](../audio/overview.md) | No | No | 15 al mese | 15 al mese | Illimitato |
| [White label](../agency/white-label.md) | No | No | Sì | Sì | Sì |

## Postazioni, progetti e crediti

I **progetti aggiuntivi** costano 10 USD al mese ciascuno in tutti i piani a pagamento. Li aggiunga o li rimuova da **Upgrade → Extra projects**.

Le **postazioni** sono il vero confine tra gratuito e a pagamento. Preview Mode e BYOK Free sono limitati al titolare dell'account. BYOK Premium consente fino a 10, BYOK Agency fino a 25, e i piani gestiti non hanno limite, perché tutti i membri attingono al saldo di crediti del titolare.

Le **ricariche di credito** sono disponibili nei piani gestiti quando resta senza saldo a metà mese:

- 500.000 crediti per 25 USD
- 2.500.000 crediti per 100 USD

Le ricariche sono acquisti una tantum, non abbonamenti. Vengono consumate solo dopo che i crediti mensili si sono esauriti e non scadono mai.

!!! note "Gli ascolti audio si conteggiano a parte"
    Ogni piano che comprende l'audio include anche i primi 10.000 ascolti a livello di account. Oltre quella soglia, gli ascolti vengono fatturati a 5,00 USD ogni 10.000 al mese. Nei piani gestiti anche la *generazione* dell'audio attinge al suo saldo di crediti.

## Codici sconto

Se dispone di un codice sconto, lo inserisca al momento del pagamento nella schermata **Upgrade**.

## Cambiare piano

Può cambiare piano in qualsiasi momento da **Impostazioni → Account** o dalla schermata **Upgrade**. Se passa da un piano gestito a uno BYOK, inserisca prima la sua chiave API di OpenRouter. Hi, Moose verifica la chiave prima di spostarvi l'instradamento dell'IA.

La sua chiave OpenRouter viene salvata per account e non per dispositivo, quindi la accompagna in una nuova installazione.
