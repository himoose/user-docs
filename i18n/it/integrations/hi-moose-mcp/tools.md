---
source_hash: 02739399b48594689facbef6808edfaaedea42f90e6577cf6c6b9bb9f23939c1
---

# Riferimento degli strumenti

Ogni strumento che Hi, Moose MCP offre a un'app collegata, con cosa riceve e cosa restituisce. Non chiami gli strumenti tu: l'app sceglie lo strumento in base a ciò che chiedi. Questa pagina ti dice cosa chiedere e cosa aspettarti.

Ogni strumento tranne `list_projects` e `get_result` riceve un **progetto**, con il nome mostrato in Hi, Moose. Di' il nome del progetto nella richiesta quando ne hai più di uno, per esempio «per il progetto Acme».

## Quanto tempo richiedono

| Strumento | Tempo tipico |
|---|---|
| Elencare progetti, brief, bozze | Pochi secondi |
| Verificare la copertura del sito | Meno di un minuto |
| Verifica di visibilità, lettura di una risposta | Pochi secondi |
| Elenco delle opportunità | Da pochi secondi a un minuto |
| Brief di contenuto, bozza, FAQ, punti chiave, immagine in evidenza | Da uno a tre minuti |
| Audit AEO | Da due a quattro minuti |
| Link interni | Circa un minuto |
| Episodio audio | 5 minuti per short, 9 per standard, 15 per deep |

Quando uno strumento impiega più tempo di quanto l'app è disposta ad aspettare, risponde «ancora in corso» con un id del lavoro. L'app usa poi `get_result` per ritirare il lavoro pronto; chiedile di controllare di nuovo se non lo fa.

## Progetti e Library

### list_projects

Elenca i progetti Hi, Moose su cui puoi lavorare. Ogni altro strumento ha bisogno di un progetto, quindi l'app di solito chiama prima questo.

Chiedi: «Elenca i miei progetti Hi, Moose.»

### list_briefs

Elenca i brief di contenuto salvati nella Library per un progetto, dal più recente, fino a 50. Usalo quando fai riferimento a un brief creato in precedenza.

Chiedi: «Mostra i brief salvati per Acme.»

### list_drafts

Elenca le bozze salvate nella Library per un progetto, dalla più recente, fino a 50.

Chiedi: «Quali bozze ho in Acme?»

### get_result

Ritira il lavoro avviato da un altro strumento, tramite l'id del lavoro. Aspetta fino a un minuto che finisca. L'app lo chiama da sola; ti serve solo quando l'app dice che il lavoro è ancora in corso e vuoi che controlli di nuovo.

## Copertura del sito

### check_site_coverage

Verifica nell'ultima scansione del tuo sito se ci sono pagine che coprono già uno o più argomenti.

| Input | Obbligatorio | Significato |
|---|---|---|
| topics | sì | Da una a quindici frasi brevi, per esempio «generazione SBOM per Python» |
| parentTopic | no | L'argomento più ampio a cui appartengono i topic, usato per valutare la copertura parziale |

Per ogni argomento risponde **covered**, **partial**, **uncovered** o **unknown**, con gli URL delle pagine più vicine come prova e la data della scansione verificata. Unknown significa che la verifica non ha potuto girare per quell'argomento, non che il sito ne è privo.

Chiedi: «Il nostro sito copre già SCA vs SAST?»

## Contenuti

### create_content_brief

Crea un brief di contenuto basato sulla ricerca: obiettivo, pubblico, motivazione, gruppi di parole chiave, struttura consigliata e vincoli, fondato sui risultati di ricerca attuali, sulla scansione del tuo sito, sulle linee guida del brand e su Brand Truth.

| Input | Obbligatorio | Significato |
|---|---|---|
| topic | sì | L'argomento, la domanda o il titolo provvisorio, fino a 400 caratteri |
| targetUrl | no | La pagina del tuo sito a cui è destinato il brief |
| templateType | no | Il tipo di contenuto: «Blog post», «Landing page», «Comparison page», «Guide» |
| guidance | no | Requisiti decisi altrove: taglio, punti da includere, tono. Fino a 4.000 caratteri. |

Restituisce il brief come testo più un id del brief che lo strumento per le bozze usa. Salvato nella Library.

Chiedi: «Scrivi un brief di contenuto per una guida alla generazione SBOM per team Python.»

### create_draft

Scrive una prima bozza pubblicabile da un brief, nella voce del tuo brand, fondata sul brief, su Brand Truth e sulle linee guida del brand, con link interni scelti dalla scansione del tuo sito e una passata di rifinitura.

| Input | Obbligatorio | Significato |
|---|---|---|
| briefId | uno dei due | Un brief creato in Hi, Moose |
| brief | uno dei due | Un brief scritto altrove, come testo, fino a 60.000 caratteri |
| briefTitle | no | Il titolo provvisorio, quando passi un brief come testo |
| templateType | no | Il tipo di contenuto, quando passi un brief come testo |
| guidance | no | Requisiti aggiuntivi, fino a 4.000 caratteri |

Restituisce la bozza come testo più un id della bozza. Salvata nella Library.

