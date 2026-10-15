---
source_hash: 638e427715918eeab4249561f6f095b46f57a8531e8ee857a78f4e07d0941c4e
---

# Seguimiento y ejecuciones

Cambiar lo que Hi, Moose sigue requiere el permiso **gestionar el seguimiento**. Iniciar una ejecución requiere el permiso **iniciar ejecuciones**. Ambos se eligen al crear la clave; consulta [Claves y autenticación](keys-and-auth.md#permissions).

## El ordenador anfitrión

Hi, Moose ejecuta parte del seguimiento en uno de tus propios ordenadores, el **dispositivo anfitrión**, que eliges en Hi, Moose en **Ajustes → Hi, Moose MCP**. Los motores de captura local (ChatGPT, Gemini, Grok, Perplexity y Google AI Mode consultados a través de un navegador) solo se ejecutan ahí, y su programación vive ahí.

Cada cambio en el seguimiento y cada ejecución por la API necesita un dispositivo anfitrión elegido para el proyecto. Sin él, la API responde `409 host_required` y nombra el ajuste que hay que cambiar. Un proyecto creado por la API toma el dispositivo anfitrión de otro proyecto de la cuenta cuando existe uno.

Tras un cambio en el seguimiento, la API entrega al ordenador anfitrión un trabajo breve para recoger los ajustes nuevos. El anfitrión lo hace en menos de un minuto mientras Hi, Moose está abierto ahí, o la próxima vez que se abra. En cualquier caso, las lecturas muestran los ajustes nuevos de inmediato.

En los planes con clave propia, los prompts, motores y programación se guardan en el ordenador anfitrión y no en la nube. La API puede leerlos e iniciar ejecuciones, pero cambiarlos responde `409 byok_not_supported`. Gestiónalos en Hi, Moose en ese ordenador.

`GET /projects/{id}/capabilities` te lo dice antes de escribir: el plan, los motores y cadencias permitidos, los límites, el ordenador anfitrión y si está en línea, y si una ejecución podría empezar ahora.

## Gestionar el seguimiento

| Endpoint | Qué hace |
|---|---|
| `POST /projects` | Crear un proyecto a partir de un nombre y una dirección web, con términos de marca y dominios opcionales. El rastreo del sitio no se inicia; el ordenador anfitrión activa el rastreo semanal programado para que ocurra más tarde. Brand Truth no es necesario. |
| `PATCH /projects/{id}` | Cambiar el nombre, la dirección web, los términos de marca o los dominios de marca |
| `PUT /projects/{id}/competitors` | Reemplazar la lista de competidores seguidos, como máximo 50 |
| `POST /projects/{id}/prompts` | Añadir un prompt con ids de tema e ids de motor opcionales |
| `PATCH /projects/{id}/prompts/{promptId}` | Cambiar el texto, los temas o los motores de un prompt, o reanudar uno en pausa |
| `DELETE /projects/{id}/prompts/{promptId}` | Dejar de seguir un prompt. Sus respuestas guardadas se conservan. |
| `PUT /projects/{id}/tracking` | Definir los motores por defecto, cadencia, hora, día de la semana, zona horaria y muestras por prompt |

Cada escritura respeta los límites del plan: número de prompts, motores permitidos, cadencias permitidas, número de proyectos y de competidores. Por encima de un límite la API responde `409 plan_limit` con el límite en el cuerpo.

### Motores en los prompts

Cada prompt tiene su propia lista de motores. `PUT /projects/{id}/tracking` con `engineIds` define el valor por defecto para los prompts que se añadan después y deja cada prompt existente como está. Para cambiar los motores de los prompts existentes, envía `applyEnginesToPrompts: true` en la misma llamada, que aplica la lista nueva a todos los prompts del proyecto, o cambia los prompts de uno en uno con `PATCH /projects/{id}/prompts/{promptId}`.

Un prompt sin motores se conserva pero se omite en las ejecuciones. `POST /projects/{id}/prompts` sin `engineIds` da al prompt nuevo los motores por defecto del proyecto.

### Reemplazar significa reemplazar

`PUT /projects/{id}/competitors` reemplaza la lista entera. Envía la lista completa que quieres conservar, no solo las adiciones. Una lista vacía elimina todos los competidores. Lo mismo vale para `brandTerms` y `brandDomains` en `PATCH /projects/{id}`.

### Ejemplo: configurar el seguimiento en un proyecto nuevo

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

Definir los motores antes de añadir prompts hace que cada prompt nuevo los reciba por defecto.

### Programación

| Campo | Valores |
|---|---|
| `cadence` | `manual` (programación desactivada), `daily`, `weekdays`, `weekly` |
| `timeOfDay` | `HH:MM` en la zona horaria del proyecto |
| `weeklyDay` | De `monday` a `sunday`, usado por `weekly` |
| `timezone` | Un nombre IANA como `Europe/Berlin` |
| `samplesPerPrompt` | Cuántas veces se consulta cada prompt por motor en una ejecución. Más muestras gastan más saldo. |

El plan decide qué cadencias están permitidas; el endpoint capabilities las lista.

## Iniciar una ejecución

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

La API responde `202 Accepted` con una solicitud de ejecución y una cabecera `Location` para consultar:

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

| Estado | Significado |
|---|---|
| `queued` | Aceptada y a punto de empezar |
| `waiting_for_host` | El ordenador anfitrión está apagado. Hi, Moose guarda la solicitud hasta 24 horas e inicia la ejecución cuando vuelve. La respuesta lleva un `warning` que lo indica. |
| `running` | En curso |
| `completed` | Terminada. `runIds` lista las ejecuciones para pasar a los endpoints runs y answers. |
| `failed` | No terminó. `error.code` dice por qué, por ejemplo `host_unavailable` tras 24 horas. |
| `canceled` | Detenida desde Hi, Moose antes de terminar |

`mode` indica dónde se ejecuta. Los proyectos cuyos motores seguidos son todos motores en la nube se ejecutan en la nube de inmediato, sin el ordenador anfitrión. Cualquier motor de captura local hace que la ejecución pase al ordenador anfitrión, por el mismo camino que el botón Ejecutar ahora. En ambos casos el proyecto necesita un ordenador anfitrión elegido.

### Salvaguardas

Para que una ejecución nunca cueste más de lo esperado:

- **Primero, el saldo.** La API estima el coste de la ejecución en motores en la nube a partir del número de prompts y motores. Si la estimación supera el saldo restante, rechaza con `409 insufficient_allowance`, la estimación y las unidades restantes. No se gasta nada. `GET /projects/{id}/capabilities` muestra la misma estimación como `allowance.estimatedUnitsPerRun`.
- **De una en una.** Una segunda solicitud mientras otra está en cola, en espera o en curso responde `409 run_in_progress` con el id de la solicitud activa.
- **Límite diario.** Como máximo 24 solicitudes de ejecución por proyecto y día. Por encima, la API responde `429 daily_run_limit`.
- **Idempotencia.** Envía una cabecera `Idempotency-Key` y un reintento dentro de 24 horas devuelve la misma solicitud con `200` y `replayed: true` en lugar de iniciar otra ejecución.
- **Algo que ejecutar.** Un proyecto sin ningún prompt que tenga un motor responde `409 no_prompts`.

### Seguir una ejecución

Consulta `GET /projects/{id}/run-requests/{requestId}` más o menos una vez por minuto. Una ejecución puede tardar desde unos minutos hasta más de una hora con conjuntos de prompts grandes. Cuando `status` es `completed`, `runIds` tiene la ejecución que leer:

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?runId=RUN_ID" \
  -H "Authorization: Bearer hmk_live_..."
```

Para evitar consultar en bucle, registra un [webhook](webhooks.md). El evento `run.completed` lleva `requestId`, así que puedes relacionarlo con la solicitud que hiciste.

Las ejecuciones iniciadas por la API aparecen en Hi, Moose como cualquier otra ejecución, y en la tabla **Trabajos recientes de agentes** en **Ajustes → Hi, Moose MCP** con la etiqueta de la clave.
