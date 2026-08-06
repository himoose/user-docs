---
source_hash: 799fa86d4b93065bdbc58d1b0a7cc5400446cfdee289750eafd31c6a0c8371b2
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/chat/overview/)

# Descripción general del Chat

## Para qué sirve

El Chat es donde habla directamente con el operador de Hi, Moose, el mismo agente principal que se describe en toda esta documentación, no una herramienta aparte. Está disponible desde la pantalla **Home** y desde la pantalla dedicada de chat, y cada conversación puede incorporar el [Context](../getting-started/context/overview.md) de su proyecto, los archivos adjuntos y los especialistas guardados para fundamentar sus respuestas.

## Iniciar una conversación

- Pulse **New chat** para empezar de cero, o continúe una conversación existente.
- El compositor muestra prompts de inicio rápido para las tareas más habituales.
- Elija algo concreto en el **[menú Tools](../tools/overview.md)** de la barra superior.
- O escriba su propia petición en lenguaje corriente. Hi, Moose decide si responder directamente, hacer una pregunta de seguimiento o ejecutar una función como [Content Briefs](../features/content-briefs.md) o [AEO Audits](../features/aeo-audits.md) y devolverle un artefacto duradero.

## Cómo decide Hi, Moose qué hacer

No hay ninguna lista de palabras clave. Moose interpreta lo que usted pide y actúa en consecuencia, de modo que puede expresarlo como quiera y obtener el mismo resultado.

Conviene conocer dos comportamientos:

- **Las peticiones explícitas ejecutan la acción.** Pida una auditoría y obtendrá el formulario de auditoría.
- **Las peticiones implícitas solo la ofrecen.** Si su pregunta apenas sugiere una función, Moose responde a la pregunta y coloca la función en una sugerencia de un toque debajo. No se apodera de la conversación.

!!! note "Las preguntas de seguimiento siguen siendo preguntas de seguimiento"
    Hacer una pregunta justo después de que Moose produzca un borrador le da una respuesta sobre ese borrador, no un borrador nuevo. Pida explícitamente una reescritura cuando quiera una.

## Adjuntar contexto

El menú de adjuntos ofrece cuatro opciones:

- **Subir un archivo o una imagen**: `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg` y `.png`. Las hojas de cálculo se convierten en texto legible en lugar de tratarse como archivos opacos.
- **Capturar pantalla**: elija una pantalla o una ventana y después recorte la zona que quiera. En macOS requiere permiso de grabación de pantalla, y Hi, Moose le guía para concederlo.
- **Añadir desde la Library**: adjunte elementos guardados de la [Library](../library/overview.md) como contexto.
- **Base de datos vectorial del sitio**: entregue a Moose su sitio indexado para que responda a partir de sus páginas reales. Véase [Site Monitoring](../site-monitoring/overview.md).

## Qué hace que una respuesta esté fundamentada

Mientras Hi, Moose trabaja, muestra lo que está haciendo realmente: recuperar resultados de búsqueda en vivo, recopilar preguntas de «Otras personas también preguntan», rastrear el dominio de un competidor, leer una página, indexar resultados, consultar datos de Search Console o aplicar su brand voice guardada. Es un rastro visible de las evidencias reales que hay detrás de la respuesta, no un indicador decorativo.

## Adónde ir a continuación

- **[Herramientas y especialistas del chat](tools-and-specialists.md)**: las herramientas que Moose puede utilizar y los especialistas guardados.
- **[El menú Tools](../tools/overview.md)**: iniciar una tarea concreta sin tener que describirla.
- **[Selección de modelo](model-selection.md)**: elegir qué modelo de IA impulsa su chat, incluidas las opciones locales y BYOK.
- **[Chats (historial)](chats-history.md)**: buscar, renombrar y reabrir conversaciones anteriores.
