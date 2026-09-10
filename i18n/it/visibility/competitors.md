---
source_hash: 1c85ff53a55d4b6ecb7d8fbdd11b64ab53c6c37bdd4cb12540b5dc7616afc495
---
# Concorrenti e Share of Voice

## A cosa serve

Rispondere alla domanda a cui i suoi numeri non possono rispondere: quando un assistente di IA consiglia qualcosa nella sua categoria, quanto spesso è lei, e chi viene scelto al posto suo?

Lo trova in **Visibility → Concorrenza**.

## Configurare i concorrenti

Aggiunga i concorrenti in **Visibility → Settings → Competitor tracking**. Ciascuno richiede un nome e, facoltativamente, un sito web.

Questo elenco è condiviso con il suo [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), perciò i concorrenti aggiunti in uno dei due punti compaiono in entrambi.

Quanti vengono monitorati nelle esecuzioni di visibilità dipende dal suo piano: **5 in Preview Mode e BYOK Free, 15 in tutti i piani a pagamento**. La schermata delle impostazioni indica il numero e la avvisa se il suo elenco è più lungo, così sa che vengono monitorati solo i primi.

Da tre a cinque concorrenti reali funzionano meglio di un elenco lungo. Sono i marchi con cui la si confronta davvero, non l'intero settore.

## Share of Voice

Lo **Share of Voice** è la fetta di attenzione che ogni marchio ottiene nelle risposte delle IA nel periodo, ma non tutte le menzioni valgono allo stesso modo.

Essere nominati per primi in una risposta vale più che essere nominati per sesti, perché è quello il nome che il lettore porta via. Per questo ogni menzione viene pesata in base al punto in cui il marchio compare nella risposta:

| Posizione nella risposta | Peso |
|---|---|
| 1ª | 1,00 |
| 2ª | 0,70 |
| 3ª | 0,50 |
| 4ª | 0,35 |
| 5ª | 0,25 |
| 6ª o successiva | 0,15 |

Una menzione di cui non è stato possibile leggere la posizione conta 0,50. In più, una risposta che **cita il sito del marchio** aggiunge altri 0,50, perché una citazione è un segnale più forte di una semplice menzione.

Il punteggio pesato di ciascun marchio viene poi diviso per il totale di tutti i marchi monitorati, e questo dà la sua quota.

La scheda Competition apre con la sua posizione, e l'elenco ordinato sotto mostra ogni marchio monitorato con la sua quota. Accanto compaiono la **quota di menzioni** e la **quota di citazioni**, cioè i conteggi semplici non pesati, così può vedere il quadro grezzo insieme a quello pesato.

!!! note "Perché il dato pesato può non coincidere con il conteggio semplice"
    Può essere menzionato quanto un concorrente e restare comunque dietro di lui nello Share of Voice, se lui arriva sempre per primo e lei sempre per quarto. Quello scarto è proprio il senso della metrica: le sta dicendo che le menzioni ci sono ma la prominenza no, che è un problema diverso e si risolve in modo diverso.

!!! warning "Share of Voice non è Mention Rate"
    Sono due numeri distinti e si muovono in modo indipendente.

    Lo **Share of Voice** è la sua fetta pesata dell'attenzione complessiva verso i marchi. È relativo: un concorrente può abbassarlo senza che nulla cambi da parte sua.

    Il **Mention Rate** (nella scheda Overview) è la quota di prompt monitorati in cui il suo marchio è stato menzionato. È assoluto, non pesato, e ignora del tutto i concorrenti.

    Il suo Mention Rate può salire mentre il suo Share of Voice scende, se i concorrenti sono cresciuti più in fretta di lei. Vale la pena seguire entrambi, per ragioni diverse.

## Andamento dello Share of Voice

Il grafico di andamento rappresenta lo **Share of Voice** o il **Tasso di menzione** nel tempo, così vede se un cambiamento dipende da una sua crescita, dalla crescita di un concorrente o dal fatto che l'intera categoria è diventata più rumorosa.

## Top Competitor Citations

Quali pagine dei concorrenti i motori di IA citano davvero come fonte. È il pannello più direttamente utile della scheda: sono le URL precise che si aggiudicano le citazioni che lei vuole, e indicano che cosa i motori di risposta considerano oggi la fonte migliore su quelle domande.

Lo confronti con **Pagine più citate** nella scheda Overview, che mostra lo stesso dato per il suo dominio.

## Competitor Gaps

Domande in cui un concorrente è comparso in una risposta dell'IA e il suo marchio no.

Ogni lacuna indica quali concorrenti sono comparsi e in quali motori è stata rilevata, con un'etichetta:

- **Nessuna visibilità**: il suo marchio non compare per questa domanda in nessun motore.
- **Parziale**: il suo marchio compare per questa domanda, ma non in tutti i motori. La riga indica in quali compare.

Le righe parziali spesso non richiedono alcun intervento. Una domanda in cui compare in quattro motori su cinque non è lo stesso problema di una in cui non compare da nessuna parte, e l'etichetta serve proprio a distinguerle a colpo d'occhio.

Se l'elenco è troncato, restringa l'intervallo di date o i filtri per vedere il resto.

## Da dove arrivano i dati sui concorrenti

Le menzioni e le citazioni dei concorrenti vengono estratte dalle stesse osservazioni delle esecuzioni di visibilità che riguardano lei. Non viene eseguito nulla in più e per questi pannelli non si scansionano i siti dei concorrenti. Se un'esecuzione è fallita o un modello non era disponibile, quelle osservazioni vengono escluse anziché contate come assenza.

## Nel report esecutivo

Share of Voice, principali citazioni dei concorrenti e lacune sono tutti inclusi nel [report esecutivo](overview.md#esportare) esportato, così il quadro competitivo arriva a clienti e responsabili senza che lei debba ricostruirlo a mano.
