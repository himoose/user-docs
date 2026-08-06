---
source_hash: d13fbe0e44e283bca3759e24ae06c4632b5ccb20e66f5806145543eb82fe5f65
---
# Borradores, vista previa y publicación

## Para qué sirve

Hi, Moose no se detiene en la recomendación: le ayuda a pasar de un brief o de una idea de edición hasta un cambio publicado, con un paso de vista previa y otro de aprobación por el camino, y un registro de lo ocurrido.

## Draft Studio

Draft Studio es donde se redactan y se pulen los borradores. La generación de borradores está construida para depender de un [brief de contenido](content-briefs.md) en lugar de funcionar como un expansor de texto a ciegas: si una tarea requiere planificación estructurada, Hi, Moose genera o confirma antes el brief y redacta a partir de él. Draft Studio también admite la edición directa de textos largos.

### Tipos de contenido

La generación de borradores sigue los mismos tipos de plantilla disponibles al [generar un brief de contenido](content-briefs.md#generar-un-brief). Cuatro tienen su propio inicio rápido en el Chat, cada uno con su estructura: [borrador de entrada de blog](blog-post-draft.md), [entrada de glosario](glossary-post.md), [contenido de landing page](landing-page-content.md) y [contenido de página de producto](product-page-content.md). La plantilla de página de soluciones también está disponible al generar un brief de contenido, aunque sin inicio rápido propio.

Todas las plantillas siguen el mismo flujo de borrador con brief previo; solo cambia la estructura, de modo que un borrador de landing page se planifica y se perfila de forma distinta a una entrada de blog, aunque ambos partan de un [brief de contenido](content-briefs.md).

Cuando usted pide una entrada y Hi, Moose produce un brief, continúa y genera el borrador en lugar de detenerse a esperar a que vuelva a pedirlo.

### Enlazado interno

Los borradores nuevos se contrastan con su sitio indexado y se insertan enlaces internos relevantes allí donde encajan de verdad. Esto requiere un [índice de búsqueda](../site-monitoring/overview.md) construido: sin él no hay nada a lo que enlazar, y Hi, Moose no se inventa enlaces.

## Preparar una edición

Ya venga de un borrador basado en un brief, de unas [FAQ](faq-generator.md), de unos [key points](key-points.md) o de una recomendación de una [AEO audit](aeo-audits.md), un cambio propuesto se prepara como una **propuesta de edición**, un artefacto duradero y no solo texto de chat, antes de que nada toque su sitio en producción.

## Vista previa

Antes de que apruebe nada, Hi, Moose puede generar una vista previa del cambio preparado para que vea qué aspecto tendrá en la página real. Para los cambios que deba revisar otra persona, Hi, Moose puede generar un enlace de revisión compartido, firmado y con caducidad, de modo que un compañero o un cliente pueda revisarlo sin necesidad de acceder a la aplicación de escritorio.

## Aprobar y publicar

- **Aprobar**: aceptar explícitamente un cambio preparado antes de que pueda publicarse. La vista previa y la publicación son siempre pasos separados; generar un borrador o una vista previa nunca se considera «terminado» por sí solo.
- **Publicar**: una vez aprobado, Hi, Moose publica el cambio a través de la conexión correspondiente ([WordPress](../integrations/wordpress.md), [Webflow](../integrations/webflow.md) o [Grav](../integrations/grav.md)) y registra qué se publicó, cuándo y por qué.

### Comportamiento según el CMS

**WordPress**: los borradores pueden enviarse a un sitio conectado como borradores preparados en lugar de publicarse directamente, y el flujo de publicación se adapta a si el destino ya está preparado o publicado. Una vez que ha enviado un borrador, Hi, Moose lo recuerda, de modo que no puede enviar el mismo varias veces por accidente.

**Webflow**: al publicar en una colección se cargan primero los demás campos obligatorios de esa colección y se le pide que los rellene, para que una publicación no falle a mitad de camino por un campo que usted no podía ver.

Una publicación fallida llega a su [Inbox](../inbox/overview.md). Una correcta no, deliberadamente.

## Work Queue

La Work Queue es donde se acumulan las ediciones preparadas, las vistas previas pendientes y los elementos que esperan su aprobación, de modo que nada quede solo dentro de una conversación de chat esperando a caer en el olvido.

## Library e historial

- La **[Library](../library/overview.md)** guarda los artefactos duraderos que ha generado (briefs, borradores, conjuntos de FAQ, key points, AEO audits) para que pueda encontrarlos y reutilizarlos más adelante en lugar de volver a generarlos.
- **[Chats (historial)](../chat/chats-history.md)** es su historial de sesiones de chat guardadas: reabra, renombre o elimine una conversación anterior. Es historial de conversaciones, no un registro de publicaciones ni de resultados de visibilidad; un registro específico que vincule los cambios publicados con la señal de visibilidad que los provocó está previsto, pero todavía no construido.

## Por qué importa

Esta ruta de vista previa → aprobación → publicación es lo que convierte una recomendación en una acción completada y trazable. Un flujo que solo produce consejos está incompleto; un flujo que termina en un cambio previsualizado, aprobado y publicado, con un registro que lo vincula a la señal de visibilidad original, es la razón de ser de Hi, Moose.
