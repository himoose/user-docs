---
source_hash: 7e432cdd4918eeb01a120c373ca83181288da1c2c0b01d3aee18207e05092124
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/send-moose/overview/)

# Send Moose

## A cosa serve

Send Moose è il posto in cui affida un lavoro invece di farlo lei. Descrive l'incarico in linguaggio semplice («scopri chi viene consigliato al posto nostro per i software di project management e perché», «controlla se la nostra pagina prezzi corrisponde ancora a quello che dicono le pagine di confronto dei concorrenti») e Moose va e lo fa, usando il web e tutto ciò che Hi, Moose già sa del suo progetto.

È la differenza tra una chat che le risponde e un agente che si mette al lavoro. La chat è una conversazione; Send Moose è un incarico che spedisce e a cui torna dopo.

Lo trova nella barra laterale, sotto **Send Moose**.

!!! warning "Send Moose è sperimentale"
    È nell'app e funziona, ma è la cosa più nuova e meno assestata di Hi, Moose. Tenga d'occhio la qualità di ciò che torna, e nei piani a pagamento tenga d'occhio il consumo di token: Scout e Skeptic girano nel cloud anche quando Moose lavora in locale.

## Che cosa porta con sé Moose

Un agente web generico parte da zero e bisogna spiegargli tutto. Moose arriva già collegato al suo progetto:

| Può leggere | Che cosa significa |
|---|---|
| I suoi dati di visibility | Panoramica, Share of Voice, concorrenti, temi, prompt e che cosa è cambiato |
| L'indice del suo sito | Pagine scansionate, che cosa è cambiato su di esse, link interni e il suo [entity graph](../features/entity-graph.md) |
| La sua storia AEO | Audit passati e il loro dettaglio, contesto delle citazioni, accesso dei crawler, copertura dei temi |
| [Google Search Console](../integrations/google-search-console.md) | I suoi dati reali di query e pagine, interrogati in modo iterativo |
| La sua [Libreria](../library/overview.md) | Brief, bozze, key points, FAQ e audit che ha già creato |
| I lavori passati | Che cosa ha trovato e deciso nelle esecuzioni precedenti di questo progetto |

Può anche eseguire dal vivo un [controllo di visibility](../visibility/overview.md) o un [audit AEO](../features/aeo-audits.md) a metà lavoro, quando la risposta lo richiede, invece di dirle di andare a lanciarlo.

## Inviare un lavoro

Descriva l'incarico e prema **Send Moose**. Due opzioni ne definiscono lo svolgimento:

- **Lavoro profondo**: lasci che il lavoro duri ore se serve: molte più pagine, molte più ricerche, più momenti di verifica. Lo usi quando la domanda è davvero ampia, non per una ricerca veloce.
- **Allega file**: fino a sei file per lavoro, come contesto che legge mentre lavora.

Può spuntare **Avvisami quando Moose ha finito** e andarsene. Il lavoro prosegue che lei stia guardando o no, e che resti sulla schermata o no.

## Guardarlo lavorare

**Guarda il browser** apre l'istanza di browser che Moose sta usando, così vede le pagine mentre le legge. **Prendi il controllo** le passa il browser se lui si è bloccato su qualcosa che lei risolve in un secondo, tipo un avviso sui cookie o un accesso, e **Torna al lavoro** glielo restituisce.

Può chiudere quella finestra quando vuole. Moose continua a lavorare.

## Moose, Scout e Skeptic

Nel piano gratuito Moose lavora da solo.

I piani a pagamento aggiungono altri due agenti al lavoro:

- **Scout** trova angolazioni che a Moose sfuggono.
- **Skeptic** contesta le prove prima che arrivino al suo risultato.

Può parlare con ciascuno di loro a metà lavoro dal thread: dire qualcosa a Moose, chiedere a Scout un'altra angolazione, chiedere a Skeptic di insistere su un'affermazione. **Continua** e **Controlla altri cinque risultati** prolungano un'esecuzione che si è fermata in un punto utile.

Scout e Skeptic girano sempre nel cloud tramite OpenRouter, anche quando Moose lavora su un modello locale, quindi costano token.

## Quando Moose ha bisogno di lei

Due cose fermano un lavoro e la aspettano invece di tirare a indovinare:

