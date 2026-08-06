---
source_hash: 9cb1f82df3ab1a21aa5b240256af6954d672dc3d11dd311e044918cd3a30f531
---
# Vérification instantanée de marque dans la recherche par IA

## À quoi cela sert

Tester une requête sur cinq moteurs de recherche par IA immédiatement et voir si votre marque apparaît, sans configurer de prompt surveillé ni attendre une exécution planifiée.

C'est l'outil du moment « je viens de penser à une question, comment est-ce que j'y apparais ? ».

## Comment en lancer une

Demandez-le à Moose dans le [chat](../chat/overview.md), en langage courant. Quelque chose comme « vérifie comment on apparaît sur logiciel de gestion de projet pour agences » suffit.

Moose propose la requête exacte et affiche une fiche de confirmation. **La vérification n'est pas encore lancée.** Vous pouvez modifier la requête sur la fiche et la lancer vous-même : une demande mal interprétée ne vous coûte donc rien.

## Ce qui est vérifié

Cinq moteurs : **ChatGPT**, **Perplexity**, **Grok**, **Google AI Mode** et **Google Search**.

La vérification interroge directement les surfaces publiques depuis votre appareil : elle ne consomme donc ni votre solde de crédits gérés ni votre clé OpenRouter.

## Lire le résultat

Le titre indique combien de moteurs ont mentionné votre marque et combien ont cité votre propre site.

Chaque moteur reçoit un verdict :

| Résultat | Signification |
|---|---|
| **Recommended** | Votre marque a été avancée comme réponse |
| **Listed among others** | Vous apparaissez, aux côtés d'alternatives |
| **Described neutrally** | Mentionnée sans recommandation ni réserve |
| **Described negatively** | Mentionnée de façon défavorable |
| **Not in the answer** | Le moteur ne vous a pas mentionné |

Vous verrez également si chaque moteur a **cité votre site** en particulier, et combien de sources il a citées au total. Être mentionné et être cité sont deux victoires différentes : être nommé dans le texte n'équivaut pas à être la source sur laquelle la réponse a été construite.

Les requêtes sont étiquetées **de marque** ou **sans marque**. Les requêtes sans marque constituent le test le plus difficile et le plus précieux, car le moteur n'avait aucune incitation à vous mentionner.

## Transformer une vérification en suivi

La fiche de résultat comporte une action **Add to tracked prompts**. Elle promeut la requête dans votre [Prompt Manager](../visibility/prompt-manager.md), qui l'exécutera dès lors selon votre planification.

!!! note "Une vérification est un instantané, pas une tendance"
    Une vérification instantanée vous dit où vous en êtes à cet instant. Les réponses d'IA varient d'une exécution à l'autre : un résultat isolé ne doit donc pas être lu comme un changement. Les prompts surveillés s'exécutent selon une planification et construisent la courbe de tendance qui, elle, indique réellement si quelque chose a bougé. Servez-vous des vérifications instantanées pour repérer les questions qui méritent d'être suivies, puis suivez-les.

## Où aller ensuite

- **[Visibility](../visibility/overview.md)** : la version planifiée de tout cela, avec tendances et historique.
- **[Prompt Manager](../visibility/prompt-manager.md)** : organiser les prompts que vous avez promus.
- **[AEO Audits](../features/aeo-audits.md)** : quand une vérification se passe mal et que vous voulez savoir pourquoi.
