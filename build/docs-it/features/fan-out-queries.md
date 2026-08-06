---
source_hash: 3b2a6720bd62d36c159ec05f39cfb8f6e59efa7a27d7e6054053a2fcb1d2c950
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/features/fan-out-queries/)

# Query fan-out di ChatGPT

## A cosa serve

Questa funzione acquisisce le singole ricerche «fan-out» che il passaggio di ricerca web di OpenAI ha eseguito mentre rispondeva al suo prompt, insieme alle fonti citate e a un'anteprima della risposta.

!!! info "Che cos'è, per la precisione"
    Hi, Moose chiama l'API Responses di OpenAI con lo strumento di ricerca web attivo e rilegge poi le ricerche compiute da quell'esecuzione. Non è un'acquisizione del fan-out del prodotto di consumo ChatGPT, che OpenAI non espone. Ciò che ottiene è l'approssimazione più vicina disponibile: lo stesso livello di ricerca web, guidato dalla stessa famiglia di modelli, così l'espansione delle query segue da vicino quella di ChatGPT Search. Lo consideri un segnale solido, non una trascrizione, e metta in conto una certa variabilità tra esecuzioni dello stesso prompt.

!!! note "Disponibilità"
    Questa funzione esegue in background un'acquisizione gestita della traccia di ricerca web di OpenAI, perciò richiede uno spazio di lavoro **gestito a pagamento**. Vale anche nei piani BYOK: BYOK mantiene locale l'esecuzione principale dei modelli, ma l'acquisizione del fan-out usa l'infrastruttura gestita di Hi, Moose, il cui funzionamento ha un costo per noi. Non è quindi compresa né in BYOK Free né in BYOK Premium. Neppure Preview Mode la comprende.

## Come eseguirla

1. Dalla [Chat](../chat/overview.md) scelga l'avvio rapido **Capture ChatGPT fan-out queries** (oppure lo chieda direttamente).
2. Inserisca il prompt che vuole esaminare.
3. Hi, Moose acquisisce la risposta di ChatGPT e restituisce:
    - Le singole query fan-out eseguite da ChatGPT.
    - Le fonti citate.
    - Un'anteprima della risposta.

Se per una determinata esecuzione OpenAI non ha esposto query fan-out distinte, Hi, Moose le mostra comunque la traccia di ricerca gestita e le fonti citate che è riuscito ad acquisire, invece di presentare un risultato vuoto o inventato.

## Perché è importante

Le query fan-out rivelano l'espansione delle query dietro una risposta ancorata al web, il che aiuta a capire quali formulazioni precise stiano portando (o mancando) citazioni verso i suoi contenuti. È materiale che confluisce direttamente in ciò che monitora in [Visibility](../visibility/overview.md) e in ciò che pianifica nei [Content Briefs](content-briefs.md).
