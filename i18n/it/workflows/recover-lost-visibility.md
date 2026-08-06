---
source_hash: 7907c08f25052f66801891d4fc6f24fe3bdcd307070021aede9005fe5995996b
---
# Recuperare la visibilità perduta

## A cosa serve

È la procedura di workflow per i **contenuti esistenti**: sorveglia i suoi risultati di [visibilità](../visibility/overview.md) e, quando qualcosa cala in modo significativo, stabilisce automaticamente se una pagina esistente può essere corretta o se servono contenuti nuovi, e prepara il lavoro per la sua revisione.

## Comporre il workflow

Il workflow si legge come un'unica frase, formata da queste scelte:

> **Quando** [lo share of mentions cala / lo share of citations cala / lo share of mentions cresce / lo share of citations cresce] **di** [una soglia, da 1 a 99 punti] **per** [tutti i temi / un tema monitorato specifico], Hi, Moose individua i prompt interessati e poi [prepara una correzione dei contenuti / mi avvisa].

- **Attivatore**: quale metrica sorvegliare e se le interessano i cali o le crescite. Se sceglie un attivatore di crescita, l'unica azione finale disponibile è **avvisami**: le crescite non hanno un percorso di correzione dei contenuti, perché non c'è nulla da riparare.
- **Soglia**: quanti punti di variazione devono essere considerati significativi, perché il rumore abituale non faccia scattare il workflow.
- **Ambito tematico**: applicare questo workflow a tutto ciò che monitora oppure limitarlo a un tema preciso.
- **Azione finale**: **preparare una correzione dei contenuti** (prosegue con la logica di diramazione qui sotto) oppure **avvisami** (crea soltanto una voce nell'Inbox, senza preparare alcuna azione sui contenuti).

## Quando l'azione finale è «preparare una correzione dei contenuti»

Altre due scelte si diramano a seconda che esista o meno una pagina adatta:

- **Se esistono pagine corrispondenti**: scelga che cosa deve fare Hi, Moose: **eseguire un AEO audit**, **generare FAQ e schema**, **generare key points** oppure **niente**.
- **Se non esiste alcuna pagina corrispondente**: scelga tra **creare un brief e una nuova bozza** oppure **niente**.

Questa diramazione è il senso stesso della procedura: non consiglia alla cieca un nuovo articolo ogni volta che la visibilità cala. Verifica prima se correggere qualcosa che lei ha già sia la mossa migliore, e propone contenuti nuovi solo quando nulla di esistente è adatto.

## Come viene eseguito

Questo workflow non ha un pulsante di esecuzione manuale. Si valuta automaticamente ogni volta che si conclude un'esecuzione di visibilità, confrontando l'ultima completata con la precedente. Quando scatta, il risultato, compresi i prompt interessati e l'azione intrapresa, arriva nella sua [Inbox](../inbox/overview.md), collegato al cambiamento di visibilità che lo ha provocato.
