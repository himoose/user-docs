---
source_hash: 6467de19290f42e43d33241a37345989dbd6267011d89947d750f7e073ea66e2
---

# Webhooks

En lugar de consultar en bucle, registra un endpoint https y Hi, Moose envía ahí un evento JSON firmado cuando termina una ejecución. Registrar, probar y borrar webhooks requiere el permiso **gestionar el seguimiento**. Listarlos, y sus entregas, solo requiere lectura.

## Endpoints

| Endpoint | Qué hace |
|---|---|
| `POST /projects/{id}/webhooks` | Registrar un endpoint. Cuerpo: `url` (https público), `events` (por defecto `run.completed` y `run.failed`), `description` opcional. El secreto de firma vuelve una sola vez en esta respuesta. Como máximo 5 por proyecto. |
| `GET /projects/{id}/webhooks` | Listar los webhooks del proyecto, sin secretos |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Eliminar uno |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Enviar ahora un evento `ping` para comprobar tu endpoint y tu código de firma |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | Las últimas 50 entregas con cada intento, estado y error |

## Registrar uno

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"url":"https://reports.acme.example/himoose","description":"Nightly dashboard refresh"}'
```

```json
{
  "id": "BGXhe1dlOnmy36j6rRTa",
  "url": "https://reports.acme.example/himoose",
  "events": ["run.completed", "run.failed"],
  "description": "Nightly dashboard refresh",
  "active": true,
  "createdAt": "2026-10-15T03:20:10.000Z",
  "secret": "whsec_..."
}
```

Guarda `secret` junto a tu clave. Solo se muestra en esta respuesta. La URL debe ser pública y usar https; las direcciones privadas, localhost y http sin cifrar se rechazan con `400 invalid_parameter`.

Después envíate un ping:

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/test \
  -H "Authorization: Bearer hmk_live_..."
```

La respuesta es el registro de entrega, y el endpoint deliveries muestra el intento con el estado HTTP que respondió tu endpoint.

## El evento

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

| Evento | Cuándo |
|---|---|
| `run.completed` | Una ejecución terminó y sus respuestas están guardadas. Cuentan las ejecuciones programadas, las del botón Ejecutar ahora y las de la API. |
| `run.failed` | Una ejecución acabó con `status` `failed` o `canceled`. `data.error` dice por qué. |
| `ping` | Lo envía el endpoint de prueba. `data` lleva el id del proyecto y un mensaje. |

`data.requestId` viene relleno cuando la ejecución se inició por la API, para que puedas relacionar el evento con tu solicitud de ejecución. Es `null` en las ejecuciones programadas y en las iniciadas desde Hi, Moose.

El evento es una señal, no los datos. Con `run.completed`, sigue `data.links.answers` o actualiza tus estadísticas diarias. Los resúmenes diarios de los días de la ejecución se reconstruyen en los diez minutos siguientes a terminar; `incompleteDays` en la respuesta de estadísticas indica cuándo aún no están listos.

## Cabeceras

| Cabecera | Valor |
|---|---|
| `X-HiMoose-Signature` | `t=<unix seconds>,v1=<hex>`, ver más abajo |
| `X-HiMoose-Event` | El nombre del evento |
| `X-HiMoose-Delivery` | El id de entrega, el mismo que en el endpoint deliveries |
| `User-Agent` | `HiMoose-Webhooks/1.0` |
| `Content-Type` | `application/json` |

## Verificar la firma

`v1` es HMAC-SHA256 sobre `<t>.<raw body>` con el secreto de tu webhook, como cadena hexadecimal en minúsculas. Verifícala sobre el cuerpo sin procesar de la petición antes de parsear el JSON, compara en tiempo constante y rechaza marcas de tiempo de más de cinco minutos.

=== "JavaScript"

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

=== "Python"

    ```python
    import hashlib
    import hmac
    import time

    def verify_himoose_signature(raw_body: bytes, header: str, secret: str) -> bool:
        parts = dict(part.split("=", 1) for part in header.split(",") if "=" in part)
        if "t" not in parts or "v1" not in parts:
            return False
        if abs(time.time() - int(parts["t"])) > 300:
            return False
        expected = hmac.new(secret.encode(), f"{parts['t']}.".encode() + raw_body, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, parts["v1"])
    ```

La mayoría de los frameworks web parsean el JSON antes de que se ejecute tu código. Asegúrate de firmar los bytes tal como llegaron, no una copia reserializada, o la firma no coincidirá.

## Reglas de entrega

- Responde con un estado 2xx en 10 segundos. Haz el trabajo después de responder, no antes. No se siguen redirecciones.
- Las entregas fallidas se reintentan al cabo de 1 minuto, 5 minutos, 30 minutos, 2 horas y 12 horas, 6 intentos en total. Una entrega está `pending` mientras quedan reintentos, `delivered` tras un 2xx y `failed` tras el último intento.
- Tras 20 fallos consecutivos el webhook se desactiva, `active` pasa a false y no se envían más eventos. Elimínalo y regístralo de nuevo para reanudar.
- Un evento puede llegar más de una vez. Usa `id` para ignorar repeticiones.
- Los eventos de un proyecto pueden llegar desordenados cuando hay un reintento de por medio. Usa `createdAt` si el orden importa.

## Ver las entregas

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/deliveries \
  -H "Authorization: Bearer hmk_live_..."
```

Cada entrega lista cada intento con su hora, el estado HTTP que respondió tu endpoint, cuánto tardó y cualquier error. Cuando un endpoint falla, este es el primer sitio donde mirar.

El propietario de la cuenta ve todos los webhooks del proyecto actual en **Ajustes → Hi, Moose REST API** con el estado de su última entrega, y puede eliminar uno ahí.
