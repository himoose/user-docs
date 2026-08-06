---
source_hash: 67912e0c53e927d4836f8b9c545fb59268db0fbc9165037df2930f6cfada0988
---
# Webflow

## À quoi cela sert

Connecter un site Webflow pour que Hi, Moose puisse inspecter ses pages et son contenu, et préparer des modifications prévisualisables en vue de leur publication : FAQ, key points, brouillons issus de briefs et recommandations d'AEO audits.

## Configurer une connexion

1. Ouvrez **Connexions** dans l'application de bureau et choisissez Webflow.
2. Cliquez sur **Connecter le MCP Webflow**. La page d'autorisation de Webflow s'ouvre dans votre navigateur. Terminez-y le processus OAuth pour finaliser la connexion.
3. Une fois connecté, choisissez quel site Webflow autorisé Hi, Moose doit utiliser pour ce [projet](../getting-started/projects.md).

## Préparer une cible d'aperçu

Hi, Moose peut découvrir des **surfaces de contenu** sur votre site Webflow connecté : pages, articles, éléments de collection et code personnalisé, ainsi qu'un gabarit de page vierge pour du contenu qui n'existe pas encore. Choisissez une cible, ajoutez des notes sur la modification ou l'intention de publication, et préparez-la comme cible d'aperçu. Vous relisez ensuite le brouillon préparé comme avec n'importe quelle autre connexion. Voir [Brouillons, aperçu et publication](../features/drafts-and-publishing.md).

## Aptitude à l'aperçu et à la publication

Toutes les connexions Webflow ne peuvent pas encore tout faire. Hi, Moose signale l'un de plusieurs états pour votre site connecté : prêt à la fois pour préparer des aperçus et pour publier, aperçu uniquement, publication uniquement, ou connecté mais pas encore prêt pour l'un ni l'autre. Les surfaces réservées au Designer (modifications nécessitant directement le Webflow Designer) ne sont pas encore prises en charge.

## Publier dans les collections

Lorsque vous publiez dans une collection, Hi, Moose charge d'abord les autres champs obligatoires de cette collection et vous demande de les renseigner, afin qu'une publication n'échoue pas en cours de route sur un champ que vous ne pouviez pas voir.

## Sécurité

L'autorisation Webflow s'effectue via votre navigateur, et la connexion qui en résulte n'est utilisée que par le processus d'arrière-plan de l'application de bureau ; elle n'est pas exposée à l'interface utilisateur.
