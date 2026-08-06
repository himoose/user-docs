---
source_hash: b6472884da7df3e651f78be6893eb9896b38a6327a26378ca1d4cc26b2d0454e
---
# Prompt Manager

## À quoi cela sert

Le Prompt Manager est l'endroit où vous construisez et organisez les requêtes réelles que Hi, Moose soumet aux moteurs d'IA : les prompts que vos clients taperaient ou poseraient de façon réaliste.

## Organiser les prompts par catégories

Les prompts sont regroupés en catégories affichées dans la liste de filtres de gauche : **Tous les prompts**, **Sans catégorie** et les catégories personnalisées que vous créez (par thème ou par campagne, par exemple). Ajoutez une nouvelle catégorie depuis le champ situé en bas de la liste. Les espaces de travail du forfait gratuit sont limités à 5 catégories.

## Ajouter et modifier un prompt

Saisissez un nouveau prompt et ajoutez-le à une catégorie. Pour chaque prompt, vous pouvez :

- Modifier le texte du prompt.
- Choisir les moteurs ou modèles d'IA sur lesquels il s'exécute. **Sélectionner des modèles** ouvre un sélecteur couvrant ChatGPT, Claude, Gemini, Grok, Perplexity, Google AI Mode, Google AI Overview et Bing Copilot (la disponibilité dépend de votre forfait et, pour les moteurs en interrogation locale, du fait que l'application de bureau soit en cours d'exécution).
- Supprimer le prompt.

Contrairement à un réglage unique valable pour tout le compte, **la sélection des modèles se fait prompt par prompt** : un prompt peut ne s'exécuter que sur ChatGPT et Gemini pendant qu'un autre s'exécute sur tous les moteurs pris en charge. Vous ne dépensez ainsi votre allocation que sur les moteurs qui comptent pour cette requête précise.

## Diagnostic Prompts

**Prompts de diagnostic** est une catégorie réservée, gérée par le système, alimentée par votre [Brand Truth Profile](../getting-started/context/brand-truth-profile.md). Plutôt que de les rédiger à la main :

1. Cliquez sur **Générer à partir de Brand Truth** (ou configurez d'abord votre Brand Truth Profile si ce n'est pas déjà fait).
2. Hi, Moose propose des prompts spécialement conçus pour repérer quand l'IA décrit mal vos clients, vos capacités ou vos concurrents.
3. Passez les suggestions en revue dans une fenêtre : activez ou désactivez chaque prompt, modifiez la formulation ou supprimez-en un entièrement avant de les ajouter à la surveillance.
4. La fenêtre affiche un coût estimé avant validation : prompts × modèles × exécutions par semaine ≈ total d'exécutions hebdomadaires.

Si votre Brand Truth Profile ne contient pas encore assez d'éléments pour générer des prompts de diagnostic pertinents, Hi, Moose vous le dit au lieu de produire du remplissage générique : ajoutez d'abord des questions de clients, des capacités clés ou des concurrents à votre profil.

## Stockage local des prompts

Sur les forfaits BYOK, qui fonctionnent uniquement en local, les catégories de prompts, les définitions de prompts et les sélections de modèles sont enregistrées sur votre appareil plutôt que synchronisées avec le cloud.
