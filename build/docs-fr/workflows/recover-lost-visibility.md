---
source_hash: 7907c08f25052f66801891d4fc6f24fe3bdcd307070021aede9005fe5995996b
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/workflows/recover-lost-visibility/)

# Récupérer la visibilité perdue

## À quoi cela sert

C'est la recette de workflow pour le **contenu existant** : elle surveille vos résultats de [visibilité](../visibility/overview.md) et, lorsque quelque chose baisse de façon significative, détermine automatiquement si une page existante peut être corrigée ou s'il faut du contenu inédit, puis prépare le travail pour votre relecture.

## Construire le workflow

Le workflow se lit comme une seule phrase, composée de ces choix :

> **Lorsque** [le share of mentions baisse / le share of citations baisse / le share of mentions augmente / le share of citations augmente] **de** [un seuil, de 1 à 99 points] **pour** [tous les thèmes / un thème surveillé précis], Hi, Moose identifie les prompts concernés, puis [prépare une correction de contenu / me prévient].

- **Déclencheur** : quel indicateur surveiller, et si ce sont les baisses ou les hausses qui vous intéressent. Notez que si vous choisissez un déclencheur de hausse, la seule action finale disponible est **me prévenir** : les hausses n'ont pas de voie de correction de contenu, puisqu'il n'y a rien à réparer.
- **Seuil** : combien de points de variation doivent être considérés comme significatifs, afin que le bruit habituel ne déclenche pas le workflow.
- **Portée thématique** : appliquer ce workflow à tout ce que vous surveillez, ou le limiter à un thème précis.
- **Action finale** : **préparer une correction de contenu** (poursuit avec la logique de branchement ci-dessous) ou **me prévenir** (crée simplement un élément dans l'Inbox, sans préparer d'action de contenu).

## Lorsque l'action finale est « préparer une correction de contenu »

Deux choix supplémentaires se ramifient selon qu'une page existante convient ou non :

- **S'il existe des pages correspondantes** : choisissez ce que Hi, Moose doit faire : **lancer une AEO audit**, **générer des FAQ et le schema**, **générer des key points** ou **rien**.
- **S'il n'existe aucune page correspondante** : choisissez entre **créer un brief et un nouveau brouillon** ou **rien**.

Ce branchement est tout l'intérêt de la recette : elle ne recommande pas aveuglément un nouvel article chaque fois que la visibilité baisse. Elle vérifie d'abord si corriger ce que vous avez déjà est la meilleure option, et ne propose du contenu inédit que lorsque rien d'existant ne convient.

## Comment il s'exécute

Ce workflow n'a pas de bouton d'exécution manuelle. Il s'évalue automatiquement chaque fois qu'une exécution de visibilité se termine, en comparant la dernière exécution achevée à la précédente. Lorsqu'il se déclenche, le résultat, y compris les prompts concernés et l'action entreprise, arrive dans votre [Inbox](../inbox/overview.md), relié au changement de visibilité qui l'a provoqué.
