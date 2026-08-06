---
source_hash: 40b089c8c06f81c797410e131c0f51ee08f0beba3baaaf1ad18b0794a101df1a
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/visibility/overview/)

# Visibility

## À quoi cela sert

Le tableau de bord Visibility montre comment votre marque se comporte réellement dans la recherche par IA : les requêtes que vos clients utilisent pour vous trouver, si votre marque est retenue et si les moteurs d'IA la décrivent avec exactitude. C'est la vue principale pour les étapes **surveiller** et **détecter** du [cycle d'opérations central](../index.md#le-cycle-doperations-central).

Le tableau de bord comporte trois onglets :

| Onglet | Question à laquelle il répond |
|---|---|
| **Overview** | Où en suis-je ? |
| **[Competition](competitors.md)** | Où en suis-je par rapport à eux ? |
| **Topics & Engines** | Où précisément suis-je fort ou faible ? |

## Indicateurs

Chaque exécution communique des indicateurs principaux pour la période sélectionnée :

- **Share of Mentions** : la fréquence à laquelle votre marque est mentionnée dans les prompts et moteurs surveillés.
- **Share of Citations** : la fréquence à laquelle votre domaine est réellement cité comme source.
- **Sentiment** : le ton moyen (positif, mitigé, neutre, négatif) des mentions.
- **Position moyenne** : où votre marque se situe généralement lorsqu'elle apparaît dans une liste ou un classement. Affiche **Not enough data** tant qu'il n'y a pas assez de mentions positionnées pour calculer une moyenne.
- **Narrative Drift** : si les réponses de l'IA s'écartent de votre positionnement voulu.
- **Feature Parity** : si les réponses de l'IA représentent fidèlement ce que vous proposez.

Narrative Drift et Feature Parity affichent **Not scored** avec un lien de configuration tant que vous n'avez pas renseigné votre Brand Truth Profile. Ces deux indicateurs n'ont de sens qu'une fois que Hi, Moose sait ce qui est vrai au sujet de votre marque pour pouvoir comparer. Voir [Brand Truth Profile](../getting-started/context/brand-truth-profile.md).

!!! note "Les observations en échec sont exclues, elles ne comptent pas comme des absences"
    Si un moteur était indisponible ou qu'une requête a échoué, cette observation est écartée de tous les indicateurs au lieu d'être notée comme « votre marque n'a pas été mentionnée ». Une exécution rencontrant des problèmes de connexion porte sur moins d'observations plutôt que de signaler une baisse fictive. La vue par prompt les étiquette **Response unavailable** et indique combien ont été exclues.

## Filtres et période

- Filtrez par **Topic**, **AI Engine**, **Prompt** (sélection multiple avec recherche), **Page**, **Sentiment**, **Narrative** ou **Feature Parity**, ou effacez tous les filtres d'un coup.
- Le filtre **Page** restreint à des URL précises, avec recherche par chemin. Il fait apparaître correctement les moteurs où l'URL n'a **pas** été citée : vous voyez donc aussi bien où une page manque que là où elle apparaît.
- Définissez une plage de dates dans **Period** puis cliquez sur **Apply**, ou cliquez sur **Compare** pour superposer une période antérieure ou l'exécution précédente.

## Tendance dans le temps

Le graphique de tendance représente **Mentions**, **Citations**, **Positive %** ou la position moyenne par intervalles de **jour**, **semaine** ou **mois**, ventilés par moteur d'IA ou avec **All models** combinés, pour voir si un moteur précis fait bouger les chiffres.

## Détail par prompt

Sous le graphique :

- **Mention Rate** ventile les résultats par moteur, en montrant lesquels vous ont mentionné et lesquels non.
- **Top Cited Pages** montre lesquelles de vos URL sont citées, et par quels moteurs.
- **Prompt-Level Breakdown** déplie n'importe quel prompt surveillé pour voir les résultats individuels par moteur, y compris la réponse complète de l'IA et le raisonnement sur le sentiment, le narratif et la parité fonctionnelle.

Chaque prompt comporte un lien **investiguer dans le chat** qui transmet les données exactes de l'observation à Moose et lui demande de recommander si l'étape suivante est un [AEO audit](../features/aeo-audits.md) d'une page existante ou un nouveau [brief et brouillon de contenu](../features/content-briefs.md).

## Topics & Engines

Cet onglet ventile les performances de deux façons :

- **Mention Rate by Topic** : la fréquence à laquelle chaque marque apparaît dans les réponses d'IA pour chaque thème.
- **Mention Rate Trend by Topic** : la même chose, ventilée dans le temps.
- **Mention Rate by Platform** : une carte de chaleur de la fréquence à laquelle chaque marque apparaît dans les réponses de chaque plateforme sur la période.

Les thèmes proviennent des catégories de vos prompts. Si vos prompts ne sont pas catégorisés, cet onglet vous invite à les organiser dans le [Prompt Manager](prompt-manager.md) plutôt que d'afficher un graphique vide.

## Exporter

**Export** propose deux formats :

- **CSV spreadsheet** : tous les résultats de la vue en cours, pour Excel ou Google Sheets.
- **PDF executive report** : un rapport prêt à imprimer de la vue en cours, incluant les graphiques et données concurrentiels de l'onglet Competition.

Les exports respectent vos filtres actifs, et la couverture du PDF indique quels filtres ont été appliqués, afin qu'un rapport ne puisse pas être pris pour une vue d'ensemble du compte. Sur les forfaits payants, le PDF porte votre [marque blanche](../agency/white-label.md) si vous l'avez configurée.

## Lancer des vérifications de visibilité

Cliquez sur **Run now** pour une vérification à la demande. Le comportement dépend de votre [forfait](../getting-started/account-modes.md) :

- **Preview Mode** effectue des vérifications en interrogation locale directement depuis votre appareil sur les surfaces publiques de recherche par IA. Hi, Moose vous demande confirmation au préalable, car enchaîner les vérifications peut déclencher des blocages temporaires pour dépassement de limite sur ces surfaces. Le scoring de sentiment, de narratif et de parité nécessite un modèle local Gemma 4 activé ; sans lui, ces vérifications sont ignorées.
- **Les forfaits BYOK** s'exécutent en local avec votre propre clé OpenRouter.
- **Les forfaits gérés** passent par l'infrastructure de Hi, Moose. S'il ne reste pas assez d'allocation ce mois-ci à votre espace de travail pour la planification en cours, les exécutions planifiées sont suspendues jusqu'à ce que vous changiez de forfait, ajustiez votre [cadence d'exécution](settings.md#planification-des-executions) ou que l'allocation se réinitialise. Hi, Moose vous indique le nombre d'unités nécessaires par rapport à celles restantes.

Vous pouvez interrompre une exécution en cours, et les exécutions interrompues par une mise à jour de l'application reprennent au lieu d'être perdues.

## Où aller ensuite

- **[Concurrents et Share of Voice](competitors.md)** : position concurrentielle, citations de concurrents et écarts.
- **[Prompt Manager](prompt-manager.md)** : ajouter, organiser et catégoriser les prompts surveillés.
- **[Paramètres de Visibility](settings.md)** : planification des exécutions, modèle de scoring, suivi des concurrents, termes et domaines de marque secondaires et modèles par défaut.
