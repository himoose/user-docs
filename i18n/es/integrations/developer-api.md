---
source_hash: 825726013c46ce2cb7c1932ac3dda84ec19a94f2c4ce33cdc108f00904718460
---
# Hi, Moose API

## Para qué sirve

La Hi, Moose API es una API REST para desarrolladores que construyen sus propios paneles, informes y aplicaciones de visibilidad en IA sobre Hi, Moose. Devuelve los mismos resultados que ves en la pantalla Visibilidad: prompts y temas seguidos, los motores consultados, cada respuesta guardada con su texto completo y sus fuentes, y las tasas de mención y de cita a lo largo del tiempo. Con los permisos adecuados, una clave también puede crear proyectos, gestionar prompts, motores y programación, e iniciar ejecuciones.

Las lecturas funcionan tanto si Hi, Moose está abierto en tu ordenador como si no, porque salen de la copia en la nube de tus resultados. Los cambios en el seguimiento y las ejecuciones necesitan el ordenador anfitrión del proyecto, explicado más abajo.

Si trabajas en Claude, ChatGPT u otra app de IA, quizá prefieras [Hi, Moose MCP](hi-moose-mcp.md). La API es para el código que escribes tú.

## Planes

La API está incluida en los planes de pago, tanto gestionados como con tu propia clave. Las cuentas gratuitas ven la página de claves de API pero no pueden crear claves, y cada petición responde `403 plan_required`.

## Crear una clave

1. Abre Hi, Moose e inicia sesión como propietario de la cuenta. Solo el propietario puede crear, ver y revocar claves.
2. Ve a **Ajustes → Hi, Moose REST API**.
3. Dale una etiqueta a la clave, elige los proyectos que puede leer (todos o uno), decide cuándo caduca y marca los permisos que necesita.
4. Haz clic en **Crear clave** y copia la clave. Se muestra una sola vez. Hi, Moose no puede mostrarla de nuevo; si la pierdes, revócala y crea otra.

Las claves empiezan por `hmk_live_` seguido de 64 caracteres. La tabla bajo el formulario lista cada clave activa con sus permisos y su fecha de creación, último uso y caducidad. **Revocar** detiene una clave de inmediato.

## Permisos

| Permiso | Qué puede hacer la clave |
|---|---|
| Leer datos de visibilidad | Todos los endpoints `GET`. Siempre activo. |
| Gestionar el seguimiento | Crear proyectos, definir términos de marca y competidores, añadir, cambiar y borrar prompts, definir motores y programación. |
| Iniciar ejecuciones | Iniciar una ejecución de visibilidad. Las ejecuciones gastan el saldo de la cuenta en motores en la nube, así que dáselo solo a una clave que lo necesite. |

Una llamada sin el permiso necesario responde `403 insufficient_scope`. Los permisos se eligen al crear la clave y no pueden cambiarse después.

## Autenticación

Envía la clave como token Bearer:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

La respuesta indica la clave, sus permisos y los ids de proyecto que puede leer.

Usa la clave solo desde tu propio servidor. La API no envía cabeceras CORS, así que una página web no puede llamarla directamente. Un panel en el navegador debe llamar a tu backend, y tu backend llama a la API. Así la clave nunca queda en la página.

## URL base y formato

```
https://api.himoose.com/v1/
```

Todo es JSON. Los nombres de campo van en camelCase y coinciden con los campos que devuelve Hi, Moose MCP. Las horas son UTC en formato RFC 3339 y las fechas son `YYYY-MM-DD`. El contrato completo está en [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json) y se importa en Postman, Insomnia y herramientas similares.

## Endpoints de lectura

