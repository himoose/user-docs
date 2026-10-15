---
source_hash: 44a098b9f501f2117290c2037c5635c5aa9f250b49d72a34e103dba9d3cb8b5b
---

# Dépannage

Que faire quand Hi, Moose MCP ne répond pas comme vous l'attendez. La plupart des problèmes viennent de l'appareil hôte : l'ordinateur où Hi, Moose reste ouvert et exécute le travail.

## « L'appareil hôte de ce projet ne s'est pas signalé »

L'ordinateur choisi comme appareil hôte est éteint, en veille, hors ligne, ou Hi, Moose y est fermé ou déconnecté.

1. Ouvrez Hi, Moose sur cet ordinateur et connectez-vous.
2. Attendez une minute et redemandez. L'hôte se signale toutes les quelques minutes tant que Hi, Moose est ouvert.
3. Si l'ordinateur n'est plus disponible, choisissez-en un autre sous **Paramètres → Hi, Moose MCP**. Seul le propriétaire du compte peut changer l'appareil hôte.

Les tâches attendent l'appareil hôte jusqu'à 15 minutes. Passé ce délai, elles expirent et l'application reçoit un message qui le signale ; redemandez une fois l'hôte de retour.

## « Ce projet n'a pas d'appareil hôte »

Personne n'a encore choisi d'appareil hôte pour le projet. Ouvrez Hi, Moose sur l'ordinateur qui doit exécuter le travail, allez dans **Paramètres → Hi, Moose MCP** et choisissez-le. Chaque projet a son propre appareil hôte, donc un nouveau projet a aussi besoin qu'on lui en choisisse un.

## L'application dit que le travail est toujours en cours

Les briefs, brouillons, audits et épisodes audio prennent plusieurs minutes, et certaines applications cessent d'attendre avant la fin du travail. Demandez à l'application de vérifier à nouveau ; elle récupère le résultat avec l'identifiant de tâche qu'elle a reçu. Le travail est aussi enregistré dans votre [Library](../../library/overview.md) dans Hi, Moose, donc rien n'est perdu si la conversation avance.

L'audio est le plus long : environ 5 minutes pour un épisode court, 9 pour standard et 15 pour approfondi. L'appareil hôte ne travaille sur rien d'autre pendant ce temps, donc une seconde demande attend derrière.

## L'application a choisi le mauvais projet

Les outils prennent le projet par son nom. Dites-le dans la demande, par exemple « pour le projet Acme », ou demandez à l'application de lister d'abord les projets puis de choisir. Si deux projets ont des noms proches, utilisez exactement celui affiché dans Hi, Moose.

## Le connecteur ne se connecte pas

- **La page de connexion ne s'ouvre jamais.** Vérifiez que l'adresse du serveur est `https://mcp.himoose.com/mcp`, sans caractère en trop, et que l'application utilise OAuth, pas une clé API.
- **Le code de connexion a expiré.** Le code est valable deux minutes. Relancez la connexion depuis l'application.
- **Claude Team ou Enterprise.** Un propriétaire doit ajouter le connecteur pour l'organisation avant que les membres puissent se connecter.
- **ChatGPT.** Les serveurs MCP personnalisés demandent une offre payante, et dans les espaces Business et Enterprise un propriétaire doit parfois d'abord autoriser les connecteurs personnalisés ou activer le Mode développeur. Les noms des menus changent ; voir [Connecter dans ChatGPT](../hi-moose-mcp.md#connect-in-chatgpt).

## L'application était connectée et ne l'est plus

L'accès expire de lui-même après 30 jours sans utilisation, et le propriétaire du compte peut révoquer une application sous **Paramètres → Hi, Moose MCP**. Reconnectez-vous depuis l'application.

## Les résultats semblent dépassés

- **La couverture du site et les liens internes** lisent la dernière exploration de votre site et nomment sa date. Les pages publiées depuis ne sont pas incluses. Lancez une exploration dans Hi, Moose et redemandez.
- **La visibilité et les opportunités** lisent uniquement les résultats enregistrés et ne lancent jamais de nouvelles vérifications. Elles couvrent les prompts suivis sur les moteurs suivis pendant la période nommée dans la réponse. Pour voir un nouveau sujet, ajoutez un prompt pour celui-ci sur l'écran Visibilité et laissez une exécution avoir lieu.

## Quelque chose s'est exécuté sans que vous l'attendiez

Le tableau **Tâches récentes des agents** sous **Paramètres → Hi, Moose MCP** liste chaque tâche : ce qui a été demandé, par quelle application, quand, et si elle est terminée. Les tâches s'exécutent avec le compte connecté sur l'appareil hôte, donc une application connectée ne peut lire et écrire que la Library de ce compte.

## Toujours bloqué

Écrivez au support avec le nom du projet, l'application que vous utilisiez, le moment approximatif et ce que l'application a répondu. Le tableau des tâches des agents aide aussi.