- **Serve la sua approvazione**: Moose sta per compiere un'azione su un sito web reale, come premere un pulsante di un modulo. Le mostra il pulsante esatto e attende **Approva e continua** oppure **Non farlo**.
- **Serve il suo aiuto**: è bloccato su qualcosa a cui può rispondere solo lei. Scriva una risposta, oppure prema **Decida Moose** perché sia lui a scegliere.

Nulla viene pubblicato, inviato o inoltrato da nessuna parte senza la sua approvazione. Vale anche per le esecuzioni programmate.

## Leggere il risultato

Un lavoro concluso ha quattro schede:

- **Risultato**: ciò che ha trovato, scritto per esteso.
- **Collaborazione**: com'è andata e chi ha contribuito a che cosa: note aggiunte da Scout, obiezioni sollevate da Skeptic, volte in cui è intervenuto lei.
- **Fonti**: ogni pagina che ha aperto, con le prove che ne ha ricavato.
- **Attività**: l'esecuzione completa, filtrabile per strumenti o per agenti.

Da lì può **Salvare nella Libreria**, **Scaricare il report** o chiedere un approfondimento sul risultato in [chat](../chat/overview.md). I file che Moose ha salvato durante il lavoro compaiono sotto **File salvati da Moose**: li apra, ne salvi una copia o li mostri nella cartella. Può salvare file CSV, Markdown, testo semplice, PDF e Word.

## I contenuti che Moose crea

Moose può produrre veri artefatti di Hi, Moose come parte di un lavoro, non solo una risposta scritta: un **content brief**, una **bozza**, dei **key points**, delle **FAQ** o un **audit AEO**. Finiscono nella sua [Libreria](../library/overview.md) come qualsiasi altra cosa, e il risultato del lavoro ci rimanda direttamente.

## Eseguire un lavoro a cadenza fissa

**Esegui a cadenza fissa** trasforma un lavoro occasionale in uno ricorrente: ogni giorno, nei giorni feriali, ogni settimana o ogni mese, a uno o più orari.

I lavori programmati compaiono sotto **Lavori programmati** e si possono mettere in pausa, riprendere o eliminare. Girano senza supervisione: Moose prende da sé le decisioni piccole, e continua a non pubblicare né inviare nulla senza la sua approvazione.

## Lavori passati

Ogni lavoro resta sotto **Lavori passati**, con ricerca e filtri per **Fatti**, **Richiamati**, **Non conclusi** e **Bloccati**, raggruppati in oggi, prima questa settimana e prima ancora. I lavori appartengono al progetto in cui sono stati eseguiti.

## Impostazioni

Le **impostazioni di Send Moose** si salvano per progetto:

- **LLM di Moose**: Automatico usa il modello locale più grande installato, oppure il modello in cloud del suo piano quando l'IA locale è spenta. Può anche fissare un modello specifico.
- **LLM di Scout** e **LLM di Skeptic**: solo nei piani a pagamento, con Gemma 4 31B come predefinito.
- **Modello per i contenuti**: quale modello scrive i brief, le bozze e le FAQ che crea. Per impostazione predefinita lo stesso che usa Moose.
- **Motore di ricerca**: con quale motore cerca.

Tutto ciò che è contrassegnato **Consuma token** gira nel cloud tramite OpenRouter invece che sul suo computer. I lavori in modalità profonda durano di più, quindi costano di più.

## Che cosa serve

- **Un modello locale, oppure un piano a pagamento.** Moose ragiona su un modello Gemma che gira sul suo computer. Lo scarichi una volta dall'avviso a schermo e i lavori non le costano nulla. I piani a pagamento possono metterlo invece su un modello in cloud. Se ha spento l'IA locale ed è nel piano gratuito, Send Moose glielo dice e le propone di riaccenderla.
- **Un sito web sul progetto**, per i lavori sul suo sito, sul suo marchio o sui concorrenti. I lavori generici sul web funzionano bene anche senza.

## Dove andare da qui

- **[Chat](../chat/overview.md)**: per il lavoro che vuole guidare passo per passo invece di affidare.
- **[Workflows](../workflows/overview.md)**: per una ricetta fissa che parte da un innesco, invece che per un incarico aperto.
- **[Libreria](../library/overview.md)**: dove restano i report e i contenuti nati da un lavoro.
