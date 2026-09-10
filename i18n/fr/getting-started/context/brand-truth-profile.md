---
source_hash: c5ff2a271e0bd65a359303913cb736f19793b0f0562c6c4941f37c02efd742fb
---
# Brand Truth Profile

## À quoi cela sert

Le Brand Truth Profile est une source de vérité lisible par machine sur la façon dont l'IA doit décrire votre entreprise : ce que vous vendez, qui vous servez et ce avec quoi vous ne devez jamais être confondu. Hi, Moose l'utilise pendant les exécutions de [Visibility](../../visibility/overview.md) pour détecter quand la réponse d'un moteur d'IA déforme votre marque ou reprend un discours obsolète, au lieu de laisser ce jugement à un score de sentiment générique.

Comme la Brand Voice, le Brand Truth Profile est délimité au [projet](../projects.md) en cours.

Tous les champs sont facultatifs, mais plus vous en renseignez, plus Hi, Moose pourra signaler précisément les déformations et recommander des corrections.

## Champs que vous pouvez renseigner

### Description principale

- **Comment l'IA doit-elle décrire votre entreprise aujourd'hui ?** : la description canonique, en une ou deux phrases, que vous aimeriez voir dans une réponse de ChatGPT, Perplexity, Gemini ou Google AI.
- **Qui est votre client idéal aujourd'hui ?** : à choisir parmi des segments courants (PME, entreprises de taille intermédiaire, grands comptes, agences, marques e-commerce, etc.), avec des notes en texte libre.

### Ce que vous proposez

- **Produits, services ou catégories de produits que l'IA doit savoir que vous proposez** : l'essentiel de ce que l'IA doit savoir que vous fournissez ; inutile de lister chaque fonctionnalité.
- **Fonctionnalités ou capacités que l'IA doit mentionner** : une par ligne. Aide Hi, Moose à détecter quand l'IA omet un élément important.

### Là où les descriptions dérapent

- **Que l'IA ou le marché se trompent-ils souvent au sujet de votre entreprise ?** : à choisir parmi des schémas de déformation courants : mauvais type de client, mauvaise catégorie de produit, positionnement obsolète, absence de nouveaux produits ou fonctionnalités, mauvais concurrents, surestimation ou sous-estimation des capacités, confusion avec une autre marque, etc.
- **Un exemple de ce que l'IA ou le marché se trompent** : un exemple concret pour étayer le schéma ci-dessus.
- **Descriptions obsolètes que nous devrions signaler** : anciennes catégories, cibles clients ou limitations qui ne s'appliquent plus.
- **Quelles erreurs de l'IA seraient les plus dommageables ?** : les catégories d'erreur les plus critiques (mauvaise description de l'entreprise, mauvaise cible client, tarifs ou disponibilité incorrects, sentiment négatif ou trompeur, confusion de marque, etc.).

### Vocabulaire

- **Mots ou expressions que l'IA doit employer** : vocabulaire privilégié, un par ligne.
- **Mots ou expressions que l'IA doit éviter** : vocabulaire à proscrire, un par ligne.

### Contexte concurrentiel

- **Principaux concurrents ou alternatives** : 3 à 5 concurrents, alternatives ou catégories d'outils, chacun avec une note facultative (par exemple « positionné uniquement grands comptes »). Sert à tester les prompts de comparaison.
- **Comparaisons à surveiller** : recherches de comparaison ou de catégories alternatives précises que Hi, Moose doit surveiller (par exemple « meilleurs outils AEO pour les petites entreprises »).

### Confiance et preuves

- **Questions de clients auxquelles l'IA doit répondre correctement** : questions de diagnostic alignées sur la façon dont les prospects achètent réellement.
- **Affirmations que l'IA doit manier avec précaution** : tarifs, performances, certifications ou autres affirmations exigeant un langage nuancé.
- **Pages ou sources qui prouvent votre positionnement actuel** : pages, documents ou études de cas précis à considérer comme des preuves importantes, chacun avec une note facultative.
- **Sources déjà connues comme obsolètes ou inexactes** : pages tierces, annuaires ou citations antérieures de l'IA connus pour décrire votre entreprise de façon erronée, chacun avec une note sur ce qui est faux.

## Comment il est utilisé

### Détecter les représentations erronées

Pendant une exécution de visibilité, Hi, Moose charge le Brand Truth Profile du projet (lorsqu'il contient des informations significatives) et l'utilise pour évaluer chaque réponse de l'IA à la recherche de déformations ou d'écarts, en la comparant à votre description canonique, à vos offres, à vos concurrents, à votre vocabulaire privilégié et à proscrire, ainsi qu'aux schémas de déformation connus, plutôt que de se contenter de vérifier si le nom de votre marque apparaît.

### Écrire un contenu qui vise votre acheteur

Le profil alimente aussi les outils de contenu. Les [content briefs](../../features/content-briefs.md), les [brouillons d'articles](../../features/blog-post-draft.md), les [key points](../../features/key-points.md) et les [FAQ](../../features/faq-generator.md) le lisent avant d'écrire quoi que ce soit, y compris vos **segments de client idéal** et les notes libres qui les accompagnent.

C'est la différence entre un brief écrit pour « des lecteurs intéressés par le sujet » et un brief écrit pour des équipes opérationnelles mid-market qui évaluent un changement de solution. Renseigner une seule fois les champs de client idéal change la production de tous les outils de rédaction par la suite, ce qui en fait parmi les champs les plus rentables de cet écran.

[Send Moose](../../send-moose/overview.md) lit lui aussi le profil sur les travaux qui concernent votre propre marque.

## En quoi cela diffère de la Brand Voice

La [Brand Voice](brand-voice.md) concerne le **style** : la façon dont votre marque doit sonner. Le Brand Truth Profile concerne les **faits** : ce qui est vrai au sujet de votre entreprise et quels discours erronés surveiller. Renseignez la Brand Voice pour définir le ton ; renseignez le Brand Truth Profile pour repérer quand l'IA se trompe sur les faits vous concernant.

## Synchronisation cloud

Comme la Brand Voice, le Brand Truth Profile est par défaut enregistré en local pour le projet en cours. Le synchroniser avec le cloud, afin de le sauvegarder et de le partager avec votre équipe, nécessite un forfait payant. Voir [Context](overview.md) pour plus de détails.

## Suivi des concurrents

La liste de concurrents de cette page est partagée avec les [paramètres de Visibility](../../visibility/settings.md). Les concurrents ajoutés à l'un ou l'autre endroit apparaissent dans les deux et alimentent le [Share of Voice, les citations de concurrents et les écarts](../../visibility/competitors.md).
