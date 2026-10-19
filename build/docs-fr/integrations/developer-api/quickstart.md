---
source_hash: bcecd80050cfb1493af12129d0dc0a3b15b503d5be08491855f621850f94d8d5
---
!!! note "Traduction automatique"
    Cette page a été traduite par IA. La version anglaise fait foi.

    [La lire en anglais](http://localhost:8000/integrations/developer-api/quickstart/)


# Démarrage rapide

Dix minutes entre une clé et un graphique du taux de mention par jour. Chaque étape est montrée en curl, Python et JavaScript.

## 1. Créer une clé

1. Ouvrez Hi, Moose et connectez-vous en tant que propriétaire du compte.
2. Allez dans **Paramètres → Hi, Moose REST API**.
3. Donnez un libellé à la clé, par exemple `Reporting dashboard`, choisissez les projets qu'elle peut lire et laissez les permissions supplémentaires désactivées. La lecture n'en demande aucune.
4. Cliquez sur **Créer la clé** et copiez-la. Elle s'affiche une seule fois.

Placez la clé dans une variable d'environnement sur votre serveur. Les exemples ci-dessous la lisent depuis `HIMOOSE_API_KEY`.

## 2. Vérifier la clé

=== "curl"

    ```bash
    curl https://api.himoose.com/v1/me \
      -H "Authorization: Bearer $HIMOOSE_API_KEY"
    ```

=== "Python"

    ```python
    import os
    import requests

    API = "https://api.himoose.com/v1"
    HEADERS = {"Authorization": f"Bearer {os.environ['HIMOOSE_API_KEY']}"}

    me = requests.get(f"{API}/me", headers=HEADERS, timeout=30).json()
    print(me["label"], me["scopes"], me["projects"])
    ```

=== "JavaScript"

    ```js
    const API = "https://api.himoose.com/v1";
    const HEADERS = { Authorization: `Bearer ${process.env.HIMOOSE_API_KEY}` };

    const me = await (await fetch(`${API}/me`, { headers: HEADERS })).json();
    console.log(me.label, me.scopes, me.projects);
    ```

La réponse indique la clé, ses permissions et les identifiants de projet qu'elle peut lire :

```json
{
  "keyId": "87ac5738",
  "label": "Reporting dashboard",
  "scopes": ["visibility:read"],
  "createdAt": "2026-10-15T02:59:10.839Z",
  "expiresAt": null,
  "account": { "plan": "premium" },
  "projects": ["Uu5UeYLZQBLdOqfBuFmz"]
}
```

## 3. Trouver le projet

=== "curl"

    ```bash
    curl https://api.himoose.com/v1/projects \
      -H "Authorization: Bearer $HIMOOSE_API_KEY"
    ```

=== "Python"

    ```python
    projects = requests.get(f"{API}/projects", headers=HEADERS, timeout=30).json()["data"]
    project = projects[0]
    print(project["id"], project["name"], project["visibility"]["trackedPrompts"], "prompts")
    ```

=== "JavaScript"

    ```js
    const { data: projects } = await (await fetch(`${API}/projects`, { headers: HEADERS })).json();
    const project = projects[0];
    console.log(project.id, project.name, project.visibility.trackedPrompts, "prompts");
    ```

Chaque projet porte un résumé : combien de prompts il suit, quels moteurs, et la date de sa dernière analyse.

## 4. Obtenir le taux de mention par jour

Le point d'accès des statistiques quotidiennes renvoie une ligne par jour et par moteur, avec les comptes et les deux taux déjà calculés. Il lit une table de résumé, donc il est rapide quelle que soit la taille.

=== "curl"

    ```bash
    curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/daily?from=2026-09-01&to=2026-09-30" \
      -H "Authorization: Bearer $HIMOOSE_API_KEY"
    ```

=== "Python"

    ```python
    stats = requests.get(
        f"{API}/projects/{project['id']}/stats/daily",
        headers=HEADERS,
        params={"from": "2026-09-01", "to": "2026-09-30"},
        timeout=30,
    ).json()

    for row in stats["data"]:
        print(row["date"], row["engineId"], f"{row['mentionRate']:.0%} mentioned", f"{row['citationRate']:.0%} cited")
    ```

=== "JavaScript"

    ```js
    const params = new URLSearchParams({ from: "2026-09-01", to: "2026-09-30" });
    const stats = await (await fetch(`${API}/projects/${project.id}/stats/daily?${params}`, { headers: HEADERS })).json();

    for (const row of stats.data) {
      console.log(row.date, row.engineId, `${Math.round(row.mentionRate * 100)}% mentioned`, `${Math.round(row.citationRate * 100)}% cited`);
    }
    ```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "incompleteDays": 0,
  "data": [
    { "date": "2026-09-01", "engineId": "chatgpt", "answers": 42, "mentioned": 17, "cited": 9, "mentionRate": 0.405, "citationRate": 0.214 },
    { "date": "2026-09-01", "engineId": "perplexity", "answers": 42, "mentioned": 22, "cited": 14, "mentionRate": 0.524, "citationRate": 0.333 }
  ]
}
```

`incompleteDays` est supérieur à zéro quand le résumé d'une journée n'était pas encore prêt. Rappelez dans quelques secondes et il se complète.

## 5. Tracer le graphique

Groupez les lignes par `engineId`, mettez `date` sur l'axe des x et `mentionRate` sur l'axe des y, une courbe par moteur. Ajoutez `engine=chatgpt` à la requête pour n'obtenir qu'un moteur, ou `topicId=...` pour vous limiter à un sujet. La page [Lire les données](reading-data.md) liste tous les filtres.

## 6. Aller plus loin

- **Part de voix :** `GET /projects/{id}/stats/competitors` donne votre marque et chaque concurrent suivi sur la même période, prêt pour un graphique en barres.
- **Les réponses derrière les chiffres :** `GET /projects/{id}/answers?mentioned=true` liste les réponses qui ont nommé la marque, avec un extrait et les sources. `GET /projects/{id}/answers/{answerId}` contient le texte complet.
- **Rafraîchir sans interroger l'API :** enregistrez un [webhook](webhooks.md) et Hi, Moose appelle votre serveur quand une analyse se termine.
- **Tout le reste :** la [référence des points d'accès](reference.md).

## Gardez la clé sur le serveur

L'API n'envoie aucun en-tête CORS, donc une page web ne peut pas l'appeler. Un tableau de bord dans le navigateur doit appeler votre backend, et votre backend appelle l'API. La clé reste ainsi hors de la page.
