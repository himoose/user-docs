---
source_hash: 422edf700d29e3ee080f114ca1c4fbdc3f92677eb196cdf636fdac1f0e5e4cad
---

# Registro de cambios

La versión del contrato está en `info.version` de [openapi.json](https://api.himoose.com/v1/openapi.json) y en el encabezado de la [referencia de endpoints](reference.md). La URL base sigue siendo `/v1` para todas las versiones listadas aquí; un cambio incompatible recibiría una URL base nueva y un aviso con mucha antelación.

## 1.2.1, 2026-10-15

Primera versión pública.

- **Lectura:** proyectos, motores, temas, prompts, competidores, ejecuciones, respuestas con texto completo, estadísticas diarias, estadísticas de competidores y capacidades.
- **Gestión del seguimiento:** crear y cambiar proyectos, reemplazar competidores, añadir, cambiar y borrar prompts, definir motores y programación.
- **Ejecuciones:** iniciar una ejecución con comprobación del saldo, de una en una, 24 por día, con claves de idempotencia y un estado que consultar.
- **Webhooks:** eventos `run.completed` y `run.failed` con firmas HMAC, reintentos y un registro de entregas.
- **Límites:** 300 peticiones por minuto y clave, 50.000 por día y cuenta.
- `PUT /projects/{id}/tracking` con `engineIds` cambia solo los motores por defecto. Los prompts existentes conservan sus motores salvo que `applyEnginesToPrompts` sea `true`.

## Previsto

- Cambios de seguimiento en planes con clave propia, cuyos ajustes hoy viven en el ordenador anfitrión.
- Oportunidades, la cola de trabajo priorizada de la pestaña Oportunidades.