Chiedi: «Scrivi l'articolo da quel brief.» oppure «Ecco un brief che ho scritto, scrivi la bozza per Acme: ...»

### create_featured_image

Crea un'immagine in evidenza per un articolo, 1200 per 630, nel tuo stile di immagini salvato quando ne è impostato uno.

| Input | Obbligatorio | Significato |
|---|---|---|
| draftId | uno dei due | Una bozza creata in Hi, Moose |
| title e summary | uno dei due | Il titolo dell'articolo e un breve riassunto, fino a 6.000 caratteri, quando non c'è una bozza |
| styleIntent | no | Un desiderio per questa singola immagine: atmosfera, scena, colori. Lo stile salvato si applica comunque. |

Restituisce l'immagine e un link al PNG. Il file viene salvato anche sul dispositivo host.

Chiedi: «Crea un'immagine in evidenza per quella bozza, luce serale, senza persone.»

### create_faqs

Scrive le domande frequenti con le risposte per un contenuto, nella voce del tuo brand, più il markup schema FAQPage pronto da incollare nella pagina. Negli account a pagamento le domande vengono prima ricavate dal comportamento di ricerca reale.

| Input | Obbligatorio | Significato |
|---|---|---|
| draftId | uno dei due | Una bozza salvata |
| url | uno dei due | Una pagina pubblicata del tuo sito |
| guidance | no | Pubblico, domande che devono comparire, tono. Fino a 4.000 caratteri. |

Chiedi: «Scrivi le FAQ per https://acme.example/guides/sbom.»

### create_key_points

Scrive i punti chiave di un contenuto: affermazioni brevi e citabili nella voce del tuo brand, che i motori di risposta possono riprendere.

| Input | Obbligatorio | Significato |
|---|---|---|
| draftId | uno dei due | Una bozza salvata |
| url | uno dei due | Una pagina pubblicata del tuo sito |
| guidance | no | Pubblico, punti che devono comparire, tono. Fino a 4.000 caratteri. |

Chiedi: «Dammi i punti chiave per la bozza della guida SBOM.»

## Audit e link

### run_aeo_audit

Esegue un audit di answer engine optimization su un contenuto: un punteggio su 100, punteggi per categoria (struttura, estraibilità, potenziale di citazione, segnali di fiducia, freschezza, prontezza alla risposta e altro), i problemi trovati e modifiche concrete con il testo proposto.

| Input | Obbligatorio | Significato |
|---|---|---|
| url | uno dei tre | Una pagina pubblicata. La scelta migliore, perché i controlli tecnici come l'accesso dei crawler IA e le date della pagina girano solo su una pagina pubblicata. |
| draftId | uno dei tre | Una bozza salvata |
| content | uno dei tre | Il contenuto come testo, per una pagina non ancora pubblicata. Fino a 50.000 caratteri. |
| targetQuery | no | La domanda o il prompt di ricerca che il contenuto dovrebbe vincere, fino a 200 caratteri. Senza, Hi, Moose ne deduce uno. |

Negli account a pagamento sono incluse le prove dalla ricerca attuale.

Chiedi: «Fai l'audit di https://acme.example/guides/sbom per la query "SBOM generation tools".»

### find_internal_links

Pianifica i link interni per un contenuto usando la scansione del tuo sito. Restituisce due elenchi: le pagine a cui questo contenuto dovrebbe rimandare, ognuna con il testo di ancoraggio da usare, e le pagine esistenti che dovrebbero aggiungere un link verso questo contenuto, ognuna con il testo di ancoraggio da usare su quella pagina. Le pagine già collegate in una delle due direzioni vengono escluse.

| Input | Obbligatorio | Significato |
|---|---|---|
| url | uno dei tre | Una pagina del tuo sito, pubblicata |
| draftId | uno dei tre | Una bozza salvata |
| content | uno dei tre | Il contenuto come testo, fino a 50.000 caratteri |
| title | no | Il titolo, quando passi il contenuto come testo |

I risultati coprono le pagine scansionate finora e indicano la data della scansione. Le pagine pubblicate dopo l'ultima scansione non sono incluse.

Chiedi: «Pianifica i link interni per la bozza della guida SBOM.»

## Visibilità nella ricerca IA

### visibility_check_topic

Risponde a «compariamo nella ricerca IA per X» dai risultati di visibilità che Hi, Moose ha salvato. Passa la domanda con parole tue; Hi, Moose la abbina ai prompt monitorati, in qualsiasi lingua.

| Input | Obbligatorio | Significato |
|---|---|---|
| question | sì | L'argomento o la domanda, fino a 400 caratteri |
| lookbackDays | no | Quanti giorni di risultati salvati leggere. Predefinito 90. |
| engine | no | Solo questo motore, per nome, per esempio «ChatGPT» |

Restituisce, per motore, se il brand è stato menzionato o citato nell'ultima esecuzione e in una precedente, i tassi di menzione e di citazione nel periodo, un breve estratto dell'ultima risposta in cui il brand è comparso, i prompt abbinati e gli altri brand visti. Ogni estratto porta un id della risposta per lo strumento successivo. I risultati coprono solo i prompt monitorati sui motori monitorati, mai l'intera ricerca IA. Legge i risultati salvati e non avvia mai nuove verifiche.

