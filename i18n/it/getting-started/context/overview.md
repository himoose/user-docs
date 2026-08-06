---
source_hash: 05fae21b2ec70be5a8bae1ca0e58f085c9da2140a80bae1dc2e083051aeffb43
---
# Context

## A cosa serve

**Contesto** è lo strato di fondamento nella navigazione di sinistra dell'app desktop. È il contesto operativo condiviso del suo progetto corrente: le informazioni che l'operatore, la chat e tutte le funzioni di generazione riutilizzano invece di ripartire da zero a ogni richiesta.

Context si compone di tre elementi distinti:

| | Ambito | A cosa serve |
|---|---|---|
| **[Brand Voice](brand-voice.md)** | Per progetto | Come deve suonare il suo marchio: tono, pubblico, valori, terminologia. Definisce lo stile di scrittura di tutto ciò che Hi, Moose genera. |
| **[Brand Truth Profile](brand-truth-profile.md)** | Per progetto | Una fonte di verità leggibile dalle macchine su ciò che la sua azienda è, vende e serve davvero. Serve a rilevare quando le risposte dell'IA la travisano o se ne discostano. |
| **[Su di lei](about-you.md)** | Per dispositivo, non per progetto | Note su di lei come persona: il suo ruolo, i suoi obiettivi e il suo modo di lavorare, perché la chat conosca la persona e non solo il marchio. |

## Perché sono tre artefatti separati

Brand Voice e Brand Truth Profile rispondono a domande diverse, anche se entrambi descrivono il suo marchio:

- **Voce del brand** risponde a «come deve suonare questo?»: tono, stile, preferenze lessicali. È una guida creativa e stilistica per i contenuti generati.
- **Profilo della verità del brand** risponde a «che cosa è vero su di noi?»: descrizione canonica, cliente ideale, offerta, concorrenti e i punti precisi su cui l'IA tende a sbagliare. È un riferimento fattuale per cogliere i travisamenti, non una guida di stile.

**Su di lei** si distingue da entrambi: non riguarda affatto il marchio. È contesto personale su **di lei**, la persona che usa l'app, salvato in locale sul suo dispositivo invece di essere legato a un progetto. La accompagna quindi tra i progetti, invece di azzerarsi a ogni cambio di spazio di lavoro.

## Dove viene usato Context

- **Voce del brand** viene riutilizzata nei [Content Briefs](../../features/content-briefs.md), nel [generatore di FAQ](../../features/faq-generator.md), nell'[estrattore di Key Points](../../features/key-points.md), in [bozze, anteprima e pubblicazione](../../features/drafts-and-publishing.md) e nelle raccomandazioni degli [AEO audits](../../features/aeo-audits.md).
- **Profilo della verità del brand** viene riutilizzato durante le esecuzioni di [Visibility](../../visibility/overview.md), dove Hi, Moose verifica se la risposta di un motore di IA sul suo marchio è coerente con la sua descrizione canonica, la sua offerta, i suoi concorrenti e i modelli noti di travisamento.
- **Su di lei** viene riutilizzato nella [Chat](../../chat/overview.md), perché le risposte tengano conto del suo ruolo, dei suoi obiettivi e del suo stile di comunicazione preferito.

## Come compilarlo

Ogni artefatto indica quanti campi ha compilato e mostra una breve anteprima non appena aggiunge qualcosa. Tutti i campi dei tre artefatti sono facoltativi: Hi, Moose funziona anche con un contesto parziale e diventa più preciso man mano che lei aggiunge dettagli.

Per la Brand Voice in particolare non deve compilare ogni campo a mano: un'azione di **compilazione automatica** può scansionare il sito del suo progetto in locale e proporre valori per i campi vuoti.

## Archiviazione locale e sincronizzazione in cloud

Per impostazione predefinita Brand Voice e Brand Truth Profile sono salvati **in locale per il progetto corrente**, mentre Su di lei è salvato **in locale sul suo dispositivo**. La sincronizzazione in cloud, che conserva Brand Voice e Brand Truth Profile e li condivide con il team, è disponibile in **tutti i piani a pagamento**, compresi i piani BYOK a pagamento. Preview Mode e BYOK Free restano solo locali; passando a un piano superiore si attiva la sincronizzazione, così il suo team condivide la stessa base ed essa è protetta se accade qualcosa alla sua macchina.

!!! note "Nei piani BYOK"
    La scansione del contesto di marca (il passaggio di compilazione automatica) e l'analisi Brand Truth vengono eseguite in locale, nell'app desktop. Hi, Moose non ha bisogno di vedere i contenuti del suo sito sui propri server per costruire o utilizzare questo contesto.
