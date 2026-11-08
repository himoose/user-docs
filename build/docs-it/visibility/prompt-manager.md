---
source_hash: 52e4fc142ac45ba9ec93251b7b681cb95c1e09d409fef443f88b56ac8cbebaa7
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/visibility/prompt-manager/)

# Prompt Manager

## A cosa serve

Nel Prompt Manager costruisce e organizza le query reali che Hi, Moose verifica sui motori di IA: i prompt che i suoi clienti digiterebbero o porrebbero in modo realistico.

## Organizzare i prompt in categorie

I prompt sono raggruppati in categorie che compaiono nell'elenco dei filtri a sinistra: **Tutti i prompt**, **Senza categoria** e le categorie personalizzate che lei crea (per tema o per campagna, per esempio). Aggiunga una nuova categoria dal campo in fondo all'elenco. Gli spazi di lavoro del piano gratuito sono limitati a 5 categorie.

## Aggiungere e modificare un prompt

Digiti un nuovo prompt e lo aggiunga a una categoria. Per ogni prompt può:

- Modificare il testo del prompt.
- Scegliere su quali motori di IA viene eseguito. **Seleziona modelli** apre un selettore con tutti i motori che il suo piano può monitorare, versioni API e con interrogazione locale comprese (veda [i motori che può monitorare](settings.md#i-motori-che-puo-monitorare)). I motori con interrogazione locale richiedono che l'app desktop sia aperta quando l'esecuzione parte.
- Ritirare il prompt (veda sotto).
- Eliminare il prompt.

A differenza di un'unica impostazione valida per tutto l'account, **la scelta dei modelli avviene prompt per prompt**: un prompt può girare solo su ChatGPT e Gemini mentre un altro copre tutti i motori supportati, così spende la sua dotazione solo sui motori che contano per quella query specifica.

## Cercare e selezionare più prompt

**Cerca prompt** filtra l'elenco per testo. Spunti più prompt e la barra degli strumenti offre **Assegna categorie**, **Assegna modelli**, **Ritira selezionati** ed **Elimina selezionati**, così una modifica su molti prompt si salva in un solo passaggio invece che un prompt alla volta. Può eliminare solo i prompt che ha creato lei, a meno che non sia il proprietario del team.

## Ritirare un prompt

Ritiri un prompt quando è diventato obsoleto ma la sua cronologia merita di essere conservata, per esempio un prompt che nomina l'anno scorso. Un prompt ritirato:

- conserva tutti i risultati passati, così andamenti e report continuano a includerli;
- resta fuori dalle nuove esecuzioni, quindi non costa nulla;
- resta fuori dall'elenco delle [Opportunità](overview.md#opportunita).

I prompt ritirati stanno nella sezione **Prompt ritirati** dell'elenco dei filtri, ciascuno con la data del ritiro, e **Ripristina** lo rimette nel monitoraggio. Aggiungere un nuovo prompt con lo stesso testo di uno ritirato non fa nulla; lo ripristini invece. Anche **Elimina** toglie un prompt dal monitoraggio futuro e conserva i dati storici delle esecuzioni per i report, ma non si può ripristinare.

## Diagnostic Prompts

**Prompt diagnostici** è una categoria riservata e gestita dal sistema, alimentata dal suo [Brand Truth Profile](../getting-started/context/brand-truth-profile.md). Invece di scriverli a mano:

1. Faccia clic su **Genera dalla Verità del brand** (o configuri prima il suo Brand Truth Profile, se non l'ha ancora fatto).
2. Hi, Moose propone prompt pensati appositamente per cogliere quando l'IA descrive male i suoi clienti, le sue capacità o i suoi concorrenti.
3. Esamini i suggerimenti in una finestra: attivi o disattivi ciascun prompt, ne modifichi la formulazione o lo rimuova del tutto prima di aggiungerli al monitoraggio.
4. La finestra mostra un costo stimato prima della conferma: prompt × modelli × esecuzioni a settimana ≈ esecuzioni totali settimanali.

Se il suo Brand Truth Profile non contiene ancora abbastanza informazioni per generare prompt diagnostici significativi, Hi, Moose glielo dice invece di produrre contenuto generico di riempimento: aggiunga prima al suo profilo domande dei clienti, capacità chiave o concorrenti.

## Archiviazione locale dei prompt

Nei piani BYOK, che funzionano solo in locale, le categorie di prompt, le definizioni dei prompt e le selezioni dei modelli vengono salvate sul suo dispositivo anziché sincronizzate con il cloud.
