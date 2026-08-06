---
source_hash: 3de48b1823942dd1ca44b6be6cf581f170fdffe9e0e850d467f3322e9e89f1a8
---
# Audio

## À quoi cela sert

Transformer un article en conversation à deux voix, puis télécharger le MP3 ou intégrer le lecteur sur votre site. Le lecteur est livré avec une transcription, ce qui ajoute à la page un texte réel, propriétaire et explorable : du contenu qu'un moteur de réponse peut récupérer.

Audio se trouve dans l'application de bureau, sous **Audio** dans la barre latérale, et se divise en trois onglets : **Générer**, **Historique** et **Analyses**.

!!! note "Audio a quitté l'ancienne application web"
    La génération audio se trouvait auparavant sur `app.himoose.com` sous le nom « Listen to this Article ». Elle fait désormais pleinement partie de l'application de bureau, avec une délimitation par projet, des statistiques d'écoute et une personnalisation du lecteur que la version web n'avait pas.

## Avant de commencer

Renseignez d'abord le site web du projet. La lecture est restreinte au domaine de votre projet et à `himoose.com` : Hi, Moose doit donc connaître le domaine avant de générer quoi que ce soit. S'il n'est pas défini, l'onglet Generate affiche une invitation **Définir le site web** à la place du composeur.

La disponibilité de l'audio dépend de votre [forfait](../getting-started/account-modes.md) : BYOK Premium et BYOK Agency incluent 15 générations par mois, les forfaits gérés sont illimités et les forfaits gratuits n'incluent pas l'audio.

## Choisir une source

Trois façons d'apporter du contenu :

- **URL d'article** : collez une URL publiée et cliquez sur **Récupérer**. Hi, Moose extrait le contenu et affiche le domaine, le nombre de mots et le temps de lecture estimé. L'article doit être accessible publiquement, et non protégé par une connexion ou un paywall.
- **Coller du texte** : donnez un titre à l'épisode et collez directement le script ou le texte de l'article.
- **Envoyer un fichier** : déposez un `.txt`, `.md`, `.docx`, `.doc` ou `.pdf`. Le fichier est lu sur votre appareil et son texte alimente le flux de collage.

## Façonner la conversation

**Angle** (facultatif) oriente ce que la conversation doit approfondir. Des suggestions rapides couvrent les angles courants : enseignements clés, expliquer à un débutant, contester l'argument, à qui cela s'adresse.

**Durée** définit la durée visée :

| Durée | Temps | Script approximatif |
|---|---|---|
| Short | 4-5 min | ~700 mots |
| Standard | 8-10 min | ~1 400 mots |
| Deep dive | 15-18 min | ~2 600 mots |

**Langue** correspond par défaut à la langue de l'article. Modifiez-le pour changer à la fois le script et les voix.

**Voix** se présentent sous forme de duos animateur/invité, avec trois combinaisons prédéfinies (chaleureuse et curieuse, posée et analytique, vive et sceptique) ou un duo personnalisé de votre choix.

## Direction avancée

Facultative : tout ce que vous laissez vide suit l'article et le duo de voix. Sept champs sont disponibles : direction de l'animateur, direction de l'invité, décor, style, rythme, accent et contexte supplémentaire.

- **Décor** : entretien en studio, discussion au coin du feu, table ronde, appel téléphonique, conversation en marchant
- **Style** : explicatif, débat, narratif, entretien, décontracté
- **Rythme** : plus lent, naturel, plus rapide
- **Accent** : américain (neutre), britannique, australien, irlandais, indien ou international neutre

Chacun de ces champs peut être remplacé par une description personnalisée, avec vos propres mots.

**Contexte supplémentaire** sert à ce que l'article ne dit pas : la prononciation d'un nom de produit, les affirmations à éviter, l'identité du public.

!!! warning "Le contexte oriente le ton, pas les faits"
    Hi, Moose n'invente pas de faits pour satisfaire une consigne. Le contexte supplémentaire modifie le cadrage et la manière de dire ; il n'ajoute pas de preuves absentes de la source.

Lorsque vous obtenez des réglages qui vous conviennent, **Enregistrer comme valeur par défaut du projet** les réutilise pour le prochain épisode de ce projet.

## Générer

Cliquez sur **Générer l'audio**. Le composeur affiche un temps de rendu estimé avant de commencer. La génération s'exécute en arrière-plan : vous pouvez quitter l'écran et continuer à travailler. L'épisode terminé apparaît dans la liste **Récents** de la barre latérale, et un clic l'ouvre directement.

Une fois terminé, vous obtenez :

- Un lecteur avec navigation, sauts de 15 secondes en arrière et en avant, et vitesse de lecture
- **Télécharger le MP3**
- **Partager** pour copier le lien audio
- La **transcription** complète, avec le nombre de tours de parole et de mots, et un bouton de copie
- **Intégrer sur votre site**, détaillé dans [Lecteur et intégration](player-and-embed.md)
- **Régénérer avec des modifications** et **Modifier les réglages**, pour ajuster la direction et relancer

## History

L'onglet **Historique** répertorie tous les épisodes du projet en cours avec leur durée, leur date de création et leur statut. Les épisodes sont délimités par projet : changer de projet change donc ce que vous voyez.

- Recherchez des épisodes par nom
- Filtrez par **All**, **Prêt** ou **Nécessite votre attention**
- Lisez, téléchargez, ouvrez les options d'intégration ou ouvrez l'épisode complet
- **Relancez** un épisode en échec

Les statuts sont Ready, Processing, Playing, Failed et Canceled.

## Où aller ensuite

- **[Lecteur et intégration](player-and-embed.md)** : thème, disposition, couleur d'accent et code d'intégration.
- **[Statistiques d'écoute](analytics.md)** : ce qui se passe une fois le lecteur en place sur une page.
