---
source_hash: 3b2a6720bd62d36c159ec05f39cfb8f6e59efa7a27d7e6054053a2fcb1d2c950
---
# Requêtes fan-out de ChatGPT

## À quoi cela sert

Cette fonctionnalité capture les recherches « fan-out » individuelles que l'étape de recherche web d'OpenAI a effectuées en répondant à votre prompt, ainsi que les sources citées et un aperçu de la réponse.

!!! info "De quoi il s'agit exactement"
    Hi, Moose appelle l'API Responses d'OpenAI avec son outil de recherche web activé, puis relit les recherches effectuées par cette exécution. Ce n'est pas une capture du fan-out propre au produit grand public ChatGPT, qu'OpenAI n'expose pas. Ce que vous obtenez est l'approximation la plus proche disponible : la même couche de recherche web, pilotée par la même famille de modèles, si bien que l'expansion des requêtes suit de près ce que fait ChatGPT Search. Traitez cela comme un signal solide plutôt que comme une transcription, et attendez-vous à une certaine variation entre deux exécutions du même prompt.

!!! note "Disponibilité"
    Cette fonctionnalité lance en arrière-plan une capture gérée de la trace de recherche web d'OpenAI : elle nécessite donc un espace de travail **géré payant**. Cela vaut aussi sur les forfaits BYOK : BYOK garde en local l'exécution principale des modèles, mais la capture du fan-out utilise l'infrastructure gérée de Hi, Moose, dont le fonctionnement nous coûte de l'argent. Elle n'est donc pas incluse dans BYOK Free ni BYOK Premium. Preview Mode ne l'inclut pas non plus.

## Comment la lancer

1. Depuis le [Chat](../chat/overview.md), choisissez le démarrage rapide **Capture ChatGPT fan-out queries** (ou demandez-le directement).
2. Saisissez le prompt que vous souhaitez examiner.
3. Hi, Moose capture la réponse de ChatGPT et renvoie :
    - Les requêtes fan-out distinctes exécutées par ChatGPT.
    - Les sources citées.
    - Un aperçu de la réponse.

Si OpenAI n'a exposé aucune requête fan-out distincte pour une exécution donnée, Hi, Moose vous montre malgré tout la trace de recherche gérée et les sources citées qu'il a pu capturer, plutôt que de présenter un résultat vide ou inventé.

## Pourquoi c'est important

Les requêtes fan-out révèlent l'expansion de requêtes qui sous-tend une réponse ancrée dans le web, ce qui aide à comprendre quelles formulations précises génèrent (ou manquent) des citations vers votre contenu. Cela alimente directement ce que vous surveillez dans [Visibility](../visibility/overview.md) et ce que vous planifiez dans les [Content Briefs](content-briefs.md).
