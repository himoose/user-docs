---
source_hash: 6b12d8d972a33f212f60d823c287d184f083cfb60d8934f6b9ac8571ceb3c32e
---
# Herramientas y especialistas del chat

## Para qué sirve

Además de escribir una petición sin más, el compositor del chat le ofrece varias formas de perfilar lo que Hi, Moose hace con su mensaje: adjuntar contexto, elegir un especialista para enfocar la conversación o iniciar un flujo de inicio rápido.

## Adjuntos

Pulse el botón de adjuntar del compositor para añadir contexto a su mensaje:

- **Subir un archivo o una imagen**: `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg` y `.png`. Las hojas de cálculo se convierten en texto legible, de modo que puede entregar un libro de trabajo a Moose y preguntarle por su contenido.
- **Capturar pantalla**: elija una pantalla o una ventana y arrastre para recortar exactamente la zona que quiere enviar. En macOS, la primera vez que lo utilice deberá conceder acceso de grabación de pantalla a Hi, Moose.
- **Añadir desde la Library**: adjunte un artefacto guardado de la [Library](../library/overview.md) (un brief, un borrador, key points o FAQ) como contexto en lugar de volver a pegarlo.
- **Base de datos vectorial del sitio**: adjunte el sitio indexado de su proyecto para que Moose responda a partir de sus páginas reales y no de lo que supone que contienen. Construya el índice desde [Site Monitoring](../site-monitoring/overview.md).

## Herramientas que Moose puede utilizar

El chat no se limita a generar texto. Durante una conversación, Moose puede utilizar herramientas en su nombre y le muestra cuándo lo hace.

| Herramienta | Qué hace |
|---|---|
| Búsqueda web | Resultados en vivo, en los planes que incluyen búsqueda web en el chat |
| Leer una página | Consultar una URL concreta |
| Búsqueda en el índice del sitio | Responder a partir de sus propias páginas indexadas |
| Search Console | Consultar sus datos conectados de [Search Console](../integrations/google-search-console.md) |
| Comprobación instantánea de marca | Consultar una pregunta en cinco motores de IA; véase [Comprobación instantánea de marca en búsqueda con IA](../tools/instant-brand-check.md) |
| Comprobación de cobertura | Averiguar si su sitio ya cubre un tema |
| Generación de imágenes | Producir una imagen para un borrador |
| Ayuda de la aplicación | Dirigirle a la documentación adecuada o al soporte |

El uso de herramientas funciona igual en los planes gestionados, en los planes BYOK y en los modelos locales Gemma 4.

!!! note "Las preguntas sobre Search Console se responden de forma agéntica"
    Moose consulta sus datos de Search Console de forma iterativa en lugar de ejecutar un informe fijo. Si hace una pregunta vaga, acotará mediante varias consultas hasta responderla, en lugar de devolver un volcado genérico.

## Especialistas

Los especialistas son puntos de entrada enfocados al mismo operador principal. No son herramientas ni memorias distintas, solo una forma de orientar la conversación hacia una tarea concreta. Abra el selector de especialista para elegir uno:

- **Especialista en Content Brief**: crear un brief conciso con estructura y siguientes pasos.
- **Especialista en Google Search Console**: preguntar a Moose por sus datos conectados de [Google Search Console](../integrations/google-search-console.md). Este especialista necesita una cuenta de Search Console conectada o una propiedad guardada para el proyecto activo antes de poder responder a partir de sus datos propios.
- **Especialista en generación de audio**: convertir una petición en un guion hablado limpio.
- **Especialista en borradores**: generar contenido en borrador listo para revisar y editar.
- **Especialista en FAQ**: redactar FAQ concisas en torno a las preguntas de mayor valor.
- **Especialista en Key Points**: extraer primero las conclusiones más importantes.

Cuando hay un especialista activo, verá su distintivo en la conversación y podrá quitarlo en cualquier momento para volver al chat general.

### Especialistas personalizados

También puede crear su propio especialista local: asígnele un nombre y un resumen del trabajo que debe atender, y después elija qué partes de su contexto puede utilizar: contexto de proyecto, perfil de marca, contexto del sitio web, historial del chat, salida orientada a borrador o salida en formato markdown. Los especialistas personalizados también pueden importarse si alguien comparte uno con usted.

## Inicios rápidos

El compositor muestra inicios rápidos de un clic para las tareas más habituales, entre ellas:

- [Ejecutar una AEO audit](../features/aeo-audits.md)
- [Crear un brief de contenido respaldado por investigación](../features/content-briefs.md)
- [Crear FAQ respaldadas por investigación](../features/faq-generator.md)
- [Generar key points optimizados](../features/key-points.md)
- [Crear un borrador de entrada de blog](../features/blog-post-draft.md)
- [Crear una entrada de glosario](../features/glossary-post.md)
- [Crear contenido de landing page](../features/landing-page-content.md)
- [Crear contenido de página de producto](../features/product-page-content.md)
- [Capturar consultas de grounding de Google AI Mode para un prompt](../features/grounding-queries.md)
- [Capturar consultas fan-out de ChatGPT para un prompt](../features/fan-out-queries.md)
- [Convertir contenido de texto en audio](../audio/overview.md)

El mismo conjunto está disponible en el **[menú Tools](../tools/overview.md)** de la barra superior, agrupado por tarea y con búsqueda.

Los inicios rápidos de consultas de grounding y de consultas fan-out le muestran las búsquedas que ejecutó un motor de IA con acceso a la web al responder a un prompt, además de las fuentes que citó. Ambos funcionan realizando una llamada gestionada a Gemini o a OpenAI y leyendo después las búsquedas que efectuó esa llamada, de modo que son una aproximación cercana a lo que hacen AI Mode y ChatGPT Search, no una captura de esos productos en sí. Como esa llamada se ejecuta en nuestra infraestructura, ambos requieren un **espacio de trabajo gestionado de pago**, y eso se mantiene incluso en los planes BYOK, ya que el paso de captura de consultas utiliza la infraestructura gestionada de Hi, Moose y no su clave local.

El inicio rápido de audio abre la pantalla de [Audio](../audio/overview.md) en la aplicación de escritorio. Antes enlazaba con la aplicación web anterior; ya no lo hace.
