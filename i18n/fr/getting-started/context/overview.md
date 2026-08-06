---
source_hash: 05fae21b2ec70be5a8bae1ca0e58f085c9da2140a80bae1dc2e083051aeffb43
---
# Context

## À quoi cela sert

**Contexte** est la couche de fondement située dans la navigation de gauche de l'application de bureau. C'est le contexte opérationnel partagé de votre projet en cours : les informations que l'opérateur, le chat et toutes les fonctions de génération réutilisent au lieu de repartir de zéro à chaque demande.

Context se compose de trois éléments distincts :

| | Portée | Utilité |
|---|---|---|
| **[Brand Voice](brand-voice.md)** | Par projet | La façon dont votre marque doit sonner : ton, public, valeurs, terminologie. Définit le style rédactionnel de tout ce que Hi, Moose génère. |
| **[Brand Truth Profile](brand-truth-profile.md)** | Par projet | Une source de vérité lisible par machine sur ce que votre entreprise est, vend et sert réellement. Sert à détecter quand les réponses de l'IA la déforment ou s'en écartent. |
| **[À propos de vous](about-you.md)** | Par appareil, pas par projet | Des notes sur vous personnellement : votre fonction, vos objectifs et votre façon de travailler, pour que le chat connaisse la personne et pas seulement la marque. |

## Pourquoi trois artefacts distincts

Brand Voice et Brand Truth Profile répondent à des questions différentes, même si tous deux décrivent votre marque :

- **Voix de marque** répond à « comment cela doit-il sonner ? » : ton, style, préférences de vocabulaire. C'est un guide créatif et stylistique pour le contenu généré.
- **Brand Truth Profile** répond à « qu'est-ce qui est vrai à notre sujet ? » : description canonique, client idéal, offres, concurrents et points précis que l'IA se trompe souvent. C'est une référence factuelle servant à repérer les déformations, pas un guide de style.

**À propos de vous** se distingue des deux : cela ne concerne pas la marque du tout. C'est un contexte personnel sur **vous**, la personne qui utilise l'application, enregistré en local sur votre appareil plutôt que rattaché à un projet. Il vous suit donc d'un projet à l'autre au lieu d'être réinitialisé à chaque changement d'espace de travail.

## Où Context est utilisé

- **Voix de marque** est réutilisée dans les [Content Briefs](../../features/content-briefs.md), le [générateur de FAQ](../../features/faq-generator.md), l'[extracteur de Key Points](../../features/key-points.md), les [brouillons, aperçus et publications](../../features/drafts-and-publishing.md) et les recommandations des [AEO audits](../../features/aeo-audits.md).
- **Brand Truth Profile** est réutilisé pendant les exécutions de [Visibility](../../visibility/overview.md), où Hi, Moose vérifie si la réponse d'un moteur d'IA sur votre marque correspond à votre description canonique, à vos offres, à vos concurrents et aux schémas de déformation connus.
- **À propos de vous** est réutilisé dans le [Chat](../../chat/overview.md), pour que les réponses tiennent compte de votre fonction, de vos objectifs et de votre style de communication préféré.

## Comment le remplir

Chaque artefact indique combien de champs vous avez renseignés et affiche un bref aperçu dès que vous ajoutez quelque chose. Tous les champs des trois artefacts sont facultatifs : Hi, Moose fonctionne avec un contexte partiel et gagne en précision à mesure que vous en ajoutez.

Pour la Brand Voice en particulier, vous n'êtes pas obligé de tout saisir à la main : une action de **remplissage automatique** peut explorer le site web de votre projet en local et proposer des valeurs pour les champs vides.

## Stockage local et synchronisation cloud

Par défaut, Brand Voice et Brand Truth Profile sont enregistrés **en local pour le projet en cours**, et À propos de vous est enregistré **en local sur votre appareil**. La synchronisation cloud, qui sauvegarde Brand Voice et Brand Truth Profile et les partage avec votre équipe, est disponible sur **tous les forfaits payants**, y compris les forfaits BYOK payants. Preview Mode et BYOK Free restent en local uniquement ; passer à un forfait supérieur active la synchronisation, si bien que votre équipe partage le même socle et que celui-ci est protégé en cas de problème sur votre machine.

!!! note "Sur les forfaits BYOK"
    L'exploration du contexte de marque (l'étape de remplissage automatique) et l'analyse Brand Truth s'exécutent en local, dans l'application de bureau. Hi, Moose n'a pas besoin de voir le contenu de votre site sur ses propres serveurs pour constituer ou utiliser ce contexte.
