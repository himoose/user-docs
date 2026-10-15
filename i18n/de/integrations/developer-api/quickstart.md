---
source_hash: bcecd80050cfb1493af12129d0dc0a3b15b503d5be08491855f621850f94d8d5
---

# Schnellstart

Zehn Minuten vom Schlüssel bis zum Diagramm der Erwähnungsrate pro Tag. Jeder Schritt ist in curl, Python und JavaScript gezeigt.

## 1. Einen Schlüssel erstellen

1. Öffnen Sie Hi, Moose und melden Sie sich als Kontoinhaber an.
2. Gehen Sie zu **Einstellungen → Hi, Moose REST API**.
3. Geben Sie dem Schlüssel eine Bezeichnung wie `Reporting dashboard`, wählen Sie die Projekte, die er lesen darf, und lassen Sie die zusätzlichen Berechtigungen aus. Lesen braucht keine.
4. Klicken Sie auf **Schlüssel erstellen** und kopieren Sie ihn. Er wird einmal angezeigt.

Legen Sie den Schlüssel in eine Umgebungsvariable auf Ihrem Server. Die Beispiele unten lesen ihn aus `HIMOOSE_API_KEY`.

## 2. Den Schlüssel prüfen

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

Die Antwort nennt den Schlüssel, seine Berechtigungen und die Projekt-IDs, die er lesen kann:

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

## 3. Das Projekt finden

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

Jedes Projekt trägt eine Zusammenfassung: wie viele Prompts es verfolgt, welche Engines, und wann es zuletzt gelaufen ist.

## 4. Die Erwähnungsrate pro Tag abrufen

Der Endpunkt für Tagesstatistiken gibt eine Zeile pro Tag und Engine zurück, mit den Zählwerten und den beiden Raten schon berechnet. Er liest eine Zusammenfassungstabelle und ist deshalb bei jeder Größe schnell.

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

`incompleteDays` ist größer als null, wenn die Zusammenfassung eines Tages noch nicht fertig war. Rufen Sie in ein paar Sekunden erneut auf, dann wird sie ergänzt.

## 5. Das Diagramm zeichnen

Gruppieren Sie die Zeilen nach `engineId`, legen Sie `date` auf die x-Achse und `mentionRate` auf die y-Achse, eine Linie pro Engine. Hängen Sie `engine=chatgpt` an die Abfrage, um eine Engine zu erhalten, oder `topicId=...`, um auf ein Thema einzugrenzen. Die Seite [Daten lesen](reading-data.md) listet jeden Filter.

## 6. Weiter gehen

- **Share of Voice:** `GET /projects/{id}/stats/competitors` liefert Ihre Marke und jeden verfolgten Wettbewerber über denselben Zeitraum, fertig für ein Balkendiagramm.
- **Die Antworten hinter den Zahlen:** `GET /projects/{id}/answers?mentioned=true` listet die Antworten, die die Marke genannt haben, mit einem Auszug und den Quellen. `GET /projects/{id}/answers/{answerId}` hat den vollen Text.
- **Aktualisieren ohne Abfragen:** registrieren Sie einen [Webhook](webhooks.md), und Hi, Moose ruft Ihren Server auf, wenn ein Lauf abgeschlossen ist.
- **Alles andere:** die [Endpunkt-Referenz](reference.md).

## Den Schlüssel auf dem Server behalten

Die API sendet keine CORS-Header, eine Webseite kann sie also nicht aufrufen. Ein Browser-Dashboard sollte Ihr Backend aufrufen, und Ihr Backend ruft die API auf. So bleibt der Schlüssel aus der Seite heraus.
