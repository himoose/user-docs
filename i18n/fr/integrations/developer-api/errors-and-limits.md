---
source_hash: 85fe7ea99ed19540350085410907cba880592b989251ce17fdb81570b24829a2
---

# Erreurs et limites

## Erreurs

Les erreurs utilisent le format Problem Details (`application/problem+json`, RFC 9457) avec un `code` stable sur lequel votre code peut s'appuyer :

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/errors-and-limits/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

- `code` est le champ à tester dans le code. Son sens ne change jamais.
- `detail` est écrit pour une personne et sa formulation peut changer.
- `type` renvoie à la section de la documentation pour ce type d'erreur.
- `requestId` identifie la requête. Indiquez-le quand vous contactez le support. Il est aussi envoyé dans l'en-tête `X-Request-Id` de chaque réponse.

Certaines erreurs portent des champs supplémentaires, nommés dans le tableau.

## Codes d'erreur

| Code | Statut | Signification | Que faire |
|---|---|---|---|
| `invalid_key` | 401 | Pas d'en-tête `Authorization`, une clé au mauvais format, ou une clé que Hi, Moose ne connaît pas | Envoyez `Authorization: Bearer hmk_live_...`. Vérifiez que la clé a été copiée en entier. |
| `key_revoked` | 401 | La clé a été révoquée dans les Paramètres | Créez une nouvelle clé. |
| `key_expired` | 401 | La clé a dépassé sa date d'expiration | Créez une nouvelle clé. |
| `plan_required` | 403 | L'offre du compte n'inclut pas l'API | Passez à une offre payante. |
| `insufficient_scope` | 403 | La clé n'a pas la permission pour cet appel. Le corps la nomme dans `scope`. | Créez une clé avec cette permission. |
| `not_found` | 404 | La ressource n'existe pas, ou la clé ne peut pas la lire. Les deux cas ne sont pas distingués. | Vérifiez l'identifiant et l'accès aux projets de la clé. |
| `method_not_allowed` | 405 | Le point d'accès existe mais pas avec cette méthode | Voir la [référence](reference.md). |
| `invalid_parameter` | 400 | Un paramètre de requête ou un champ du corps est absent, mal formé ou hors limites. `detail` le nomme. | Corrigez la requête. |
| `range_too_wide` | 400 | La période de `from` à `to` dépasse 366 jours | Demandez une période plus courte. |
| `unsupported_filter_combination` | 400 | Des filtres qui ne peuvent pas être combinés, par exemple `engine` avec deux des paramètres `promptId`, `topicId` et `runId` | Retirez un filtre. |
| `host_required` | 409 | Le projet n'a pas d'ordinateur hôte choisi | Choisissez-en un dans Hi, Moose sous **Paramètres → Hi, Moose MCP**. |
| `byok_not_supported` | 409 | Avec cette offre, les réglages de suivi résident sur l'ordinateur hôte, donc l'API ne peut pas les modifier | Modifiez-les dans Hi, Moose sur cet ordinateur. |
| `plan_limit` | 409 | Une limite de l'offre est atteinte. Le corps porte `limit`. | Consultez `GET /projects/{id}/capabilities` pour les limites. |
| `run_in_progress` | 409 | Une demande d'analyse est déjà en file, en attente ou en cours. Le corps porte `requestId` et `requestStatus`. | Attendez qu'elle se termine. |
| `insufficient_allowance` | 409 | L'analyse coûterait plus que le crédit restant. Le corps porte `estimatedUnits`, `remainingUnits` et `periodEndsAt`. | Rechargez, ou réduisez les prompts, les moteurs ou les échantillons. |
| `no_prompts` | 409 | Le projet n'a aucun prompt suivi doté d'un moteur | Ajoutez d'abord des prompts et des moteurs. |
| `rate_limited` | 429 | La limite par minute ou par jour est atteinte | Attendez le nombre de secondes indiqué par `Retry-After`. |
| `daily_run_limit` | 429 | Le projet a fait ses 24 demandes d'analyse du jour | Réessayez demain. |
| `internal` | 500 | Quelque chose a échoué côté Hi, Moose | Réessayez avec un délai croissant. Si cela persiste, contactez le support avec le `requestId`. |

Un `502` ou `503` sans corps signifie que l'API n'a pas pu joindre son backend. Réessayez avec un délai croissant.

## Limites de débit

| Limite | Valeur |
|---|---|
| Par clé | 300 requêtes par minute |
| Par compte | 50 000 requêtes par jour |
| Demandes d'analyse par projet | 24 par jour, une à la fois |
| Webhooks par projet | 5 |
| Lignes par page | 200 |
| Période par requête | 366 jours |

Au-delà de la limite, l'API répond `429 rate_limited` avec un en-tête `Retry-After`. Chaque réponse porte `RateLimit-Policy`, et les réponses réussies portent `RateLimit` avec le budget restant de la journée, selon le brouillon IETF des en-têtes de limite de débit :

```
RateLimit-Policy: "per-minute";q=300;w=60, "per-day";q=50000;w=86400
RateLimit: "per-day";r=49871;t=61234
```

La limite par minute est comptée par clé en bordure de réseau et reste approximative ; une courte rafale un peu au-dessus peut passer. La limite par jour est comptée par compte sur l'ensemble de ses clés.

## Rester sous les limites

- **Mettez en cache de votre côté.** Les statistiques quotidiennes portent `Cache-Control: max-age=60`. Un tableau de bord qui se rafraîchit chaque minute lit le résumé une fois par minute et par graphique, pas une fois par visiteur.
- **Utilisez les résumés.** Les statistiques quotidiennes et les statistiques concurrents sont construites à partir d'une table de résumé. Tracez vos graphiques à partir d'elles, et ne lisez les réponses individuelles que quand quelqu'un ouvre une ligne.
- **Utilisez les ETag.** Les réponses portent un `ETag`. Renvoyez-le dans `If-None-Match` et un `304` ne coûte presque rien.
- **Utilisez les webhooks** plutôt que d'interroger l'API pour savoir quand une analyse se termine. Voir [Webhooks](webhooks.md).
- **Patientez sur un 429.** Attendez le nombre de secondes de `Retry-After`, puis réessayez. Ne réessayez pas immédiatement.

## Identifiants de requête

Chaque réponse porte `X-Request-Id`. Consignez-le à côté de votre propre journal de requêtes pour qu'un signalement de problème puisse être rapproché des journaux de Hi, Moose. Les corps d'erreur le répètent dans `requestId`.
