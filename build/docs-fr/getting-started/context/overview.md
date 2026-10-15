---
source_hash: 25544d4dba4331f336f53923c9a635bc4442b022e472aec88392d921d34dfefb
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/getting-started/context/overview/)

# Context

## À quoi cela sert

**Contexte** est la couche de fondement située dans la navigation de gauche de l'application de bureau. C'est le contexte opérationnel partagé de votre projet en cours : les informations que l'opérateur, le chat et toutes les fonctions de génération réutilisent au lieu de repartir de zéro à chaque demande.

Context se compose de quatre éléments :

| | Portée | Utilité |
|---|---|---|
| **[Brand Voice](brand-voice.md)** | Par projet | La façon dont votre marque doit sonner : ton, public, valeurs, terminologie. Définit le style rédactionnel de tout ce que Hi, Moose génère. |
| **[Brand Truth Profile](brand-truth-profile.md)** | Par projet | Une source de vérité lisible par machine sur ce que votre entreprise est, vend et sert réellement. Sert à détecter quand les réponses de l'IA la déforment ou s'en écartent. |
| **[Documents de marque](brand-documents.md)** | Par projet | Votre propre message house, votre charte éditoriale et vos documents de positionnement. Hi, Moose les découpe en sections, applique vos règles d'écriture à tout et va chercher le reste quand un travail en a besoin. |
| **[À propos de vous](about-you.md)** | Par appareil, pas par projet | Des notes sur vous personnellement : votre fonction, vos objectifs et votre façon de travailler, pour que le chat connaisse la personne et pas seulement la marque. |

## Pourquoi des artefacts distincts

Brand Voice et Brand Truth Profile répondent à des questions différentes, même si tous deux décrivent votre marque :

- **Voix de marque** répond à « comment cela doit-il sonner ? » : ton, style, préférences de vocabulaire. C'est un guide créatif et stylistique pour le contenu généré.
- **Brand Truth Profile** répond à « qu'est-ce qui est vrai à notre sujet ? » : description canonique, client idéal, offres, concurrents et points précis que l'IA se trompe souvent. C'est une référence factuelle servant à repérer les déformations, pas un guide de style.

**Les documents de marque** contiennent la matière source complète derrière les deux. La Brand Voice et le Brand Truth Profile restent des résumés courts. Vos documents gardent le détail, et Hi, Moose y cherche les sections adaptées à chaque travail. Vous pouvez aussi vous en servir pour remplir les deux profils.

**À propos de vous** se distingue de tous ces éléments : cela ne concerne pas la marque du tout. C'est un contexte personnel sur **vous**, la personne qui utilise l'application, enregistré en local sur votre appareil plutôt que rattaché à un projet. Il vous suit donc d'un projet à l'autre au lieu d'être réinitialisé à chaque changement d'espace de travail.

## Où Context est utilisé

- **Voix de marque** est réutilisée dans les [Content Briefs](../../features/content-briefs.md), le [générateur de FAQ](../../features/faq-generator.md), l'[extracteur de Key Points](../../features/key-points.md), les [brouillons, aperçus et publications](../../features/drafts-and-publishing.md) et les recommandations des [AEO audits](../../features/aeo-audits.md).
- **Brand Truth Profile** est réutilisé pendant les exécutions de [Visibility](../../visibility/overview.md), où Hi, Moose vérifie si la réponse d'un moteur d'IA sur votre marque correspond à votre description canonique, à vos offres, à vos concurrents et aux schémas de déformation connus.
- **Les documents de marque** sont réutilisés dans les Content Briefs, les brouillons d'articles de blog, les Key Points, le générateur de FAQ, les recherches de [Send Moose](../../send-moose/overview.md) et le [Chat](../../chat/overview.md), où le chat peut aussi y faire des recherches. Voir [Où vos documents sont utilisés](brand-documents.md#ou-vos-documents-sont-utilises).
- **À propos de vous** est réutilisé dans le [Chat](../../chat/overview.md), pour que les réponses tiennent compte de votre fonction, de vos objectifs et de votre style de communication préféré.

## Comment le remplir

Chaque artefact indique combien de champs vous avez renseignés et affiche un bref aperçu dès que vous ajoutez quelque chose. Tous les champs sont facultatifs : Hi, Moose fonctionne avec un contexte partiel et gagne en précision à mesure que vous en ajoutez.

Pour la Brand Voice en particulier, vous n'êtes pas obligé de tout saisir à la main : une action de **remplissage automatique** peut explorer le site web de votre projet en local et proposer des valeurs pour les champs vides.

Si vous avez déjà un message house ou une charte éditoriale, importez-le dans les [documents de marque](brand-documents.md) et cliquez sur **Remplir les profils depuis les documents**. Hi, Moose propose des valeurs pour la Brand Voice et le Brand Truth Profile, chacune appuyée par une citation de votre document, et vous choisissez celles à appliquer.

## Stockage local et synchronisation cloud

Par défaut, Brand Voice, Brand Truth Profile et les documents de marque sont enregistrés **en local pour le projet en cours**, et À propos de vous est enregistré **en local sur votre appareil**. La synchronisation cloud, qui sauvegarde Brand Voice, Brand Truth Profile et les documents de marque et les partage avec votre équipe, est disponible sur **tous les forfaits payants**, y compris les forfaits BYOK payants. Preview Mode et BYOK Free restent en local uniquement ; passer à un forfait supérieur active la synchronisation, si bien que votre équipe partage le même socle et que celui-ci est protégé en cas de problème sur votre machine.

!!! note "Sur les forfaits BYOK"
    L'exploration du contexte de marque (l'étape de remplissage automatique) et l'analyse Brand Truth s'exécutent en local, dans l'application de bureau. Hi, Moose n'a pas besoin de voir le contenu de votre site sur ses propres serveurs pour constituer ou utiliser ce contexte.
