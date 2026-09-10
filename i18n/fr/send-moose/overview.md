---
source_hash: 7e432cdd4918eeb01a120c373ca83181288da1c2c0b01d3aee18207e05092124
---
# Send Moose

## À quoi cela sert

Send Moose, c'est l'endroit où vous confiez un travail au lieu de le faire vous-même. Vous décrivez la mission en langage courant (« trouve qui est recommandé à notre place pour les logiciels de gestion de projet, et pourquoi », « vérifie si notre page tarifs correspond encore à ce que disent les pages comparatives de nos concurrents ») et Moose va le faire, en utilisant le web et tout ce que Hi, Moose sait déjà de votre projet.

C'est la différence entre un chat qui vous répond et un agent qui se met au travail. Le chat est une conversation ; Send Moose est une mission que vous lancez et que vous retrouvez plus tard.

Vous le trouverez dans la barre latérale, sous **Send Moose**.

!!! warning "Send Moose est expérimental"
    C'est dans l'application et cela fonctionne, mais c'est ce qu'il y a de plus récent et de moins stabilisé dans Hi, Moose. Surveillez la qualité de ce qui revient, et surveillez votre consommation de jetons sur les forfaits payants : Scout et Skeptic s'exécutent dans le cloud même quand Moose tourne en local.

## Ce que Moose apporte avec lui

Un agent web générique part de rien et il faut tout lui expliquer. Moose arrive déjà connecté à votre projet :

| Il peut lire | Ce que cela signifie |
|---|---|
| Vos données de visibilité | Vue d'ensemble, Share of Voice, concurrents, thèmes, prompts et ce qui a changé |
| Votre index de site | Pages explorées, ce qui y a changé, liens internes et votre [entity graph](../features/entity-graph.md) |
| Votre historique AEO | Audits passés et leur détail, contexte de citation, accès des crawlers, couverture des sujets |
| [Google Search Console](../integrations/google-search-console.md) | Vos données réelles de requêtes et de pages, interrogées de façon itérative |
| Votre [Bibliothèque](../library/overview.md) | Briefs, brouillons, key points, FAQ et audits déjà réalisés |
| Les travaux passés | Ce qu'il a trouvé et décidé lors d'exécutions précédentes de ce projet |

Il peut aussi lancer une [vérification de visibilité](../visibility/overview.md) en direct ou un [audit AEO](../features/aeo-audits.md) au milieu d'un travail, quand la réponse l'exige, plutôt que de vous dire d'aller le lancer vous-même.

## Lancer un travail

Décrivez la mission et appuyez sur **Send Moose**. Deux options en déterminent le déroulé :

- **Travail approfondi** : laissez la mission durer des heures si nécessaire : beaucoup plus de pages, beaucoup plus de recherches, plus de points d'étape. À utiliser quand la question est vraiment large, pas pour une recherche rapide.
- **Joindre des fichiers** : jusqu'à six fichiers par mission, comme contexte qu'il lit en travaillant.

Vous pouvez cocher **Me prévenir quand Moose a terminé** et partir. Le travail continue que vous le regardiez ou non, et que vous restiez sur l'écran ou non.

## Le regarder travailler

**Voir le navigateur** ouvre l'instance de navigateur utilisée par Moose, pour voir les pages à mesure qu'il les lit. **Prendre le contrôle** vous rend la main s'il bloque sur quelque chose que vous pouvez lever en une seconde (un bandeau de cookies, une connexion), et **Retour au travail** la lui rend.

Vous pouvez fermer cette fenêtre quand vous voulez. Moose continue de travailler.

## Moose, Scout et Skeptic

Sur le forfait gratuit, Moose travaille seul.

Les forfaits payants ajoutent deux autres agents à la mission :

- **Scout** trouve des angles auxquels Moose n'a pas pensé.
- **Skeptic** conteste les preuves avant qu'elles n'atteignent votre résultat.

Vous pouvez parler à chacun d'eux en cours de mission depuis le fil : dire quelque chose à Moose, demander un autre angle à Scout, demander à Skeptic d'appuyer davantage sur une affirmation. **Continuer** et **Vérifier cinq résultats de plus** prolongent une exécution qui s'est arrêtée à un endroit intéressant.

Scout et Skeptic s'exécutent toujours dans le cloud via OpenRouter, même quand Moose tourne sur un modèle local : ils consomment donc des jetons.

## Quand Moose a besoin de vous

Deux situations arrêtent une mission et vous attendent plutôt que de deviner :

