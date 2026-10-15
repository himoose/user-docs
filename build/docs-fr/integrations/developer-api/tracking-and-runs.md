---
source_hash: 638e427715918eeab4249561f6f095b46f57a8531e8ee857a78f4e07d0941c4e
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](https://himoose.com/docs/integrations/developer-api/tracking-and-runs/)


# Suivi et analyses

Changer ce que Hi, Moose suit nécessite la permission **gérer le suivi**. Lancer une analyse nécessite la permission **lancer des analyses**. Les deux se choisissent à la création de la clé, voir [Clés et authentification](keys-and-auth.md#permissions).

## L'ordinateur hôte

Hi, Moose exécute une partie du suivi sur l'un de vos propres ordinateurs, l'**appareil hôte**, que vous choisissez dans Hi, Moose sous **Paramètres → Hi, Moose MCP**. Les moteurs à récupération locale (ChatGPT, Gemini, Grok, Perplexity et Google AI Mode interrogés via un navigateur) ne s'exécutent que là, et leur planification y réside.

Chaque changement de suivi et chaque analyse via l'API nécessite un appareil hôte choisi pour le projet. Sans lui, l'API répond `409 host_required` et nomme le réglage à changer. Un projet créé par l'API reprend l'appareil hôte d'un autre projet du compte quand il y en a un.

Après un changement de suivi, l'API confie à l'ordinateur hôte une courte tâche pour récupérer les nouveaux réglages. L'hôte le fait en moins d'une minute tant que Hi, Moose y est ouvert, ou à sa prochaine ouverture. Les lectures montrent les nouveaux réglages immédiatement dans tous les cas.

Avec les offres à clé personnelle, les prompts, les moteurs et la planification sont conservés sur l'ordinateur hôte plutôt que dans le cloud. L'API peut les lire et lancer des analyses, mais les modifier répond `409 byok_not_supported`. Gérez-les dans Hi, Moose sur cet ordinateur.

`GET /projects/{id}/capabilities` vous renseigne avant d'écrire : l'offre, les moteurs et cadences autorisés, les limites, l'ordinateur hôte et s'il est en ligne, et si une analyse pourrait démarrer maintenant.

## Gérer le suivi

| Point d'accès | Ce qu'il fait |
|---|---|
| `POST /projects` | Créer un projet à partir d'un nom et d'une adresse de site, avec des termes de marque et des domaines facultatifs. L'exploration du site n'est pas lancée ; l'ordinateur hôte active l'exploration hebdomadaire planifiée pour qu'elle ait lieu plus tard. Brand Truth n'est pas requis. |
| `PATCH /projects/{id}` | Changer le nom, l'adresse du site, les termes de marque ou les domaines de marque |
| `PUT /projects/{id}/competitors` | Remplacer la liste des concurrents suivis, au plus 50 |
| `POST /projects/{id}/prompts` | Ajouter un prompt avec des identifiants de sujet et de moteur facultatifs |
| `PATCH /projects/{id}/prompts/{promptId}` | Changer le texte, les sujets ou les moteurs d'un prompt, ou reprendre un prompt en pause |
| `DELETE /projects/{id}/prompts/{promptId}` | Arrêter de suivre un prompt. Ses réponses enregistrées sont conservées. |
| `PUT /projects/{id}/tracking` | Définir les moteurs par défaut, la cadence, l'heure, le jour de la semaine, le fuseau horaire et les échantillons par prompt |

Chaque écriture respecte les limites de l'offre : nombre de prompts, moteurs autorisés, cadences autorisées, nombre de projets et de concurrents. Au-delà d'une limite, l'API répond `409 plan_limit` avec la limite dans le corps.

### Les moteurs des prompts

Chaque prompt a sa propre liste de moteurs. `PUT /projects/{id}/tracking` avec `engineIds` définit la valeur par défaut des prompts ajoutés ensuite et laisse chaque prompt existant tel quel. Pour changer les moteurs des prompts existants, envoyez `applyEnginesToPrompts: true` dans le même appel, ce qui applique la nouvelle liste à chaque prompt du projet, ou modifiez les prompts un par un avec `PATCH /projects/{id}/prompts/{promptId}`.

Un prompt sans moteur est conservé mais ignoré lors des analyses. `POST /projects/{id}/prompts` sans `engineIds` donne au nouveau prompt les moteurs par défaut du projet.

### Remplacer veut dire remplacer

`PUT /projects/{id}/competitors` remplace toute la liste. Envoyez la liste complète que vous voulez garder, pas seulement les ajouts. Une liste vide supprime tous les concurrents. Il en va de même pour `brandTerms` et `brandDomains` sur `PATCH /projects/{id}`.

### Exemple : configurer le suivi d'un nouveau projet

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"America/Chicago"}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/competitors \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '[{"name":"Competitor One","domain":"competitor-one.example"},{"name":"Competitor Two","domain":"competitor-two.example"}]'
```

Définir les moteurs avant d'ajouter les prompts fait que chaque nouveau prompt les reçoit par défaut.

### Planification

| Champ | Valeurs |
|---|---|
| `cadence` | `manual` (planification désactivée), `daily`, `weekdays`, `weekly` |
| `timeOfDay` | `HH:MM` dans le fuseau horaire du projet |
| `weeklyDay` | `monday` à `sunday`, utilisé par `weekly` |
| `timezone` | Un nom IANA comme `Europe/Berlin` |
| `samplesPerPrompt` | Combien de fois chaque prompt est posé par moteur lors d'une analyse. Plus d'échantillons consomment plus de crédit. |

L'offre décide des cadences autorisées ; le point d'accès capabilities les liste.

## Lancer une analyse

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

L'API répond `202 Accepted` avec une demande d'analyse et un en-tête `Location` à interroger :

```json
{
  "id": "NKxlhmW52Pkc2QwVD4oP",
  "status": "queued",
  "mode": "host",
  "createdAt": "2026-10-15T03:39:56.404Z",
  "updatedAt": "2026-10-15T03:39:56.404Z",
  "completedAt": null,
  "runIds": [],
  "promptCount": 5,
  "estimatedUnits": 0,
  "warning": null,
  "error": null,
  "host": { "online": true, "lastSeenAt": "2026-10-15T03:39:20.475Z" }
}
```

| Statut | Signification |
|---|---|
| `queued` | Acceptée et sur le point de démarrer |
| `waiting_for_host` | L'ordinateur hôte est éteint. Hi, Moose garde la demande jusqu'à 24 heures et lance l'analyse dès son retour. La réponse porte un `warning` qui l'indique. |
| `running` | En cours |
| `completed` | Terminée. `runIds` liste les analyses à passer aux points d'accès runs et answers. |
| `failed` | Non terminée. `error.code` dit pourquoi, par exemple `host_unavailable` après 24 heures. |
| `canceled` | Arrêtée depuis Hi, Moose avant la fin |

`mode` indique où l'analyse s'exécute. Les projets dont les moteurs suivis sont tous des moteurs cloud s'exécutent dans le cloud immédiatement, sans l'ordinateur hôte. Tout moteur à récupération locale fait passer l'analyse à l'ordinateur hôte, par le même chemin que le bouton Lancer maintenant. Dans les deux cas, le projet a besoin d'un ordinateur hôte choisi.

### Garde-fous

Pour qu'une analyse ne coûte jamais plus que prévu :

- **Le crédit d'abord.** L'API estime le coût de l'analyse sur les moteurs cloud à partir du nombre de prompts et de moteurs. Si l'estimation dépasse le solde restant, elle refuse avec `409 insufficient_allowance`, l'estimation et les unités restantes. Rien n'est dépensé. `GET /projects/{id}/capabilities` montre la même estimation dans `allowance.estimatedUnitsPerRun`.
- **Une à la fois.** Une seconde demande pendant qu'une autre est en file, en attente ou en cours répond `409 run_in_progress` avec l'identifiant de la demande active.
- **Plafond quotidien.** Au plus 24 demandes d'analyse par projet et par jour. Au-delà, l'API répond `429 daily_run_limit`.
- **Idempotence.** Envoyez un en-tête `Idempotency-Key` et une nouvelle tentative dans les 24 heures renvoie la même demande avec `200` et `replayed: true` au lieu de lancer une autre analyse.
- **Quelque chose à analyser.** Un projet sans aucun prompt doté d'un moteur répond `409 no_prompts`.

### Suivre une analyse

Interrogez `GET /projects/{id}/run-requests/{requestId}` environ une fois par minute. Une analyse peut prendre de quelques minutes à plus d'une heure sur de grands jeux de prompts. Une fois que `status` vaut `completed`, `runIds` contient l'analyse à lire :

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?runId=RUN_ID" \
  -H "Authorization: Bearer hmk_live_..."
```

Pour éviter d'interroger l'API, enregistrez un [webhook](webhooks.md). L'événement `run.completed` porte `requestId`, pour le relier à la demande que vous avez faite.

Les analyses lancées par l'API apparaissent dans Hi, Moose comme toute autre analyse, et dans le tableau **Tâches récentes des agents** sous **Paramètres → Hi, Moose MCP** avec le libellé de la clé.
