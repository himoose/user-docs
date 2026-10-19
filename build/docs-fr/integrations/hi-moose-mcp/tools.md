---
source_hash: 02739399b48594689facbef6808edfaaedea42f90e6577cf6c6b9bb9f23939c1
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](http://localhost:8000/integrations/hi-moose-mcp/tools/)


# Référence des outils

Chaque outil que Hi, Moose MCP propose à une application connectée, avec ce qu'il prend en entrée et ce qu'il renvoie. Vous n'appelez pas les outils vous-même : l'application choisit l'outil selon ce que vous demandez. Cette page vous dit quoi demander et à quoi vous attendre.

Chaque outil sauf `list_projects` et `get_result` prend un **projet**, par le nom affiché dans Hi, Moose. Dites le nom du projet dans votre demande quand vous en avez plusieurs, par exemple « pour le projet Acme ».

## Combien de temps ça prend

| Outil | Durée habituelle |
|---|---|
| Lister les projets, briefs, brouillons | Quelques secondes |
| Vérifier la couverture du site | Moins d'une minute |
| Vérification de visibilité, lire une réponse | Quelques secondes |
| Liste des opportunités | De quelques secondes à une minute |
| Brief de contenu, brouillon, FAQ, points clés, image à la une | Une à trois minutes |
| Audit AEO | Deux à quatre minutes |
| Liens internes | Environ une minute |
| Épisode audio | 5 minutes pour court, 9 pour standard, 15 pour approfondi |

Quand un outil prend plus de temps que l'application n'attend, il répond « toujours en cours » avec un identifiant de tâche. L'application utilise ensuite `get_result` pour récupérer le travail terminé ; demandez-lui de vérifier à nouveau si elle ne le fait pas.

## Projets et Library

### list_projects

Liste les projets Hi, Moose sur lesquels vous pouvez travailler. Tous les autres outils ont besoin d'un projet, donc l'application appelle en général celui-ci en premier.

Demandez : « Liste mes projets Hi, Moose. »

### list_briefs

Liste les briefs de contenu enregistrés dans la Library pour un projet, du plus récent au plus ancien, jusqu'à 50. Utilisez-le quand vous faites référence à un brief créé plus tôt.

Demandez : « Montre les briefs enregistrés pour Acme. »

### list_drafts

Liste les brouillons enregistrés dans la Library pour un projet, du plus récent au plus ancien, jusqu'à 50.

Demandez : « Quels brouillons ai-je dans Acme ? »

### get_result

Récupère un travail démarré par un autre outil, par identifiant de tâche. Attend jusqu'à une minute qu'il se termine. L'application l'appelle d'elle-même ; vous n'en avez besoin que quand l'application dit que le travail est toujours en cours et que vous voulez qu'elle vérifie à nouveau.

## Couverture du site

### check_site_coverage

Vérifie dans la dernière exploration de votre site les pages qui couvrent déjà un ou plusieurs sujets.

| Entrée | Obligatoire | Signification |
|---|---|---|
| topics | oui | Une à quinze phrases courtes, par exemple « génération de SBOM pour Python » |
| parentTopic | non | Le sujet plus large auquel appartiennent les sujets, utilisé pour juger la couverture partielle |

Pour chaque sujet, il répond **covered**, **partial**, **uncovered** ou **unknown**, avec les URL des pages les plus proches comme preuves et la date de l'exploration vérifiée. Unknown signifie que la vérification n'a pas pu s'exécuter pour ce sujet, pas que le site ne le couvre pas.

Demandez : « Notre site couvre-t-il déjà SCA vs SAST ? »

## Contenu

### create_content_brief

Crée un brief de contenu fondé sur la recherche : objectif, audience, justification, groupes de mots-clés, structure recommandée et contraintes, à partir des résultats de recherche en direct, de l'exploration de votre site, de vos règles de marque et du Brand Truth.

| Entrée | Obligatoire | Signification |
|---|---|---|
| topic | oui | Le sujet, la question ou le titre de travail, jusqu'à 400 caractères |
| targetUrl | non | La page de votre site pour laquelle le brief est destiné |
| templateType | non | Le type de contenu : « Blog post », « Landing page », « Comparison page », « Guide » |
| guidance | non | Les exigences décidées ailleurs : angle, points à inclure, ton. Jusqu'à 4 000 caractères. |

Renvoie le brief en texte plus un identifiant de brief que l'outil de brouillon utilise. Enregistré dans la Library.

Demandez : « Rédige un brief de contenu pour un guide sur la génération de SBOM pour les équipes Python. »

### create_draft

Rédige un premier brouillon publiable à partir d'un brief, dans la voix de votre marque, fondé sur le brief, le Brand Truth et les règles de marque, avec des liens internes choisis dans l'exploration de votre site et une passe de relecture.

| Entrée | Obligatoire | Signification |
|---|---|---|
| briefId | l'un des deux | Un brief créé dans Hi, Moose |
| brief | l'un des deux | Un brief écrit ailleurs, en texte, jusqu'à 60 000 caractères |
| briefTitle | non | Le titre de travail, quand vous passez un brief en texte |
| templateType | non | Le type de contenu, quand vous passez un brief en texte |
| guidance | non | Exigences supplémentaires, jusqu'à 4 000 caractères |

Renvoie le brouillon en texte plus un identifiant de brouillon. Enregistré dans la Library.

Demandez : « Rédige l'article à partir de ce brief. » ou « Voici un brief que j'ai écrit, rédige-le pour Acme : ... »

### create_featured_image

Crée une image à la une pour un article, en 1200 par 630, dans votre style d'image enregistré quand il y en a un.

| Entrée | Obligatoire | Signification |
|---|---|---|
| draftId | l'un des deux | Un brouillon créé dans Hi, Moose |
| title et summary | l'un des deux | Le titre de l'article et un court résumé, jusqu'à 6 000 caractères, quand il n'y a pas de brouillon |
| styleIntent | non | Un souhait pour cette seule image : ambiance, scène, couleurs. Le style enregistré s'applique toujours. |

Renvoie l'image et un lien vers le PNG. Le fichier est aussi enregistré sur l'appareil hôte.

Demandez : « Crée une image à la une pour ce brouillon, lumière du soir, sans personnes. »

### create_faqs

Rédige des questions fréquentes avec leurs réponses pour un contenu, dans la voix de votre marque, plus le balisage FAQPage prêt à coller dans la page. Sur les comptes payants, les questions sont d'abord recherchées à partir du comportement de recherche réel.

| Entrée | Obligatoire | Signification |
|---|---|---|
| draftId | l'un des deux | Un brouillon enregistré |
| url | l'un des deux | Une page publiée sur votre site |
| guidance | non | Audience, questions qui doivent apparaître, ton. Jusqu'à 4 000 caractères. |

Demandez : « Rédige une FAQ pour https://acme.example/guides/sbom. »

### create_key_points

Rédige les points clés d'un contenu : des énoncés courts et citables, dans la voix de votre marque, que les moteurs de réponse peuvent reprendre.

| Entrée | Obligatoire | Signification |
|---|---|---|
| draftId | l'un des deux | Un brouillon enregistré |
| url | l'un des deux | Une page publiée sur votre site |
| guidance | non | Audience, points qui doivent apparaître, ton. Jusqu'à 4 000 caractères. |

Demandez : « Donne-moi les points clés du brouillon du guide SBOM. »

## Audits et liens

### run_aeo_audit

Lance un audit d'optimisation pour les moteurs de réponse sur un contenu : un score sur 100, des scores par catégorie (structure, extractibilité, potentiel de citation, signaux de confiance, fraîcheur, aptitude à répondre et plus), les problèmes trouvés, et des changements concrets avec le texte proposé.

| Entrée | Obligatoire | Signification |
|---|---|---|
| url | l'un des trois | Une page en ligne. Le meilleur choix, parce que les vérifications techniques comme l'accès des robots d'IA et les dates de page ne s'exécutent que sur une page en ligne. |
| draftId | l'un des trois | Un brouillon enregistré |
| content | l'un des trois | Le contenu en texte, pour une page pas encore en ligne. Jusqu'à 50 000 caractères. |
| targetQuery | non | La question ou le prompt de recherche que le contenu doit gagner, jusqu'à 200 caractères. Sans lui, Hi, Moose en déduit un. |

Sur les comptes payants, les preuves de recherche en direct sont incluses.

Demandez : « Audite https://acme.example/guides/sbom pour la requête “SBOM generation tools”. »

### find_internal_links

Planifie les liens internes d'un contenu à partir de l'exploration de votre propre site. Renvoie deux listes : les pages vers lesquelles ce contenu devrait pointer, chacune avec le texte d'ancrage à utiliser, et les pages existantes qui devraient ajouter un lien vers ce contenu, chacune avec le texte d'ancrage à utiliser sur cette page. Les pages déjà liées dans un sens ou l'autre sont exclues.

| Entrée | Obligatoire | Signification |
|---|---|---|
| url | l'un des trois | Une page de votre site, en ligne |
| draftId | l'un des trois | Un brouillon enregistré |
| content | l'un des trois | Le contenu en texte, jusqu'à 50 000 caractères |
| title | non | Le titre, quand vous passez le contenu en texte |

Les résultats couvrent les pages explorées jusqu'ici et nomment la date de l'exploration. Les pages publiées depuis la dernière exploration ne sont pas incluses.

Demandez : « Planifie les liens internes pour le brouillon du guide SBOM. »

## Visibilité dans la recherche IA

### visibility_check_topic

Répond à « apparaissons-nous dans la recherche IA pour X » à partir des résultats de visibilité que Hi, Moose a enregistrés. Posez la question avec vos propres mots ; Hi, Moose la rapproche des prompts suivis, dans n'importe quelle langue.

| Entrée | Obligatoire | Signification |
|---|---|---|
| question | oui | Le sujet ou la question, jusqu'à 400 caractères |
| lookbackDays | non | Combien de jours de résultats enregistrés lire. Par défaut 90. |
| engine | non | Seulement ce moteur, par son nom, par exemple « ChatGPT » |

Renvoie, par moteur, si la marque a été mentionnée ou citée lors de la dernière exécution et lors d'une exécution antérieure, les taux de mention et de citation sur la période, un court extrait de la dernière réponse où la marque est apparue, les prompts rapprochés, et les autres marques vues. Chaque extrait porte un identifiant de réponse pour l'outil suivant. Les résultats couvrent les prompts suivis sur les moteurs suivis seulement, jamais toute la recherche IA. Il lit les résultats enregistrés et ne lance jamais de nouvelles vérifications.

Demandez : « Apparaissons-nous dans la recherche IA pour la génération de SBOM ? »

### visibility_get_answer

Récupère une réponse enregistrée par son identifiant de réponse : le prompt, le moteur, la date, si la marque a été mentionnée ou citée, les sources listées par le moteur, les notes du correcteur et le texte complet de la réponse. Le texte est ce que le moteur a écrit à ce moment-là.

Demandez : « Montre-moi la réponse complète de ChatGPT pour ce résultat. »

### visibility_list_opportunities

Renvoie la file de travail classée que Hi, Moose construit à partir des résultats de visibilité enregistrés, les mêmes lignes que l'onglet Opportunités. Chaque ligne nomme l'écart exact, la prochaine étape en une phrase, la priorité avec ses raisons, la constance de l'écart d'une exécution à l'autre, l'effort, le statut fixé par l'équipe et un identifiant d'opportunité.

| Entrée | Obligatoire | Signification |
|---|---|---|
| lookbackDays | non | Jours de résultats enregistrés à lire. Par défaut 7, comme l'onglet Opportunités. Au plus 90. |
| limit | non | Lignes à renvoyer, les meilleures d'abord. Par défaut 10, au plus 25. |
| action | non | Un seul type de ligne : `create-coverage`, `improve-page`, `earn-inclusion`, `correct-description` ou `investigate-change` |
| priority | non | `high`, `medium` ou `low` |
| includeClosed | non | Renvoyer aussi les lignes marquées terminées, écartées ou reportées. Par défaut false. |
| opportunityId | non | Un identifiant venant d'un résultat précédent. Renvoie les preuves complètes de cette seule ligne au lieu de la liste. |

Les cinq types de ligne : **create-coverage** (aucune de vos pages ne répond à un prompt que les concurrents gagnent), **improve-page** (une de vos pages est citée ou est la plus proche, mais la marque est absente ou classée derrière), **earn-inclusion** (une page tierce citée par les moteurs nomme des concurrents mais pas vous), **correct-description** (les réponses répètent une affirmation sur la marque qui demande vérification) et **investigate-change** (la marque était nommée ou citée avant et ne l'est plus).

Demandez : « Sur quoi devrions-nous travailler pour la recherche IA cette semaine ? » puis « Montre-moi les preuves pour la première. »

## Audio

### create_audio

Crée un épisode « écouter cet article » : une conversation parlée à deux voix sur le contenu, rendue en MP3 et hébergée par Hi, Moose, plus l'extrait HTML du lecteur intégrable.

| Entrée | Obligatoire | Signification |
|---|---|---|
| url | l'un des trois | Une page en ligne |
| draftId | l'un des trois | Un brouillon enregistré |
| content et title | l'un des trois | L'article en texte, de 1 200 à 200 000 caractères, avec son titre |
| length | non | `short` (environ 4 minutes), `standard` ou `deep`. Par défaut short. |
| hostVoice, guestVoice | non | Deux voix différentes. Par défaut Sulafat et Fenrir. |
| language | non | Langue de la narration. Par défaut : la langue du contenu. |
| focus | non | Ce sur quoi la conversation doit se concentrer, jusqu'à 500 caractères |
| theme, layout, color, showTitle, customTitle, showTranscript, hideAttribution | non | L'apparence du lecteur, voir plus bas |

La [page des réglages audio](https://himoose.com/hi-moose-mcp/audio/) vous permet d'écouter chaque voix, de choisir la durée, la langue et l'apparence du lecteur, et de copier une ligne de réglages à coller dans le chat. Pendant le rendu de l'épisode, l'appareil hôte ne travaille sur rien d'autre. Si le résultat dit que l'épisode est toujours en cours de rendu, l'outil suivant le récupère quelques minutes plus tard.

Demandez : « Transforme https://acme.example/guides/sbom en audio, court, avec Zephyr et Charon. »

### get_audio_embed

Renvoie l'extrait du lecteur pour un épisode existant, avec une nouvelle apparence quand des champs du lecteur sont passés. L'audio n'est pas rendu à nouveau. C'est aussi le moyen de récupérer un épisode qui était toujours en cours de rendu.

| Entrée | Obligatoire | Signification |
|---|---|---|
| audioId | oui | L'identifiant de l'épisode |
| theme | non | `dark`, `light` ou `auto`. Par défaut dark. |
| layout | non | `full` ou `compact`. Par défaut full. |
| color | non | Couleur d'accent en hexadécimal, par exemple `#5688b0` |
| showTitle, customTitle | non | Afficher une ligne de titre, ou définir la vôtre |
| showTranscript | non | Afficher le bouton de transcription. Par défaut true. |
| hideAttribution | non | Masquer la ligne « Audio by Hi, Moose ». Offres payantes seulement. |

Demandez : « Donne-moi le lecteur compact clair pour cet épisode. »

## Ce que les outils ne peuvent pas faire

Ils ne peuvent pas modifier les réglages ni les membres de l'équipe, changer ce que Hi, Moose suit, lancer des analyses de visibilité, ni rien supprimer. Pour les tableaux de bord et l'automatisation, utilisez la [Hi, Moose API](../developer-api.md).
