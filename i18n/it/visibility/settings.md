---
source_hash: 185a9611ccdaef3c98b73cc4349bc1d586a1fa03b38212ecab7ffca94af54a21
---
# Impostazioni di Visibility

## A cosa serve

Le impostazioni di Visibility governano con quale frequenza Hi, Moose controlla la visibilità, quale modello valuta i risultati e quali termini di marca e domini contano nelle sue metriche. I prompt e i temi si gestiscono nel [Prompt Manager](prompt-manager.md); questa schermata riguarda la meccanica delle esecuzioni.

## Pianificazione delle esecuzioni

- **Frequenza**: giornaliera, nei giorni feriali, settimanale o solo manuale.
- **Orario di esecuzione preferito** e, per la frequenza settimanale, un **giorno della settimana**. Le esecuzioni avvengono nel suo fuso orario locale.
- **Campioni per prompt**: le esecuzioni programmate possono ripetere ogni prompt più volte e mediare i risultati per ottenere un tasso di visibilità più stabile. Il pulsante manuale **Esegui ora** usa sempre un solo campione. Aumentare questo valore moltiplica in egual misura il consumo di token, e Hi, Moose la avvisa prima di salvare un valore più alto.

!!! note "Le esecuzioni programmate richiedono che questo dispositivo sia acceso"
    In **Preview Mode** e nei piani **BYOK** la pianificazione gira in locale sulla sua macchina: un'esecuzione programmata non può partire se il computer è spento o in sospensione, o se Hi, Moose è completamente chiuso. Tenga l'app aperta (o ridotta nella barra delle applicazioni) perché le esecuzioni programmate possano avvenire. I **piani gestiti** sbloccano una pianificazione in cloud sempre attiva, che non dipende dallo stato del suo dispositivo. I motori con interrogazione locale richiedono comunque l'app aperta, in qualunque piano, perché quei controlli partono dalla sua macchina.

## Notifiche via e-mail

Attivi **Report email pianificati sulla visibilità** per ricevere il report di visibilità via e-mail al termine delle esecuzioni programmate. È una preferenza di notifica personale, distinta dalle [impostazioni di notifica dell'Inbox](../inbox/notifications.md).

## Termini e domini di marca secondari

- **Termini di marca secondari**: formulazioni alternative o varianti ortografiche del suo marchio che devono contare anch'esse come menzione.
- **Domini secondari**: altri domini che devono contare come citazioni valide del marchio per questo progetto, oltre al suo dominio principale.

## Monitoraggio dei concorrenti

Aggiunga i marchi con cui questo progetto viene confrontato. Ogni concorrente richiede un nome e, facoltativamente, un sito web.

Quando una risposta dell'IA ne menziona o ne cita uno, il dato alimenta [Share of Voice, citazioni dei concorrenti e lacune](competitors.md).

Questo elenco è condiviso con il suo [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), perciò i concorrenti aggiunti in uno dei due punti compaiono in entrambi. Il numero di concorrenti monitorati nelle esecuzioni di visibilità è limitato: la schermata indica il limite e la avvisa se il suo elenco lo supera, così sa che vengono monitorati solo i primi.

## Modello di valutazione

Scelga il modello che Hi, Moose usa per valutare sentiment, scostamento narrativo e copertura funzionale dopo aver acquisito una risposta:

- Il **valore automatico** si adatta al suo piano:
    - **Preview Mode** usa un modello locale Gemma 4 attivo. La valutazione viene saltata finché non ne è installato e attivo uno (Impostazioni → Local Model).
    - **I piani BYOK** valutano con la sua chiave OpenRouter.
    - **I piani gestiti** valutano tramite l'instradamento dei modelli gestiti di Hi, Moose (la valutazione con modello locale resta valida dove è supportata).
- Può anche selezionare un modello specifico anziché l'opzione automatica.

I modelli gratuiti di OpenRouter non sono più proposti come opzione di valutazione. Si sono rivelati abbastanza inaffidabili nella valutazione strutturata da rendere i risultati non degni di essere riportati.

## Modelli predefiniti per i nuovi prompt

Scelga quali motori sono preselezionati ogni volta che aggiunge un prompt nel [Prompt Manager](prompt-manager.md); potrà comunque modificare la selezione prompt per prompt. I modelli contrassegnati come **A pagamento** richiedono un piano a pagamento o BYOK; Preview Mode è limitato ai modelli con interrogazione locale. Ogni modello selezionato qui incide sul consumo di token quando vengono eseguite le verifiche di visibilità.

## Ripetere la configurazione iniziale

Riavvii in qualsiasi momento la procedura guidata di configurazione della visibilità per aggiornare da zero il dominio monitorato, i suoi prompt e le sue preferenze di monitoraggio.
