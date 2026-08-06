---
source_hash: 57477f3edd7e63b53a23c12a7676c0c723e2f37903e1f4aa75a613f296e8277b
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/integrations/wordpress/)

# WordPress

## À quoi cela sert

Connecter un site WordPress à Hi, Moose pour que l'application de bureau puisse préparer et appliquer directement des modifications de contenu (FAQ, key points, brouillons issus de briefs et recommandations d'AEO audits), avec une étape d'aperçu et une étape d'approbation avant toute mise en ligne.

## Comment fonctionne la connexion

L'application de bureau est le côté actif de cette connexion : elle identifie l'article cible, récupère son contenu actuel, construit la modification proposée en local et appelle directement les points d'accès REST de votre site WordPress en HTTPS pour préparer la modification. Votre site WordPress reste passif : il expose un point d'accès qui attend d'être appelé et n'a jamais besoin de contacter Hi, Moose de lui-même.

Cela signifie que :

- Le jeton de votre site et vos identifiants de connexion ne sont jamais détenus par l'interface utilisateur, uniquement par le processus d'arrière-plan de l'application de bureau.
- Sur les forfaits BYOK, les étapes de modèle local intervenant dans la préparation d'une modification (comme repérer la section exacte de contenu à remplacer) s'exécutent avec votre propre clé OpenRouter, et non via un appel hébergé par Hi, Moose.

## Configurer une connexion

1. Ouvrez **Connexions** dans l'application de bureau et choisissez WordPress.
2. Téléchargez le plugin connecteur, installez-le dans votre administration WordPress, puis collez l'URL de votre site et la clé d'API de ce projet dans les réglages du plugin.
3. De retour dans Hi, Moose, enregistrez la connexion et vérifiez que le connecteur signale un ping réussi depuis votre site.

## Environnements

Chaque installation WordPress que vous connectez (production, préproduction ou les deux) constitue un **environnement** distinct, avec son propre jeton de site et son propre secret HMAC, totalement isolés l'un de l'autre. Choisissez l'environnement cible par défaut des nouvelles modifications et basculez de l'un à l'autre à tout moment. Si un site de préproduction est protégé par une authentification HTTP Basic, vous pouvez enregistrer ces identifiants pour cet environnement précis afin que Hi, Moose puisse y accéder.

## Correctifs

Chaque modification WordPress, qu'elle provienne des [FAQ](../features/faq-generator.md), des [key points](../features/key-points.md), d'un [brouillon](../features/drafts-and-publishing.md) ou d'un remplacement de texte manuel que vous créez vous-même, est suivie comme un **correctif** : une entrée de registre locale, propre à chaque environnement, avec son propre statut.

Un correctif passe par des états explicites : **Brouillon**, **En préparation**, **Appliqué**, **Abandonné**, **Restauré** ou **Failed**. Depuis la liste des correctifs, vous pouvez :

- **Préparer** un correctif sur votre site WordPress pour l'aperçu.
- **Appliquer** un correctif préparé pour le mettre en ligne.
- **Écarter** un correctif que vous ne souhaitez pas utiliser.
- **Annuler** un correctif appliqué.
- **Promouvoir** un correctif vers un autre environnement (de la préproduction vers la production, par exemple) pour l'y préparer à nouveau et le relire.

Une fois un brouillon envoyé, Hi, Moose s'en souvient : vous ne pouvez donc pas envoyer le même plusieurs fois par inadvertance.

## Plugin Listen to this Article

Le plugin WordPress **Listen to This Article**, distinct, intègre le lecteur audio et la transcription générés par [Audio](../audio/overview.md) dans l'application de bureau. Installez-le depuis [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/), ou collez directement le code d'intégration dans votre article. Voir [Lecteur et intégration](../audio/player-and-embed.md).

## Prérequis

- WordPress 6.0 ou supérieur, avec un accès administrateur pour installer la connexion sur votre site.
- Un projet configuré dans l'application de bureau.
