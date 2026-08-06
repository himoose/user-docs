---
source_hash: f081840e659e67696268902173c5c0f26e8413e1debac31049488ad42cb5c005
---
# Paramètres

## À quoi cela sert

Les Paramètres vous permettent de gérer votre profil, votre forfait, vos modèles, votre équipe et le comportement de l'application sur cet ordinateur. Ils sont organisés en dix sections dans la colonne de gauche.

| Section | Contenu |
|---|---|
| General | Informations de profil et comportement de l'application sur cet ordinateur |
| Usage | Solde de crédits et date de réinitialisation |
| Compte | E-mail, mot de passe, forfait, clé OpenRouter |
| Local Model | Téléchargement et activation du modèle sur l'appareil |
| Équipe | Sièges, invitations, rôles |
| [Site Monitoring](../site-monitoring/overview.md) | Planification de l'exploration, index de recherche, pages surveillées, chemins bloqués |
| [Branding](../agency/white-label.md) | Rapports en marque blanche et attribution audio (forfaits payants uniquement) |
| Logs | Journaux d'actions et export CSV |
| Data & Backup | Sauvegarde et restauration locales |
| Troubleshooting | Cache, journal de diagnostic, réinitialisation des données locales |

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

Téléchargez et activez un modèle approuvé sur l'appareil, comme Gemma 4. L'exécution locale n'utilise jamais les modèles de Hi, Moose ni votre clé OpenRouter : elle se déroule entièrement sur votre machine et son usage est gratuit.

Les modèles locaux sont disponibles sur tous les forfaits et sont **obligatoires** sur Preview Mode pour les [AEO audits](../features/aeo-audits.md) et le scoring de visibilité.

!!! note "La taille du contexte s'adapte à votre RAM"
    Hi, Moose dimensionne la fenêtre de contexte du modèle selon la mémoire disponible sur votre machine : un même modèle utilise donc une fenêtre plus petite sur un portable de 16 Go que sur une station de travail plus puissante.

## Équipe

Invitez des membres, consultez leurs rôles et révoquez des accès. Les limites de sièges dépendent de votre forfait. Consultez [Gestion de l'équipe](team-management.md) pour le parcours complet.

## Site Monitoring

Planification de l'exploration, index de recherche local, pages surveillées et chemins bloqués. C'est un domaine à part entière, qui dispose de sa propre page : **[Site Monitoring](../site-monitoring/overview.md)**.

Les connexions aux CMS et aux sources de données sont distinctes et se trouvent dans l'écran **Connections**, et non dans les Paramètres :

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

Appliquez votre marque blanche aux rapports PDF exportés et aux lecteurs audio intégrés. Disponible sur tous les forfaits payants et modifiable par le titulaire de l'abonnement. Voir **[Marque blanche](../agency/white-label.md)**.

## Logs

Journaux d'actions du projet en cours, avec le type, l'utilisateur, la date, le statut et les métadonnées de chaque action enregistrée. Sur les forfaits gérés, les journaux partagés de l'équipe se synchronisent aux côtés de vos journaux locaux.

**Export CSV** les télécharge. L'export des journaux d'actions de l'équipe est réservé aux titulaires d'espaces de travail gérés payants.

## Data & Backup

Créez une sauvegarde compressée `.hmbk` de votre historique sur l'appareil, et importez-la ultérieurement pour le restaurer.

**Les sauvegardes comprennent** les enregistrements de la base de données locale et les planifications de visibilité BYOK enregistrées : vos briefs, audits, aperçus, historique de site monitoring, état de l'Inbox et autres artefacts de travail non sensibles restent donc portables.

**Les sauvegardes ne comprennent pas** l'état de session, les identifiants de connecteurs, les clés d'API, les fichiers de modèles locaux ni les pièces jointes.

!!! warning "L'import écrase définitivement les données locales"
    Un import remplace les données locales Hi, Moose de cet appareil par le contenu de la sauvegarde. La boîte de dialogue de confirmation vous indique combien d'enregistrements seront restaurés et à quelle date la sauvegarde a été créée. Redémarrez ensuite l'application pour que tous les écrans se rechargent à partir des données restaurées.

Les imports n'acceptent que les fichiers `.hmbk` exportés par l'application de bureau Hi, Moose.

## Troubleshooting

Trois outils de récupération. Tous n'affectent que l'état local du bureau et ne touchent jamais aux données du cloud.

**Vider le cache temporaire** : efface le cache HTTP, les service workers et les autres états jetables. Conserve votre session et votre historique de travail local. Essayez cela en premier.

**Journal de diagnostic** : Hi, Moose conserve un petit journal d'erreurs sur cet appareil. **Ouvrir le dossier des journaux** vous y conduit ; si le support vous le demande, envoyez le fichier `main-errors.log`. Le journal reste sur votre appareil sauf si vous choisissez de le partager.

**Réinitialiser les données locales de l'application** : supprime définitivement les artefacts, briefs, aperçus, historique de visibilité et autres états de travail locaux de l'appareil. Cette action est irréversible. Votre session et les identifiants de connecteurs enregistrés sont conservés.
