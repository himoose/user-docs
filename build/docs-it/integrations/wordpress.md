---
source_hash: 57477f3edd7e63b53a23c12a7676c0c723e2f37903e1f4aa75a613f296e8277b
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](https://himoose.com/docs/integrations/wordpress/)

# WordPress

## A cosa serve

Collegare un sito WordPress a Hi, Moose perché l'app desktop possa preparare e applicare direttamente modifiche ai contenuti (FAQ, key points, bozze basate su brief e raccomandazioni degli AEO audits), con un passaggio di anteprima e uno di approvazione prima che qualcosa vada in produzione.

## Come funziona la connessione

L'app desktop è il lato attivo di questa connessione: individua l'articolo di destinazione, ne recupera il contenuto attuale, costruisce in locale la modifica proposta e chiama direttamente in HTTPS gli endpoint REST del suo sito WordPress per prepararla. Il suo sito WordPress resta passivo: espone un endpoint che attende di essere chiamato e non deve mai contattare Hi, Moose di propria iniziativa.

Questo significa che:

- Il token del suo sito e le credenziali di connessione non sono mai in mano all'interfaccia utente, ma soltanto al processo in background dell'app desktop.
- Nei piani BYOK i passaggi con modello locale che intervengono nella preparazione di una modifica (come individuare la sezione esatta di contenuto da sostituire) girano con la sua chiave OpenRouter e non tramite una chiamata ospitata da Hi, Moose.

## Configurare una connessione

1. Apra **Connections** nell'app desktop e scelga WordPress.
2. Scarichi il plugin connettore, lo installi nell'amministrazione di WordPress e incolli poi la URL del suo sito e la chiave API di questo progetto nelle impostazioni del plugin.
3. Tornato in Hi, Moose, salvi la connessione e verifichi che il connettore segnali un ping riuscito dal suo sito.

## Ambienti

Ogni installazione WordPress che collega (produzione, staging o entrambe) è un **ambiente** a sé, con il proprio token del sito e il proprio segreto HMAC, del tutto isolati l'uno dall'altro. Scelga quale ambiente è la destinazione predefinita delle nuove modifiche e passi dall'uno all'altro quando vuole. Se un sito di staging è protetto da autenticazione HTTP Basic, può salvare quelle credenziali specificamente per quell'ambiente, così Hi, Moose può raggiungerlo.

## Patch

Ogni modifica a WordPress, che provenga dalle [FAQ](../features/faq-generator.md), dai [key points](../features/key-points.md), da una [bozza](../features/drafts-and-publishing.md) o da una sostituzione manuale di testo creata da lei, viene tracciata come **patch**: una voce di registro locale, propria di ciascun ambiente, con un proprio stato.

Una patch attraversa stati espliciti: **Draft**, **Staged**, **Applied**, **Discarded**, **Rolled back** o **Failed**. Dall'elenco delle patch può:

- **Preparare** una patch sul suo sito WordPress per l'anteprima.
- **Applicare** una patch preparata per mandarla in produzione.
- **Scartare** una patch che non intende usare.
- **Annullare** una patch applicata.
- **Promuovere** una patch verso un altro ambiente (per esempio da staging a produzione) per riprepararla lì e rivederla.

Una volta inviata una bozza, Hi, Moose se ne ricorda, così non può inviare la stessa più volte per errore.

## Plugin Listen to this Article

Il plugin WordPress **Listen to This Article**, che è separato, incorpora il player audio e la trascrizione generati da [Audio](../audio/overview.md) nell'app desktop. Lo installi da [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/), oppure incolli il codice di incorporamento direttamente nel suo articolo. Veda [Player e incorporamento](../audio/player-and-embed.md).

## Requisiti

- WordPress 6.0 o superiore, con accesso da amministratore per installare la connessione sul suo sito.
- Un progetto configurato nell'app desktop.