| Endpoint | Qué devuelve |
|---|---|
| `GET /me` | La clave, sus permisos y los ids de proyecto legibles |
| `GET /projects` | Proyectos que la clave puede leer, con número de prompts seguidos, motores y última ejecución |
| `GET /projects/{id}` | Un proyecto |
| `GET /projects/{id}/capabilities` | Qué puede hacer el proyecto en su plan: motores, cadencias, límites, saldo restante, el ordenador anfitrión, si una ejecución puede empezar ahora |
| `GET /projects/{id}/engines` | Los motores de IA que sigue el proyecto, con un `id` estable para los filtros |
| `GET /projects/{id}/topics` | Temas que agrupan los prompts, con número de prompts |
| `GET /projects/{id}/prompts` | Prompts seguidos con ids de tema, ids de motor y estado |
| `GET /projects/{id}/competitors` | Marcas competidoras seguidas |
| `GET /projects/{id}/runs` | Ejecuciones de visibilidad con estado, hora de inicio y fin, número de prompts y de respuestas |
| `GET /projects/{id}/answers` | Respuestas guardadas: prompt, motor, fecha, mencionada, citada, posición, sentimiento, extracto, competidores vistos, URLs de fuentes |
| `GET /projects/{id}/answers/{answerId}` | Una respuesta con su texto completo, motivo del sentimiento, desvío narrativo y fuentes |
| `GET /projects/{id}/stats/daily` | Por día y motor: respuestas, menciones, citas y las dos tasas |
| `GET /projects/{id}/stats/competitors` | Cuota de voz de tu marca y de cada competidor seguido en un periodo |
| `GET /projects/{id}/run-requests` | Ejecuciones recientes iniciadas por la API y su estado |

### Ejemplo: tasa de mención por día

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

`incompleteDays` es mayor que cero cuando el resumen de un día aún no estaba listo. Vuelve a llamar en unos segundos y se completa.

## El ordenador anfitrión

Hi, Moose ejecuta parte del seguimiento en uno de tus propios ordenadores, el **dispositivo anfitrión**, que eliges en Hi, Moose en **Ajustes → Hi, Moose MCP**. Los motores de captura local (ChatGPT, Gemini, Grok, Perplexity y Google AI Mode consultados a través de un navegador) solo se ejecutan ahí, y su programación vive ahí.

Cada cambio en el seguimiento y cada ejecución por la API necesita un dispositivo anfitrión elegido para el proyecto. Sin él, la API responde `409 host_required` y nombra el ajuste que hay que cambiar. Un proyecto creado por la API toma el dispositivo anfitrión de otro proyecto de la cuenta cuando existe uno.

En los planes con clave propia, los prompts, motores y programación se guardan en el ordenador anfitrión y no en la nube. La API puede leerlos e iniciar ejecuciones, pero cambiarlos responde `409 byok_not_supported`. Gestiónalos en Hi, Moose en ese ordenador.

## Gestionar el seguimiento

Requiere el permiso **gestionar el seguimiento**.

| Endpoint | Qué hace |
|---|---|
| `POST /projects` | Crear un proyecto a partir de un nombre y una dirección web, con términos de marca y dominios opcionales. El rastreo del sitio no se inicia; el ordenador anfitrión activa el rastreo semanal programado para que ocurra más tarde. Brand Truth no es necesario. |
| `PATCH /projects/{id}` | Cambiar el nombre, la dirección web, los términos de marca o los dominios de marca |
| `PUT /projects/{id}/competitors` | Reemplazar la lista de competidores seguidos, como máximo 50 |
| `POST /projects/{id}/prompts` | Añadir un prompt con ids de tema e ids de motor opcionales |
| `PATCH /projects/{id}/prompts/{promptId}` | Cambiar el texto, los temas o los motores de un prompt |
| `DELETE /projects/{id}/prompts/{promptId}` | Dejar de seguir un prompt |
| `PUT /projects/{id}/tracking` | Definir motores, cadencia, hora, día de la semana, zona horaria y muestras por prompt. Los motores nuevos se aplican a todos los prompts salvo que `applyEnginesToPrompts` sea false. |

