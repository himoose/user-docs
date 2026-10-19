---
source_hash: bcecd80050cfb1493af12129d0dc0a3b15b503d5be08491855f621850f94d8d5
---
!!! note "Traduzione automatica"
    Questa pagina è stata tradotta da un'IA. La versione inglese è quella di riferimento.

    [Leggila in inglese](http://localhost:8000/integrations/developer-api/quickstart/)


# Guida rapida

Dieci minuti da una chiave a un grafico del tasso di menzione per giorno. Ogni passo è mostrato in curl, Python e JavaScript.

## 1. Crea una chiave

1. Apri Hi, Moose e accedi come proprietario dell'account.
2. Vai in **Impostazioni → Hi, Moose REST API**.
3. Dai un'etichetta alla chiave, per esempio `Reporting dashboard`, scegli i progetti che può leggere e lascia disattivati i permessi aggiuntivi. Per leggere non ne serve nessuno.
4. Fai clic su **Crea chiave** e copiala. Viene mostrata una sola volta.

Metti la chiave in una variabile d'ambiente sul tuo server. Gli esempi qui sotto la leggono da `HIMOOSE_API_KEY`.

## 2. Verifica la chiave

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

La risposta indica la chiave, i suoi permessi e gli id dei progetti che può leggere:

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

## 3. Trova il progetto

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

Ogni progetto porta un riepilogo: quanti prompt monitora, quali motori e quando è stata l'ultima esecuzione.

## 4. Ottieni il tasso di menzione per giorno

L'endpoint delle statistiche giornaliere restituisce una riga per giorno e motore, con i conteggi e i due tassi già calcolati. Legge una tabella di riepilogo, quindi è veloce a qualsiasi dimensione.

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

`incompleteDays` è maggiore di zero quando il riepilogo di un giorno non era ancora pronto. Richiama tra qualche secondo e si completa.

## 5. Disegna il grafico

Raggruppa le righe per `engineId`, metti `date` sull'asse x e `mentionRate` sull'asse y, una linea per motore. Aggiungi `engine=chatgpt` alla query per avere un solo motore, oppure `topicId=...` per restringere a un argomento. La pagina [Leggere i dati](reading-data.md) elenca tutti i filtri.

## 6. Vai oltre

- **Share of voice:** `GET /projects/{id}/stats/competitors` restituisce il tuo brand e ogni concorrente monitorato sullo stesso periodo, pronti per un grafico a barre.
- **Le risposte dietro i numeri:** `GET /projects/{id}/answers?mentioned=true` elenca le risposte che hanno nominato il brand, con un estratto e le fonti. `GET /projects/{id}/answers/{answerId}` ha il testo completo.
- **Aggiornare senza interrogare in continuazione:** registra un [webhook](webhooks.md) e Hi, Moose chiama il tuo server quando un'esecuzione termina.
- **Tutto il resto:** il [riferimento degli endpoint](reference.md).

## Tieni la chiave sul server

L'API non invia intestazioni CORS, quindi una pagina web non può chiamarla. Una dashboard nel browser deve chiamare il tuo backend, e il tuo backend chiama l'API. Così la chiave resta fuori dalla pagina.