- **Attend votre approbation** : Moose s'apprête à déclencher une action sur un vrai site web, comme appuyer sur un bouton de formulaire. Il vous montre le bouton exact et attend **Approuver et continuer** ou **Ne le fais pas**.
- **A besoin de votre aide** : il bloque sur quelque chose que vous seul pouvez trancher. Tapez une réponse, ou appuyez sur **Laisser Moose décider** pour qu'il tranche lui-même.

Rien n'est publié, envoyé ni soumis nulle part sans votre approbation préalable. Cela vaut aussi pour les exécutions planifiées.

## Lire le résultat

Une mission terminée comporte quatre onglets :

- **Résultat** : ce qu'il a trouvé, rédigé.
- **Collaboration** : comment cela s'est passé et qui a apporté quoi : notes ajoutées par Scout, objections soulevées par Skeptic, fois où vous êtes intervenu.
- **Sources** : chaque page qu'il a ouverte, avec les preuves qu'il en a tirées.
- **Activité** : l'exécution complète, filtrable par outils ou par agents.

De là, vous pouvez **Enregistrer dans la Bibliothèque**, **Télécharger le rapport**, ou poser une question de suivi sur le résultat dans le [chat](../chat/overview.md). Les fichiers enregistrés par Moose pendant la mission apparaissent sous **Fichiers enregistrés par Moose** : ouvrez-les, enregistrez-en une copie ou affichez-les dans leur dossier. Il peut enregistrer des fichiers CSV, Markdown, texte brut, PDF et Word.

## Le contenu que Moose crée

Moose peut produire de véritables artefacts Hi, Moose dans le cadre d'une mission, et pas seulement une réponse rédigée : un **content brief**, un **brouillon**, des **key points**, des **FAQ** ou un **audit AEO**. Ils atterrissent dans votre [Bibliothèque](../library/overview.md) comme tout le reste, et le résultat de la mission y renvoie directement.

## Lancer une mission de façon planifiée

**Lancer selon une planification** transforme une mission ponctuelle en mission récurrente : chaque jour, en semaine, chaque semaine ou chaque mois, à une ou plusieurs heures de la journée.

Les missions planifiées apparaissent sous **Missions planifiées** et peuvent être suspendues, reprises ou supprimées. Elles s'exécutent sans surveillance : Moose tranche lui-même les petites décisions, et ne publie ni n'envoie toujours rien sans votre approbation.

## Missions passées

Toutes les missions sont conservées sous **Missions passées**, avec recherche et filtres **Terminées**, **Rappelées**, **Non abouties** et **Bloquées**, regroupées par aujourd'hui, plus tôt cette semaine et avant. Les missions appartiennent au projet dans lequel elles ont été lancées.

## Paramètres

Les **paramètres de Send Moose** sont enregistrés par projet :

- **LLM de Moose** : Automatique utilise le plus grand modèle local installé, ou le modèle cloud de votre forfait quand l'IA locale est désactivée. Vous pouvez aussi fixer un modèle précis.
- **LLM de Scout** et **LLM de Skeptic** : forfaits payants uniquement, avec Gemma 4 31B par défaut.
- **Modèle de contenu** : quel modèle rédige les briefs, brouillons et FAQ qu'il crée. Par défaut, le même que Moose.
- **Moteur de recherche** : avec quel moteur il effectue ses recherches.

Tout ce qui est marqué **Consomme des jetons** s'exécute dans le cloud via OpenRouter plutôt que sur votre ordinateur. Les missions en travail approfondi durent le plus longtemps, elles coûtent donc le plus cher.

## Ce dont il a besoin

- **Un modèle local, ou un forfait payant.** Moose réfléchit sur un modèle Gemma qui tourne sur votre ordinateur. Téléchargez-le une fois depuis l'invite affichée à l'écran et les missions ne vous coûtent rien. Les forfaits payants peuvent le placer sur un modèle cloud. Si vous avez désactivé l'IA locale et que vous êtes sur le forfait gratuit, Send Moose vous le signale et propose de la réactiver.
- **Un site web sur le projet**, pour les missions qui concernent votre propre site, votre marque ou vos concurrents. Les missions web générales fonctionnent très bien sans.

## Où aller ensuite

- **[Chat](../chat/overview.md)** : pour un travail que vous voulez piloter tour par tour plutôt que déléguer.
- **[Workflows](../workflows/overview.md)** : pour une recette figée qui se déclenche sur un événement, plutôt qu'une mission ouverte.
- **[Bibliothèque](../library/overview.md)** : où sont conservés les rapports et le contenu issus d'une mission.