Cada escritura respeta los límites del plan: número de prompts, motores permitidos, cadencias permitidas, número de proyectos y de competidores. Por encima de un límite la API responde `409 plan_limit` con el límite en el cuerpo. Consulta primero `GET /projects/{id}/capabilities`.

### Ejemplo: configurar el seguimiento en un proyecto nuevo

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"Europe/Madrid"}'
```

## Iniciar una ejecución

Requiere el permiso **iniciar ejecuciones**.

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

La API responde `202 Accepted` con una solicitud de ejecución y una cabecera `Location` para consultar. Estados:

| Estado | Significado |
|---|---|
| `queued` | Aceptada y a punto de empezar |
| `waiting_for_host` | El ordenador anfitrión está apagado. Hi, Moose guarda la solicitud hasta 24 horas e inicia la ejecución cuando vuelve. La respuesta lleva un `warning` que lo indica. |
| `running` | En curso |
| `completed` | Terminada. `runIds` lista las ejecuciones para los endpoints runs y answers. |
| `failed` | No terminó. `error.code` dice por qué, por ejemplo `host_unavailable` tras 24 horas. |

Los proyectos cuyos motores seguidos son todos motores en la nube se ejecutan en la nube de inmediato, sin el ordenador anfitrión. Cualquier motor de captura local hace que la ejecución pase al ordenador anfitrión, por el mismo camino que el botón Ejecutar ahora.

Salvaguardas para que una ejecución nunca cueste más de lo esperado:

- **Primero, el saldo.** La API estima el coste de la ejecución en motores en la nube a partir del número de prompts y motores. Si la estimación supera el saldo restante, rechaza con `409 insufficient_allowance`, la estimación y las unidades restantes. No se gasta nada. `GET /projects/{id}/capabilities` muestra la misma estimación como `allowance.estimatedUnitsPerRun`.
- **De una en una.** Una segunda solicitud mientras otra está en cola, en espera o en curso responde `409 run_in_progress` con el id de la solicitud activa.
- **Límite diario.** Como máximo 24 solicitudes de ejecución por proyecto y día. Por encima, la API responde `429 daily_run_limit`.
- **Idempotencia.** Envía una cabecera `Idempotency-Key` y un reintento dentro de 24 horas devuelve la misma solicitud en lugar de iniciar otra.

Una ejecución puede tardar desde unos minutos hasta más de una hora con conjuntos de prompts grandes. Consulta la solicitud cada minuto más o menos, no cada segundo.

## Filtros y paginación

- **Periodo:** `from` y `to` como `YYYY-MM-DD`, inclusivos, UTC. Por defecto son los últimos 30 días. El periodo más amplio en una petición es de 366 días.
- **Motor:** `engine=chatgpt&engine=gemini` se repite para varios motores. Los ids vienen del endpoint engines.
- **Respuestas:** además `topicId`, `promptId`, `runId`, `mentioned=true|false` y `cited=true|false`. Combina `engine` con como mucho uno de `promptId`, `topicId` o `runId`.
- **Páginas:** las listas devuelven `{ "data": [...], "nextCursor": "..." }`. Pasa `nextCursor` como `cursor` para obtener la página siguiente. `limit` es 50 por defecto y 200 como máximo. `nextCursor` es `null` en la última página.
- **Caché:** las respuestas llevan un `ETag`. Devuélvelo en `If-None-Match` para recibir `304 Not Modified` cuando nada ha cambiado.

## Límites de peticiones

| Límite | Valor |
|---|---|
| Por clave | 60 peticiones por minuto |
| Por cuenta | 10.000 peticiones por día |
| Solicitudes de ejecución por proyecto | 24 por día, de una en una |
| Filas por página | 200 |
| Periodo por petición | 366 días |

Por encima del límite la API responde `429` con una cabecera `Retry-After`. Cada respuesta lleva `RateLimit-Policy`, y las respuestas correctas llevan `RateLimit` con el presupuesto restante del día.

## Errores

Los errores usan el formato Problem Details (`application/problem+json`) con un `code` estable:

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

| Código | Estado | Significado |
|---|---|---|
| `invalid_key`, `key_revoked`, `key_expired` | 401 | La clave falta, está mal formada, revocada o caducada |
| `plan_required` | 403 | El plan de la cuenta no incluye la API |
| `insufficient_scope` | 403 | La clave no tiene el permiso para esta llamada |
| `not_found` | 404 | No existe ese recurso, o la clave no puede leerlo |
| `invalid_parameter`, `range_too_wide`, `unsupported_filter_combination` | 400 | Hay que corregir un parámetro o un campo |
| `host_required` | 409 | Elige primero un dispositivo anfitrión para el proyecto en Hi, Moose |
| `byok_not_supported` | 409 | En este plan los ajustes de seguimiento viven en el ordenador anfitrión |
| `plan_limit` | 409 | Se alcanzó un límite del plan; el cuerpo lo nombra |
| `run_in_progress`, `insufficient_allowance`, `no_prompts` | 409 | La ejecución no puede empezar ahora; el cuerpo dice por qué |
| `rate_limited`, `daily_run_limit` | 429 | Espera los segundos de `Retry-After` |

Indica el `requestId` cuando contactes con soporte.

## El texto de las respuestas no es de confianza

El texto de las respuestas, los extractos y los títulos de las fuentes vienen de los motores de IA, no de Hi, Moose. Muéstralos como texto plano en tu panel, nunca como HTML, y no los pases a tus propias herramientas de IA como instrucciones.

## Webhooks

En lugar de consultar, registra un endpoint https y Hi, Moose envía ahí un evento JSON firmado cuando termina una ejecución. Registrar y borrar webhooks requiere el permiso **gestionar el seguimiento**. Listarlos, y sus entregas, solo requiere lectura.

| Endpoint | Qué hace |
|---|---|
| `POST /projects/{id}/webhooks` | Registrar un endpoint. Cuerpo: `url` (https público), `events` (por defecto `run.completed` y `run.failed`), `description` opcional. El secreto de firma vuelve una sola vez en esta respuesta. Como máximo 5 por proyecto. |
| `GET /projects/{id}/webhooks` | Listar los webhooks del proyecto, sin secretos |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Eliminar uno |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Enviar ahora un evento `ping` para comprobar tu endpoint y tu código de firma |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | Las últimas 50 entregas con cada intento, estado y error |

### El evento

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

`data.requestId` viene relleno cuando la ejecución se inició por la API, para que puedas relacionar el evento con tu solicitud. `run.failed` lleva `status` `failed` o `canceled` y el texto de `error`.

### Verificar la firma

Cada llamada lleva `X-HiMoose-Signature: t=<segundos unix>,v1=<hex>`, donde `v1` es HMAC-SHA256 sobre `<t>.<cuerpo sin procesar>` con el secreto de tu webhook. Verifícala sobre el cuerpo sin procesar antes de parsear el JSON y rechaza marcas de tiempo de más de cinco minutos. La llamada también lleva `X-HiMoose-Event` y `X-HiMoose-Delivery`.

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

### Reglas de entrega

- Responde con un estado 2xx en 10 segundos. No se siguen redirecciones.
- Las entregas fallidas se reintentan al cabo de 1 minuto, 5 minutos, 30 minutos, 2 horas y 12 horas, 6 intentos en total.
- Tras 20 fallos consecutivos el webhook se desactiva. Elimínalo y regístralo de nuevo para reanudar.
- Un evento puede llegar más de una vez. Usa `id` para ignorar repeticiones.
- El propietario de la cuenta ve todos los webhooks del proyecto actual en **Ajustes → Hi, Moose REST API** y puede eliminar uno ahí.

## Qué viene después

Los cambios de seguimiento para planes con clave propia son lo siguiente. Todo lo demás documentado aquí ya está en marcha.
