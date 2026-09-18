---
source_hash: 399cb3ab67be171f7aec402853ccc087cffad8b03562b16db57f4d80c7058766
---
# Documents de marque

## À quoi cela sert

Les documents de marque vous permettent d'importer les documents que votre équipe tient déjà à jour, comme un message house, une charte éditoriale ou des messages de positionnement et par persona. Hi, Moose les lit avant d'écrire quoi que ce soit pour le projet : les briefs, brouillons, FAQ et réponses de chat suivent vos propres règles et reprennent vos messages approuvés.

Vous n'avez pas à coller un message house de 50 pages dans chaque demande. Hi, Moose découpe chaque document en sections, applique vos règles d'écriture à chaque travail et ne va chercher les autres sections que lorsqu'un travail en a besoin.

Vous pouvez aussi vous servir de vos documents pour [remplir la Brand Voice et le Brand Truth Profile](#remplir-brand-voice-et-brand-truth-depuis-vos-documents) en une seule étape.

Les documents de marque sont propres au [projet](../projects.md) en cours. Ouvrez-les depuis la carte **Documents de marque** de l'écran [Context](overview.md).

## Importer un document

1. Ouvrez **Contexte** et cliquez sur **Importer un document de marque** dans la carte Documents de marque (ou sur **Gérer les documents de marque** si vous en avez déjà).
2. Cliquez sur **Importer un document** et choisissez un fichier.
3. Hi, Moose lit le fichier, le découpe en sections, étiquette chaque section et l'indexe pour la recherche. La progression s'affiche à l'écran.

**Fichiers pris en charge :** Markdown, texte brut, Word (`.docx`) et PDF.

Les titres deviennent des sections : un document avec des titres clairs donne les meilleurs résultats. Un message house avec un titre pour chaque pilier, persona et produit se découpe proprement. Un PDF fait d'un seul long bloc de texte, non.

L'étiquetage d'un document volumineux peut prendre plusieurs minutes. Vous pouvez quitter l'écran pendant ce temps. Hi, Moose continue de travailler et vous prévient quand le document est prêt, avec une notification si l'application est en arrière-plan.

**Limites :** jusqu'à 25 documents par projet et environ 500 000 caractères par document.

## Comment les sections sont classées

Chaque section reçoit un type. Le type détermine quand Hi, Moose l'utilise.

| Type | Contenu | Quand il est utilisé |
|---|---|---|
| **Règles** | Comment écrire pour cette marque : voix, nommage, mots à employer et à éviter. | Toujours actif, pour chaque travail. |
| **Socle de l'entreprise** | Positionnement et identité valables pour n'importe quel contenu. | Toujours actif, pour chaque travail. |
| **Preuves** | Chiffres, clients, citations et liens que Hi, Moose peut citer. | Sollicité quand c'est pertinent. |
| **Textes approuvés** | Texte réutilisable comme les propositions de valeur et les boilerplates. | Sollicité quand c'est pertinent. |
| **Playbooks** | Messages pour une audience, un produit, une solution ou un secteur. | Sollicité quand c'est pertinent. |

Les sections peuvent aussi porter des indicateurs :

- **Toujours actif** : la section est intégrée à chaque travail.
- **Interne uniquement** : le document indique que cette section est interne. Hi, Moose s'en sert pour orienter le positionnement, mais ne la cite ni ne la paraphrase jamais dans un contenu.
- **Brouillon** : la section est marquée comme brouillon dans le document source.
- **Vérifier l'approbation** : la source indique que le contenu doit être validé avant utilisation.
- **Modifié ici** : vous avez modifié la section dans Hi, Moose.

Ces indicateurs aident, mais ne sont pas une garantie. Relisez vous-même chaque brouillon avant publication.

### Vérifier et modifier les sections

Cliquez sur **Voir les sections** sur un document pour afficher ses sections regroupées par type. Cliquez sur **Modifier la section** pour corriger le texte d'une section, puis sur **Enregistrer la section**. Les sections modifiées portent l'indicateur **Modifié ici**.

Si l'écran affiche **Étiqueté d'après les titres seulement**, aucun modèle n'était disponible au moment du traitement du document : les sections ont été étiquetées uniquement d'après leurs titres. Connectez une clé OpenRouter, chargez un modèle local ou connectez-vous à un forfait payant, puis remplacez le document pour obtenir des étiquettes plus fines.

## Remplacer un document et historique des versions

Quand votre message house change, cliquez sur **Remplacer** et importez le nouveau fichier. Hi, Moose le compare à la version précédente et ne relit que les sections modifiées. Le document indique combien de sections ont été ajoutées, modifiées et retirées.

Les cinq dernières versions de chaque document restent listées sous **Versions**. Importer un fichier identique ne change rien.

Cliquez sur **Retirer** pour supprimer un document avec toutes ses versions et sections. Les briefs et brouillons déjà rédigés conservent leur contenu.

## Voir ce que Moose utilisera

Avant d'écrire, vous pouvez vérifier quelles sections un travail irait chercher. Sous **Voir ce que Moose utilisera**, saisissez un sujet ou le type de contenu que vous comptez écrire (par exemple « post LinkedIn sur la sécurité du code généré par IA pour des ingénieurs sécurité ») et cliquez sur **Afficher les sections**.

Hi, Moose liste les sections qu'il irait chercher. Cliquez sur **Afficher le texte exact que reçoit Moose** pour voir le texte complet qu'il recevrait. Si aucune section ne correspond assez, vos règles toujours actives s'appliquent quand même.

## Remplir Brand Voice et Brand Truth depuis vos documents

Si vos documents décrivent déjà votre voix, votre public, vos offres et vos concurrents, inutile de les ressaisir dans la [Brand Voice](brand-voice.md) et le [Brand Truth Profile](brand-truth-profile.md).

1. Sur l'écran Documents de marque, cliquez sur **Remplir les profils depuis les documents**.
2. Hi, Moose lit vos documents et propose des valeurs pour les champs de la Brand Voice et du Brand Truth Profile.
3. Passez en revue les suggestions. Chacune affiche la citation de votre document qui l'appuie.
4. Choisissez les champs voulus et cliquez sur **Appliquer**.

Rien n'est enregistré tant que vous n'appliquez pas. Voici comment les suggestions sont cochées :

- Les champs **Vide aujourd'hui** sont cochés par défaut.
- Les champs **Différent de la valeur actuelle** sont décochés, pour que votre propre formulation l'emporte sauf si vous en décidez autrement. La valeur actuelle s'affiche à côté de la suggestion.
- Une suggestion est écartée si le texte cité n'apparaît pas mot pour mot dans votre document. La boîte de dialogue indique combien ont été écartées.

Champs que Hi, Moose peut remplir :

- **Brand Voice :** nom de la marque, résumé, public, ton, style rédactionnel, valeurs de la marque, termes de marque secondaires, terminologie privilégiée et à éviter, et éléments de preuve.
- **Brand Truth Profile :** la façon dont l'IA doit décrire l'entreprise, les segments de client idéal et leurs notes, les produits et services, les capacités clés, les erreurs de représentation courantes, les discours obsolètes, le vocabulaire privilégié et à éviter, les concurrents, les affirmations sensibles et les erreurs les plus dommageables.

Le remplissage des profils nécessite un modèle : une clé OpenRouter, un modèle local ou un forfait payant.

## Où vos documents sont utilisés

Dès qu'un projet contient des documents de marque, Hi, Moose s'en sert dans :

- les [Content Briefs](../../features/content-briefs.md), les [brouillons d'articles de blog](../../features/blog-post-draft.md), les [Key Points](../../features/key-points.md) et le [générateur de FAQ](../../features/faq-generator.md). Chacun reçoit vos règles toujours actives et les sections qui correspondent le mieux au sujet ;
- le [Chat](../../chat/overview.md). Vos règles font partie de chaque conversation, et le chat peut chercher dans vos documents quand une question demande des détails sur un produit, un persona ou une preuve ;
- les recherches de [Send Moose](../../send-moose/overview.md) et la passe de finition du contenu généré, qui reçoivent toutes deux vos règles.

Les documents de marque fonctionnent avec la Brand Voice et le Brand Truth Profile. Ces profils restent le résumé court de qui vous êtes. Vos documents apportent tout le détail qui se trouve derrière.

## Stockage et synchronisation

Les documents de marque sont enregistrés en local pour le projet en cours. Sur un forfait payant, ils se synchronisent avec le reste de votre projet : toute votre équipe dispose des mêmes documents, et ils sont sauvegardés. Pendant que les modifications d'un collègue arrivent, l'écran affiche **Synchronisation depuis votre équipe...**.

Supprimer un projet supprime aussi ses documents de marque.
