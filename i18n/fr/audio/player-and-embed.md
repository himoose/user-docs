---
source_hash: b5d0a07f31228ccaaa2c18a76dddb8de404f3871f7b879591e111c89bae3e9c5
---
# Lecteur et intégration

## À quoi cela sert

Adapter le style du lecteur audio intégré à la page qui va l'accueillir, puis copier le code d'intégration. Ouvrez-le depuis un épisode terminé avec **Customize player**, ou depuis l'action d'intégration de l'onglet **History**.

## Options du lecteur

- **Thème** : Dark, Light ou Auto. Auto suit le réglage de l'appareil de chaque visiteur.
- **Disposition** : Full ou Compact.
- **Couleur d'accent** : n'importe quelle valeur hexadécimale à 6 chiffres, par exemple `#5688b0`.
- **Afficher le titre** : désactivez-le lorsque l'intégration se place sous votre propre titre.
- **Titre personnalisé** : laissez vide pour utiliser le titre de l'épisode.
- **Bouton de transcription** : affichez ou masquez le bouton de transcription du lecteur.

Un aperçu en direct se met à jour à mesure que vous modifiez les réglages. Si le script du lecteur est inaccessible pendant l'aperçu, celui-ci se rabat sur un balisage simple ; le code d'intégration copié reste correct.

## Copier le code d'intégration

Cliquez sur **Copy embed code** et collez-le dans votre page.

- **WordPress** : collez-le dans le bloc HTML ou code de l'article, ou utilisez le [plugin Listen to This Article](https://wordpress.org/plugins/listen-to-this-article/).
- **Webflow** : collez-le dans un élément Embed.
- **Grav** : collez-le dans le contenu de la page, là où le HTML brut est autorisé.

## La lecture est restreinte par domaine

L'audio généré ne se lit que sur le domaine du site web de votre projet et sur `himoose.com`. Ce réglage provient du champ site web du projet, et c'est la raison pour laquelle ce champ doit être renseigné avant toute génération. Si vous intégrez le lecteur sur un domaine non autorisé, la lecture sera refusée.

## Attribution d'agence

Sur les forfaits avec [marque blanche](../agency/white-label.md), le lecteur intégré peut porter l'attribution de votre agence plutôt que celle de Hi, Moose. Cela se règle dans **Paramètres → Branding** :

- **Attribution de l'intégration audio** : le texte affiché sur le lecteur. Laissez-le vide pour utiliser « Audio by » suivi du nom de votre agence.
- **Lien d'attribution** : une adresse `https://` complète. Laissez-le vide pour réutiliser votre lien de marque principal.

L'attribution constitue un véritable lien de retour vers votre site depuis chaque page client portant le lecteur, et c'est tout son intérêt pour les agences.

!!! warning "L'attribution s'applique au code copié après enregistrement"
    Modifier la marque ne réécrit pas les intégrations déjà en place. Recopiez le code d'intégration après enregistrement pour récupérer la nouvelle attribution.

## En quoi cela aide l'AEO

La transcription ajoute à la page un texte structuré, propriétaire et explorable. C'est du contenu réel supplémentaire qu'un moteur de réponse peut récupérer et citer, et cela peut renforcer les signaux d'extractibilité et d'exhaustivité d'une [AEO audit](../features/aeo-audits.md). Ce n'est pas en soi un critère noté de « présence multimédia » : la valeur réside dans le texte que le lecteur apporte avec lui.
