---
source_hash: 9705deb0dc37b51cf84f956088049d0d7d87b416de55439c84ef17b2ef0d3d9c
---
# Inbox

## À quoi cela sert

L'Inbox est l'endroit où Hi, Moose fait remonter ce qui mérite votre attention : constats triés, audits et événements de publication, chacun rattaché à un artefact réel plutôt qu'à une notification générique. Il transforme des signaux dispersés (variations de sentiment dans la visibilité, écarts narratifs, inexactitudes de parité fonctionnelle, résultats d'AEO audits, issues de publication et demandes d'approbation) en une file de travail unique et hiérarchisée.

## Ce qui apparaît dans l'Inbox

Chaque élément de l'Inbox renvoie à quelque chose de concret que vous pouvez ouvrir et traiter :

- **Signaux de visibilité** : sentiment négatif ou mitigé détecté dans une réponse d'IA, écart narratif ou inexactitude de parité fonctionnelle par rapport à votre [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), ou [exécution de visibilité](../visibility/overview.md) terminée ou en échec.
- **Résultats d'AEO audits** : un audit terminé, ou un audit dont le plan d'action a fait ressortir une recommandation prioritaire.
- **Détections de changements sur le site** : un récapitulatif unique par exploration de [site monitoring](../site-monitoring/overview.md), qui s'ouvre sur un tableau de toutes les pages modifiées avec leur niveau d'impact. Les pages inaccessibles et les pannes générales du site sont signalées comme des types de changement distincts.
- **Rapports de workflows** : résultats de l'exécution d'un [workflow](../workflows/overview.md), par exemple une analyse planifiée qui a généré de nouveaux articles ou signalé une opportunité dans la recherche par IA.
- **Événements de publication** : une publication **en échec**, ou une modification en attente de votre approbation. Les publications réussies ne créent plus d'élément dans l'Inbox, car un mur d'avis « cela a fonctionné » finit par enterrer ceux qui exigent votre attention.
- **Un message de bienvenue** de Moose à la fin du parcours d'accueil, qui vous suggère une première action sensée.

Chaque élément propose une action suivante lorsque cela a du sens (ouvrir l'artefact, lancer un brief, donner suite à un audit, relire un brouillon, approuver une modification ou relancer une exécution en échec) : vous ne lisez pas seulement une notification, vous êtes à un clic d'agir.

Les récapitulatifs de site monitoring comportent en outre une action **Ask Moose about all of this** qui transmet l'instantané de l'exploration au [chat](../chat/overview.md) et lui demande par quoi commencer.

## Filtrer l'Inbox

Deux filtres déterminent ce que vous voyez :

- **Statut** : la valeur par défaut est **Active**, c'est-à-dire tout ce qui n'a pas été écarté (éléments ouverts, en cours et terminés). Basculez sur un statut précis, ou sur **All** pour inclure les éléments écartés que vous souhaiteriez rouvrir.
- **Sévérité** : **Critical**, **Warning**, **Notice**, **Info**, ou toutes.

Les éléments sont regroupés par date (par exemple « Hier », « Plus anciens ») avec un compteur par groupe, pour voir rapidement ce qui vous attend. Les boîtes volumineuses sont paginées plutôt que chargées d'un seul bloc.

**Tout marquer comme lu** efface le compteur sur l'ensemble de votre Inbox, et pas seulement sur la page affichée.

!!! note "L'Inbox conserve ses 200 éléments les plus récents"
    Les plus anciens sont purgés automatiquement. L'Inbox est une file de travail, pas une archive : tout ce qui est durable se trouve dans la [Library](../library/overview.md) ou dans l'artefact vers lequel l'élément pointe.

## Choisir ce qui vous alerte

Cliquez sur **Notifications** pour ouvrir vos préférences de notification par projet. Voir [Notifications de l'Inbox](notifications.md) pour le détail de chaque réglage.

## Géré et BYOK

L'Inbox fonctionne de la même manière que votre espace de travail soit géré ou BYOK : les éléments sont écrits par le côté qui a réellement généré l'événement sous-jacent (le cloud pour les workflows gérés, le processus local de bureau pour BYOK), et vous voyez dans les deux cas une file unifiée.