Chiedi: «Compariamo nella ricerca IA per la generazione SBOM?»

### visibility_get_answer

Recupera una risposta salvata tramite il suo id: il prompt, il motore, la data, se il brand è stato menzionato o citato, le fonti elencate dal motore, le note del valutatore e il testo completo della risposta. Il testo è ciò che il motore ha scritto in quel momento.

Chiedi: «Mostrami la risposta completa di ChatGPT da quel risultato.»

### visibility_list_opportunities

Restituisce la coda di lavoro in ordine di priorità che Hi, Moose costruisce dai risultati di visibilità salvati, le stesse righe della scheda Opportunità. Ogni riga indica la lacuna esatta, il passo successivo in una frase, la priorità con le sue ragioni, quanto la lacuna si è ripetuta tra le esecuzioni, lo sforzo, lo stato impostato dal team e un id dell'opportunità.

| Input | Obbligatorio | Significato |
|---|---|---|
| lookbackDays | no | Giorni di risultati salvati da leggere. Predefinito 7, come la scheda Opportunità. Al massimo 90. |
| limit | no | Righe da restituire, le migliori per prime. Predefinito 10, al massimo 25. |
| action | no | Solo un tipo di riga: `create-coverage`, `improve-page`, `earn-inclusion`, `correct-description` o `investigate-change` |
| priority | no | `high`, `medium` o `low` |
| includeClosed | no | Restituisce anche le righe segnate come fatte, scartate o rimandate. Predefinito false. |
| opportunityId | no | Un id da un risultato precedente. Restituisce le prove complete di quella sola riga invece dell'elenco. |

I cinque tipi di riga: **create-coverage** (nessuna tua pagina risponde a un prompt che i concorrenti vincono), **improve-page** (una tua pagina è citata o è la più vicina ma il brand è escluso o dietro agli altri), **earn-inclusion** (una pagina di terzi citata dai motori nomina i concorrenti ma non te), **correct-description** (le risposte ripetono un'affermazione sul brand da verificare) e **investigate-change** (il brand era nominato o citato prima e ora non più).

Chiedi: «Su cosa dovremmo lavorare per la ricerca IA questa settimana?» e poi «Mostrami le prove per la prima.»

## Audio

### create_audio

Crea un episodio «ascolta questo articolo»: una conversazione parlata a due voci sul contenuto, resa come MP3 e ospitata da Hi, Moose, più lo snippet HTML per il lettore incorporabile.

| Input | Obbligatorio | Significato |
|---|---|---|
| url | uno dei tre | Una pagina pubblicata |
| draftId | uno dei tre | Una bozza salvata |
| content e title | uno dei tre | L'articolo come testo, da 1.200 a 200.000 caratteri, con il suo titolo |
| length | no | `short` (circa 4 minuti), `standard` o `deep`. Predefinito short. |
| hostVoice, guestVoice | no | Due voci diverse. Predefinite Sulafat e Fenrir. |
| language | no | Lingua della narrazione. Predefinita: la lingua del contenuto. |
| focus | no | Su cosa deve concentrarsi la conversazione, fino a 500 caratteri |
| theme, layout, color, showTitle, customTitle, showTranscript, hideAttribution | no | L'aspetto del lettore, vedi sotto |

La [pagina delle impostazioni audio](https://himoose.com/hi-moose-mcp/audio/) ti permette di ascoltare ogni voce, scegliere durata, lingua e aspetto del lettore, e copiare una riga di impostazioni da incollare nella chat. Mentre l'episodio viene generato il dispositivo host non lavora su nient'altro. Se il risultato dice che l'episodio è ancora in generazione, lo strumento successivo lo ritira qualche minuto dopo.

Chiedi: «Trasforma https://acme.example/guides/sbom in audio, short, con Zephyr e Charon.»

### get_audio_embed

Restituisce lo snippet del lettore per un episodio esistente, con un nuovo aspetto quando vengono passati i campi del lettore. L'audio non viene rigenerato. È anche il modo per ritirare un episodio che era ancora in generazione.

| Input | Obbligatorio | Significato |
|---|---|---|
| audioId | sì | L'id dell'episodio |
| theme | no | `dark`, `light` o `auto`. Predefinito dark. |
| layout | no | `full` o `compact`. Predefinito full. |
| color | no | Colore di accento in esadecimale, per esempio `#5688b0` |
| showTitle, customTitle | no | Mostra una riga del titolo, oppure imposta il tuo |
| showTranscript | no | Mostra il pulsante della trascrizione. Predefinito true. |
| hideAttribution | no | Nasconde la riga «Audio by Hi, Moose». Solo piani a pagamento. |

Chiedi: «Dammi il lettore compatto chiaro per quell'episodio.»

## Cosa non possono fare gli strumenti

Non possono modificare impostazioni o membri del team, cambiare cosa monitora Hi, Moose, avviare esecuzioni di visibilità o eliminare nulla. Per dashboard e automazioni, usa la [Hi, Moose API](../developer-api.md).
