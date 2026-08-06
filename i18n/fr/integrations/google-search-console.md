---
source_hash: 07b1b5e8bf746dc48362fa004a86b7566ef960fafcbe265cebb6ecd32d7aff91
---
# Google Search Console

## À quoi cela sert

Connecter Google Search Console pour que Hi, Moose puisse intégrer vos données de performance de recherche Google (impressions, clics et requêtes) à la même base de preuves locale que celle utilisée par [Visibility](../visibility/overview.md), les [AEO audits](../features/aeo-audits.md) et les [briefs de contenu](../features/content-briefs.md).

!!! note "Disponibilité"
    La connexion à Google Search Console est incluse dans tous les forfaits payants : BYOK Premium, BYOK Agency et tous les forfaits gérés. Elle n'est pas incluse dans BYOK Free ni dans Preview Mode. Voir [Types de compte et forfaits](../getting-started/account-modes.md).

## Pourquoi cela reste en local

L'accès à Search Console nécessite les identifiants OAuth de votre compte Google, et Hi, Moose les traite comme sensibles par conception : l'autorisation s'effectue dans votre navigateur et les jetons obtenus sont stockés **uniquement sur votre machine**. Les services cloud de Hi, Moose ne reçoivent jamais vos jetons d'accès, vos jetons de rafraîchissement ni vos secrets client Google pour cette connexion : l'application de bureau est la seule à dialoguer avec Google Search Console en votre nom.

## Configurer une connexion

1. Ouvrez **Connections** dans l'application de bureau et choisissez Google Search Console.
2. Autorisez l'accès dans votre navigateur.
3. Rattachez une propriété Search Console au [projet](../getting-started/projects.md) actif.

## Ce que vous pouvez en faire

- Récupérer un instantané local des performances par page et par requête pour la propriété rattachée.
- Comparer le dernier instantané à une période antérieure pour repérer les changements significatifs.
- Interroger vos données Search Console directement dans le chat. Moose les interroge de façon agentique, en affinant à travers plusieurs requêtes pour répondre à une question vague, au lieu d'exécuter un rapport figé. Le modèle interprète votre question, mais c'est l'application de bureau qui valide et exécute chaque requête sous-jacente en local : vos données et la garde de vos jetons restent donc sur l'appareil.
- Alimenter le diagnostic de visibilité avec les preuves Search Console et hiérarchiser les pages méritant un brief de contenu ou une AEO audit.

## Où résident les données

Les données Search Console intégrées à Hi, Moose sont stockées **en local sur votre appareil**, et non dans le cloud de Hi, Moose. Elles font partie de votre base de preuves locale et sont incluses dans une [sauvegarde locale](../getting-started/settings.md#data-backup) plutôt que synchronisées entre machines.

## Portée actuelle

Cette connexion est en lecture seule dans la version 1 : Hi, Moose n'écrit pas dans Search Console. Une seule propriété peut être rattachée par projet pour le moment.

Search Console nécessite un forfait payant. Elle n'est incluse ni dans Preview Mode ni dans BYOK Free.

!!! note "Mettez l'application à jour si la connexion échoue sous Windows"
    Les programmes d'installation Windows antérieurs à la v0.3.245 étaient livrés sans les identifiants Google nécessaires à la connexion : celle-ci échouait donc systématiquement dans l'application installée. La mise à jour corrige le problème.
