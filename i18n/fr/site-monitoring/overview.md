---
source_hash: 87a7b6f091685fae0a59b09ee8abe0ec965085647eb82bd29c1661777efb87ab
---
# Surveillance du site

## À quoi cela sert

Hi, Moose conserve une image locale de votre site web : quelles pages existent, ce qu'elles contiennent et ce qui a changé depuis la dernière fois. Cette image alimente trois choses : les alertes de changements pertinents pour l'AEO dans votre [Inbox](../inbox/overview.md), l'index de recherche sémantique que Moose utilise pour répondre aux questions sur votre propre site, et l'inventaire de pages dont se servent les [audits](../features/aeo-audits.md) et les [briefs](../features/content-briefs.md).

Tout cela se trouve dans **Paramètres → Surveillance du site**, délimité au projet en cours.

## L'exploration planifiée

Activez **Exécuter l'exploration hebdomadaire du site** et Hi, Moose actualisera les pages surveillées à une cadence hebdomadaire, en vous avertissant lorsque des changements significatifs apparaissent. Choisissez le jour et l'heure dans votre horaire local.

Les explorations manuelles restent disponibles dans tous les cas. **Lancer l'exploration maintenant** lance immédiatement une exploration complète, avec la progression dans la barre d'état en bas de la fenêtre. Vous pouvez **arrêter** une exploration en cours : les pages trouvées jusque-là sont conservées plutôt que jetées.

Les grands sites prennent quelques minutes.

## L'index de recherche

Sous les commandes d'exploration se trouve le **Index de recherche**, l'index sémantique local que Moose utilise pour répondre aux questions sur les pages de votre site. Il indique combien de pages sont indexées, combien de passages ces pages ont produits et à quand remonte sa dernière mise à jour.

L'indexation se fait au niveau des passages, pas des pages. Une page longue devient de nombreux passages consultables séparément, et c'est pourquoi Moose peut citer un paragraphe précis au lieu de vous dire qu'une page traite « globalement » d'un sujet.

- **Reconstruire l'index** réindexe entièrement.
- Si des pages sont nouvelles ou modifiées depuis la dernière mise à jour de l'index, Hi, Moose vous indique combien. Elles seront indexées à la prochaine exploration, ou vous pouvez reconstruire l'index maintenant.

!!! note "L'index est honnête sur ce qu'il n'a pas"
    Si vous interrogez Moose sur une page qui n'a pas été indexée, il vous le dit et vous oriente vers le lancement d'une exploration, plutôt que de deviner à partir de l'URL de la page.

## Pages surveillées

Les pages que Hi, Moose vérifie à la recherche de changements pertinents pour l'AEO. Les pages découvertes par l'exploration du site, par [Google Search Console](../integrations/google-search-console.md) et par les [exécutions de visibilité](../visibility/overview.md) y apparaissent automatiquement.

Vous pouvez aussi ajouter des pages à la main avec une URL complète, rechercher et filtrer la liste, la parcourir page par page et retirer les pages qui ne vous intéressent pas.

## Chemins bloqués

Les explorations ignorent les chemins bloqués et tout ce qui s'y rattache, et les pages correspondantes sont retirées de la surveillance.

La correspondance se fait par préfixe de segment de chemin. Bloquer `/results/` couvre `/results/` et l'ensemble de ses sous-chemins, mais **pas** `/results-archive/` : c'est le segment qui doit correspondre, pas seulement la chaîne de caractères.

C'est l'outil adapté aux pages de résultats de recherche, aux pages de listes filtrées, aux archives paginées et à tout ce qui génère un grand nombre d'URL quasi identiques que vous préférez ne pas explorer, ne pas indexer et pour lesquelles vous ne voulez pas d'alertes.

## Ce qui arrive dans votre Inbox

Une exploration produit **un seul récapitulatif par exécution**, et non un élément par page modifiée. Le récapitulatif s'ouvre sur un tableau des pages modifiées indiquant ce qui a changé, un niveau d'impact et des actions par page.

Les niveaux d'impact sont **Critique**, **Notable**, **Faible**, **Inaccessible** et **Non examinée**.

Deux réglages régulent le bruit :

- **Inclure les changements AEO informatifs** : désactivé par défaut. Une fois activé, les changements à faible impact génèrent également des éléments dans l'Inbox.
- **Sévérité minimale de notification du système d'exploitation** : seuls les éléments de l'Inbox situés à ce niveau ou au-dessus déclenchent une notification du bureau. Réglez-le sur Info si vous souhaitez que les changements à faible impact remontent aussi au niveau du système d'exploitation.

## Demander à Moose ce qui a changé

Le récapitulatif comporte une action **Demander à Moose à propos de tout ceci** qui transmet l'instantané complet de l'exploration au chat et lui demande ce qui compte le plus et par quoi commencer. Les pages individuelles disposent de leur propre action **Demander à Moose**, qui ne transmet que le changement enregistré pour cette page.

Les deux se limitent à l'instantané enregistré. Si celui-ci n'explique pas pourquoi quelque chose a changé, Moose a pour consigne de le dire plutôt que d'inventer une raison.

## Pages inaccessibles

Si une page ou l'ensemble du site est inaccessible, cela est signalé comme un type de changement à part entière au lieu d'être ignoré en silence. Une panne générale du site produit un unique élément **Site inaccessible** au lieu d'une alerte par page.
