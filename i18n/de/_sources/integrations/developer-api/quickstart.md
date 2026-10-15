# Quickstart

Ten minutes from a key to a chart of mention rate by day. Every step is shown in curl, Python and JavaScript.

## 1. Create a key

1. Open Hi, Moose and sign in as the account owner.
2. Go to **Settings → Hi, Moose REST API**.
3. Give the key a label such as `Reporting dashboard`, pick the projects it may read, and leave the extra permissions off. Reading needs none.
4. Click **Create key** and copy it. It is shown once.

Put the key in an environment variable on your server. The examples below read it from `HIMOOSE_API_KEY`.

## 2. Check the key

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

The answer names the key, its permissions and the project ids it can read:

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

## 3. Find the project

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

Each project carries a summary: how many prompts it tracks, which engines, and when it last ran.

## 4. Get mention rate by day

The daily stats endpoint returns one row per day and engine, with the counts and the two rates already worked out. It reads a summary table, so it is fast at any size.

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

`incompleteDays` is above zero when a day's summary was not ready yet. Call again in a few seconds and it fills in.

## 5. Draw the chart

Group the rows by `engineId`, put `date` on the x axis and `mentionRate` on the y axis, one line per engine. Add `engine=chatgpt` to the query to get one engine, or `topicId=...` to narrow to one topic. The [reading data](reading-data.md) page lists every filter.

## 6. Go further

- **Share of voice:** `GET /projects/{id}/stats/competitors` gives your brand and every tracked competitor over the same range, ready for a bar chart.
- **The answers behind the numbers:** `GET /projects/{id}/answers?mentioned=true` lists the answers that named the brand, with an excerpt and the sources. `GET /projects/{id}/answers/{answerId}` has the full text.
- **Refresh without polling:** register a [webhook](webhooks.md) and Hi, Moose calls your server when a run finishes.
- **Everything else:** the [endpoint reference](reference.md).

## Keep the key on the server

The API sends no CORS headers, so a web page cannot call it. A browser dashboard should call your backend, and your backend calls the API. That keeps the key out of the page.
