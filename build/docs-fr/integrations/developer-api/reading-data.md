---
source_hash: 28ad9511fc5703f0dd6c90a7f591758445fdd08a95dcdb389dc29a304c90278d
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](http://localhost:8000/integrations/developer-api/reading-data/)


# Lire les données

Chaque clé peut lire. Les lectures viennent de la copie cloud de vos résultats, donc elles fonctionnent que Hi, Moose soit ouvert ou non sur votre ordinateur, et elles ne lancent jamais de nouvelles vérifications.

## Les points d'accès en lecture

| Point d'accès | Ce qu'il renvoie |
|---|---|
| `GET /me` | La clé, ses permissions et les identifiants de projet lisibles |
| `GET /projects` | Les projets que la clé peut lire, avec le nombre de prompts suivis, les moteurs et la dernière analyse |
| `GET /projects/{id}` | Un projet |
| `GET /projects/{id}/capabilities` | Ce que le projet peut faire avec son offre : moteurs, cadences, limites, crédit restant, l'ordinateur hôte, si une analyse peut démarrer maintenant |
| `GET /projects/{id}/engines` | Les moteurs d'IA suivis par le projet, avec un `id` stable pour les filtres et si chacun s'exécute dans le cloud ou sur l'ordinateur hôte |
| `GET /projects/{id}/topics` | Les sujets qui regroupent les prompts, avec le nombre de prompts |
| `GET /projects/{id}/prompts` | Les prompts suivis avec identifiants de sujet, identifiants de moteur et statut |
| `GET /projects/{id}/competitors` | Les marques concurrentes suivies et leurs domaines |
| `GET /projects/{id}/runs` | Les analyses de visibilité avec statut, heures de début et de fin, nombre de prompts et de réponses |
| `GET /projects/{id}/answers` | Les réponses enregistrées : prompt, moteur, date, mentionnée, citée, position, sentiment, extrait, concurrents vus, URL des sources |
| `GET /projects/{id}/answers/{answerId}` | Une réponse avec son texte complet, la raison du sentiment, la dérive narrative et les sources |
| `GET /projects/{id}/stats/daily` | Par jour et par moteur : réponses, mentions, citations et les deux taux |
| `GET /projects/{id}/stats/competitors` | La part de voix de votre marque et de chaque concurrent suivi sur une période |
| `GET /projects/{id}/run-requests` | Les analyses récentes lancées par l'API et leur statut |
| `GET /projects/{id}/webhooks` | Les webhooks du projet, sans les secrets |

Le détail champ par champ de chacun est dans la [référence des points d'accès](reference.md).

## Comment les données s'articulent

- Un **projet** suit un site. Il a des **prompts**, les questions posées, regroupés en **sujets**.
- Chaque prompt s'exécute sur un ou plusieurs **moteurs** : ChatGPT, Perplexity, Gemini et d'autres. Les identifiants de moteur comme `chatgpt` ou `chatgpt-local-fetch` viennent du point d'accès engines et sont les valeurs acceptées par chaque filtre `engine`.
- Une **analyse** pose chaque prompt actif à ses moteurs et enregistre une **réponse** par prompt, moteur et échantillon. Les analyses démarrent selon la planification du projet, depuis le bouton Lancer maintenant, ou depuis l'API.
- Chaque réponse est notée : `mentioned` quand la marque a été nommée, `cited` quand une page du site de la marque a été donnée comme source, plus `position`, `sentiment` et les **concurrents** vus.
- Les **statistiques quotidiennes** comptent les réponses par jour et par moteur et calculent `mentionRate` et `citationRate`. Les **statistiques concurrents** font de même par marque sur une période.

## Taux de mention par jour

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

Les taux sont des fractions de 0 à 1. Les jours sans réponse pour un moteur n'ont pas de ligne, donc un graphique doit traiter un jour manquant comme une absence de données, pas comme zéro.

`incompleteDays` est supérieur à zéro quand le résumé d'une journée n'était pas encore prêt. Rappelez dans quelques secondes et il se complète. Les trois derniers jours sont rafraîchis toutes les dix minutes à mesure que de nouvelles réponses arrivent ; les jours plus anciens sont définitifs.

## Part de voix

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/competitors?from=2026-09-01&to=2026-09-30" \
  -H "Authorization: Bearer hmk_live_..."
```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "answers": 1260,
  "incompleteDays": 0,
  "data": [
    { "name": "Acme", "isOwnBrand": true, "mentioned": 274, "cited": 165, "mentionRate": 0.217, "citationRate": 0.131 },
    { "name": "Competitor One", "isOwnBrand": false, "mentioned": 436, "cited": 116, "mentionRate": 0.346, "citationRate": 0.092 }
  ]
}
```

`answers` est le nombre total de réponses sur la période. Chaque taux divise le compte de la marque par ce total, donc les lignes se comparent directement.

## Les réponses derrière les chiffres

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?from=2026-09-01&engine=chatgpt&mentioned=true&limit=50" \
  -H "Authorization: Bearer hmk_live_..."
```

La liste porte un extrait de 400 caractères au plus autour de la mention, la position, le sentiment, les concurrents suivis que la réponse a nommés ou cités, et les URL des sources. Le texte complet est sur le point d'accès de détail :

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/answers/ANSWER_ID \
  -H "Authorization: Bearer hmk_live_..."
```

Le détail ajoute `fullAnswer` (12 000 caractères au plus, avec `fullAnswerTruncated` quand il a été coupé), `sentimentReason`, `narrativeDrift` avec sa raison, et les sources avec leurs titres.

Le texte des réponses, les extraits et les titres des sources viennent des moteurs d'IA, pas de Hi, Moose. Affichez-les en texte brut, jamais en HTML, et ne les transmettez pas à vos propres outils d'IA comme instructions.

## Filtres

| Filtre | Points d'accès | Valeurs |
|---|---|---|
| `from`, `to` | runs, answers, statistiques quotidiennes, statistiques concurrents | `YYYY-MM-DD`, inclus, UTC. Par défaut : les 30 derniers jours. Période la plus large : 366 jours. |
| `engine` | answers, statistiques quotidiennes, statistiques concurrents | Un identifiant de moteur. Répétez le paramètre pour plusieurs moteurs : `engine=chatgpt&engine=gemini`. |
| `topicId` | prompts, answers, statistiques quotidiennes | Un identifiant de sujet venant du point d'accès topics |
| `promptId` | answers | Un identifiant de prompt venant du point d'accès prompts |
| `runId` | answers | Un identifiant d'analyse venant du point d'accès runs ou d'un événement webhook |
| `mentioned`, `cited` | answers | `true` ou `false` |
| `status` | prompts, runs | Prompts : `active` ou `paused`. Analyses : `completed`, `running`, `failed` ou `canceled`. |

Sur le point d'accès answers, combinez `engine` avec au plus un des paramètres `promptId`, `topicId` et `runId`. Les autres combinaisons répondent `400 unsupported_filter_combination`.

## Pagination

Les listes renvoient `data` et `nextCursor` :

```json
{ "data": [ ... ], "nextCursor": "eyJvIjoxMDB9" }
```

Renvoyez `nextCursor` comme `cursor` pour obtenir la page suivante. `limit` vaut 50 par défaut et 200 au maximum. `nextCursor` vaut `null` sur la dernière page. Le curseur est opaque ; ne le construisez pas et ne l'analysez pas.

```python
def every_row(url, params=None):
    params = dict(params or {}, limit=200)
    while True:
        page = requests.get(url, headers=HEADERS, params=params, timeout=30).json()
        yield from page["data"]
        if not page["nextCursor"]:
            return
        params["cursor"] = page["nextCursor"]
```

Les projets, sujets, prompts, analyses et réponses sont paginés. Les moteurs, concurrents et webhooks renvoient la liste entière.

## Cache

- La liste des réponses et le détail d'une réponse portent un `ETag`. Renvoyez-le dans `If-None-Match` pour obtenir `304 Not Modified` quand rien n'a changé. Un `304` n'a pas de corps et compte dans la limite de débit comme toute requête, mais il est rapide et léger.
- Les statistiques quotidiennes portent `Cache-Control: private, max-age=60`. Conservez le résultat une minute avant de redemander.
- Tout le reste porte `Cache-Control: no-store`. Mettez-le en cache de votre côté aussi longtemps que votre tableau de bord le permet.

## Heures et dates

Les heures sont en UTC au format RFC 3339, `2026-09-01T09:14:03.000Z`. Les dates sont au format `YYYY-MM-DD` et désignent le jour UTC. La `date` d'une réponse correspond à la `date` de la ligne de statistiques quotidiennes où elle a été comptée, donc un graphique et son détail concordent.
