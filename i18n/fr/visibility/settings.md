---
source_hash: 185a9611ccdaef3c98b73cc4349bc1d586a1fa03b38212ecab7ffca94af54a21
---
# Paramètres de Visibility

## À quoi cela sert

Les paramètres de Visibility déterminent à quelle fréquence Hi, Moose vérifie la visibilité, quel modèle note les résultats et quels termes de marque et domaines comptent dans vos indicateurs. Les prompts et les thèmes se gèrent dans le [Prompt Manager](prompt-manager.md) ; cet écran concerne la mécanique des exécutions.

## Planification des exécutions

- **Fréquence** : quotidienne, jours ouvrés, hebdomadaire ou manuelle uniquement.
- **Heure d'exécution préférée** et, pour la cadence hebdomadaire, un **jour de la semaine**. Les exécutions ont lieu dans votre fuseau horaire local.
- **Échantillons par prompt** : les exécutions planifiées peuvent répéter chaque prompt plusieurs fois et moyenner les résultats pour obtenir un taux de visibilité plus stable. Le bouton manuel **Exécuter maintenant** utilise toujours un seul échantillon. Augmenter cette valeur multiplie la consommation de jetons d'autant, et Hi, Moose vous avertit avant d'enregistrer une valeur plus élevée.

!!! note "Les exécutions planifiées nécessitent que cet appareil soit allumé"
    Sur **Preview Mode** et les forfaits **BYOK**, la planification s'exécute en local sur votre machine : une exécution planifiée ne peut pas démarrer si l'ordinateur est éteint ou en veille, ou si Hi, Moose est complètement fermé. Gardez l'application ouverte (ou réduite dans la barre d'état système) pour que les exécutions planifiées puissent avoir lieu. Les **forfaits gérés** débloquent un planificateur cloud toujours actif, qui ne dépend pas de l'état de votre appareil. Les moteurs en interrogation locale exigent toujours que l'application soit ouverte, quel que soit le forfait, puisque ces vérifications partent de votre machine.

## Notifications par e-mail

Activez **Rapports de visibilité planifiés par e-mail** pour recevoir le rapport de visibilité par e-mail une fois les exécutions planifiées terminées. Il s'agit d'une préférence de notification personnelle, distincte des [réglages de notification de l'Inbox](../inbox/notifications.md).

## Termes et domaines de marque secondaires

- **Termes de marque secondaires** : formulations alternatives ou variantes orthographiques de votre marque qui doivent également compter comme une mention.
- **Domaines secondaires** : autres domaines devant compter comme des citations valables de votre marque pour ce projet, en plus de votre domaine principal.

## Suivi des concurrents

Ajoutez les marques auxquelles ce projet est comparé. Chaque concurrent demande un nom et, éventuellement, un site web.

Lorsqu'une réponse d'IA en mentionne ou en cite un, cela alimente le [Share of Voice, les citations de concurrents et les écarts](competitors.md).

Cette liste est partagée avec votre [Brand Truth Profile](../getting-started/context/brand-truth-profile.md) : les concurrents ajoutés à l'un ou l'autre endroit apparaissent dans les deux. Le nombre de concurrents suivis dans les exécutions de visibilité est plafonné : l'écran indique ce nombre et vous avertit si votre liste le dépasse, afin que vous sachiez que seuls les premiers sont suivis.

## Modèle de scoring

Choisissez le modèle utilisé par Hi, Moose pour noter le sentiment, l'écart narratif et la parité fonctionnelle une fois une réponse capturée :

- La **valeur automatique** s'adapte à votre forfait :
    - **Preview Mode** utilise un modèle local Gemma 4 activé. Le scoring est ignoré tant qu'aucun modèle n'est installé et actif (Paramètres → Local Model).
    - **Les forfaits BYOK** notent avec votre propre clé OpenRouter.
    - **Les forfaits gérés** notent via le routage de modèles gérés de Hi, Moose (le scoring par modèle local s'applique toujours là où il est pris en charge).
- Vous pouvez aussi sélectionner un modèle précis plutôt que l'option automatique.

Les modèles gratuits d'OpenRouter ne sont plus proposés comme option de scoring. Ils se sont révélés assez peu fiables sur le scoring structuré pour que les résultats ne méritent pas d'être communiqués.

## Modèles par défaut pour les nouveaux prompts

Choisissez quels moteurs sont présélectionnés chaque fois que vous ajoutez un prompt dans le [Prompt Manager](prompt-manager.md) ; vous pourrez ensuite modifier la sélection prompt par prompt. Les modèles marqués **Payant** nécessitent un forfait payant ou BYOK ; Preview Mode est limité aux modèles en interrogation locale. Chaque modèle coché ici compte dans la consommation de jetons lors des exécutions de visibilité.

## Refaire le parcours d'accueil

Relancez à tout moment l'assistant d'accueil de la visibilité pour mettre à jour de zéro votre domaine surveillé, vos prompts et vos préférences de suivi.
