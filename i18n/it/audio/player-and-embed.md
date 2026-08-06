---
source_hash: b5d0a07f31228ccaaa2c18a76dddb8de404f3871f7b879591e111c89bae3e9c5
---
# Player e incorporamento

## A cosa serve

Adattare l'aspetto del player audio incorporato alla pagina che lo ospiterà e poi copiare il codice di incorporamento. Lo apra da un episodio completato con **Personalizza il player**, oppure dall'azione di incorporamento nella scheda **Cronologia**.

## Opzioni del player

- **Tema**: Dark, Light o Auto. Auto segue l'impostazione del dispositivo di ciascun visitatore.
- **Disposizione**: Full o Compact.
- **Colore d'accento**: un qualsiasi valore esadecimale a 6 cifre, per esempio `#5688b0`.
- **Mostrare il titolo**: lo disattivi quando l'incorporamento sta sotto un suo titolo.
- **Titolo personalizzato**: lo lasci vuoto per usare il titolo dell'episodio.
- **Pulsante della trascrizione**: mostri o nasconda il comando della trascrizione nel player.

Un'anteprima dal vivo si aggiorna mentre modifica le impostazioni. Se lo script del player non è raggiungibile durante l'anteprima, questa ripiega su un markup semplice; il codice di incorporamento copiato resta comunque corretto.

## Copiare il codice di incorporamento

Faccia clic su **Copia il codice di incorporamento** e lo incolli nella sua pagina.

- **WordPress**: lo incolli nel blocco HTML o di codice dell'articolo, oppure usi il [plugin Listen to This Article](https://wordpress.org/plugins/listen-to-this-article/).
- **Webflow**: lo incolli in un elemento Embed.
- **Grav**: lo incolli nel contenuto della pagina, dove è consentito l'HTML grezzo.

## La riproduzione è vincolata al dominio

L'audio generato viene riprodotto soltanto sul dominio del sito del suo progetto e su `himoose.com`. Il vincolo deriva dal campo del sito del progetto, ed è il motivo per cui quel campo deve essere compilato prima di poter generare. Se incorpora il player su un dominio non autorizzato, la riproduzione verrà rifiutata.

## Attribuzione dell'agenzia

Nei piani con [personalizzazione white label](../agency/white-label.md), il player incorporato può riportare l'attribuzione della sua agenzia anziché quella di Hi, Moose. La imposti in **Impostazioni → Brand**:

- **Attribuzione dell'incorporamento audio**: il testo mostrato sul player. Lo lasci vuoto per usare «Audio by» seguito dal nome della sua agenzia.
- **Link di attribuzione**: un indirizzo `https://` completo. Lo lasci vuoto per riutilizzare il suo link di marca principale.

L'attribuzione è un vero link verso il suo sito da ogni pagina cliente che ospita il player, ed è precisamente ciò che la rende preziosa per le agenzie.

!!! warning "L'attribuzione vale per il codice copiato dopo il salvataggio"
    Modificare il branding non riscrive gli incorporamenti già collocati. Ricopi il codice di incorporamento dopo il salvataggio per recepire la nuova attribuzione.

## Perché aiuta l'AEO

La trascrizione aggiunge alla pagina testo strutturato, di prima mano e scansionabile. È contenuto reale in più che un motore di risposta può recuperare e citare, e può rafforzare i segnali di estraibilità e completezza in un [AEO audit](../features/aeo-audits.md). Non è di per sé un criterio valutato del tipo «ha contenuti multimediali»: il valore sta nel testo che il player porta con sé.
