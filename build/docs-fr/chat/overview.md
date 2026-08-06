---
source_hash: 799fa86d4b93065bdbc58d1b0a7cc5400446cfdee289750eafd31c6a0c8371b2
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/chat/overview/)

# Vue d'ensemble du Chat

## À quoi cela sert

Le Chat est l'endroit où vous parlez directement à l'opérateur Hi, Moose, le même agent principal décrit dans toute cette documentation, et non un outil distinct. Il est accessible depuis l'écran **Accueil** et depuis l'écran de chat dédié, et chaque conversation peut mobiliser le [Context](../getting-started/context/overview.md) de votre projet, les fichiers joints et les spécialistes enregistrés pour fonder ses réponses.

## Démarrer une conversation

- Cliquez sur **Nouveau chat** pour partir de zéro, ou poursuivez une conversation existante.
- Le champ de saisie propose des démarrages rapides pour les tâches courantes.
- Choisissez quelque chose de précis dans le **[menu Tools](../tools/overview.md)** de la barre supérieure.
- Ou formulez votre demande en langage courant. Hi, Moose décide s'il répond directement, pose une question de suivi ou lance une fonctionnalité comme les [Content Briefs](../features/content-briefs.md) ou les [AEO Audits](../features/aeo-audits.md) pour vous restituer un artefact durable.

## Comment Hi, Moose décide quoi faire

Il n'y a aucune liste de mots-clés. Moose interprète ce que vous demandez et s'oriente en conséquence : vous pouvez donc formuler les choses comme vous le souhaitez et obtenir le même résultat.

Deux comportements méritent d'être connus :

- **Les demandes explicites lancent l'action.** Demandez un audit et vous obtenez le formulaire d'audit.
- **Les demandes implicites se contentent de la proposer.** Si votre question ne fait que suggérer une fonctionnalité, Moose répond à la question et place la fonctionnalité sur une suggestion en un clic juste en dessous. Il ne détourne pas la conversation.

!!! note "Les questions de suivi restent des questions de suivi"
    Poser une question juste après que Moose a produit un brouillon vous donne une réponse à propos de ce brouillon, pas un nouveau brouillon. Demandez explicitement une réécriture lorsque vous en voulez une.

## Joindre du contexte

Le menu des pièces jointes propose quatre options :

- **Envoyer un fichier ou une image** : `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg` et `.png`. Les feuilles de calcul sont converties en texte lisible plutôt que traitées comme des fichiers opaques.
- **Capturer l'écran** : choisissez un écran ou une fenêtre, puis découpez la zone souhaitée. Sur macOS, cela nécessite l'autorisation d'enregistrement de l'écran, et Hi, Moose vous guide pour l'accorder.
- **Ajouter depuis la Library** : joignez des éléments enregistrés de la [Library](../library/overview.md) comme contexte.
- **Base de données vectorielle du site** : confiez à Moose votre site indexé pour qu'il réponde à partir de vos pages réelles. Voir [Surveillance du site](../site-monitoring/overview.md).

## Ce qui rend une réponse fondée

Pendant que Hi, Moose travaille, il montre ce qu'il fait réellement : récupérer des résultats de recherche en direct, collecter des questions « Autres questions posées », explorer le domaine d'un concurrent, lire une page, indexer des résultats, consulter des données Search Console ou appliquer votre brand voice enregistrée. C'est une trace visible des preuves réelles derrière la réponse, pas un indicateur décoratif.

## Où aller ensuite

- **[Outils et spécialistes du chat](tools-and-specialists.md)** : les outils que Moose peut mobiliser et les spécialistes enregistrés.
- **[Le menu Tools](../tools/overview.md)** : lancer une tâche précise sans avoir à la décrire.
- **[Choix du modèle](model-selection.md)** : choisir le modèle d'IA qui anime votre chat, y compris les options locales et BYOK.
- **[Chats (historique)](chats-history.md)** : retrouver, renommer et rouvrir des conversations passées.
