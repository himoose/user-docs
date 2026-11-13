---
source_hash: bf06b2d4371815f46d4209e9c058c88a274ce098682e93731da1f9cafde41e72
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/visibility/second-turn-queries/)

# Requêtes de second tour

## À quoi cela sert

Les moteurs d'IA terminent souvent une réponse en invitant à poser la question suivante. Une requête de second tour est cette question suivante, rédigée en entier pour être compréhensible seule. Hi, Moose les relève pendant les exécutions de visibilité et les affiche dans l'onglet **Requêtes de second tour**, avec la fréquence d'apparition de chacune et l'indication de sa couverture par votre site.

Par exemple, un moteur peut terminer une réponse par « Voulez-vous que je compare ces deux options côte à côte ? ». La requête de second tour est ce qu'une personne saisirait pour accepter, par exemple « Comparer les rehausseurs de bureau assis-debout et les bureaux assis-debout complets pour un petit bureau à domicile ».

## Activer la fonction

Ouvrez les [Paramètres de Visibility](settings.md#requetes-de-second-tour) et allez à la section **Requêtes de second tour**. Activez **Relever les requêtes de second tour**. L'option est désactivée par défaut et s'active séparément pour chaque projet.

Tant que l'option est désactivée, rien n'est relevé et l'onglet Requêtes de second tour reste masqué.

Vous pouvez activer l'option avec les forfaits gérés payants, BYOK Premium et BYOK Agency. Avec Preview Mode et BYOK Free, l'interrupteur est grisé et affiche la mention **Disponible avec les offres payantes**.

L'activation ajoute un petit appel au modèle pour chaque réponse d'une exécution. Avec les forfaits gérés payants, ces appels sont décomptés de l'allocation de votre forfait. Avec BYOK Premium et BYOK Agency, ils sont facturés sur votre clé OpenRouter.

## L'onglet Requêtes de second tour

L'onglet se trouve juste après **Opportunités** dans le tableau de bord Visibility. Il n'apparaît que lorsque l'option est activée. Il reste vide jusqu'à la première exécution de visibilité qui suit l'activation, car les réponses des exécutions précédentes ne sont pas traitées.

L'onglet suit la période et les filtres sélectionnés en haut de Visibility. Une requête figure dans la liste lorsqu'une réponse de cette période la contenait.

### Vues

- **Les plus fréquentes** est la vue par défaut. Elle affiche une seule liste classée selon le nombre de réponses qui contenaient chaque requête.
- **Par prompt** regroupe les requêtes sous le prompt surveillé que chacune a suivi.

### Ce qu'affiche une ligne

- La requête.
- **Réponses contenant cette requête : N**, où N est le nombre de réponses qui la contenaient.
- Les moteurs et le thème.
- Le résultat de la [couverture du site](#couverture-du-site).
- **Afficher les détails**, qui liste les prompts que la requête a suivis sous **Apparaît après ces prompts**, avec un lien **Voir la réponse** pour chaque prompt. Les derniers mots du moteur y figurent aussi.

## Comment les nouvelles requêtes sont triées

La première fois qu'une nouvelle requête apparaît, Hi, Moose vérifie si elle est assez précise et assez proche du sujet pour être suivie. Il vérifie aussi si elle a le même sens qu'une requête déjà présente dans la liste. Les requêtes qui ont le même sens sont comptées ensemble. Les requêtes génériques, comme « dites-m'en plus », sont écartées.

Ce tri a lieu à l'ouverture de l'onglet. La première fois que vous l'ouvrez après une exécution, l'onglet affiche **Tri des nouvelles requêtes : X sur Y**.

## Couverture du site

Chaque requête est vérifiée une fois par rapport aux pages explorées du site de votre projet. La ligne affiche ensuite l'un de ces résultats :

- **Couverte sur le site :** suivi de la page.
- **Couverte en partie sur le site :** suivi de la page.
- **Non couverte sur le site**.

La couverture est vérifiée de nouveau lorsqu'une nouvelle exploration du site se termine.

La vérification nécessite une exploration du site terminée sur votre appareil, ou sur l'appareil qui héberge l'index du site. Sans exploration terminée, la ligne affiche **Couverture du site non vérifiée**. Dans l'application web sans appareil de bureau hôte, la couverture n'est pas vérifiée.

## Boutons de chaque ligne

- **Ajouter aux prompts suivis** ajoute la requête comme prompt surveillé sous le même thème que le prompt qu'elle a suivi. Le bouton indique ensuite **Suivi**.
- **Créer un brouillon** s'affiche lorsque votre site ne couvre pas la requête. Il ouvre un nouveau chat avec le formulaire du [brief de contenu](../features/content-briefs.md) déjà rempli.
- **Mettre à jour cette page** s'affiche lorsque votre site couvre la requête en partie. Il ouvre le formulaire de mise à jour de contenu pour cette page, avec la requête comme cible.
- **Ignorer** masque la ligne. **Afficher les requêtes ignorées** fait réapparaître les lignes ignorées et **Rétablir** remet une ligne dans la liste.

## Quand la liste se met à jour

Tant que l'option est activée, les nouvelles requêtes sont relevées dans chaque réponse à chaque exécution de visibilité. Elles sont triées à la prochaine ouverture de l'onglet.

Comme l'onglet suit la période sélectionnée, une requête ne figure plus dans la liste lorsqu'aucune réponse de cette période ne la contenait. Choisissez une période plus longue pour la revoir.

## Équipes et forfaits

Avec les forfaits gérés payants, les requêtes relevées, les requêtes ignorées et les résultats de couverture sont synchronisés avec le cloud, si bien que les membres de l'équipe voient la même liste. Avec BYOK Premium et BYOK Agency, tout reste sur votre appareil.

## Ce qui n'est pas inclus

- Les questions « Related » de Perplexity et les questions « People also ask » de Google ne sont pas relevées.
- Les requêtes de second tour ne font pas partie du [rapport exécutif PDF](overview.md#exporter).
- Les requêtes de second tour ne sont pas disponibles via les outils de [Hi, Moose MCP](../integrations/hi-moose-mcp.md).
