---
source_hash: 5b66e35e4cc4b5ac9c7567edd481631bcbd56d2ff1ca7f0d3e2f1b0c1fbbd5c3
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/integrations/hi-moose-mcp/)

# Hi, Moose MCP

## À quoi ça sert

Hi, Moose MCP permet aux applications d'IA dans lesquelles vous travaillez déjà d'utiliser Hi, Moose. Ajoutez-le comme connecteur MCP dans Claude, ChatGPT ou toute autre application compatible MCP avec connexion, connectez-vous avec votre compte Hi, Moose et demandez du travail à Hi, Moose depuis cette application. MCP (Model Context Protocol) est le standard que ces applications utilisent pour se connecter à des outils externes.

Le travail s'exécute sur l'un de vos propres appareils, l'**appareil hôte**, où Hi, Moose reste ouvert et connecté. Les résultats reviennent dans l'application et sont enregistrés dans votre [Library](../library/overview.md).

## Ce qu'une application connectée peut faire

Avec les outils actuels, une application connectée peut :

- Lister vos projets Hi, Moose
- Lister les briefs et brouillons enregistrés dans votre Library
- Vérifier si votre site couvre déjà un sujet, avec les pages qui le couvrent et la date de l'exploration vérifiée
- Créer un brief de contenu
- Rédiger un brouillon à partir d'un brief
- Créer une image à la une
- Rédiger une FAQ avec le balisage FAQPage pour un brouillon enregistré ou une page de votre site
- Rédiger les points clés d'un brouillon enregistré ou d'une page de votre site
- Lancer un audit AEO d'une page en ligne, d'un brouillon enregistré ou d'un texte collé, avec scores, problèmes et corrections proposées
- Récupérer un travail terminé

Elle ne peut pas modifier les réglages ni les membres de l'équipe, et ne peut rien supprimer. D'autres outils arrivent.

## Avant de commencer

1. Ouvrez Hi, Moose sur l'appareil qui doit exécuter le travail et connectez-vous.
2. Allez dans **Réglages → Hi, Moose MCP** et choisissez cet appareil comme appareil hôte du projet. Seul le propriétaire du compte peut choisir l'appareil hôte.
3. Copiez l'adresse du serveur affichée à cet endroit :

```
https://mcp.himoose.com/mcp
```

## Connecter dans Claude

Dans Claude.ai et l'application de bureau Claude :

1. Ouvrez **Réglages → Connecteurs** (aussi accessible à claude.ai/customize/connectors).
2. Choisissez **Ajouter un connecteur personnalisé**, collez l'adresse du serveur et cliquez sur **Ajouter**. Laissez vides les champs du client OAuth.
3. Cliquez sur **Connecter** à côté de Hi, Moose MCP. Une page Hi, Moose s'ouvre, montre ce que l'application pourra faire et vous demande de vous connecter avec votre compte Hi, Moose.
4. Démarrez une nouvelle conversation et demandez par exemple : « Liste mes projets Hi, Moose ».

Sur les offres Team et Enterprise, un propriétaire ajoute d'abord le connecteur pour l'organisation, puis chaque membre se connecte.

Dans Claude Code :

```
claude mcp add --transport http himoose https://mcp.himoose.com/mcp
```

Lancez ensuite `/mcp` dans Claude Code et suivez la connexion.

## Connecter dans ChatGPT

ChatGPT prend en charge les serveurs MCP personnalisés dans ses offres payantes. Les noms des menus changent de temps en temps ; voici le chemin actuel.

1. Ouvrez **Réglages → Apps** (appelé **Connecteurs** dans certaines versions). Dans les espaces Business et Enterprise, un propriétaire doit parfois d'abord autoriser les connecteurs personnalisés.
2. Choisissez **Ajouter**, puis **Créer un serveur MCP personnalisé**. Les anciennes versions affichent **Créer une app MCP** et peuvent exiger d'abord le **Mode développeur** dans les réglages avancés.
3. Collez l'adresse du serveur, choisissez **OAuth** comme authentification et enregistrez.
4. Connectez-vous avec votre compte Hi, Moose sur la page qui s'ouvre.
5. Dans une conversation, activez le connecteur pour cette conversation et demandez du travail à Hi, Moose.

## Autres applications

Toute application capable d'ajouter un serveur MCP distant avec connexion OAuth fonctionne de la même façon : ajoutez l'adresse du serveur, connectez-vous avec votre compte Hi, Moose et utilisez-le depuis là.

## Comment une demande s'exécute

1. L'application envoie votre demande à Hi, Moose MCP.
2. Hi, Moose MCP la transmet à l'appareil hôte, qui exécute le travail avec l'exploration, le Brand Truth et la recherche du projet.
3. Le résultat revient dans l'application et est enregistré dans votre Library.

Un brief, un brouillon, une image, une FAQ ou une liste de points clés prend une à trois minutes, un audit AEO deux à quatre. Si l'application dit que le travail est toujours en cours, demandez-lui de vérifier à nouveau ; elle récupère le résultat dès qu'il est prêt. Si l'appareil hôte est éteint ou déconnecté, l'application reçoit un message qui le signale.

Les tâches s'exécutent avec le compte connecté sur l'appareil hôte : la Library qu'elles lisent et écrivent est donc celle de ce compte. Le tableau **Tâches récentes des agents** dans les Réglages montre ce qui a été demandé, par quelle application, et si c'est terminé.

## Déconnecter une application

Allez dans **Réglages → Hi, Moose MCP**. Le tableau **Applications connectées** liste chaque application connectée à votre compte. **Révoquer** déconnecte cette application. Cela peut prendre jusqu'à une minute, et l'application pourra se reconnecter plus tard. L'accès expire aussi de lui-même après 30 jours sans utilisation.
