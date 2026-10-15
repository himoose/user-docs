---
source_hash: bcecd80050cfb1493af12129d0dc0a3b15b503d5be08491855f621850f94d8d5
---

# Inicio rápido

Diez minutos desde una clave hasta un gráfico de tasa de mención por día. Cada paso se muestra en curl, Python y JavaScript.

## 1. Crear una clave

1. Abre Hi, Moose e inicia sesión como propietario de la cuenta.
2. Ve a **Ajustes → Hi, Moose REST API**.
3. Dale a la clave una etiqueta como `Reporting dashboard`, elige los proyectos que puede leer y deja desmarcados los permisos extra. Para leer no hace falta ninguno.
4. Haz clic en **Crear clave** y cópiala. Se muestra una sola vez.

Guarda la clave en una variable de entorno de tu servidor. Los ejemplos de abajo la leen de `HIMOOSE_API_KEY`.

## 2. Comprobar la clave

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

La respuesta indica la clave, sus permisos y los ids de proyecto que puede leer:

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

## 3. Encontrar el proyecto

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

Cada proyecto lleva un resumen: cuántos prompts sigue, qué motores y cuándo fue su última ejecución.

## 4. Obtener la tasa de mención por día

El endpoint de estadísticas diarias devuelve una fila por día y motor, con los recuentos y las dos tasas ya calculadas. Lee una tabla de resumen, así que es rápido a cualquier tamaño.

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

`incompleteDays` es mayor que cero cuando el resumen de un día aún no estaba listo. Vuelve a llamar en unos segundos y se completa.

## 5. Dibujar el gráfico

Agrupa las filas por `engineId`, pon `date` en el eje x y `mentionRate` en el eje y, una línea por motor. Añade `engine=chatgpt` a la consulta para obtener un solo motor, o `topicId=...` para limitarla a un tema. La página [Leer datos](reading-data.md) lista todos los filtros.

## 6. Ir más allá

- **Cuota de voz:** `GET /projects/{id}/stats/competitors` devuelve tu marca y cada competidor seguido en el mismo periodo, listo para un gráfico de barras.
- **Las respuestas detrás de los números:** `GET /projects/{id}/answers?mentioned=true` lista las respuestas que nombraron la marca, con un extracto y las fuentes. `GET /projects/{id}/answers/{answerId}` tiene el texto completo.
- **Actualizar sin consultar en bucle:** registra un [webhook](webhooks.md) y Hi, Moose llama a tu servidor cuando termina una ejecución.
- **Todo lo demás:** la [referencia de endpoints](reference.md).

## Mantén la clave en el servidor

La API no envía cabeceras CORS, así que una página web no puede llamarla. Un panel en el navegador debe llamar a tu backend, y tu backend llama a la API. Así la clave nunca queda en la página.
