---
source_hash: 422edf700d29e3ee080f114ca1c4fbdc3f92677eb196cdf636fdac1f0e5e4cad
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/integrations/developer-api/changelog/)


# Journal des modifications

La version du contrat est dans `info.version` de [openapi.json](https://api.himoose.com/v1/openapi.json) et dans le titre de la [référence des points d'accès](reference.md). L'URL de base reste `/v1` pour chaque version listée ici ; un changement incompatible recevrait une nouvelle URL de base et un long préavis.

## 1.2.1, 2026-10-15

Première version publique.

- **Lecture :** projets, moteurs, sujets, prompts, concurrents, analyses, réponses avec texte complet, statistiques quotidiennes, statistiques concurrents et capacités.
- **Gestion du suivi :** créer et modifier des projets, remplacer les concurrents, ajouter, modifier et supprimer des prompts, définir les moteurs et la planification.
- **Analyses :** lancer une analyse avec vérification du crédit, une à la fois, 24 par jour, avec clés d'idempotence et un statut à interroger.
- **Webhooks :** événements `run.completed` et `run.failed` avec signatures HMAC, nouvelles tentatives et journal des livraisons.
- **Limites :** 300 requêtes par minute et par clé, 50 000 par jour et par compte.
- `PUT /projects/{id}/tracking` avec `engineIds` ne change que les moteurs par défaut. Les prompts existants conservent leurs moteurs sauf si `applyEnginesToPrompts` vaut `true`.

## Prévu

- Les changements de suivi sur les offres à clé personnelle, dont les réglages résident aujourd'hui sur l'ordinateur hôte.
- Les opportunités, la file de travail classée de l'onglet Opportunités.
