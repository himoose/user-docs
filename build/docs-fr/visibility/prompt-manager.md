---
source_hash: 52e4fc142ac45ba9ec93251b7b681cb95c1e09d409fef443f88b56ac8cbebaa7
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/visibility/prompt-manager/)

# Prompt Manager

## À quoi cela sert

Le Prompt Manager est l'endroit où vous construisez et organisez les requêtes réelles que Hi, Moose soumet aux moteurs d'IA : les prompts que vos clients taperaient ou poseraient de façon réaliste.

## Organiser les prompts par catégories

Les prompts sont regroupés en catégories affichées dans la liste de filtres de gauche : **Tous les prompts**, **Sans catégorie** et les catégories personnalisées que vous créez (par thème ou par campagne, par exemple). Ajoutez une nouvelle catégorie depuis le champ situé en bas de la liste. Les espaces de travail du forfait gratuit sont limités à 5 catégories.

## Ajouter et modifier un prompt

Saisissez un nouveau prompt et ajoutez-le à une catégorie. Pour chaque prompt, vous pouvez :

- Modifier le texte du prompt.
- Choisir les moteurs d'IA sur lesquels il s'exécute. **Sélectionner des modèles** ouvre un sélecteur avec tous les moteurs que votre forfait peut suivre, versions API et interrogation locale comprises (voir [les moteurs que vous pouvez suivre](settings.md#les-moteurs-que-vous-pouvez-suivre)). Les moteurs en interrogation locale ont besoin que l'application de bureau soit ouverte au moment de l'exécution.
- Retirer le prompt (voir plus bas).
- Supprimer le prompt.

Contrairement à un réglage unique valable pour tout le compte, **la sélection des modèles se fait prompt par prompt** : un prompt peut ne s'exécuter que sur ChatGPT et Gemini pendant qu'un autre s'exécute sur tous les moteurs pris en charge. Vous ne dépensez ainsi votre allocation que sur les moteurs qui comptent pour cette requête précise.

## Rechercher et sélectionner plusieurs prompts

**Rechercher des prompts** filtre la liste par texte. Cochez plusieurs prompts et la barre d'outils propose **Attribuer des catégories**, **Attribuer des modèles**, **Retirer la sélection** et **Supprimer la sélection**, de sorte qu'un changement sur de nombreux prompts s'enregistre en une seule étape au lieu d'un prompt à la fois. Vous ne pouvez supprimer que les prompts que vous avez créés, sauf si vous êtes propriétaire de l'équipe.

## Retirer un prompt

Retirez un prompt quand il est devenu obsolète mais que son historique mérite d'être conservé, par exemple un prompt qui nomme l'année dernière. Un prompt retiré :

- conserve tous ses résultats passés, donc les tendances et les rapports les incluent toujours ;
- est exclu des nouvelles exécutions, donc il ne coûte rien ;
- est exclu de la liste des [Opportunités](overview.md#opportunites).

Les prompts retirés se trouvent dans la section **Prompts retirés** de la liste de filtres, chacun avec la date de son retrait, et **Restaurer** le remet dans le suivi. Ajouter un nouveau prompt avec le même texte qu'un prompt retiré ne fait rien ; restaurez-le à la place. **Supprimer** retire aussi un prompt du suivi futur et conserve les données d'exécution historiques pour les rapports, mais sans possibilité de restauration.

## Diagnostic Prompts

**Prompts de diagnostic** est une catégorie réservée, gérée par le système, alimentée par votre [Brand Truth Profile](../getting-started/context/brand-truth-profile.md). Plutôt que de les rédiger à la main :

1. Cliquez sur **Générer à partir de Brand Truth** (ou configurez d'abord votre Brand Truth Profile si ce n'est pas déjà fait).
2. Hi, Moose propose des prompts spécialement conçus pour repérer quand l'IA décrit mal vos clients, vos capacités ou vos concurrents.
3. Passez les suggestions en revue dans une fenêtre : activez ou désactivez chaque prompt, modifiez la formulation ou supprimez-en un entièrement avant de les ajouter à la surveillance.
4. La fenêtre affiche un coût estimé avant validation : prompts × modèles × exécutions par semaine ≈ total d'exécutions hebdomadaires.

Si votre Brand Truth Profile ne contient pas encore assez d'éléments pour générer des prompts de diagnostic pertinents, Hi, Moose vous le dit au lieu de produire du remplissage générique : ajoutez d'abord des questions de clients, des capacités clés ou des concurrents à votre profil.

## Stockage local des prompts

Sur les forfaits BYOK, qui fonctionnent uniquement en local, les catégories de prompts, les définitions de prompts et les sélections de modèles sont enregistrées sur votre appareil plutôt que synchronisées avec le cloud.
