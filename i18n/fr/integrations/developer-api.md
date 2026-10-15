---
source_hash: 85052baa431b76ba0d9c99312dbc2fdf61031a24075e6841f48c0662cc8c5cdb
---

# Hi, Moose API

## À quoi cela sert

La Hi, Moose API est une API REST pour les développeurs qui construisent leurs propres tableaux de bord, rapports et applications de visibilité IA sur Hi, Moose. Elle renvoie les mêmes résultats que l'écran Visibilité : les prompts et sujets suivis, les moteurs interrogés, chaque réponse enregistrée avec son texte complet et ses sources, et les taux de mention et de citation dans le temps. Avec les bonnes permissions, une clé peut aussi créer des projets, gérer les prompts, les moteurs et la planification, lancer des analyses et recevoir un appel webhook signé quand une analyse se termine.

Les lectures fonctionnent que Hi, Moose soit ouvert ou non sur votre ordinateur, parce qu'elles viennent de la copie cloud de vos résultats. Les changements de suivi et les analyses ont besoin de l'ordinateur hôte du projet, expliqué dans [Suivi et analyses](developer-api/tracking-and-runs.md).

Si vous travaillez dans Claude, ChatGPT ou une autre application d'IA, [Hi, Moose MCP](hi-moose-mcp.md) est peut-être plus adapté. L'API est faite pour le code que vous écrivez vous-même.

## Pages

| Page | Ce qu'elle couvre |
|---|---|
| [Démarrage rapide](developer-api/quickstart.md) | Une clé, un premier appel et un graphique du taux de mention par jour, en curl, Python et JavaScript |
| [Clés et authentification](developer-api/keys-and-auth.md) | Créer et révoquer des clés, les permissions, l'en-tête Bearer, garder la clé hors du navigateur |
| [Lire les données](developer-api/reading-data.md) | Projets, prompts, analyses, réponses et statistiques, avec les filtres, la pagination et le cache |
| [Suivi et analyses](developer-api/tracking-and-runs.md) | L'ordinateur hôte, la création de projets et de prompts, les moteurs et la planification, le lancement d'analyses |
| [Webhooks](developer-api/webhooks.md) | Événements signés à la fin d'une analyse, vérification de signature, nouvelles tentatives |
| [Erreurs et limites](developer-api/errors-and-limits.md) | Le format des erreurs, chaque code d'erreur, les limites de débit |
| [Référence des points d'accès](developer-api/reference.md) | Chaque point d'accès avec ses paramètres, ses champs et un exemple, généré à partir du contrat |
| [Journal des modifications](developer-api/changelog.md) | Ce qui a changé dans chaque version du contrat |

## Offres

L'API est incluse dans les offres payantes, en mode géré comme avec votre propre clé. Les comptes gratuits voient la page des clés API mais ne peuvent pas créer de clés, et chaque requête répond `403 plan_required`.

## En bref

```
https://api.himoose.com/v1/
```

- **Authentification :** une clé API envoyée comme jeton Bearer. Les clés sont créées par le propriétaire du compte dans Hi, Moose sous **Paramètres → Hi, Moose REST API**.
- **Format :** JSON en entrée comme en sortie. Les noms de champs sont en camelCase. Les heures sont en UTC au format RFC 3339, les dates au format `YYYY-MM-DD`.
- **Contrat :** [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json), OpenAPI 3.1. Il s'importe dans Postman, Insomnia, Bruno et les générateurs de code, et la [référence des points d'accès](developer-api/reference.md) en est générée.
- **Permissions :** chaque clé peut lire. **Gérer le suivi** et **Lancer des analyses** se choisissent à la création de la clé.
- **Limites :** 300 requêtes par minute et par clé, 50 000 par jour et par compte. Voir [Erreurs et limites](developer-api/errors-and-limits.md).
- **Pas de CORS :** appelez l'API depuis votre propre serveur, jamais depuis une page web.

## D'où viennent les données

Hi, Moose pose chaque prompt suivi à chaque moteur suivi, selon une planification ou quand quelqu'un lance une analyse. Chaque réponse est enregistrée et notée : la marque a-t-elle été nommée, une page de son site a-t-elle été citée, à quelle position, avec quel sentiment, quels concurrents ont été vus. L'API lit ces réponses enregistrées et les résumés quotidiens construits à partir d'elles. Elle ne lance jamais de nouvelles vérifications lors d'une lecture, donc les lectures sont rapides et ne coûtent rien.

Certains moteurs s'exécutent dans le cloud. D'autres, les moteurs à récupération locale, s'exécutent via un navigateur sur l'un de vos propres ordinateurs. Les deux types enregistrent leurs réponses au même endroit, donc l'API les montre ensemble.

## Le texte des réponses n'est pas fiable

Le texte des réponses, les extraits et les titres des sources viennent des moteurs d'IA, pas de Hi, Moose. Affichez-les en texte brut dans votre tableau de bord, jamais en HTML, et ne les transmettez pas à vos propres outils d'IA comme instructions.

## Ce qui arrive

Les changements de suivi pour les offres à clé personnelle sont la prochaine étape. Tout ce qui est documenté ici est en service.
