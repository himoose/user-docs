---
source_hash: 40b089c8c06f81c797410e131c0f51ee08f0beba3baaaf1ad18b0794a101df1a
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/visibility/overview/)

# Visibility

## A cosa serve

Il pannello Visibility mostra come il suo marchio si comporta davvero nella ricerca con IA: le query che i clienti usano per trovarla, se il suo marchio entra nella rosa dei candidati e se i motori di IA lo descrivono con accuratezza. È la vista principale per i passaggi **monitorare** e **rilevare** del [ciclo operativo centrale](../index.md#il-ciclo-operativo-centrale).

Il pannello ha tre schede:

| Scheda | A quale domanda risponde |
|---|---|
| **Overview** | Come sto andando? |
| **[Competition](competitors.md)** | Come sto andando rispetto a loro? |
| **Topics & Engines** | Dove esattamente sono forte o debole? |

## Metriche

Ogni esecuzione riporta alcune metriche principali per il periodo selezionato:

- **Share of Mentions**: quanto spesso il suo marchio viene menzionato nei prompt e nei motori monitorati.
- **Share of Citations**: quanto spesso il suo dominio viene effettivamente citato come fonte.
- **Sentiment**: il tono medio (positivo, misto, neutro, negativo) delle menzioni.
- **Posizione media**: dove tende a collocarsi il suo marchio quando compare in un elenco o in una classifica. Mostra **Not enough data** finché non ci sono abbastanza menzioni posizionate per calcolare una media.
- **Narrative Drift**: se le risposte dell'IA si allontanano dal suo posizionamento voluto.
- **Feature Parity**: se le risposte dell'IA rappresentano con accuratezza ciò che lei offre.

Narrative Drift e Feature Parity mostrano **Not scored** con un link di configurazione finché non ha compilato il suo Brand Truth Profile. Queste due metriche hanno senso solo quando Hi, Moose sa che cosa è vero sul suo marchio per poterlo confrontare. Veda [Brand Truth Profile](../getting-started/context/brand-truth-profile.md).

!!! note "Le osservazioni fallite vengono escluse, non contate come assenze"
    Se un motore non era disponibile o una richiesta è fallita, quell'osservazione resta fuori da tutte le metriche invece di essere valutata come «il suo marchio non è stato menzionato». Un'esecuzione con problemi di connessione riferisce su meno osservazioni anziché segnalare un calo inesistente. La vista per prompt le contrassegna come **Response unavailable** e indica quante ne sono state escluse.

## Filtri e periodo

- Filtri per **Topic**, **AI Engine**, **Prompt** (selezione multipla con ricerca), **Page**, **Sentiment**, **Narrative** o **Feature Parity**, oppure azzeri tutti i filtri in una volta.
- Il filtro **Page** restringe a URL specifiche ed è ricercabile per percorso. Mostra correttamente anche i motori in cui l'URL **non** è stata citata, così vede sia dove una pagina manca sia dove compare.
- Imposti un intervallo di date in **Period** e faccia clic su **Apply**, oppure su **Compare** per sovrapporre un periodo precedente o l'esecuzione precedente.

## Andamento nel tempo

Il grafico di andamento rappresenta **Mentions**, **Citations**, **Positive %** o la posizione media in intervalli di **giorno**, **settimana** o **mese**, suddivisi per motore di IA oppure con **All models** aggregati, così vede se è un motore in particolare a muovere i numeri.

## Dettaglio per prompt

Sotto il grafico:

- **Mention Rate** suddivide i risultati per motore, indicando quali l'hanno menzionata e quali no.
- **Top Cited Pages** mostra quali sue URL vengono citate e da quali motori.
- **Prompt-Level Breakdown** espande qualsiasi prompt monitorato per vedere i singoli risultati per motore, compresa la risposta completa dell'IA e il ragionamento su sentiment, narrativa e copertura funzionale.

Ogni prompt ha un link per **approfondire nella chat** che consegna a Moose i dati esatti dell'osservazione e gli chiede di raccomandare se il passo successivo debba essere un [AEO audit](../features/aeo-audits.md) di una pagina esistente o un nuovo [brief con bozza](../features/content-briefs.md).

## Topics & Engines

Questa scheda scompone il rendimento in due modi:

- **Mention Rate by Topic**: quanto spesso ogni marchio compare nelle risposte dell'IA per ciascun tema.
- **Mention Rate Trend by Topic**: lo stesso dato, distribuito nel tempo.
- **Mention Rate by Platform**: una mappa di calore della frequenza con cui ogni marchio compare nelle risposte di ciascuna piattaforma nel periodo.

I temi provengono dalle categorie dei suoi prompt. Se i suoi prompt non sono categorizzati, questa scheda la invita a organizzarli nel [Prompt Manager](prompt-manager.md) invece di mostrare un grafico vuoto.

## Esportare

**Export** offre due formati:

- **CSV spreadsheet**: tutti i risultati della vista corrente, per Excel o Google Sheets.
- **PDF executive report**: un report pronto per la stampa della vista corrente, compresi i grafici e i dati competitivi della scheda Competition.

Le esportazioni rispettano i filtri attivi, e la copertina del PDF indica quali filtri sono stati applicati, perché un report non possa essere scambiato per un quadro completo dell'account. Nei piani a pagamento il PDF porta il suo [marchio white label](../agency/white-label.md), se lo ha configurato.

## Eseguire i controlli di visibilità

Faccia clic su **Run now** per un controllo su richiesta. Il comportamento dipende dal suo [piano](../getting-started/account-modes.md):

- **Preview Mode** esegue controlli con interrogazione locale direttamente dal suo dispositivo sulle superfici pubbliche di ricerca con IA. Hi, Moose le chiede conferma prima, perché controlli ravvicinati possono attivare blocchi temporanei per limiti di richieste su quelle superfici. La valutazione di sentiment, narrativa e copertura richiede un modello locale Gemma 4 attivo; senza di esso quei controlli vengono saltati.
- **I piani BYOK** girano in locale con la sua chiave OpenRouter.
- **I piani gestiti** passano dall'infrastruttura di Hi, Moose. Se al suo spazio di lavoro non resta abbastanza dotazione questo mese per la pianificazione attuale, le esecuzioni programmate si sospendono finché non cambia piano, non modifica la sua [frequenza di esecuzione](settings.md#pianificazione-delle-esecuzioni) o la dotazione non si rinnova. Hi, Moose le indica quante unità servono rispetto a quelle rimaste.

Può interrompere un'esecuzione in anticipo, e le esecuzioni interrotte da un aggiornamento dell'app riprendono invece di andare perse.

## Dove andare da qui

- **[Concorrenti e Share of Voice](competitors.md)**: posizione competitiva, citazioni dei concorrenti e lacune.
- **[Prompt Manager](prompt-manager.md)**: aggiungere, organizzare e categorizzare i prompt monitorati.
- **[Impostazioni di Visibility](settings.md)**: pianificazione delle esecuzioni, modello di valutazione, monitoraggio dei concorrenti, termini e domini di marca secondari e modelli predefiniti.
