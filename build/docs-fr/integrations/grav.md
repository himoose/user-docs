---
source_hash: 1d027fe8d7c0bf155818720c05a7777b1744c302a9ab057860377dc301df1947
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/integrations/grav/)

# Grav

## À quoi cela sert

Connecter un site [Grav](https://getgrav.org) en production via le plugin Hi, Moose pour Grav, afin que l'application de bureau puisse inspecter le contenu Grav et exécuter directement des actions distantes de création, mise à jour, publication et annulation.

## Installer le plugin

1. Depuis **Connexions → Grav** dans l'application de bureau, ouvrez le lien de téléchargement et récupérez l'archive ZIP du plugin Hi, Moose. La version actuelle est la **0.1.1** et elle nécessite Grav 1.7.0 ou supérieur.
2. Dans votre administration Grav, ouvrez **Plugins**, envoyez le ZIP et terminez l'installation.
3. Activez le plugin, puis ouvrez ses réglages dans l'administration Grav.
4. Copiez le lot de connexion qui s'y affiche : vous le collerez dans Hi, Moose à l'étape suivante.

## Se connecter dans Hi, Moose

1. Ouvrez **Connexions** dans l'application de bureau et choisissez Grav.
2. Saisissez l'URL de votre site Grav.
3. Laissez la route du connecteur vide, sauf si votre plugin Grav utilise une route non standard. Sinon, Hi, Moose utilise la route du lot de connexion ou se rabat sur `/himoose-connector`.
4. Collez le lot de connexion copié depuis le plugin, puis enregistrez.
5. Cliquez sur **Tester le connecteur** pour valider la connexion avec votre site Grav en production.

## État de la connexion

Après le test, Hi, Moose signale l'un de plusieurs états : le connecteur n'est pas encore entièrement configuré, il est enregistré mais pas encore validé, il a répondu mais les actions distantes d'écriture ne sont pas pleinement activées (lecture seule), il est entièrement prêt pour la lecture et l'écriture distante, ou la dernière validation a échoué et les réglages du site ou les secrets du plugin demandent votre attention.

## Ce que la connexion permet

Une fois prête, le connecteur Grav peut lister le contenu, lire le contenu brut, et créer, mettre à jour et publier du contenu directement, en suivant le même parcours préparé et relisible que celui employé par [Brouillons, aperçu et publication](../features/drafts-and-publishing.md) pour les autres connexions.

## Sécurité

L'URL de votre site Grav et le lot de connexion sont enregistrés en local et accessibles uniquement au processus d'arrière-plan de l'application de bureau ; ils ne sont jamais exposés à l'interface utilisateur.
