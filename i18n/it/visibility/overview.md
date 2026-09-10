---
source_hash: e5cf87efe7298e31a0e0c034a7c0d36431b70c08378225d4dd5c73357dd59a4f
---
# Visibility

## A cosa serve

Il pannello Visibility mostra come il suo marchio si comporta davvero nella ricerca con IA: le query che i clienti usano per trovarla, se il suo marchio entra nella rosa dei candidati e se i motori di IA lo descrivono con accuratezza. È la vista principale per i passaggi **monitorare** e **rilevare** del [ciclo operativo centrale](../index.md#il-ciclo-operativo-centrale).

Il pannello ha sei schede:

| Scheda | A quale domanda risponde |
|---|---|
| **Panoramica** | Come sto andando? |
| **[Concorrenza](competitors.md)** | Come sto andando rispetto a loro? |
| **Menzioni** | Quali marchi vengono nominati in queste risposte? |
| **Citazioni** | Su quali fonti si appoggiano davvero i motori? |
| **Temi e motori** | Dove esattamente sono forte o debole? |
| **Prompt** | Che cosa è successo su ogni singolo prompt? |

## Metriche

Ogni esecuzione riporta alcune metriche principali per il periodo selezionato:

- **Quota di menzioni**: quanto spesso il suo marchio viene menzionato nei prompt e nei motori monitorati.
- **Quota di citazioni**: quanto spesso il suo dominio viene effettivamente citato come fonte.
- **Sentiment**: il tono medio (positivo, misto, neutro, negativo) delle menzioni.
- **Posizione media**: dove tende a collocarsi il suo marchio quando compare in un elenco o in una classifica. Mostra **Dati insufficienti** finché non ci sono abbastanza menzioni posizionate per calcolare una media.
- **Deriva narrativa**: se le risposte dell'IA si allontanano dal suo posizionamento voluto.
- **Parità delle funzionalità**: se le risposte dell'IA rappresentano con accuratezza ciò che lei offre.

Narrative Drift e Feature Parity mostrano **Non valutato** con un link di configurazione finché non ha compilato il suo Brand Truth Profile. Queste due metriche hanno senso solo quando Hi, Moose sa che cosa è vero sul suo marchio per poterlo confrontare. Veda [Brand Truth Profile](../getting-started/context/brand-truth-profile.md).

!!! note "Le osservazioni fallite vengono escluse, non contate come assenze"
    Se un motore non era disponibile o una richiesta è fallita, quell'osservazione resta fuori da tutte le metriche invece di essere valutata come «il suo marchio non è stato menzionato». Un'esecuzione con problemi di connessione riferisce su meno osservazioni anziché segnalare un calo inesistente. La vista per prompt le contrassegna come **Risposta non disponibile** e indica quante ne sono state escluse.

## Filtri e periodo

- Filtri per **Argomento**, **Motore IA**, **Prompt** (selezione multipla con ricerca), **Pagina**, **Sentiment**, **Narrativa** o **Parità delle funzionalità**, oppure azzeri tutti i filtri in una volta.
- Il filtro **Pagina** restringe a URL specifiche ed è ricercabile per percorso. Mostra correttamente anche i motori in cui l'URL **non** è stata citata, così vede sia dove una pagina manca sia dove compare.
- Imposti un intervallo di date in **Periodo** e faccia clic su **Applica**, oppure su **Confronta** per sovrapporre un periodo precedente o l'esecuzione precedente.

## Andamento nel tempo

Il grafico di andamento rappresenta **Menzioni**, **Citazioni**, **% positivo** o la posizione media in intervalli di **giorno**, **settimana** o **mese**, suddivisi per motore di IA oppure con **Tutti i modelli** aggregati, così vede se è un motore in particolare a muovere i numeri.

## Dettaglio per prompt

Sotto il grafico:

- **Tasso di menzione** suddivide i risultati per motore, indicando quali l'hanno menzionata e quali no.
- **Pagine più citate** mostra quali sue URL vengono citate e da quali motori.
- **Suddivisione per prompt** espande qualsiasi prompt monitorato per vedere i singoli risultati per motore, compresa la risposta completa dell'IA e il ragionamento su sentiment, narrativa e copertura funzionale.

Ogni prompt ha un link per **approfondire nella chat** che consegna a Moose i dati esatti dell'osservazione e gli chiede di raccomandare se il passo successivo debba essere un [AEO audit](../features/aeo-audits.md) di una pagina esistente o un nuovo [brief con bozza](../features/content-briefs.md).

## La scheda Panoramica

La Panoramica si apre con un riepilogo scritto del taglio corrente: qualche paragrafo che dice a che punto è, che cosa si è mosso e che cosa merita uno sguardo, in frasi e non in cifre. È generato dalla stessa scheda dati che usa il report, e può premere **Riscrivi il riepilogo** se lo vuole redatto di nuovo. Quando non è disponibile alcun modello per scriverlo, la Panoramica ripiega su una versione costruita direttamente dai numeri e lo dichiara.

Sotto il riepilogo ci sono due blocchi:

- **A che punto è**: il suo Share of Voice, il tasso di menzione sulle risposte lette, le citazioni, la posizione media quando viene nominato e il tasso di menzione per motore, con l'intero campo dei marchi monitorati accanto.
- **L'IA la sta descrivendo in modo accurato?**: allineamento del posizionamento, ripartizione del tono e un elenco di **risposte da rivedere**: le risposte precise in cui un motore ha descritto male una capacità o si è allontanato dal suo posizionamento. Ognuna apre la risposta o ci salta nella scheda Prompt.

## Menzioni

La scheda **Menzioni** è l'elenco completo di ogni marchio, prodotto o sito web che i motori hanno nominato nelle risposte del taglio corrente: non solo lei e i suoi concorrenti monitorati, ma tutti quelli che sono comparsi.

Ogni riga mostra in quante risposte il marchio è stato nominato, il dato come percentuale delle risposte nel taglio, la sua quota su tutte le menzioni, la sua posizione media tra i marchi nominati in una risposta e il verdetto di sentiment più frequente. Passi il puntatore su un valore di sentiment per la ripartizione positivo/misto/neutro/negativo, e su un'intestazione di colonna per la definizione esatta.

Sopra la tabella, un **andamento della presenza nelle menzioni** traccia nel tempo i marchi più menzionati, e lei.

È qui che trova i concorrenti che non sapeva di avere. I marchi vengono letti dal testo della risposta dal modello di punteggio, perciò l'elenco fa emergere nomi che lei non ha mai aggiunto al monitoraggio.

## Citazioni

La scheda **Citazioni** applica la stessa idea alle fonti: ogni dominio o pagina che i motori hanno citato nel taglio corrente.

Passi tra **Per dominio** e **Per URL di pagina**, e filtri su **Tutto** oppure **Né lei né un concorrente** per vedere le fonti di terze parti che stanno plasmando le risposte. Ogni fonte è categorizzata: il suo marchio, concorrente, social, sito di recensioni, pubblicazione, riferimento, sviluppo o altro.

Le colonne sono:

| Colonna | Che cosa significa |
|---|---|
| **Prompt citati** | In quante risposte questo dominio o URL è stato citato |
| **Presenza %** | Il dato come quota sulle risposte nel taglio |
| **Numero di citazioni** | Quante volte in tutto è stato citato, ripetizioni comprese |
| **Visibilità %** | La sua quota su tutte le citazioni del taglio |
| **Posizione media** | La sua posizione media negli elenchi di citazioni dei motori |
| **Variazione** | Movimento rispetto al periodo di confronto o all'esecuzione precedente |

**Dettagli** su una riga elenca le pagine che ci stanno dietro e i prompt per cui ciascuna pagina è stata citata. Qualsiasi dominio della tabella può essere aggiunto direttamente ai suoi concorrenti monitorati con **Monitora come concorrente**, così un nome scoperto qui entra nello [Share of Voice](competitors.md) senza doverlo ridigitare.

Entrambe le tabelle si scaricano in CSV.

!!! note "I motori che non navigano non restituiscono citazioni"
    Le citazioni arrivano dai motori che consultano il web mentre rispondono. Un modello locale, o un motore che risponde solo dal proprio addestramento, non ne restituisce nessuna: una tabella vuota sotto un filtro stretto non segnala quindi per forza un problema del suo sito.

## Topics & Engines

Questa scheda scompone il rendimento in due modi:

- **Tasso di menzione per tema**: quanto spesso ogni marchio compare nelle risposte dell'IA per ciascun tema.
- **Andamento del tasso di menzione per tema**: lo stesso dato, distribuito nel tempo.
- **Tasso di menzione per piattaforma**: una mappa di calore della frequenza con cui ogni marchio compare nelle risposte di ciascuna piattaforma nel periodo.

I temi provengono dalle categorie dei suoi prompt. Se i suoi prompt non sono categorizzati, questa scheda la invita a organizzarli nel [Prompt Manager](prompt-manager.md) invece di mostrare un grafico vuoto.

## Esportare

**Esporta** offre due formati:

- **Foglio di calcolo CSV**: tutti i risultati della vista corrente, per Excel o Google Sheets.
- **Report esecutivo PDF**: un report completo in tredici sezioni sulla vista corrente, scritto per essere consegnato a chi non era nella stanza.

Il report si apre con una narrazione scritta invece che con una sequenza di grafici, poi attraversa: a che punto è, se l'IA la descrive in modo accurato, il movimento nel periodo, motore per motore, dove l'IA la cita, le domande che vincono i concorrenti, per che cosa vengono citati i concorrenti, il campo completo, i marchi nominati nelle risposte delle IA, i domini che l'IA cita, il tasso di menzione per motore, il tasso di menzione per tema e una sezione finale che spiega come leggere ogni metrica.

Le esportazioni rispettano i filtri attivi, e la copertina del PDF indica quali filtri sono stati applicati, perché un report non possa essere scambiato per un quadro completo dell'account. Nei piani a pagamento il PDF porta il suo [marchio white label](../agency/white-label.md), se lo ha configurato.

## Eseguire i controlli di visibilità

Faccia clic su **Esegui ora** per un controllo su richiesta. Il comportamento dipende dal suo [piano](../getting-started/account-modes.md):

- **Preview Mode** esegue controlli con interrogazione locale direttamente dal suo dispositivo sulle superfici pubbliche di ricerca con IA. Hi, Moose le chiede conferma prima, perché controlli ravvicinati possono attivare blocchi temporanei per limiti di richieste su quelle superfici. La valutazione di sentiment, narrativa e copertura richiede un modello locale Gemma 4 attivo; senza di esso quei controlli vengono saltati.
- **I piani BYOK** girano in locale con la sua chiave OpenRouter.
- **I piani gestiti** passano dall'infrastruttura di Hi, Moose. Se al suo spazio di lavoro non resta abbastanza dotazione questo mese per la pianificazione attuale, le esecuzioni programmate si sospendono finché non cambia piano, non modifica la sua [frequenza di esecuzione](settings.md#pianificazione-delle-esecuzioni) o la dotazione non si rinnova. Hi, Moose le indica quante unità servono rispetto a quelle rimaste.

Può interrompere un'esecuzione in anticipo, e le esecuzioni interrotte da un aggiornamento dell'app riprendono invece di andare perse.

## Quanta cronologia viene conservata

Ogni osservazione prodotta da un'esecuzione viene archiviata in locale, così che tendenze, confronti e le tabelle Menzioni e Citazioni possano guardare più indietro delle ultime esecuzioni. L'archivio conserva fino a **400 giorni** per spazio di lavoro e fino a 200.000 osservazioni; oltre l'uno o l'altro limite, le righe più vecchie vengono eliminate.

Nei piani gestiti a pagamento, anche le esecuzioni di visibilità che girano sulla sua macchina sincronizzano i risultati nel cloud, così i colleghi vedono la stessa cronologia che vede lei e non solo le esecuzioni avvenute sul proprio dispositivo.

## Dove andare da qui

- **[Concorrenti e Share of Voice](competitors.md)**: posizione competitiva, citazioni dei concorrenti e lacune.
- **[Prompt Manager](prompt-manager.md)**: aggiungere, organizzare e categorizzare i prompt monitorati.
- **[Impostazioni di Visibility](settings.md)**: pianificazione delle esecuzioni, modello di valutazione, monitoraggio dei concorrenti, termini e domini di marca secondari e modelli predefiniti.
