---
source_hash: 85fe7ea99ed19540350085410907cba880592b989251ce17fdb81570b24829a2
---

# Errores y límites

## Errores

Los errores usan el formato Problem Details (`application/problem+json`, RFC 9457) con un `code` estable sobre el que puedes ramificar:

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/errors-and-limits/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

- `code` es el campo que hay que comprobar en el código. Nunca cambia de significado.
- `detail` está escrito para una persona y su redacción puede cambiar.
- `type` enlaza a la sección de la documentación para ese tipo de error.
- `requestId` identifica la petición. Indícalo cuando contactes con soporte. También se envía como cabecera `X-Request-Id` en cada respuesta.

Algunos errores llevan campos extra, indicados en la tabla.

## Códigos de error

| Código | Estado | Significado | Qué hacer |
|---|---|---|---|
| `invalid_key` | 401 | No hay cabecera `Authorization`, la clave tiene un formato incorrecto o Hi, Moose no la conoce | Envía `Authorization: Bearer hmk_live_...`. Comprueba que la clave se copió entera. |
| `key_revoked` | 401 | La clave se revocó en Ajustes | Crea una clave nueva. |
| `key_expired` | 401 | La clave pasó su fecha de caducidad | Crea una clave nueva. |
| `plan_required` | 403 | El plan de la cuenta no incluye la API | Pasa a un plan de pago. |
| `insufficient_scope` | 403 | La clave no tiene el permiso para esta llamada. El cuerpo lo nombra en `scope`. | Crea una clave con ese permiso. |
| `not_found` | 404 | No existe ese recurso, o la clave no puede leerlo. Los dos casos no se distinguen. | Comprueba el id y el acceso a proyectos de la clave. |
| `method_not_allowed` | 405 | El endpoint existe pero no con este método | Consulta la [referencia](reference.md). |
| `invalid_parameter` | 400 | Falta un parámetro de consulta o un campo del cuerpo, está mal formado o fuera de rango. `detail` lo nombra. | Corrige la petición. |
| `range_too_wide` | 400 | De `from` a `to` hay más de 366 días | Pide un periodo más corto. |
| `unsupported_filter_combination` | 400 | Filtros que no se pueden combinar, por ejemplo `engine` con dos de `promptId`, `topicId` y `runId` | Quita un filtro. |
| `host_required` | 409 | El proyecto no tiene ordenador anfitrión elegido | Elige uno en Hi, Moose en **Ajustes → Hi, Moose MCP**. |
| `byok_not_supported` | 409 | En este plan los ajustes de seguimiento viven en el ordenador anfitrión, así que la API no puede cambiarlos | Cámbialos en Hi, Moose en ese ordenador. |
| `plan_limit` | 409 | Se alcanzó un límite del plan. El cuerpo lleva `limit`. | Consulta los límites en `GET /projects/{id}/capabilities`. |
| `run_in_progress` | 409 | Ya hay una solicitud de ejecución en cola, en espera o en curso. El cuerpo lleva `requestId` y `requestStatus`. | Espera a que termine. |
| `insufficient_allowance` | 409 | La ejecución costaría más que el saldo restante. El cuerpo lleva `estimatedUnits`, `remainingUnits` y `periodEndsAt`. | Recarga, o reduce prompts, motores o muestras. |
| `no_prompts` | 409 | El proyecto no tiene ningún prompt seguido con un motor | Añade prompts y motores primero. |
| `rate_limited` | 429 | Se alcanzó el límite por minuto o por día | Espera los segundos de `Retry-After`. |
| `daily_run_limit` | 429 | El proyecto ya hizo sus 24 solicitudes de ejecución de hoy | Inténtalo mañana. |
| `internal` | 500 | Algo falló en el lado de Hi, Moose | Reintenta con espera creciente. Si persiste, contacta con soporte con el `requestId`. |

Un `502` o `503` sin cuerpo significa que la API no pudo llegar a su backend. Reintenta con espera creciente.

## Límites de peticiones

| Límite | Valor |
|---|---|
| Por clave | 300 peticiones por minuto |
| Por cuenta | 50.000 peticiones por día |
| Solicitudes de ejecución por proyecto | 24 por día, de una en una |
| Webhooks por proyecto | 5 |
| Filas por página | 200 |
| Periodo por petición | 366 días |

Por encima del límite la API responde `429 rate_limited` con una cabecera `Retry-After`. Cada respuesta lleva `RateLimit-Policy`, y las respuestas correctas llevan `RateLimit` con el presupuesto restante del día, siguiendo el borrador de cabeceras de límite de peticiones del IETF:

```
RateLimit-Policy: "per-minute";q=300;w=60, "per-day";q=50000;w=86400
RateLimit: "per-day";r=49871;t=61234
```

El límite por minuto se cuenta por clave en el borde de la red y es aproximado; una ráfaga corta un poco por encima puede pasar. El límite por día se cuenta por cuenta entre todas sus claves.

## Mantenerse dentro de los límites

- **Caché por tu parte.** Las estadísticas diarias llevan `Cache-Control: max-age=60`. Un panel que se actualiza cada minuto lee el resumen una vez por minuto y gráfico, no una vez por visitante.
- **Usa los resúmenes.** Las estadísticas diarias y las de competidores se construyen a partir de una tabla de resumen. Dibuja los gráficos con ellas y lee respuestas individuales solo cuando alguien abre una fila.
- **Usa ETags.** Las respuestas llevan un `ETag`. Devuélvelo en `If-None-Match` y un `304` cuesta casi nada.
- **Usa webhooks** en lugar de consultar en bucle hasta que termine una ejecución. Consulta [Webhooks](webhooks.md).
- **Espera ante un 429.** Duerme los segundos de `Retry-After` y reintenta después. No reintentes de inmediato.

## Ids de petición

Cada respuesta lleva `X-Request-Id`. Regístralo junto a tu propio registro de peticiones para que un informe de problema se pueda cruzar con los registros de Hi, Moose. Los cuerpos de error lo repiten como `requestId`.
