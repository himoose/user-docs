---
source_hash: 1d8f1dffb939a9b3587c4b3a3f298386f6f202a5a02672b6b3dfd79bbccc2135
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/features/entity-graph/)

# Entity Graph

## À quoi cela sert

Un entity graph est la carte de ce dont votre site parle réellement : les personnes, les produits, les lieux, les organisations et les sujets que vos pages nomment, et la manière dont tout cela se relie.

C'est important parce que les moteurs de réponse ne lisent pas votre site comme une liste de pages. Ils le lisent comme un ensemble de choses et de relations. Un site qui établit clairement « nous sommes cette entreprise, nous fabriquons ces produits, pour ces clients, dans cette catégorie » donne au moteur quelque chose à retrouver et à citer. Un site où cela reste implicite le laisse deviner.

L'entity graph vous montre lesquelles de ces choses votre site a déjà rendues claires, lesquelles sont ténues, et ce qu'un moteur en retiendrait.

Lancez-le depuis **Outils → Créer un entity graph**, ou demandez-le simplement dans le [chat](../chat/overview.md).

## Avant de pouvoir en construire un

Le graphe est construit à partir des pages que Hi, Moose a déjà explorées : le projet a donc besoin **d'un site web et d'au moins une exploration terminée**. S'il n'y en a pas encore, la fiche de lancement vous le dit et vous renvoie vers [Surveillance du site](../site-monitoring/overview.md) pour en lancer une.

La fiche vous indique sur quoi elle travaille : combien de pages explorées, et la date de la dernière exploration terminée.

## Rapide ou complet

Deux profondeurs :

- **Rapide** : données structurées uniquement. Lit le balisage schema, les métadonnées et la structure de page que votre site publie déjà. S'exécute instantanément, sans coût.
- **Complet** : tout ce que fait le mode rapide, plus une passe d'IA qui lit vos meilleures pages et nomme les entités qui ne sont balisées nulle part. Prend quelques minutes.

En mode complet, vous choisissez combien de pages la passe d'IA peut lire. Les exécutions plus larges prennent plus de temps et, sur les forfaits gérés, les appels au modèle cloud consomment votre allocation mensuelle. La passe s'exécute avec le modèle sélectionné dans le menu de modèles du chat : choisissez donc le modèle d'abord si vous en voulez un en particulier. Un modèle local chargé garde l'ensemble sur votre machine, et gratuitement.

## Ce que vous obtenez

Le graphe rapporte :

- **Entités** : tout ce qui a été trouvé, avec son type, ses alias, le nombre de pages où elle apparaît et un score de **saillance** indiquant sa centralité pour le site.
- **Relations** : la façon dont ces entités se relient, réparties en trois familles :
    - **Étiquetées** : une relation que vos données structurées ou la passe d'IA énoncent explicitement.
    - **Page partagée** : deux entités qui reviennent ensemble sur les mêmes pages.
    - **Sémantiques** : deux entités que le langage traite comme liées, même si rien ne les relie formellement.
- **Entités par type** : la répartition, souvent la vue la plus utile à elle seule. Un site qui vend un logiciel et affiche quarante personnes pour trois produits a un problème de récit qu'il vaut mieux connaître.

Un tableau des **entités principales** présente les plus saillantes avec leur type, leur nombre de pages et leur saillance. L'ensemble complet s'exporte en **CSV** ou en **PDF** ; le tableau à l'écran est plafonné, et il indique combien d'entités supplémentaires les exports contiennent.

## Quand la passe d'IA ne s'exécute pas

Le mode complet se dégrade au lieu d'échouer. Si la passe d'IA ne peut pas s'exécuter, vous obtenez tout de même le graphe issu des données structurées, des pages partagées et de la similarité sémantique, et la fiche vous dit quel cas s'applique :

- **Aucun modèle disponible** : chargez un modèle local ou ajoutez une clé OpenRouter, puis relancez en mode complet.
- **Rien de nouveau à lire** : toutes les pages éligibles avaient déjà été analysées lors d'une exécution précédente.
- **La passe a échoué** : elle n'a pas pu aller au bout.
- **Allocation épuisée** : sur les forfaits gérés, la passe s'arrête en même temps que vos crédits mensuels, et le graphe contient tout ce qui a été analysé jusque-là.

## Moose peut le relire

Une fois le graphe créé, le [chat](../chat/tools-and-specialists.md) peut l'interroger directement. Demandez sur quelles entités votre site est le plus solide, ce qui est relié à tel produit, ou ce qui manque à côté d'un sujet que vous cherchez à gagner : Moose lit le graphe plutôt que de réexplorer ou de deviner.

[Send Moose](../send-moose/overview.md) le lit également, dans le cadre de l'intelligence de site qu'il apporte à un travail.

## Où aller ensuite

- **[Surveillance du site](../site-monitoring/overview.md)** : l'exploration dont le graphe est issu.
- **[Content Briefs](content-briefs.md)** : transformer un manque du graphe en page.
- **[Audits AEO](aeo-audits.md)** : vérifier si une page donnée énonce clairement ses entités.
