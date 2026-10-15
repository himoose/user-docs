---
source_hash: 3856622231055de776fe82082345666ad4d8429b9d735111e9d399831a122f47
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/features/grounding-queries/)

# Requêtes de grounding d'AI Mode

## À quoi cela sert

Cette fonctionnalité vous montre les recherches Google que Gemini a effectuées en fondant sa réponse à un prompt, ainsi que les sources citées et la réponse ancrée qu'il a rédigée.

!!! info "De quoi il s'agit exactement"
    Hi, Moose demande à l'API Gemini de répondre à votre prompt avec l'ancrage par recherche Google activé, puis relit la liste des recherches émises par ce modèle. Ce n'est pas un enregistrement de l'AI Mode grand public de Google. AI Mode est une surface distincte, qui n'expose ses requêtes internes à personne. Ce que vous obtenez est l'approximation la plus proche disponible : le même index de recherche, la même famille de modèles et des formulations de requêtes très proches de celles que produit AI Mode. Traitez cela comme un signal solide plutôt que comme une transcription, et attendez-vous à une certaine variation entre deux exécutions du même prompt.

!!! note "Disponibilité"
    Cette fonctionnalité lance en arrière-plan un appel d'ancrage géré à Gemini : elle nécessite donc un espace de travail **géré payant**. Cela vaut aussi sur les forfaits BYOK : BYOK garde en local la génération principale du chat, mais la capture des requêtes de grounding utilise l'infrastructure gérée de Hi, Moose, dont le fonctionnement nous coûte de l'argent. Elle n'est donc pas incluse dans BYOK Free ni BYOK Premium. Preview Mode ne l'inclut pas non plus.

## Comment la lancer

1. Depuis le [Chat](../chat/overview.md), choisissez le démarrage rapide **Capturer les requêtes de grounding AI Mode** (ou demandez-le directement).
2. Saisissez le prompt que vous souhaitez examiner.
3. Hi, Moose vérifie les requêtes de grounding de Gemini pour ce prompt et renvoie :
    - Les requêtes de grounding réellement utilisées par Gemini.
    - Les sources citées.
    - La réponse ancrée elle-même.

## Pourquoi c'est important

Les requêtes de grounding montrent comment un moteur de réponse transforme un seul prompt en un éventail de recherches réelles. C'est utile pour comprendre pourquoi votre page est reprise ou non, et pour repérer des variantes de requêtes que vous ne surveillez pas actuellement dans [Visibility](../visibility/overview.md) ou dans le [Prompt Manager](../visibility/prompt-manager.md).

## Si une exécution échoue

Si Hi, Moose ne parvient pas à collecter de véritables requêtes de grounding pour un prompt, il vous le dit plutôt que de présenter une supposition. Réessayez dans un instant, ou vérifiez que l'espace de travail dispose bien d'un abonnement géré actif.
