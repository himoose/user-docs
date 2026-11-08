---
source_hash: 0a9a56ce00908be9642b519b71a66ed53535f416da94c0f65e7bb741595259e0
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/getting-started/settings/)

# Paramètres

## À quoi cela sert

Les Paramètres vous permettent de gérer votre profil, votre forfait, vos modèles, votre équipe et le comportement de l'application sur cet ordinateur. Ils sont organisés en sections dans la colonne de gauche ; quelques-unes n'apparaissent que pour le propriétaire du compte ou sur les forfaits payants.

| Section | Contenu |
|---|---|
| Général | Informations de profil et comportement de l'application sur cet ordinateur |
| Utilisation | Solde de crédits et date de réinitialisation |
| Compte | E-mail, mot de passe, forfait, clé OpenRouter |
| IA locale | Téléchargement et activation du modèle sur l'appareil |
| Équipe | Sièges, invitations, rôles |
| [Surveillance du site](../site-monitoring/overview.md) | Planification de l'exploration, index de recherche, pages surveillées, chemins bloqués |
| [Image de marque](../agency/white-label.md) | Rapports en marque blanche et attribution audio (forfaits payants uniquement) |
| Connexions aux comptes | Les sites où Moose est connecté pour les exécutions de visibilité et Send Moose |
| [Hi, Moose MCP](../integrations/hi-moose-mcp.md) | Appareil hôte, modèle pour les tâches de rédaction, applications connectées, tâches récentes |
| [API REST Hi, Moose](../integrations/developer-api.md) | Clés d'API et webhooks (propriétaire uniquement) |
| Journaux | Journaux d'actions et export CSV (propriétaire uniquement) |
| Données et sauvegarde | Sauvegarde et restauration locales |
| Historique de visibilité | La copie locale de vos réponses de recherche IA et son budget d'espace |
| Dépannage | Cache, journal de diagnostic, réinitialisation des données locales |

## General

**Informations de profil** : votre nom d'usage, votre fonction et votre localisation. Elles personnalisent l'application et clarifient l'attribution du travail partagé.

**Comportement de l'application** contrôle la manière dont Hi, Moose s'exécute sur cet ordinateur :

- **Lancer Hi, Moose à l'ouverture de session** : après un redémarrage, l'application s'ouvre discrètement en arrière-plan pour que le travail planifié continue de s'exécuter. Vous pouvez ouvrir la fenêtre à tout moment depuis la barre d'état système ou la barre de menus.
- **Partager des statistiques d'usage anonymes** : envoie des événements anonymes et agrégés (fonctionnalités utilisées, version de l'application, erreurs) afin que nous puissions améliorer le produit. Ne sont jamais envoyés votre contenu, vos prompts, vos clés ni les sites que vous analysez, et votre adresse IP est écartée. Vous pouvez désactiver cette option à tout moment.

## Usage

Sur les forfaits gérés, cette section affiche votre solde de crédits et ce qu'il reste pour le mois.

!!! note "Le mois est calculé en UTC"
    Les crédits sont réinitialisés au début de chaque mois en UTC, et non dans votre fuseau horaire. Les Paramètres affichent la date correspondante chez vous : tard le dernier jour du mois, la réinitialisation peut donc sembler en avance.

Les forfaits BYOK ne consomment pas de solde de crédits Hi, Moose pour l'inférence, puisque la génération s'exécute avec votre propre clé. Le coût des modèles est réglé directement à OpenRouter.

## Compte

- Modifiez votre adresse e-mail, vérifiez-la et réinitialisez votre mot de passe sur les comptes e-mail et mot de passe. Les comptes Google sont gérés via Google.
- Les changements d'adresse e-mail attendent votre confirmation par lien avant de prendre effet, puis votre session dans l'application est mise à jour.
- Consultez votre forfait actuel et changez-en. Voir [Types de compte et forfaits](account-modes.md).

### Ajouter votre clé d'API OpenRouter

