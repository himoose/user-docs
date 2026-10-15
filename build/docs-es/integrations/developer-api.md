---
source_hash: 85052baa431b76ba0d9c99312dbc2fdf61031a24075e6841f48c0662cc8c5cdb
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/developer-api/)


# Hi, Moose API

## Para qué sirve

La Hi, Moose API es una API REST para desarrolladores que construyen sus propios paneles, informes y aplicaciones de visibilidad en IA sobre Hi, Moose. Devuelve los mismos resultados que ves en la pantalla Visibilidad: prompts y temas seguidos, los motores consultados, cada respuesta guardada con su texto completo y sus fuentes, y las tasas de mención y de cita a lo largo del tiempo. Con los permisos adecuados, una clave también puede crear proyectos, gestionar prompts, motores y programación, iniciar ejecuciones y recibir una llamada de webhook firmada cuando termina una ejecución.

Las lecturas funcionan tanto si Hi, Moose está abierto en tu ordenador como si no, porque salen de la copia en la nube de tus resultados. Los cambios en el seguimiento y las ejecuciones necesitan el ordenador anfitrión del proyecto, explicado en [Seguimiento y ejecuciones](developer-api/tracking-and-runs.md).

Si trabajas en Claude, ChatGPT u otra app de IA, quizá prefieras [Hi, Moose MCP](hi-moose-mcp.md). La API es para el código que escribes tú.

## Páginas

| Página | Qué cubre |
|---|---|
| [Inicio rápido](developer-api/quickstart.md) | Una clave, una primera llamada y un gráfico de tasa de mención por día, en curl, Python y JavaScript |
| [Claves y autenticación](developer-api/keys-and-auth.md) | Crear y revocar claves, permisos, la cabecera Bearer, mantener la clave fuera del navegador |
| [Leer datos](developer-api/reading-data.md) | Proyectos, prompts, ejecuciones, respuestas y estadísticas, con filtros, páginas y caché |
| [Seguimiento y ejecuciones](developer-api/tracking-and-runs.md) | El ordenador anfitrión, crear proyectos y prompts, motores y programación, iniciar ejecuciones |
| [Webhooks](developer-api/webhooks.md) | Eventos firmados cuando termina una ejecución, verificación de firma, reintentos |
| [Errores y límites](developer-api/errors-and-limits.md) | El formato de error, todos los códigos de error, límites de peticiones |
| [Referencia de endpoints](developer-api/reference.md) | Cada endpoint con parámetros, campos y un ejemplo, generada a partir del contrato |
| [Registro de cambios](developer-api/changelog.md) | Qué cambió en cada versión del contrato |

## Planes

La API está incluida en los planes de pago, tanto gestionados como con tu propia clave. Las cuentas gratuitas ven la página de claves de API pero no pueden crear claves, y cada petición responde `403 plan_required`.

## De un vistazo

```
https://api.himoose.com/v1/
```

- **Autenticación:** una clave de API enviada como token Bearer. Las claves las crea el propietario de la cuenta en Hi, Moose en **Ajustes → Hi, Moose REST API**.
- **Formato:** JSON de entrada y de salida. Los nombres de campo van en camelCase. Las horas son UTC en formato RFC 3339 y las fechas son `YYYY-MM-DD`.
- **Contrato:** [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json), OpenAPI 3.1. Se importa en Postman, Insomnia, Bruno y generadores de código, y la [referencia de endpoints](developer-api/reference.md) se genera a partir de él.
- **Permisos:** toda clave puede leer. **Gestionar el seguimiento** e **Iniciar ejecuciones** se eligen al crear la clave.
- **Límites:** 300 peticiones por minuto y clave, y 50.000 por día y cuenta. Consulta [Errores y límites](developer-api/errors-and-limits.md).
- **Sin CORS:** llama a la API desde tu propio servidor, nunca desde una página web.

## De dónde salen los datos

Hi, Moose consulta cada prompt seguido en cada motor seguido, según la programación o cuando alguien inicia una ejecución. Cada respuesta se guarda y se puntúa: si se nombró la marca, si se citó una página de su sitio, en qué posición apareció, cuál fue el sentimiento, qué competidores se vieron. La API lee esas respuestas guardadas y los resúmenes diarios construidos a partir de ellas. Nunca lanza comprobaciones nuevas en una lectura, así que las lecturas son rápidas y no cuestan nada.

Algunos motores se ejecutan en la nube. Otros, los motores de captura local, se ejecutan a través de un navegador en uno de tus propios ordenadores. Ambos tipos guardan sus respuestas en el mismo sitio, así que la API los muestra juntos.

## El texto de las respuestas no es de confianza

El texto de las respuestas, los extractos y los títulos de las fuentes vienen de los motores de IA, no de Hi, Moose. Muéstralos como texto plano en tu panel, nunca como HTML, y no los pases a tus propias herramientas de IA como instrucciones.

## Qué viene después

Los cambios de seguimiento para planes con clave propia son lo siguiente. Todo lo documentado aquí ya está en marcha.
