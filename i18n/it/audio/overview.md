---
source_hash: 3de48b1823942dd1ca44b6be6cf581f170fdffe9e0e850d467f3322e9e89f1a8
---
# Audio

## A cosa serve

Trasformare un articolo in una conversazione a due voci e poi scaricare l'MP3 o incorporare il player nel suo sito. Il player porta con sé una trascrizione, che aggiunge alla pagina testo reale, di prima mano e scansionabile: contenuto che un motore di risposta può recuperare.

Audio si trova nell'app desktop sotto **Audio** nella barra laterale, diviso in tre schede: **Generate**, **History** e **Analytics**.

!!! note "Audio ha lasciato la vecchia app web"
    La generazione audio si trovava un tempo su `app.himoose.com` con il nome «Listen to this Article». Ora fa parte a pieno titolo dell'app desktop, con delimitazione per progetto, statistiche di ascolto e personalizzazione del player che la versione web non aveva.

## Prima di iniziare

Imposti prima il sito del progetto. La riproduzione è limitata al dominio del suo progetto e a `himoose.com`, perciò Hi, Moose deve conoscere il dominio prima di generare qualsiasi cosa. Se non è impostato, la scheda Generate mostra l'invito **Set website** al posto dell'editor.

La disponibilità dell'audio dipende dal suo [piano](../getting-started/account-modes.md): BYOK Premium e BYOK Agency comprendono 15 generazioni al mese, i piani gestiti sono illimitati e i piani gratuiti non comprendono l'audio.

## Scegliere una sorgente

Tre modi per fornire contenuti:

- **URL dell'articolo**: incolli una URL pubblicata e faccia clic su **Fetch**. Hi, Moose estrae il contenuto e mostra dominio, numero di parole e tempo di lettura stimato. L'articolo deve essere accessibile pubblicamente, non protetto da accesso o paywall.
- **Incollare testo**: dia un titolo all'episodio e incolli direttamente il copione o il testo dell'articolo.
- **Caricare un file**: trascini un file `.txt`, `.md`, `.docx`, `.doc` o `.pdf`. Il file viene letto sul suo dispositivo e il suo testo confluisce nel flusso di incollaggio.

## Dare forma alla conversazione

**Focus** (facoltativo) indirizza ciò su cui la conversazione deve approfondire. Ci sono suggerimenti rapidi per le angolazioni più comuni: conclusioni principali, spiegarlo a chi comincia, mettere in discussione la tesi, a chi interessa.

**Length** definisce la durata desiderata:

| Durata | Tempo | Copione approssimativo |
|---|---|---|
| Short | 4-5 min | ~700 parole |
| Standard | 8-10 min | ~1.400 parole |
| Deep dive | 15-18 min | ~2.600 parole |

**Language** segue per impostazione predefinita la lingua dell'articolo. La modifichi per cambiare sia il copione sia le voci.

**Voices** si presentano come coppie di conduttore e ospite, con tre combinazioni predefinite (calda e curiosa, pacata e analitica, brillante e scettica) oppure una coppia personalizzata scelta da lei.

## Regia avanzata

Facoltativa: tutto ciò che lascia vuoto segue l'articolo e la coppia di voci. Sono disponibili sette campi: regia del conduttore, regia dell'ospite, ambientazione, stile, ritmo, accento e contesto aggiuntivo.

- **Ambientazione**: intervista in studio, conversazione informale, tavola rotonda, telefonata, chiacchierata in movimento
- **Stile**: esplicativo, dibattito, narrativo, intervista, informale
- **Ritmo**: più lento, naturale, più rapido
- **Accento**: americano (neutro), britannico, australiano, irlandese, indiano oppure internazionale neutro

Ognuno di questi campi può essere sostituito da una descrizione personalizzata, con parole sue.

**Contesto aggiuntivo** serve per ciò che l'articolo non dice: come pronunciare il nome di un prodotto, quali affermazioni evitare, chi è il pubblico.

!!! warning "Il contesto orienta il tono, non i fatti"
    Hi, Moose non inventa fatti per soddisfare un'indicazione. Il contesto aggiuntivo cambia l'inquadratura e il modo di dire; non aggiunge evidenze assenti nella fonte.

Quando trova impostazioni che la convincono, **Save as project default** le riutilizza per il prossimo episodio di questo progetto.

## Generare

Faccia clic su **Generate audio**. L'editor mostra un tempo di elaborazione stimato prima di partire. La generazione avviene in background, quindi può lasciare la schermata e continuare a lavorare: l'episodio finito compare nell'elenco **Recents** della barra laterale, e un clic lo apre direttamente.

Al termine ottiene:

- Un player con ricerca, salti di 15 secondi avanti e indietro e velocità di riproduzione
- **Download MP3**
- **Share**, per copiare il link dell'audio
- La **trascrizione** completa, con il conteggio dei turni di parola e delle parole, e un pulsante per copiarla
- **Embed on your site**, descritto in [Player e incorporamento](player-and-embed.md)
- **Regenerate with edits** e **Edit settings**, per ritoccare la regia ed eseguire di nuovo

## History

La scheda **History** elenca ogni episodio del progetto corrente con durata, data di creazione e stato. Gli episodi sono delimitati per progetto, quindi cambiare progetto cambia ciò che vede.

- Cerchi episodi per nome
- Filtri per **All**, **Ready** o **Needs attention**
- Riproduca, scarichi, apra le opzioni di incorporamento oppure apra l'episodio completo
- **Riprovi** un episodio fallito

Gli stati sono Ready, Processing, Playing, Failed e Canceled.

## Dove andare da qui

- **[Player e incorporamento](player-and-embed.md)**: tema, disposizione, colore d'accento e codice di incorporamento.
- **[Statistiche di ascolto](analytics.md)**: che cosa succede una volta che il player è su una pagina.
