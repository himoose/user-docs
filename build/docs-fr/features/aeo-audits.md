---
source_hash: a8e831ea98a893f4158e5124991eae0686f8eb64e2448fe9541f8444c4680099
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/features/aeo-audits/)

# AEO Audits

## À quoi cela sert

Une AEO audit (audit d'optimisation pour les moteurs de réponse) évalue la capacité d'une page à être comprise, récupérée et citée par des systèmes d'IA comme ChatGPT, Google AI Overviews, Perplexity et Gemini, puis vous remet un plan d'action hiérarchisé et étayé par des preuves pour l'améliorer.

Cela remplace les « conseils AEO » ponctuels par un artefact durable et comparable : chaque audit produit une fiche de score et un plan d'action que vous pouvez reconsulter, et les audits ultérieurs sur la même page permettent de vérifier si vos modifications ont réellement fait bouger le score.

## Ce qui est évalué

Le score global est une composition pondérée de huit catégories, chacune notée de 0 à 100 :

1. **Fraîcheur** : signaux d'actualité et de mise à jour.
2. **Structure** : titres, listes, tableaux et découpage en paragraphes qu'un moteur de réponse peut analyser.
3. **Semantic Clarity** : à quel point le contenu correspond étroitement à votre requête cible et à son intention.
4. **Extractibilité** : avec quelle facilité un moteur de réponse peut extraire une définition, un fait ou un point clé.
5. **Citation Potential** : signaux d'attribution et de sourcing, fondés sur les liens de référence externes de la page.
6. **Exhaustivité** : couverture des sous-sujets que les personnes et les moteurs de réponse attendent pour cette requête.
7. **Trust Signals** : cohérence, précision et nuance des affirmations dans la façon dont la page présente son attribution et ses sources. Cette catégorie ne vérifie pas les affirmations auprès de sources externes : elle mesure à quel point les affirmations de la page elle-même sont bien attribuées et précises.
8. **Answer Readiness** : placement d'une réponse directe près du début, une idée par bloc, langage référentiel clair (en évitant les « ceci / cela / ils » vagues) et dénomination cohérente des entités. Le scoring tient compte de la langue en anglais, allemand, espagnol, français, italien et portugais.

L'audit suit également des signaux d'Engagement, d'Entity Recognition et de Media Enrichment, même s'ils n'entrent pas dans le score global et n'apparaissent pas sur la fiche de score.

## Vérifications d'infrastructure et de récupération

En parallèle du scoring de contenu, chaque audit vérifie si un moteur de réponse peut ne serait-ce que récupérer la page :

- **Accès des robots d'IA** : vérifie les règles du robots.txt pour chacun des jetons de robots d'IA propres à OpenAI, Anthropic, Perplexity, Google et Bing (en traitant séparément leurs robots d'entraînement, d'indexation et de consultation en direct, puisqu'un site peut bloquer l'un et autoriser l'autre). Un robot de récupération ou d'indexation bloqué est signalé comme critique ; un agent de consultation en direct bloqué est de priorité moyenne ; un blocage limité à l'entraînement est noté comme un choix de politique légitime et neutre, sans effet sur les citations.
- **Rendu côté serveur et détection de coquille rendue côté client** : la plupart des robots d'IA n'exécutent pas JavaScript. Si le contenu essentiel d'une page n'apparaît qu'après un rendu côté client, cela est signalé comme un constat critique et majeur, et non comme une note technique mineure, car c'est un problème de récupération qui précède toute optimisation de contenu.
- **Hygiène de récupération** : vérifie un échantillon de liens internes à la recherche de liens brisés et de chaînes de redirections.
- **Présence dans l'index Bing** : vérifie si la page semble indexée par Bing, puisque Microsoft Copilot et une partie de la recherche ChatGPT s'appuient sur l'index de Bing. Les verdicts sont délibérément prudents : un résultat non concluant est signalé comme tel plutôt que deviné, et le verdict « non référencée » n'est affiché que lorsque la vérification dispose d'un signal réel pour l'étayer.

## Contexte externe et de couverture

- **Panorama des citations** : lorsqu'une recherche en direct est effectuée, l'audit indique quels domaines un moteur de réponse a réellement cités pour la requête cible, si le site audité en fait partie, et si des sources tierces (sites communautaires, sites d'avis, Wikipédia, YouTube) dominent la réponse. C'est communiqué comme un contexte que vous ne pouvez pas vraiment corriger en modifiant votre propre page, plutôt qu'intégré au score.
- **Votre propre historique de visibilité** : si l'URL auditée a été citée dans vos [exécutions de visibilité](../visibility/overview.md) récentes, l'audit l'intègre, afin que les recommandations tiennent compte de la façon dont la page se comporte déjà dans les réponses d'IA au lieu de la traiter comme une inconnue. Les exécutions en échec en sont exclues, pour qu'une panne ne soit pas lue comme une absence de citations.
- **Couverture fan-out** : confronte la page à des requêtes connexes vers lesquelles un moteur de réponse pourrait étendre la requête d'origine (questions « Autres questions posées », recherches associées, mots-clés secondaires). Lorsque plusieurs d'entre elles ne sont pas traitées sur la page, cela devient une recommandation concrète de « couvrir ces questions connexes ».

## Niveaux de preuve des recommandations

Chaque problème et chaque recommandation sont étiquetés selon la solidité des preuves qui les étayent :

- **Prouvé** : conditions préalables de récupération solidement étayées empiriquement (accès des robots, rendu côté serveur, liens fonctionnels, indexation par les moteurs).
- **Indicatif** : étayées par des recherches observationnelles à grande échelle, sans garantie (placement de la réponse en tête, actualité, clarté structurelle).
- **Best-practice** : plausibles et peu coûteuses, mais sans preuve d'effet sur les citations d'IA (ajout de statistiques, de citations ou d'un sourcing plus soigné).

L'audit ne recommande ni le balisage schema/JSON-LD, ni les fichiers `llms.txt`, ni les tactiques de bourrage de mots-clés comme moyens d'améliorer les citations d'IA, la recherche actuelle ne permettant pas de les considérer comme des leviers de citation.

## Combien de recommandations vous obtenez

Le nombre de recommandations dépend du nombre de problèmes réels détectés, pondéré par le score global de la page : une page qui présente de vrais problèmes reçoit davantage de recommandations, une page déjà bien notée en reçoit moins, parfois aucune. Le nombre n'est jamais gonflé pour atteindre un objectif fixe.

## Lancer un audit

1. Fournissez une URL en production ou collez un brouillon, ainsi que la requête cible qu'une personne emploierait pour trouver ce contenu.
2. Hi, Moose capture un instantané délimité du contenu et de la structure de la page, en utilisant comme preuve principale la version statique (non rendue par JavaScript), car c'est ce qui se rapproche le plus de ce que voient réellement la plupart des robots d'IA.
3. Lorsque c'est utile, il collecte de véritables preuves issues des moteurs de réponse ou des citations pour la requête cible.
4. Si votre projet dispose d'une propriété [Google Search Console](../integrations/google-search-console.md) connectée pour cette URL, vos données de performance propriétaires entrent dans la hiérarchisation et dans la prudence des recommandations. Cela ne modifie pas le score AEO sous-jacent.
5. Hi, Moose note la page, crée une référence (ou vérifie par rapport à une référence antérieure) et assemble l'audit en un artefact durable assorti d'un plan d'action explicite.

## Vérifier l'amélioration

Comme chaque audit est enregistré comme référence, relancer un audit sur la même page après modifications produit un **résultat de vérification**, qui indique si le score s'est réellement amélioré, et pas seulement si vous avez apporté des modifications.

## Intégrité

Les AEO audits n'inventent jamais de preuves. Si Hi, Moose ne parvient pas à collecter les preuves ou à mener réellement à bien une étape de scoring, l'audit échoue explicitement et vous en explique la raison, plutôt que de présenter une supposition comme un résultat abouti. Si la recherche en direct et l'analyse concurrentielle ne peuvent aboutir lors d'un audit géré payant, l'audit se termine malgré tout avec les preuves de page dont il dispose, en indiquant explicitement que la recherche en direct était indisponible pour cette exécution.

## Droits selon le forfait

- **Preview Mode (gratuit)** exécute les audits sur un modèle local Gemma 4 activé. Il n'y a plus d'allocation mensuelle gratuite d'audits dans le cloud : installez un [modèle local](../getting-started/settings.md#local-model) et les audits sont gratuits, aussi souvent que vous le souhaitez.
- **Les forfaits BYOK** exécutent les audits en local avec votre propre clé OpenRouter.
- **Les forfaits gérés** utilisent les modèles gérés de Hi, Moose sur le solde de crédits habituel de votre compte. Il n'y a pas de monnaie distincte de « crédits d'audit » à suivre.

## Actions suivantes après un audit

Le plan d'action d'un audit débouche directement sur d'autres fonctionnalités : générer un [brief de contenu](content-briefs.md), préparer une [modification et son aperçu](drafts-and-publishing.md) ou ajouter des FAQ ou des key points. L'audit est donc un point de départ pour agir, et pas seulement un rapport.
