---
source_hash: 90bb543cefb714f7fdb6facb1f7799b751aff22949ece082264e7713b4992995
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/chat/model-selection/)

# Scelta del modello

## A cosa serve

Ogni chat è alimentata da un modello di IA preciso, e il selettore di modello le permette di vedere e cambiare quello che sta usando, compresi i modelli locali sul dispositivo.

## Scegliere un modello

Apra il selettore di modello per vedere i modelli disponibili nel suo [piano](../getting-started/account-modes.md). Ogni opzione porta delle etichette, così sa che cosa ottiene prima di cambiare:

- **Free** / **HiMoose Cloud** / **Paid or BYOK**: quali piani possono usare quel modello.
- **Speed: Slow / Average / Very Fast**: un'idea approssimativa del tempo di risposta.
- **Local**: gira interamente sul suo dispositivo (veda più sotto).
- Un'**etichetta con moltiplicatore** sui modelli più costosi, che indica quanto consumano in più del suo saldo rispetto all'opzione standard.

L'offerta segue ciò che pubblicano i fornitori di modelli e comprende attualmente le famiglie Claude, GPT, Gemini e Gemma. Se un modello non è disponibile nel suo piano, Hi, Moose glielo dice apertamente invece di ripiegare in silenzio su un altro.

## Modelli locali

I modelli locali approvati, come Gemma 4 di Google, girano **interamente sul suo computer**. Nessun token consumato, nessun passaggio dal cloud e nessun dato lascia il suo dispositivo. La prima volta che seleziona un modello locale, Hi, Moose la guida nella configurazione.

Una volta scaricate e attivate, le risposte locali sono rapide su Apple Silicon. Sui Mac con processore Intel il modello gira sulla CPU e sarà nettamente più lento dei modelli in cloud; Hi, Moose la avverte prima che avvii il download.

I modelli locali non sono una versione ridotta. Gemma 4 supporta la chiamata di strumenti, perciò gli [strumenti della chat](tools-and-specialists.md) funzionano su un modello locale come su uno in cloud.

!!! note "Preview Mode dipende da un modello locale"
    Nel piano gratuito gli [AEO audits](../features/aeo-audits.md) e la valutazione della visibilità funzionano solo con un modello locale attivo. È il motivo principale per configurarne uno subito.

## Modelli più costosi

Alcuni modelli consumano molto più del suo saldo rispetto all'opzione standard. Se ne sceglie uno, Hi, Moose le chiede prima conferma e indica all'incirca quante volte più token consuma, perché non esaurisca il saldo per sbaglio.

I modelli più cari sono vincolati al piano. Se il suo non li comprende, compaiono come non disponibili anziché essere nascosti.

## Ancoraggio tramite ricerca web

La chat può fondare le proprie risposte su risultati di ricerca web in tempo reale per la conversazione in corso. È disponibile in BYOK Premium, BYOK Agency e in tutti i piani gestiti. Non è compresa in BYOK Free né in Preview Mode.

## Lingua

La chat segue una preferenza di lingua, così può lavorare in una lingua diversa da quella dell'interfaccia dell'app.

## Quando un modello non può essere usato

Al posto di una risposta può comparire un messaggio se:

- il modello selezionato non è momentaneamente disponibile (ne provi un altro),
- il modello non è consentito nel suo piano (ne scelga uno compreso), oppure
- è stata allegata un'immagine a un modello che non supporta l'input di immagini. Hi, Moose le indica un modello che lo fa e le propone il passaggio.

## Come si lega a BYOK

Nei piani BYOK la scelta del modello determina quale modello chiama la sua chiave OpenRouter. L'inferenza continua a essere eseguita in locale nell'app desktop. Veda [Tipi di account e piani](../getting-started/account-modes.md) per capire come cambia l'accesso ai modelli tra i piani.

La sua chiave OpenRouter viene salvata per account e non per dispositivo. Se non ne ha ancora salvata una, Hi, Moose gliela chiede la prima volta che una funzione ne ha bisogno, invece di fallire in silenzio.
