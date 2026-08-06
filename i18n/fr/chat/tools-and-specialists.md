---
source_hash: 6b12d8d972a33f212f60d823c287d184f083cfb60d8934f6b9ac8571ceb3c32e
---
# Outils et spécialistes du chat

## À quoi cela sert

Au-delà de la simple saisie d'une demande, le champ de saisie du chat vous offre plusieurs façons d'orienter ce que Hi, Moose fait de votre message : joindre du contexte, choisir un spécialiste pour cadrer la conversation, ou lancer un démarrage rapide.

## Pièces jointes

Cliquez sur le bouton de pièce jointe du champ de saisie pour ajouter du contexte à votre message :

- **Envoyer un fichier ou une image** : `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg` et `.png`. Les feuilles de calcul sont converties en texte lisible : vous pouvez donc confier un classeur à Moose et l'interroger sur son contenu.
- **Capturer l'écran** : choisissez un écran ou une fenêtre, puis faites glisser pour découper exactement la zone à envoyer. Sur macOS, vous devrez accorder à Hi, Moose l'accès à l'enregistrement de l'écran lors de la première utilisation.
- **Ajouter depuis la Library** : joignez un artefact enregistré de la [Library](../library/overview.md) (un brief, un brouillon, des key points ou des FAQ) comme contexte, au lieu de le recoller.
- **Base de données vectorielle du site** : joignez le site indexé de votre projet pour que Moose réponde à partir de vos pages réelles et non de ce qu'il suppose s'y trouver. Construisez l'index depuis [Surveillance du site](../site-monitoring/overview.md).

## Outils que Moose peut mobiliser

Le chat ne se limite pas à générer du texte. Au cours d'une conversation, Moose peut mobiliser des outils en votre nom et vous indique quand il le fait.

| Outil | Fonction |
|---|---|
| Recherche web | Résultats en direct, sur les forfaits incluant la recherche web dans le chat |
| Lire une page | Consulter une URL précise |
| Recherche dans l'index du site | Répondre à partir de vos propres pages indexées |
| Search Console | Interroger vos données [Search Console](../integrations/google-search-console.md) connectées |
| Vérification instantanée de marque | Interroger une requête sur cinq moteurs d'IA ; voir [Vérification instantanée de marque](../tools/instant-brand-check.md) |
| Vérification de couverture | Déterminer si votre site couvre déjà un sujet |
| Génération d'images | Produire une image pour un brouillon |
| Aide sur l'application | Vous orienter vers la bonne documentation ou vers le support |

L'usage des outils fonctionne de la même façon sur les forfaits gérés, les forfaits BYOK et les modèles locaux Gemma 4.

!!! note "Les questions sur Search Console reçoivent une réponse agentique"
    Moose interroge vos données Search Console de façon itérative plutôt que d'exécuter un rapport figé. Posez une question vague et il affinera à travers plusieurs requêtes pour y répondre, au lieu de renvoyer un export générique.

## Spécialistes

Les spécialistes sont des points d'entrée ciblés vers le même opérateur principal. Ce ne sont ni des outils ni des mémoires distincts, seulement une façon d'orienter la conversation vers une tâche précise. Ouvrez le sélecteur de spécialiste pour en choisir un :

- **Spécialiste Content Brief** : construire un brief resserré avec structure et prochaines étapes.
- **Spécialiste Google Search Console** : interroger Moose sur vos données [Google Search Console](../integrations/google-search-console.md) connectées. Ce spécialiste a besoin d'un compte Search Console connecté ou d'une propriété enregistrée pour le projet actif avant de pouvoir répondre à partir de vos données propriétaires.
- **Spécialiste Génération audio** : transformer une demande en script parlé propre.
- **Spécialiste Brouillons** : générer du contenu de brouillon prêt à être relu et modifié.
- **Spécialiste FAQ** : rédiger des FAQ concises autour des questions à plus forte valeur.
- **Spécialiste Key Points** : faire ressortir d'abord les enseignements les plus importants.

Lorsqu'un spécialiste est actif, son étiquette apparaît sur la conversation, et vous pouvez la retirer à tout moment pour revenir au chat général.

### Spécialistes personnalisés

Vous pouvez aussi créer votre propre spécialiste local : donnez-lui un nom et un résumé du travail qu'il doit prendre en charge, puis choisissez les parties de votre contexte auxquelles il a accès : contexte de projet, profil de marque, contexte du site web, historique du chat, sortie orientée brouillon ou sortie au format markdown. Les spécialistes personnalisés peuvent également être importés si quelqu'un en partage un avec vous.

## Démarrages rapides

Le champ de saisie propose des démarrages rapides en un clic pour les tâches courantes, notamment :

- [Lancer une AEO audit](../features/aeo-audits.md)
- [Créer un brief de contenu étayé par la recherche](../features/content-briefs.md)
- [Créer des FAQ étayées par la recherche](../features/faq-generator.md)
- [Générer des key points optimisés](../features/key-points.md)
- [Créer un brouillon d'article de blog](../features/blog-post-draft.md)
- [Créer un article de glossaire](../features/glossary-post.md)
- [Créer du contenu de landing page](../features/landing-page-content.md)
- [Créer du contenu de page produit](../features/product-page-content.md)
- [Capturer les requêtes de grounding de Google AI Mode pour un prompt](../features/grounding-queries.md)
- [Capturer les requêtes fan-out de ChatGPT pour un prompt](../features/fan-out-queries.md)
- [Transformer du contenu texte en audio](../audio/overview.md)

Le même ensemble est disponible depuis le **[menu Tools](../tools/overview.md)** de la barre supérieure, regroupé par tâche et consultable par recherche.

Les démarrages rapides de requêtes de grounding et de requêtes fan-out vous montrent les recherches qu'un moteur d'IA connecté au web a effectuées en répondant à un prompt, ainsi que les sources qu'il a citées. Tous deux fonctionnent en lançant un appel géré à Gemini ou à OpenAI, puis en relisant les recherches effectuées par cet appel : ce sont donc des approximations proches de ce que font AI Mode et ChatGPT Search, et non une capture de ces produits eux-mêmes. Comme cet appel s'exécute sur notre infrastructure, tous deux nécessitent un **espace de travail géré payant**, y compris sur les forfaits BYOK, puisque l'étape de capture des requêtes utilise l'infrastructure gérée de Hi, Moose et non votre clé locale.

Le démarrage rapide audio ouvre l'écran [Audio](../audio/overview.md) dans l'application de bureau. Il renvoyait auparavant vers l'ancienne application web ; ce n'est plus le cas.
