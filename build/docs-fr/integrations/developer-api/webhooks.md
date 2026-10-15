---
source_hash: 6467de19290f42e43d33241a37345989dbd6267011d89947d750f7e073ea66e2
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/integrations/developer-api/webhooks/)


# Webhooks

Au lieu d'interroger l'API, enregistrez un point d'accès https et Hi, Moose y envoie un événement JSON signé quand une analyse se termine. Enregistrer, tester et supprimer des webhooks nécessite la permission **gérer le suivi**. Les lister, ainsi que leurs livraisons, ne demande que la lecture.

## Points d'accès

| Point d'accès | Ce qu'il fait |
|---|---|
| `POST /projects/{id}/webhooks` | Enregistrer un point d'accès. Corps : `url` (https public), `events` (par défaut `run.completed` et `run.failed`), `description` facultative. Le secret de signature revient une seule fois dans cette réponse. Au plus 5 par projet. |
| `GET /projects/{id}/webhooks` | Lister les webhooks du projet, sans les secrets |
| `DELETE /projects/{id}/webhooks/{webhookId}` | En supprimer un |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Envoyer un événement `ping` maintenant, pour vérifier votre point d'accès et votre code de signature |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | Les 50 dernières livraisons avec chaque tentative, statut et erreur |

## En enregistrer un

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"url":"https://reports.acme.example/himoose","description":"Nightly dashboard refresh"}'
```

```json
{
  "id": "BGXhe1dlOnmy36j6rRTa",
  "url": "https://reports.acme.example/himoose",
  "events": ["run.completed", "run.failed"],
  "description": "Nightly dashboard refresh",
  "active": true,
  "createdAt": "2026-10-15T03:20:10.000Z",
  "secret": "whsec_..."
}
```

Stockez `secret` à côté de votre clé. Il ne s'affiche que dans cette réponse. L'URL doit être publique et en https ; les adresses privées, localhost et le http simple sont refusés avec `400 invalid_parameter`.

Envoyez-vous ensuite un ping :

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/test \
  -H "Authorization: Bearer hmk_live_..."
```

La réponse est l'enregistrement de livraison, et le point d'accès deliveries montre la tentative avec le statut HTTP renvoyé par votre point d'accès.

## L'événement

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

| Événement | Quand |
|---|---|
| `run.completed` | Une analyse s'est terminée et ses réponses sont enregistrées. Les analyses planifiées, celles du bouton Lancer maintenant et celles de l'API comptent toutes. |
| `run.failed` | Une analyse s'est terminée avec `status` `failed` ou `canceled`. `data.error` dit pourquoi. |
| `ping` | Envoyé par le point d'accès de test. `data` porte l'identifiant du projet et un message. |

`data.requestId` est renseigné quand l'analyse a été lancée par l'API, pour relier l'événement à votre demande d'analyse. Il vaut `null` pour les analyses planifiées et celles lancées dans Hi, Moose.

L'événement est un signal, pas les données. Sur `run.completed`, suivez `data.links.answers` ou rafraîchissez vos statistiques quotidiennes. Les résumés quotidiens des jours de l'analyse sont reconstruits dans les dix minutes suivant sa fin ; `incompleteDays` dans la réponse des statistiques indique quand ils ne sont pas encore prêts.

## En-têtes

| En-tête | Valeur |
|---|---|
| `X-HiMoose-Signature` | `t=<unix seconds>,v1=<hex>`, voir plus bas |
| `X-HiMoose-Event` | Le nom de l'événement |
| `X-HiMoose-Delivery` | L'identifiant de livraison, le même que sur le point d'accès deliveries |
| `User-Agent` | `HiMoose-Webhooks/1.0` |
| `Content-Type` | `application/json` |

## Vérifier la signature

`v1` est le HMAC-SHA256 de `<t>.<raw body>` avec le secret de votre webhook, en hexadécimal minuscule. Vérifiez-le sur le corps brut de la requête avant d'analyser le JSON, comparez en temps constant et rejetez les horodatages de plus de cinq minutes.

=== "JavaScript"

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

=== "Python"

    ```python
    import hashlib
    import hmac
    import time

    def verify_himoose_signature(raw_body: bytes, header: str, secret: str) -> bool:
        parts = dict(part.split("=", 1) for part in header.split(",") if "=" in part)
        if "t" not in parts or "v1" not in parts:
            return False
        if abs(time.time() - int(parts["t"])) > 300:
            return False
        expected = hmac.new(secret.encode(), f"{parts['t']}.".encode() + raw_body, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, parts["v1"])
    ```

La plupart des frameworks web analysent le JSON avant que votre code s'exécute. Assurez-vous de signer les octets tels que reçus, pas une copie resérialisée, sinon la signature ne correspondra pas.

## Règles de livraison

- Répondez avec un statut 2xx sous 10 secondes. Faites le travail après avoir répondu, pas avant. Les redirections ne sont pas suivies.
- Les livraisons échouées sont retentées après 1 minute, 5 minutes, 30 minutes, 2 heures et 12 heures, 6 tentatives en tout. Une livraison est `pending` tant qu'il reste des tentatives, `delivered` après un 2xx, `failed` après la dernière tentative.
- Après 20 échecs consécutifs, le webhook est désactivé, `active` passe à false et plus aucun événement n'est envoyé. Supprimez-le et enregistrez-le à nouveau pour reprendre.
- Un événement peut arriver plus d'une fois. Utilisez `id` pour ignorer les répétitions.
- Les événements d'un même projet peuvent arriver dans le désordre quand une nouvelle tentative intervient. Utilisez `createdAt` si l'ordre compte.

## Voir les livraisons

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/deliveries \
  -H "Authorization: Bearer hmk_live_..."
```

Chaque livraison liste chaque tentative avec son heure, le statut HTTP renvoyé par votre point d'accès, sa durée et l'erreur éventuelle. Quand un point d'accès se comporte mal, c'est le premier endroit où regarder.

Le propriétaire du compte voit tous les webhooks du projet courant sous **Paramètres → Hi, Moose REST API** avec le statut de leur dernière livraison, et peut en supprimer un là.
