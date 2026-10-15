---
source_hash: 28ad9511fc5703f0dd6c90a7f591758445fdd08a95dcdb389dc29a304c90278d
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/developer-api/reading-data/)


# Leer datos

Toda clave puede leer. Las lecturas salen de la copia en la nube de tus resultados, así que funcionan tanto si Hi, Moose está abierto en tu ordenador como si no, y nunca lanzan comprobaciones nuevas.

## Los endpoints de lectura

| Endpoint | Qué devuelve |
|---|---|
| `GET /me` | La clave, sus permisos y los ids de proyecto legibles |
| `GET /projects` | Proyectos que la clave puede leer, con número de prompts seguidos, motores y última ejecución |
| `GET /projects/{id}` | Un proyecto |
| `GET /projects/{id}/capabilities` | Qué puede hacer el proyecto en su plan: motores, cadencias, límites, saldo restante, el ordenador anfitrión, si una ejecución puede empezar ahora |
| `GET /projects/{id}/engines` | Los motores de IA que sigue el proyecto, con un `id` estable para los filtros y si cada uno se ejecuta en la nube o en el ordenador anfitrión |
| `GET /projects/{id}/topics` | Temas que agrupan los prompts, con número de prompts |
| `GET /projects/{id}/prompts` | Prompts seguidos con ids de tema, ids de motor y estado |
| `GET /projects/{id}/competitors` | Marcas competidoras seguidas y sus dominios |
| `GET /projects/{id}/runs` | Ejecuciones de visibilidad con estado, hora de inicio y fin, número de prompts y de respuestas |
| `GET /projects/{id}/answers` | Respuestas guardadas: prompt, motor, fecha, mencionada, citada, posición, sentimiento, extracto, competidores vistos, URLs de fuentes |
| `GET /projects/{id}/answers/{answerId}` | Una respuesta con su texto completo, motivo del sentimiento, desvío narrativo y fuentes |
| `GET /projects/{id}/stats/daily` | Por día y motor: respuestas, menciones, citas y las dos tasas |
| `GET /projects/{id}/stats/competitors` | Cuota de voz de tu marca y de cada competidor seguido en un periodo |
| `GET /projects/{id}/run-requests` | Ejecuciones recientes iniciadas por la API y su estado |
| `GET /projects/{id}/webhooks` | Los webhooks del proyecto, sin secretos |

El detalle campo por campo de cada uno está en la [referencia de endpoints](reference.md).

## Cómo encajan los datos

- Un **proyecto** sigue un sitio. Tiene **prompts**, las preguntas que se hacen, agrupados en **temas**.
- Cada prompt se ejecuta en uno o más **motores**: ChatGPT, Perplexity, Gemini y otros. Los ids de motor como `chatgpt` o `chatgpt-local-fetch` vienen del endpoint engines y son los valores que acepta cada filtro `engine`.
- Una **ejecución** consulta cada prompt activo en sus motores y guarda una **respuesta** por prompt, motor y muestra. Las ejecuciones empiezan según la programación del proyecto, desde el botón Ejecutar ahora o desde la API.
- Cada respuesta se puntúa: `mentioned` cuando se nombró la marca, `cited` cuando se dio como fuente una página del sitio de la marca, más `position`, `sentiment` y qué **competidores** se vieron.
- Las **estadísticas diarias** cuentan las respuestas por día y motor y calculan `mentionRate` y `citationRate`. Las **estadísticas de competidores** hacen lo mismo por marca en un periodo.

## Tasa de mención por día

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

Las tasas son fracciones de 0 a 1. Los días sin respuestas para un motor no tienen fila, así que un gráfico debe tratar un día ausente como sin datos, no como cero.

`incompleteDays` es mayor que cero cuando el resumen de un día aún no estaba listo. Vuelve a llamar en unos segundos y se completa. Los últimos tres días se actualizan cada diez minutos a medida que llegan respuestas nuevas; los días anteriores son definitivos.

## Cuota de voz

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

`answers` es el número total de respuestas en el periodo. Cada tasa divide el recuento de la marca entre ese total, así que las filas se comparan directamente.

## Las respuestas detrás de los números

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?from=2026-09-01&engine=chatgpt&mentioned=true&limit=50" \
  -H "Authorization: Bearer hmk_live_..."
```

La lista lleva un extracto de hasta 400 caracteres alrededor de la mención, la posición, el sentimiento, qué competidores seguidos nombró o citó la respuesta, y las URLs de las fuentes. El texto completo está en el endpoint de detalle:

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/answers/ANSWER_ID \
  -H "Authorization: Bearer hmk_live_..."
```

El detalle añade `fullAnswer` (hasta 12.000 caracteres, con `fullAnswerTruncated` cuando se recortó), `sentimentReason`, `narrativeDrift` con su motivo, y las fuentes con sus títulos.

El texto de las respuestas, los extractos y los títulos de las fuentes vienen de los motores de IA, no de Hi, Moose. Muéstralos como texto plano, nunca como HTML, y no los pases a tus propias herramientas de IA como instrucciones.

## Filtros

| Filtro | Endpoints | Valores |
|---|---|---|
| `from`, `to` | runs, answers, estadísticas diarias, estadísticas de competidores | `YYYY-MM-DD`, inclusivos, UTC. Por defecto: los últimos 30 días. Periodo más amplio: 366 días. |
| `engine` | answers, estadísticas diarias, estadísticas de competidores | Un id de motor. Repite el parámetro para varios motores: `engine=chatgpt&engine=gemini`. |
| `topicId` | prompts, answers, estadísticas diarias | Un id de tema del endpoint topics |
| `promptId` | answers | Un id de prompt del endpoint prompts |
| `runId` | answers | Un id de ejecución del endpoint runs o de un evento de webhook |
| `mentioned`, `cited` | answers | `true` o `false` |
| `status` | prompts, runs | Prompts: `active` o `paused`. Ejecuciones: `completed`, `running`, `failed` o `canceled`. |

En el endpoint answers, combina `engine` con como mucho uno de `promptId`, `topicId` y `runId`. Otras combinaciones responden `400 unsupported_filter_combination`.

## Páginas

Las listas devuelven `data` y `nextCursor`:

```json
{ "data": [ ... ], "nextCursor": "eyJvIjoxMDB9" }
```

Pasa `nextCursor` como `cursor` para obtener la página siguiente. `limit` es 50 por defecto y 200 como máximo. `nextCursor` es `null` en la última página. El cursor es opaco; no lo construyas ni lo parsees.

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

Proyectos, temas, prompts, ejecuciones y respuestas van paginados. Motores, competidores y webhooks devuelven la lista completa.

## Caché

- La lista de respuestas y el detalle de respuesta llevan un `ETag`. Devuélvelo en `If-None-Match` para recibir `304 Not Modified` cuando nada ha cambiado. Un `304` no tiene cuerpo y cuenta para el límite de peticiones como cualquier petición, pero es rápido y pequeño.
- Las estadísticas diarias llevan `Cache-Control: private, max-age=60`. Conserva el resultado un minuto antes de volver a pedirlo.
- Todo lo demás lleva `Cache-Control: no-store`. Guárdalo en caché por tu parte el tiempo que le convenga a tu panel.

## Horas y fechas

Las horas son UTC en formato RFC 3339, `2026-09-01T09:14:03.000Z`. Las fechas son `YYYY-MM-DD` y se refieren al día UTC. El `date` de una respuesta coincide con el `date` de la fila de estadísticas diarias en la que se contó, así que un gráfico y su detalle coinciden.