Sur les forfaits BYOK, ajoutez ici votre clé [OpenRouter](https://openrouter.ai). Hi, Moose valide la clé avant d'y basculer le routage de l'IA. Une fois ajoutée :

- Les fonctionnalités d'IA s'exécutent en local, dans l'application de bureau, avec votre clé
- Vous choisissez les modèles pris en charge à utiliser pour le chat et la génération
- Votre clé et vos prompts ne transitent jamais par les serveurs de Hi, Moose pour l'inférence BYOK

La clé est enregistrée par compte et non par appareil : elle vous suit lors d'une nouvelle installation.

## Local Model

Téléchargez et activez un modèle approuvé sur l'appareil, comme Gemma 4. Les réponses d'un modèle local sont générées sur votre machine, sans les modèles gérés de Hi, Moose ni votre clé OpenRouter, et son usage est gratuit. Par défaut, le chat utilise une courte étape de routage dans le cloud pour choisir le bon outil pour chaque message, et envoie pour cela le texte du message à un service de routage cloud. Désactivez **Routage intelligent** dans **Paramètres → IA locale** pour que cette étape reste aussi sur votre appareil.

Les modèles locaux sont disponibles sur tous les forfaits et sont **obligatoires** sur Preview Mode pour les [AEO audits](../features/aeo-audits.md) et le scoring de visibilité.

!!! note "La taille du contexte s'adapte à votre RAM"
    Hi, Moose dimensionne la fenêtre de contexte du modèle selon la mémoire disponible sur votre machine : un même modèle utilise donc une fenêtre plus petite sur un portable de 16 Go que sur une station de travail plus puissante.

## Équipe

Invitez des membres, consultez leurs rôles et révoquez des accès. Les limites de sièges dépendent de votre forfait. Consultez [Gestion de l'équipe](team-management.md) pour le parcours complet.

## Site Monitoring

Planification de l'exploration, index de recherche local, pages surveillées et chemins bloqués. C'est un domaine à part entière, qui dispose de sa propre page : **[Surveillance du site](../site-monitoring/overview.md)**.

Les connexions aux CMS et aux sources de données sont distinctes et se trouvent dans l'écran **Connexions**, et non dans les Paramètres :

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

Appliquez votre marque blanche aux rapports PDF exportés et aux lecteurs audio intégrés. Disponible sur tous les forfaits payants et modifiable par le titulaire de l'abonnement. Voir **[Marque blanche](../agency/white-label.md)**.

## Connexions aux comptes

Moose utilise son propre navigateur pour les exécutions de visibilité en interrogation locale et pour Send Moose. Cette section liste les sites où il peut être connecté, regroupés en moteurs de réponse IA (ChatGPT, Google AI Mode et Gemini, Grok, Perplexity, Bing Copilot) et en sites utilisés par les agents de Send Moose (Reddit, LinkedIn, X), chacun avec un badge **Connecté** ou **Non connecté**. Ouvrez un site ici et connectez-vous une fois ; chaque exécution suivante reprend la session. Se connecter supprime aussi les vérifications « confirmez que vous êtes humain » que les moteurs affichent lors des premières exécutions. Les connexions restent sur cet ordinateur et ne vont jamais dans le cloud.

Le badge est une estimation à partir des cookies de chaque site. Si une exécution vous demande encore de vous connecter, ouvrez le site ici et reconnectez-vous.

Une boîte de **messagerie web** peut être ajoutée pour Send Moose, afin que Moose puisse lire les liens de confirmation pendant qu'il travaille sur une tâche. Il n'envoie, ne répond, ne supprime ni ne modifie jamais de réglages. Utilisez une boîte créée pour Moose et gardez votre messagerie personnelle à part.

## Hi, Moose MCP

Connectez Claude, ChatGPT ou toute autre application MCP à votre compte Hi, Moose, choisissez l'appareil hôte qui exécute le travail, choisissez le **modèle pour les tâches de rédaction** et consultez les applications connectées et les tâches récentes. Voir **[Hi, Moose MCP](../integrations/hi-moose-mcp.md)**.

## API REST Hi, Moose

Cette section n'apparaît que pour le propriétaire du compte. Créez et révoquez les clés d'API qui lisent vos données de visibilité enregistrées depuis vos propres tableaux de bord et rapports, choisissez ce que chaque clé peut faire (lire les données de visibilité, gérer le suivi, lancer des exécutions) et consultez ou supprimez les webhooks enregistrés pour le projet. Voir **[API Hi, Moose](../integrations/developer-api.md)**.

## Logs

Journaux d'actions du projet en cours, avec le type, l'utilisateur, la date, le statut et les métadonnées de chaque action enregistrée. Sur les forfaits gérés, les journaux partagés de l'équipe se synchronisent aux côtés de vos journaux locaux.

**Exporter en CSV** les télécharge. L'export des journaux d'actions de l'équipe est réservé aux titulaires d'espaces de travail gérés payants.

## Data & Backup

Créez une sauvegarde compressée `.hmbk` de votre historique sur l'appareil, et importez-la ultérieurement pour le restaurer.

**Les sauvegardes comprennent** les enregistrements de la base de données locale et les planifications de visibilité BYOK enregistrées : vos briefs, audits, aperçus, historique de site monitoring, état de l'Inbox et autres artefacts de travail non sensibles restent donc portables.

**Les sauvegardes ne comprennent pas** l'état de session, les identifiants de connecteurs, les clés d'API, les fichiers de modèles locaux ni les pièces jointes.

!!! warning "L'import écrase définitivement les données locales"
    Un import remplace les données locales Hi, Moose de cet appareil par le contenu de la sauvegarde. La boîte de dialogue de confirmation vous indique combien d'enregistrements seront restaurés et à quelle date la sauvegarde a été créée. Redémarrez ensuite l'application pour que tous les écrans se rechargent à partir des données restaurées.

Les imports n'acceptent que les fichiers `.hmbk` exportés par l'application de bureau Hi, Moose.

## Historique de visibilité

Hi, Moose conserve sur cet ordinateur une copie de vos réponses de recherche IA pour que la page Visibility puisse afficher n'importe quelle période sans la retélécharger. Cette section indique l'espace occupé par la copie du projet en cours et les dates qu'elle couvre, ainsi qu'un **budget d'espace** : quand la copie dépasse cette taille, les jours les plus anciens sont supprimés de cet ordinateur seulement, et ils reviennent depuis le cloud quand vous choisissez une période qui en a besoin. Sur les forfaits sans copie cloud, rien n'est supprimé automatiquement ; sauvegardez plutôt les réponses dans Données et sauvegarde.

## Troubleshooting

Trois outils de récupération. Tous n'affectent que l'état local du bureau et ne touchent jamais aux données du cloud.

**Vider le cache temporaire** : efface le cache HTTP, les service workers et les autres états jetables. Conserve votre session et votre historique de travail local. Essayez cela en premier.

**Journal de diagnostic** : Hi, Moose conserve un petit journal d'erreurs sur cet appareil. **Ouvrir le dossier des journaux** vous y conduit ; si le support vous le demande, envoyez le fichier `main-errors.log`. Le journal reste sur votre appareil sauf si vous choisissez de le partager.

**Réinitialiser les données locales de l'application** : supprime définitivement les artefacts, briefs, aperçus, historique de visibilité et autres états de travail locaux de l'appareil. Cette action est irréversible. Votre session et les identifiants de connecteurs enregistrés sont conservés.
