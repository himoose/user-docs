---
source_hash: d13fbe0e44e283bca3759e24ae06c4632b5ccb20e66f5806145543eb82fe5f65
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/features/drafts-and-publishing/)

# Brouillons, aperçu et publication

## À quoi cela sert

Hi, Moose ne s'arrête pas à la recommandation : il vous aide à passer d'un brief ou d'une idée de modification jusqu'à un changement publié, avec une étape d'aperçu et une étape d'approbation entre les deux, et un enregistrement de ce qui s'est passé.

## Draft Studio

Draft Studio est l'endroit où les brouillons sont rédigés et affinés. La génération de brouillons est conçue pour s'appuyer sur un [brief de contenu](content-briefs.md) plutôt que de fonctionner comme un générateur de texte à l'aveugle : si une tâche exige une planification structurée, Hi, Moose génère ou confirme d'abord le brief, puis rédige à partir de celui-ci. Draft Studio prend aussi en charge l'édition directe de textes longs.

### Types de contenu

La génération de brouillons suit les mêmes types de modèles que ceux disponibles lors de la [génération d'un brief de contenu](content-briefs.md#generer-un-brief). Quatre disposent de leur propre démarrage rapide dans le Chat, chacun avec sa structure : [brouillon d'article de blog](blog-post-draft.md), [article de glossaire](glossary-post.md), [contenu de landing page](landing-page-content.md) et [contenu de page produit](product-page-content.md). Le modèle de page de solutions est également disponible lors de la génération d'un brief, sans démarrage rapide dédié.

Tous les modèles suivent le même flux « brief d'abord » ; seule la structure diffère : un brouillon de landing page est donc planifié et façonné différemment d'un article de blog, même si tous deux partent d'un [brief de contenu](content-briefs.md).

Lorsque vous demandez un article et que Hi, Moose produit un brief, il enchaîne et génère le brouillon au lieu de s'arrêter en attendant que vous le redemandiez.

### Maillage interne

Les nouveaux brouillons sont confrontés à votre site indexé, et des liens internes pertinents sont insérés là où ils s'imposent réellement. Cela nécessite un [index de recherche](../site-monitoring/overview.md) construit : sans lui, il n'y a rien vers quoi pointer, et Hi, Moose n'invente pas de liens.

## Préparer une modification

Qu'elle vienne d'un brouillon issu d'un brief, de [FAQ](faq-generator.md), de [key points](key-points.md) ou d'une recommandation d'[AEO audit](aeo-audits.md), une modification proposée est préparée comme une **proposition de modification**, un artefact durable et non un simple texte de chat, avant que quoi que ce soit ne touche votre site en production.

## Aperçu

Avant toute approbation, Hi, Moose peut générer un aperçu de la modification préparée pour que vous voyiez son rendu sur la page réelle. Pour les changements devant être relus par quelqu'un d'autre, Hi, Moose peut générer un lien de relecture partagé, signé et à durée limitée, permettant à un collègue ou à un client de relire sans accès à l'application de bureau.

## Approuver et publier

- **Approuver** : accepter explicitement une modification préparée avant qu'elle puisse être publiée. L'aperçu et la publication sont toujours des étapes distinctes ; générer un brouillon ou un aperçu n'est jamais considéré comme « terminé » en soi.
- **Publier** : une fois approuvée, Hi, Moose publie la modification via la connexion correspondante ([WordPress](../integrations/wordpress.md), [Webflow](../integrations/webflow.md) ou [Grav](../integrations/grav.md)) et enregistre ce qui a été publié, quand et pourquoi.

### Comportement selon le CMS

**WordPress** : les brouillons peuvent être envoyés vers un site connecté en tant que brouillons préparés plutôt que d'être mis en ligne directement, et le flux de publication s'adapte selon que la cible est déjà préparée ou publiée. Une fois un brouillon envoyé, Hi, Moose s'en souvient : vous ne pouvez donc pas envoyer le même plusieurs fois par inadvertance.

**Webflow** : publier dans une collection charge d'abord les autres champs obligatoires de cette collection et vous demande de les renseigner, afin qu'une publication n'échoue pas en cours de route sur un champ que vous ne pouviez pas voir.

Une publication en échec arrive dans votre [Inbox](../inbox/overview.md). Une publication réussie non, délibérément.

## Work Queue

La Work Queue rassemble les modifications préparées, les aperçus en attente et les éléments en attente de votre approbation, afin que rien ne reste enfoui dans une transcription de chat en attendant d'être oublié.

## Library et historique

- La **[Library](../library/overview.md)** conserve les artefacts durables que vous avez générés (briefs, brouillons, jeux de FAQ, key points, AEO audits) pour que vous puissiez les retrouver et les réutiliser au lieu de les régénérer.
- **[Chats (historique)](../chat/chats-history.md)** est l'historique de vos sessions de chat enregistrées : rouvrez, renommez ou supprimez une conversation passée. C'est un historique de conversations, pas un journal de publication ni de résultats de visibilité ; un registre dédié reliant les changements publiés au signal de visibilité qui les a déclenchés est prévu mais pas encore construit.

## Pourquoi cela compte

Ce parcours aperçu → approbation → publication est ce qui transforme une recommandation en action aboutie et traçable. Un flux qui ne produit que des conseils est incomplet ; un flux qui se termine par un changement prévisualisé, approuvé et publié, avec un enregistrement le reliant au signal de visibilité d'origine, c'est toute la raison d'être de Hi, Moose.
