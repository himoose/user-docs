---
source_hash: e5cf87efe7298e31a0e0c034a7c0d36431b70c08378225d4dd5c73357dd59a4f
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/visibility/overview/)

# Visibility

## À quoi cela sert

Le tableau de bord Visibility montre comment votre marque se comporte réellement dans la recherche par IA : les requêtes que vos clients utilisent pour vous trouver, si votre marque est retenue et si les moteurs d'IA la décrivent avec exactitude. C'est la vue principale pour les étapes **surveiller** et **détecter** du [cycle d'opérations central](../index.md#le-cycle-doperations-central).

Le tableau de bord comporte six onglets :

| Onglet | Question à laquelle il répond |
|---|---|
| **Vue d'ensemble** | Où en suis-je ? |
| **[Concurrence](competitors.md)** | Où en suis-je par rapport à eux ? |
| **Mentions** | Quelles marques sont nommées dans ces réponses ? |
| **Citations** | Sur quelles sources les moteurs s'appuient-ils réellement ? |
| **Thèmes et moteurs** | Où précisément suis-je fort ou faible ? |
| **Prompts** | Que s'est-il passé sur chaque prompt individuel ? |

## Indicateurs

Chaque exécution communique des indicateurs principaux pour la période sélectionnée :

- **Part des mentions** : la fréquence à laquelle votre marque est mentionnée dans les prompts et moteurs surveillés.
- **Part des citations** : la fréquence à laquelle votre domaine est réellement cité comme source.
- **Sentiment** : le ton moyen (positif, mitigé, neutre, négatif) des mentions.
- **Position moyenne** : où votre marque se situe généralement lorsqu'elle apparaît dans une liste ou un classement. Affiche **Données insuffisantes** tant qu'il n'y a pas assez de mentions positionnées pour calculer une moyenne.
- **Dérive narrative** : si les réponses de l'IA s'écartent de votre positionnement voulu.
- **Feature Parity** : si les réponses de l'IA représentent fidèlement ce que vous proposez.

Narrative Drift et Feature Parity affichent **Non noté** avec un lien de configuration tant que vous n'avez pas renseigné votre Brand Truth Profile. Ces deux indicateurs n'ont de sens qu'une fois que Hi, Moose sait ce qui est vrai au sujet de votre marque pour pouvoir comparer. Voir [Brand Truth Profile](../getting-started/context/brand-truth-profile.md).

!!! note "Les observations en échec sont exclues, elles ne comptent pas comme des absences"
    Si un moteur était indisponible ou qu'une requête a échoué, cette observation est écartée de tous les indicateurs au lieu d'être notée comme « votre marque n'a pas été mentionnée ». Une exécution rencontrant des problèmes de connexion porte sur moins d'observations plutôt que de signaler une baisse fictive. La vue par prompt les étiquette **Réponse indisponible** et indique combien ont été exclues.

## Filtres et période

- Filtrez par **Sujet**, **Moteur IA**, **Prompt** (sélection multiple avec recherche), **Page**, **Sentiment**, **Narration** ou **Feature Parity**, ou effacez tous les filtres d'un coup.
- Le filtre **Page** restreint à des URL précises, avec recherche par chemin. Il fait apparaître correctement les moteurs où l'URL n'a **pas** été citée : vous voyez donc aussi bien où une page manque que là où elle apparaît.
- Définissez une plage de dates dans **Période** puis cliquez sur **Appliquer**, ou cliquez sur **Comparer** pour superposer une période antérieure ou l'exécution précédente.

## Tendance dans le temps

Le graphique de tendance représente **Mentions**, **Citations**, **% positif** ou la position moyenne par intervalles de **jour**, **semaine** ou **mois**, ventilés par moteur d'IA ou avec **Tous les modèles** combinés, pour voir si un moteur précis fait bouger les chiffres.

## Détail par prompt

Sous le graphique :

- **Taux de mention** ventile les résultats par moteur, en montrant lesquels vous ont mentionné et lesquels non.
- **Pages les plus citées** montre lesquelles de vos URL sont citées, et par quels moteurs.
- **Répartition par prompt** déplie n'importe quel prompt surveillé pour voir les résultats individuels par moteur, y compris la réponse complète de l'IA et le raisonnement sur le sentiment, le narratif et la parité fonctionnelle.

Chaque prompt comporte un lien **investiguer dans le chat** qui transmet les données exactes de l'observation à Moose et lui demande de recommander si l'étape suivante est un [AEO audit](../features/aeo-audits.md) d'une page existante ou un nouveau [brief et brouillon de contenu](../features/content-briefs.md).

## L'onglet Vue d'ensemble

La Vue d'ensemble s'ouvre sur un résumé rédigé de la coupe en cours : quelques paragraphes qui disent où vous en êtes, ce qui a bougé et ce qui mérite un coup d'œil, en phrases plutôt qu'en chiffres. Il est généré à partir de la même fiche de données que le rapport, et vous pouvez demander **Réécrire le résumé** si vous le voulez autrement. Lorsqu'aucun modèle n'est disponible pour l'écrire, la Vue d'ensemble bascule sur une version construite directement à partir des chiffres et le signale.

Sous le résumé, deux blocs :

- **Où vous en êtes** : votre Share of Voice, le taux de mention sur les réponses lues, les citations, le rang moyen lorsque vous êtes nommé et le taux de mention par moteur, avec l'ensemble des marques suivies à côté de vous.
- **L'IA vous décrit-elle correctement ?** : alignement du positionnement, répartition du ton, et une liste de **réponses à revoir** : les réponses précises où un moteur a mal décrit une capacité ou s'est écarté de votre positionnement. Chacune ouvre la réponse ou y saute dans l'onglet Prompts.

## Mentions

L'onglet **Mentions** est la liste complète de chaque marque, produit ou site web que les moteurs ont nommé dans les réponses de la coupe en cours : pas seulement vous et vos concurrents suivis, mais tous ceux qui sont apparus.

Chaque ligne indique dans combien de réponses la marque a été nommée, ce chiffre en pourcentage des réponses de la coupe, sa part de l'ensemble des mentions, son rang moyen parmi les marques nommées dans une réponse, et son verdict de sentiment le plus fréquent. Survolez une valeur de sentiment pour la répartition positif/mixte/neutre/négatif, et un en-tête de colonne pour sa définition exacte.

Au-dessus du tableau, une **tendance de présence des mentions** trace les marques les plus mentionnées, et vous, dans le temps.

C'est ici que vous trouvez les concurrents dont vous ignoriez l'existence. Les marques sont lues dans le texte de la réponse par le modèle de scoring : la liste fait donc remonter des noms que vous n'avez jamais ajoutés à votre suivi.

## Citations

L'onglet **Citations** applique la même idée aux sources : chaque domaine ou page que les moteurs ont cité dans la coupe en cours.

Basculez entre **Par domaine** et **Par URL de page**, et filtrez sur **Tout** ou **Ni vous ni un concurrent** pour voir les sources tierces qui façonnent les réponses. Chaque source est catégorisée : votre marque, concurrent, réseau social, site d'avis, publication, référence, développement ou autre.

Les colonnes sont les suivantes :

| Colonne | Ce que cela signifie |
|---|---|
| **Prompts cités** | Dans combien de réponses ce domaine ou cette URL a été cité |
| **Présence %** | Ce chiffre rapporté aux réponses de la coupe |
| **Nombre de citations** | Total des citations, répétitions comprises |
| **Visibilité %** | Sa part de l'ensemble des citations de la coupe |
| **Rang moyen** | Sa position moyenne dans les listes de citations des moteurs |
| **Évolution** | Mouvement par rapport à la période de comparaison ou à l'exécution précédente |

**Détails** sur une ligne liste les pages qui la composent et les prompts pour lesquels chaque page a été citée. N'importe quel domaine du tableau peut être ajouté directement à vos concurrents suivis avec **Suivre comme concurrent**, de sorte qu'un nom découvert ici entre dans le [Share of Voice](competitors.md) sans avoir à le ressaisir.

Les deux tableaux se téléchargent en CSV.

!!! note "Les moteurs qui ne naviguent pas ne renvoient aucune citation"
    Les citations proviennent des moteurs qui consultent le web pendant qu'ils répondent. Un modèle local, ou un moteur qui répond à partir de son seul entraînement, n'en renvoie aucune : un tableau vide sous un filtre étroit ne signale donc pas forcément un problème sur votre site.

## Topics & Engines

Cet onglet ventile les performances de deux façons :

- **Taux de mention par thème** : la fréquence à laquelle chaque marque apparaît dans les réponses d'IA pour chaque thème.
- **Évolution du taux de mention par thème** : la même chose, ventilée dans le temps.
- **Taux de mention par plateforme** : une carte de chaleur de la fréquence à laquelle chaque marque apparaît dans les réponses de chaque plateforme sur la période.

Les thèmes proviennent des catégories de vos prompts. Si vos prompts ne sont pas catégorisés, cet onglet vous invite à les organiser dans le [Prompt Manager](prompt-manager.md) plutôt que d'afficher un graphique vide.

## Exporter

**Exporter** propose deux formats :

- **Feuille de calcul CSV** : tous les résultats de la vue en cours, pour Excel ou Google Sheets.
- **Rapport exécutif PDF** : un rapport complet en treize sections sur la vue en cours, écrit pour être remis à quelqu'un qui n'était pas dans la pièce.

Le rapport s'ouvre sur un récit rédigé plutôt que sur un empilement de graphiques, puis déroule : où vous en êtes, si l'IA vous décrit correctement, le mouvement sur la période, moteur par moteur, où l'IA vous cite, les questions que les concurrents gagnent, ce pour quoi les concurrents sont cités, le champ complet, les marques nommées dans les réponses d'IA, les domaines que l'IA cite, le taux de mention par moteur, le taux de mention par thème, et une section finale expliquant comment lire chaque indicateur.

Les exports respectent vos filtres actifs, et la couverture du PDF indique quels filtres ont été appliqués, afin qu'un rapport ne puisse pas être pris pour une vue d'ensemble du compte. Sur les forfaits payants, le PDF porte votre [marque blanche](../agency/white-label.md) si vous l'avez configurée.

## Lancer des vérifications de visibilité

Cliquez sur **Exécuter maintenant** pour une vérification à la demande. Le comportement dépend de votre [forfait](../getting-started/account-modes.md) :

- **Preview Mode** effectue des vérifications en interrogation locale directement depuis votre appareil sur les surfaces publiques de recherche par IA. Hi, Moose vous demande confirmation au préalable, car enchaîner les vérifications peut déclencher des blocages temporaires pour dépassement de limite sur ces surfaces. Le scoring de sentiment, de narratif et de parité nécessite un modèle local Gemma 4 activé ; sans lui, ces vérifications sont ignorées.
- **Les forfaits BYOK** s'exécutent en local avec votre propre clé OpenRouter.
- **Les forfaits gérés** passent par l'infrastructure de Hi, Moose. S'il ne reste pas assez d'allocation ce mois-ci à votre espace de travail pour la planification en cours, les exécutions planifiées sont suspendues jusqu'à ce que vous changiez de forfait, ajustiez votre [cadence d'exécution](settings.md#planification-des-executions) ou que l'allocation se réinitialise. Hi, Moose vous indique le nombre d'unités nécessaires par rapport à celles restantes.

Vous pouvez interrompre une exécution en cours, et les exécutions interrompues par une mise à jour de l'application reprennent au lieu d'être perdues.

## Quel historique est conservé

Chaque observation produite par une exécution est archivée localement, afin que les tendances, les comparaisons et les tableaux Mentions et Citations puissent remonter plus loin que les dernières exécutions. L'archive conserve jusqu'à **400 jours** par espace de travail et jusqu'à 200 000 observations ; au-delà de l'une ou l'autre limite, les lignes les plus anciennes sont supprimées.

Sur les forfaits gérés payants, les exécutions de visibilité lancées sur votre machine synchronisent aussi leurs résultats vers le cloud, de sorte que vos collègues voient le même historique que vous, et pas seulement les exécutions effectuées sur leur propre appareil.

## Où aller ensuite

- **[Concurrents et Share of Voice](competitors.md)** : position concurrentielle, citations de concurrents et écarts.
- **[Prompt Manager](prompt-manager.md)** : ajouter, organiser et catégoriser les prompts surveillés.
- **[Paramètres de Visibility](settings.md)** : planification des exécutions, modèle de scoring, suivi des concurrents, termes et domaines de marque secondaires et modèles par défaut.
