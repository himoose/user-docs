---
source_hash: 90bb543cefb714f7fdb6facb1f7799b751aff22949ece082264e7713b4992995
---
# Choix du modèle

## À quoi cela sert

Chaque chat s'appuie sur un modèle d'IA précis, et le sélecteur de modèle vous permet de voir et de changer celui que vous utilisez, y compris les modèles locaux exécutés sur l'appareil.

## Choisir un modèle

Ouvrez le sélecteur de modèle pour voir les modèles disponibles sur votre [forfait](../getting-started/account-modes.md). Chaque option porte des étiquettes pour que vous sachiez ce que vous obtenez avant de changer :

- **Gratuit** / **HiMoose Cloud** / **Payant ou BYOK** : quels forfaits peuvent utiliser ce modèle.
- **Speed: Slow / Average / Very Fast** : une idée approximative du temps de réponse.
- **Local** : s'exécute entièrement sur votre appareil (voir ci-dessous).
- Une **étiquette multiplicateur** sur les modèles les plus coûteux, indiquant à quel point ils consomment davantage votre solde que l'option standard.

L'offre suit ce que publient les fournisseurs de modèles et comprend actuellement les familles Claude, GPT, Gemini et Gemma. Si un modèle n'est pas disponible sur votre forfait, Hi, Moose vous le dit directement plutôt que de basculer silencieusement sur un autre.

## Modèles locaux

Les modèles locaux approuvés, comme Gemma 4 de Google, s'exécutent **entièrement sur votre ordinateur**. Aucun jeton consommé, aucun aller-retour vers le cloud et aucune donnée ne quitte votre appareil. La première fois que vous sélectionnez un modèle local, Hi, Moose vous guide dans l'installation.

Une fois téléchargées et activées, les réponses locales sont rapides sur Apple Silicon. Sur les Mac à processeur Intel, le modèle s'exécute sur le CPU et sera nettement plus lent que les modèles cloud ; Hi, Moose vous en avertit avant que vous ne lanciez le téléchargement.

Les modèles locaux ne sont pas une option au rabais. Gemma 4 prend en charge l'appel d'outils : les [outils du chat](tools-and-specialists.md) fonctionnent donc sur un modèle local comme sur un modèle cloud.

!!! note "Preview Mode dépend d'un modèle local"
    Sur le forfait gratuit, les [AEO audits](../features/aeo-audits.md) et le scoring de visibilité ne fonctionnent qu'avec un modèle local activé. C'est la principale raison d'en installer un rapidement.

## Modèles plus coûteux

Certains modèles consomment nettement plus de votre solde que l'option standard. Si vous en choisissez un, Hi, Moose vous demande confirmation au préalable et indique approximativement combien de fois plus de jetons il consomme, afin que vous n'épuisiez pas votre solde par accident.

Les modèles les plus chers sont conditionnés au forfait. Si le vôtre ne les inclut pas, ils apparaissent comme indisponibles plutôt que masqués.

## Ancrage par recherche web

Le chat peut fonder ses réponses sur des résultats de recherche web en direct pour la conversation en cours. Cette option est disponible sur BYOK Premium, BYOK Agency et tous les forfaits gérés. Elle n'est pas incluse dans BYOK Free ni dans Preview Mode.

## Langue

Le chat suit une préférence de langue : vous pouvez donc travailler dans une langue différente de celle de l'interface de l'application.

## Lorsqu'un modèle ne peut pas être utilisé

Un message peut s'afficher à la place d'une réponse si :

- le modèle sélectionné est temporairement indisponible (essayez-en un autre),
- le modèle n'est pas autorisé sur votre forfait (choisissez-en un qui y est inclus), ou
- une image a été jointe à un modèle qui ne prend pas en charge les images en entrée. Hi, Moose vous indique un modèle qui le fait et vous propose de basculer.

## Comment cela s'articule avec BYOK

Sur les forfaits BYOK, le choix du modèle détermine quel modèle votre propre clé OpenRouter appelle. L'inférence continue de s'exécuter en local, dans l'application de bureau. Voir [Types de compte et forfaits](../getting-started/account-modes.md) pour savoir comment l'accès aux modèles varie selon les forfaits.

Votre clé OpenRouter est enregistrée par compte et non par appareil. Si vous n'en avez pas encore enregistré, Hi, Moose vous la demande la première fois qu'une fonctionnalité en a besoin, plutôt que d'échouer en silence.
