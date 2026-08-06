---
source_hash: 3856622231055de776fe82082345666ad4d8429b9d735111e9d399831a122f47
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/features/grounding-queries/)

# Query di grounding di AI Mode

## A cosa serve

Questa funzione le mostra le ricerche Google che Gemini ha eseguito mentre fondava la propria risposta a un prompt, insieme alle fonti citate e alla risposta ancorata che ha prodotto.

!!! info "Che cos'è, per la precisione"
    Hi, Moose chiede all'API di Gemini di rispondere al suo prompt con l'ancoraggio alla ricerca Google attivo, e poi rilegge l'elenco delle ricerche che quel modello ha effettuato. Non è una registrazione dell'AI Mode di consumo di Google. AI Mode è una superficie distinta e non espone a nessuno le proprie query interne. Ciò che ottiene è l'approssimazione più vicina disponibile: lo stesso indice di ricerca, la stessa famiglia di modelli e formulazioni delle query molto simili a quelle prodotte da AI Mode. Lo consideri un segnale solido, non una trascrizione, e metta in conto una certa variabilità tra esecuzioni dello stesso prompt.

!!! note "Disponibilità"
    Questa funzione esegue in background una chiamata gestita di ancoraggio a Gemini, perciò richiede uno spazio di lavoro **gestito a pagamento**. Vale anche nei piani BYOK: BYOK mantiene locale la generazione principale della chat, ma l'acquisizione delle query di grounding usa l'infrastruttura gestita di Hi, Moose, il cui funzionamento ha un costo per noi. Non è quindi compresa né in BYOK Free né in BYOK Premium. Neppure Preview Mode la comprende.

## Come eseguirla

1. Dalla [Chat](../chat/overview.md) scelga l'avvio rapido **Acquisisci le query di grounding di AI Mode** (oppure lo chieda direttamente).
2. Inserisca il prompt che vuole esaminare.
3. Hi, Moose verifica le query di grounding di Gemini per quel prompt e restituisce:
    - Le query di grounding effettivamente usate da Gemini.
    - Le fonti citate.
    - La risposta ancorata stessa.

## Perché è importante

Le query di grounding le mostrano come un motore di risposta trasforma un singolo prompt in un ventaglio di ricerche reali. È utile per capire perché la sua pagina viene ripresa oppure no, e per individuare varianti di query che al momento non sta monitorando in [Visibility](../visibility/overview.md) o nel [Prompt Manager](../visibility/prompt-manager.md).

## Se un'esecuzione fallisce

Se Hi, Moose non riesce a raccogliere query di grounding reali per un prompt, glielo dice invece di presentare una supposizione. Riprovi tra poco, oppure verifichi che lo spazio di lavoro abbia un abbonamento gestito attivo.
