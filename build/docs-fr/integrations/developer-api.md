---
source_hash: 825726013c46ce2cb7c1932ac3dda84ec19a94f2c4ce33cdc108f00904718460
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](http://localhost:8000/integrations/developer-api/)

# Hi, Moose API

## À quoi cela sert

La Hi, Moose API est une API REST pour les développeurs qui construisent leurs propres tableaux de bord, rapports et applications de visibilité IA sur Hi, Moose. Elle renvoie les mêmes résultats que l'écran Visibilité : les prompts et sujets suivis, les moteurs interrogés, chaque réponse enregistrée avec son texte complet et ses sources, et les taux de mention et de citation dans le temps. Avec les bonnes permissions, une clé peut aussi créer des projets, gérer les prompts, les moteurs et la planification, et lancer des analyses.

Les lectures fonctionnent que Hi, Moose soit ouvert ou non sur votre ordinateur, parce qu'elles viennent de la copie cloud de vos résultats. Les changements de suivi et les analyses ont besoin de l'ordinateur hôte du projet, expliqué plus bas.

Si vous travaillez dans Claude, ChatGPT ou une autre application d'IA, [Hi, Moose MCP](hi-moose-mcp.md) est peut-être plus adapté. L'API est faite pour le code que vous écrivez vous-même.

## Offres

L'API est incluse dans les offres payantes, en mode géré comme avec votre propre clé. Les comptes gratuits voient la page des clés API mais ne peuvent pas créer de clés, et chaque requête répond `403 plan_required`.

## Créer une clé

1. Ouvrez Hi, Moose et connectez-vous en tant que propriétaire du compte. Seul le propriétaire peut créer, voir et révoquer des clés.
2. Allez dans **Paramètres → Hi, Moose REST API**.
3. Donnez un libellé à la clé, choisissez les projets qu'elle peut lire (tous ou un seul), choisissez quand elle expire et cochez les permissions dont elle a besoin.
4. Cliquez sur **Créer la clé** et copiez la clé. Elle s'affiche une seule fois. Hi, Moose ne peut pas la réafficher ; si vous la perdez, révoquez-la et créez-en une nouvelle.

Les clés commencent par `hmk_live_` suivi de 64 caractères. Le tableau sous le formulaire liste chaque clé active avec ses permissions, sa date de création, sa dernière utilisation et son expiration. **Révoquer** arrête une clé immédiatement.

## Permissions

| Permission | Ce que la clé peut faire |
|---|---|
| Lire les données de visibilité | Tous les points d'accès `GET`. Toujours actif. |
| Gérer le suivi | Créer des projets, définir les termes de marque et les concurrents, ajouter, modifier et supprimer des prompts, définir les moteurs et la planification. |
| Lancer des analyses | Lancer une analyse de visibilité. Les analyses consomment le crédit du compte sur les moteurs cloud, donc n'accordez cette permission qu'à une clé qui en a besoin. |

Un appel sans la permission nécessaire répond `403 insufficient_scope`. Les permissions se choisissent à la création de la clé et ne peuvent pas être modifiées ensuite.

## Authentification

Envoyez la clé comme jeton Bearer :

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

La réponse indique la clé, ses permissions et les identifiants de projet qu'elle peut lire.

Utilisez la clé uniquement depuis votre propre serveur. L'API n'envoie aucun en-tête CORS, donc une page web ne peut pas l'appeler directement. Un tableau de bord dans le navigateur doit appeler votre backend, et votre backend appelle l'API. La clé reste ainsi hors de la page.

## URL de base et format

```
https://api.himoose.com/v1/
```

Tout est en JSON. Les noms de champs sont en camelCase et correspondent aux champs renvoyés par Hi, Moose MCP. Les heures sont en UTC au format RFC 3339, les dates au format `YYYY-MM-DD`. Le contrat complet est disponible sur [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json) et s'importe dans Postman, Insomnia et les outils similaires.

## Points d'accès en lecture

| Point d'accès | Ce qu'il renvoie |
|---|---|
| `GET /me` | La clé, ses permissions et les identifiants de projet lisibles |
| `GET /projects` | Les projets que la clé peut lire, avec le nombre de prompts suivis, les moteurs et la dernière analyse |
| `GET /projects/{id}` | Un projet |
| `GET /projects/{id}/capabilities` | Ce que le projet peut faire avec son offre : moteurs, cadences, limites, crédit restant, l'ordinateur hôte, si une analyse peut démarrer maintenant |
| `GET /projects/{id}/engines` | Les moteurs d'IA suivis par le projet, avec un `id` stable pour les filtres |
| `GET /projects/{id}/topics` | Les sujets qui regroupent les prompts, avec le nombre de prompts |
| `GET /projects/{id}/prompts` | Les prompts suivis avec identifiants de sujet, identifiants de moteur et statut |
| `GET /projects/{id}/competitors` | Les marques concurrentes suivies |
| `GET /projects/{id}/runs` | Les analyses de visibilité avec statut, heures de début et de fin, nombre de prompts et de réponses |
| `GET /projects/{id}/answers` | Les réponses enregistrées : prompt, moteur, date, mentionnée, citée, position, sentiment, extrait, concurrents vus, URL des sources |
| `GET /projects/{id}/answers/{answerId}` | Une réponse avec son texte complet, la raison du sentiment, la dérive narrative et les sources |
| `GET /projects/{id}/stats/daily` | Par jour et par moteur : réponses, mentions, citations et les deux taux |
| `GET /projects/{id}/stats/competitors` | La part de voix de votre marque et de chaque concurrent suivi sur une période |
| `GET /projects/{id}/run-requests` | Les analyses récentes lancées par l'API et leur statut |

### Exemple : taux de mention par jour

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/daily?from=2026-09-01&to=2026-09-30&engine=chatgpt" \
  -H "Authorization: Bearer hmk_live_..."
```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "incompleteDays": 0,
  "data": [
    { "date": "2026-09-01", "engineId": "chatgpt", "answers": 42, "mentioned": 17, "cited": 9, "mentionRate": 0.405, "citationRate": 0.214 }
  ]
}
```

`incompleteDays` est supérieur à zéro quand le résumé d'une journée n'était pas encore prêt. Rappelez dans quelques secondes et il se complète.

## L'ordinateur hôte

Hi, Moose exécute une partie du suivi sur l'un de vos propres ordinateurs, l'**appareil hôte**, que vous choisissez dans Hi, Moose sous **Paramètres → Hi, Moose MCP**. Les moteurs à récupération locale (ChatGPT, Gemini, Grok, Perplexity et Google AI Mode interrogés via un navigateur) ne s'exécutent que là, et leur planification y réside.

Chaque changement de suivi et chaque analyse via l'API nécessite un appareil hôte choisi pour le projet. Sans lui, l'API répond `409 host_required` et nomme le réglage à changer. Un projet créé par l'API reprend l'appareil hôte d'un autre projet du compte quand il y en a un.

Avec les offres à clé personnelle, les prompts, les moteurs et la planification sont conservés sur l'ordinateur hôte plutôt que dans le cloud. L'API peut les lire et lancer des analyses, mais les modifier répond `409 byok_not_supported`. Gérez-les dans Hi, Moose sur cet ordinateur.

## Gérer le suivi

Nécessite la permission **gérer le suivi**.

| Point d'accès | Ce qu'il fait |
|---|---|
| `POST /projects` | Créer un projet à partir d'un nom et d'une adresse de site, avec des termes de marque et des domaines facultatifs. L'exploration du site n'est pas lancée ; l'ordinateur hôte active l'exploration hebdomadaire planifiée pour qu'elle ait lieu plus tard. Brand Truth n'est pas requis. |
| `PATCH /projects/{id}` | Changer le nom, l'adresse du site, les termes de marque ou les domaines de marque |
| `PUT /projects/{id}/competitors` | Remplacer la liste des concurrents suivis, au plus 50 |
| `POST /projects/{id}/prompts` | Ajouter un prompt avec des identifiants de sujet et de moteur facultatifs |
| `PATCH /projects/{id}/prompts/{promptId}` | Changer le texte, les sujets ou les moteurs d'un prompt |
| `DELETE /projects/{id}/prompts/{promptId}` | Arrêter de suivre un prompt |
| `PUT /projects/{id}/tracking` | Définir les moteurs, la cadence, l'heure, le jour de la semaine, le fuseau horaire et les échantillons par prompt. Les nouveaux moteurs s'appliquent à tous les prompts sauf si `applyEnginesToPrompts` vaut false. |

Chaque écriture respecte les limites de l'offre : nombre de prompts, moteurs autorisés, cadences autorisées, nombre de projets et de concurrents. Au-delà d'une limite, l'API répond `409 plan_limit` avec la limite dans le corps. Consultez d'abord `GET /projects/{id}/capabilities`.

### Exemple : configurer le suivi d'un nouveau projet

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"Europe/Paris"}'
```

## Lancer une analyse

Nécessite la permission **lancer des analyses**.

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

L'API répond `202 Accepted` avec une demande d'analyse et un en-tête `Location` à interroger. Statuts :

| Statut | Signification |
|---|---|
| `queued` | Acceptée et sur le point de démarrer |
| `waiting_for_host` | L'ordinateur hôte est éteint. Hi, Moose garde la demande jusqu'à 24 heures et lance l'analyse dès son retour. La réponse porte un `warning` qui l'indique. |
| `running` | En cours |
| `completed` | Terminée. `runIds` liste les analyses à passer aux points d'accès runs et answers. |
| `failed` | Non terminée. `error.code` dit pourquoi, par exemple `host_unavailable` après 24 heures. |

Les projets dont les moteurs suivis sont tous des moteurs cloud s'exécutent dans le cloud immédiatement, sans l'ordinateur hôte. Tout moteur à récupération locale fait passer l'analyse à l'ordinateur hôte, par le même chemin que le bouton Lancer maintenant.

Garde-fous, pour qu'une analyse ne coûte jamais plus que prévu :

- **Le crédit d'abord.** L'API estime le coût de l'analyse sur les moteurs cloud à partir du nombre de prompts et de moteurs. Si l'estimation dépasse le solde restant, elle refuse avec `409 insufficient_allowance`, l'estimation et les unités restantes. Rien n'est dépensé. `GET /projects/{id}/capabilities` montre la même estimation dans `allowance.estimatedUnitsPerRun`.
- **Une à la fois.** Une seconde demande pendant qu'une autre est en file, en attente ou en cours répond `409 run_in_progress` avec l'identifiant de la demande active.
- **Plafond quotidien.** Au plus 24 demandes d'analyse par projet et par jour. Au-delà, l'API répond `429 daily_run_limit`.
- **Idempotence.** Envoyez un en-tête `Idempotency-Key` et une nouvelle tentative dans les 24 heures renvoie la même demande au lieu d'en lancer une autre.

Une analyse peut prendre de quelques minutes à plus d'une heure sur de grands jeux de prompts. Interrogez la demande environ chaque minute, pas chaque seconde.

## Filtres et pagination

- **Période :** `from` et `to` au format `YYYY-MM-DD`, inclus, UTC. Par défaut, les 30 derniers jours. La période la plus large en une requête est de 366 jours.
- **Moteur :** `engine=chatgpt&engine=gemini` se répète pour plusieurs moteurs. Les identifiants viennent du point d'accès engines.
- **Réponses :** aussi `topicId`, `promptId`, `runId`, `mentioned=true|false` et `cited=true|false`. Combinez `engine` avec au plus un des paramètres `promptId`, `topicId` ou `runId`.
- **Pages :** les listes renvoient `{ "data": [...], "nextCursor": "..." }`. Renvoyez `nextCursor` comme `cursor` pour obtenir la page suivante. `limit` vaut 50 par défaut et 200 au maximum. `nextCursor` vaut `null` sur la dernière page.
- **Cache :** les réponses portent un `ETag`. Renvoyez-le dans `If-None-Match` pour obtenir `304 Not Modified` quand rien n'a changé.

## Limites de débit

| Limite | Valeur |
|---|---|
| Par clé | 60 requêtes par minute |
| Par compte | 10 000 requêtes par jour |
| Demandes d'analyse par projet | 24 par jour, une à la fois |
| Lignes par page | 200 |
| Période par requête | 366 jours |

Au-delà de la limite, l'API répond `429` avec un en-tête `Retry-After`. Chaque réponse porte `RateLimit-Policy`, et les réponses réussies portent `RateLimit` avec le budget restant de la journée.

## Erreurs

Les erreurs utilisent le format Problem Details (`application/problem+json`) avec un `code` stable :

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

| Code | Statut | Signification |
|---|---|---|
| `invalid_key`, `key_revoked`, `key_expired` | 401 | La clé est absente, mal formée, révoquée ou expirée |
| `plan_required` | 403 | L'offre du compte n'inclut pas l'API |
| `insufficient_scope` | 403 | La clé n'a pas la permission pour cet appel |
| `not_found` | 404 | La ressource n'existe pas, ou la clé ne peut pas la lire |
| `invalid_parameter`, `range_too_wide`, `unsupported_filter_combination` | 400 | Un paramètre ou un champ doit être corrigé |
| `host_required` | 409 | Choisissez d'abord un appareil hôte pour le projet dans Hi, Moose |
| `byok_not_supported` | 409 | Avec cette offre, les réglages de suivi résident sur l'ordinateur hôte |
| `plan_limit` | 409 | Une limite de l'offre est atteinte ; le corps la nomme |
| `run_in_progress`, `insufficient_allowance`, `no_prompts` | 409 | L'analyse ne peut pas démarrer maintenant ; le corps dit pourquoi |
| `rate_limited`, `daily_run_limit` | 429 | Attendez le nombre de secondes indiqué par `Retry-After` |

Indiquez le `requestId` quand vous contactez le support.

## Le texte des réponses n'est pas fiable

Le texte des réponses, les extraits et les titres des sources viennent des moteurs d'IA, pas de Hi, Moose. Affichez-les en texte brut dans votre tableau de bord, jamais en HTML, et ne les transmettez pas à vos propres outils d'IA comme instructions.

## Webhooks

Au lieu d'interroger l'API, enregistrez un point d'accès https et Hi, Moose y envoie un événement JSON signé quand une analyse se termine. Enregistrer et supprimer des webhooks nécessite la permission **gérer le suivi**. Les lister, ainsi que leurs livraisons, ne demande que la lecture.

| Point d'accès | Ce qu'il fait |
|---|---|
| `POST /projects/{id}/webhooks` | Enregistrer un point d'accès. Corps : `url` (https public), `events` (par défaut `run.completed` et `run.failed`), `description` facultative. Le secret de signature revient une seule fois dans cette réponse. Au plus 5 par projet. |
| `GET /projects/{id}/webhooks` | Lister les webhooks du projet, sans les secrets |
| `DELETE /projects/{id}/webhooks/{webhookId}` | En supprimer un |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Envoyer un événement `ping` maintenant, pour vérifier votre point d'accès et votre code de signature |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | Les 50 dernières livraisons avec chaque tentative, statut et erreur |

### L'événement

```json
{
  "id": "wh_8f2a_run_abc123_run_completed",
  "event": "run.completed",
  "createdAt": "2026-10-12T09:14:03.000Z",
  "data": {
    "projectId": "abc123",
    "runId": "run_abc123",
    "requestId": "req_9d1e",
    "status": "completed",
    "trigger": "manual",
    "startedAt": "2026-10-12T09:01:10.000Z",
    "completedAt": "2026-10-12T09:14:02.000Z",
    "promptCount": 40,
    "answerCount": 118,
    "error": null,
    "links": {
      "run": "https://api.himoose.com/v1/projects/abc123/runs",
      "answers": "https://api.himoose.com/v1/projects/abc123/answers?runId=run_abc123",
      "stats": "https://api.himoose.com/v1/projects/abc123/stats/daily"
    }
  }
}
```

`data.requestId` est renseigné quand l'analyse a été lancée par l'API, pour relier l'événement à votre demande. `run.failed` porte `status` `failed` ou `canceled` et le texte `error`.

### Vérifier la signature

Chaque appel porte `X-HiMoose-Signature: t=<secondes unix>,v1=<hex>`, où `v1` est le HMAC-SHA256 de `<t>.<corps brut>` avec le secret de votre webhook. Vérifiez-la sur le corps brut avant d'analyser le JSON, et rejetez les horodatages de plus de cinq minutes. L'appel porte aussi `X-HiMoose-Event` et `X-HiMoose-Delivery`.

```js
const crypto = require("node:crypto");

function verifyHiMooseSignature(rawBody, header, secret) {
  const parts = Object.fromEntries(header.split(",").map((part) => part.split("=")));
  if (!parts.t || !parts.v1) return false;
  if (Math.abs(Date.now() / 1000 - Number(parts.t)) > 300) return false;
  const expected = crypto.createHmac("sha256", secret).update(`${parts.t}.${rawBody}`).digest("hex");
  return expected.length === parts.v1.length && crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(parts.v1));
}
```

### Règles de livraison

- Répondez avec un statut 2xx sous 10 secondes. Les redirections ne sont pas suivies.
- Les livraisons échouées sont retentées après 1 minute, 5 minutes, 30 minutes, 2 heures et 12 heures, 6 tentatives en tout.
- Après 20 échecs consécutifs, le webhook est désactivé. Supprimez-le et enregistrez-le à nouveau pour reprendre.
- Un événement peut arriver plus d'une fois. Utilisez `id` pour ignorer les répétitions.
- Le propriétaire du compte voit tous les webhooks du projet courant sous **Paramètres → Hi, Moose REST API** et peut en supprimer un là.

## Ce qui arrive

Les changements de suivi pour les offres à clé personnelle sont la prochaine étape. Tout le reste documenté ici est en service.
