---
source_hash: 87a7b6f091685fae0a59b09ee8abe0ec965085647eb82bd29c1661777efb87ab
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/site-monitoring/overview/)

# Site Monitoring

## Para qué sirve

Hi, Moose mantiene una imagen local de su sitio web: qué páginas existen, qué contienen y qué ha cambiado desde la última vez. Esa imagen alimenta tres cosas: los avisos de cambios relevantes para AEO en su [Inbox](../inbox/overview.md), el índice de búsqueda semántica que Moose utiliza para responder preguntas sobre su propio sitio, y el inventario de páginas del que se nutren las [auditorías](../features/aeo-audits.md) y los [briefs](../features/content-briefs.md).

Todo esto se encuentra en **Configuración → Site Monitoring**, acotado al proyecto actual.

## El rastreo programado

Active **Run weekly site crawl** y Hi, Moose actualizará las páginas supervisadas con cadencia semanal y le avisará cuando aparezcan cambios relevantes. Elija el día y la hora en su horario local.

Los rastreos manuales siguen disponibles en cualquier caso. **Run crawl now** inicia un rastreo completo de inmediato, con el progreso en la barra de estado inferior de la ventana. Puede **detener** un rastreo en curso, y las páginas encontradas hasta ese momento se conservan en lugar de descartarse.

Los sitios grandes tardan unos minutos.

## El índice de búsqueda

Debajo de los controles de rastreo está el **Search index**, el índice semántico local que Moose utiliza para responder preguntas sobre las páginas de su sitio. Indica cuántas páginas están indexadas, cuántos pasajes han producido esas páginas y cuándo se actualizó por última vez.

La indexación es por pasajes, no por páginas. Una página larga se convierte en muchos pasajes buscables por separado, y por eso Moose puede citar un párrafo concreto en lugar de decirle que una página trata «en general» de un tema.

- **Rebuild index** vuelve a indexar desde cero.
- Si hay páginas nuevas o modificadas desde la última actualización del índice, Hi, Moose le indica cuántas. Se indexarán en el próximo rastreo, o puede reconstruir el índice ahora.

!!! note "El índice es honesto sobre lo que no tiene"
    Si pregunta a Moose por una página que no se ha indexado, se lo dirá y le indicará que ejecute un rastreo, en lugar de deducir la respuesta a partir de la URL.

## Páginas supervisadas

Las páginas que Hi, Moose comprueba en busca de cambios relevantes para AEO. Las páginas encontradas por el descubrimiento del sitio, por [Google Search Console](../integrations/google-search-console.md) y por las [ejecuciones de visibilidad](../visibility/overview.md) aparecen aquí automáticamente.

También puede añadir páginas a mano con una URL completa, buscar y filtrar la lista, pasar páginas y eliminar las que no le interesen.

## Rutas bloqueadas

Los rastreos omiten las rutas bloqueadas y todo lo que cuelga de ellas, y las páginas coincidentes se retiran de la supervisión.

La coincidencia es por prefijo de segmento de ruta. Bloquear `/results/` cubre `/results/` y todas sus subrutas, pero **no** `/results-archive/`: tiene que coincidir el segmento, no solo la cadena de texto.

Es la herramienta adecuada para páginas de resultados de búsqueda, páginas de listado filtradas, archivos paginados y cualquier otra cosa que genere un gran número de URL casi idénticas que prefiera no rastrear, indexar ni recibir avisos sobre ellas.

## Qué llega a su Inbox

Un rastreo produce **un único resumen por ejecución**, no un elemento por página modificada. El resumen se abre en una tabla de páginas modificadas con qué ha cambiado, un nivel de impacto y acciones por página.

Los niveles de impacto son **Critical**, **Notable**, **Low**, **Unreachable** y **Not reviewed**.

Dos controles regulan el ruido:

- **Include informational AEO changes**: desactivado de forma predeterminada. Al activarlo, los cambios de bajo impacto también generan elementos en el Inbox.
- **OS notification minimum severity**: solo los elementos del Inbox iguales o superiores a este nivel muestran una notificación de escritorio. Póngalo en Info si quiere que los cambios de bajo impacto también aparezcan a nivel del sistema operativo.

## Preguntar a Moose qué ha cambiado

El resumen incluye una acción **Ask Moose about all of this** que entrega la instantánea completa del rastreo al chat y le pregunta qué es lo más importante y qué hacer primero. Las páginas individuales tienen su propia acción **Ask Moose**, que pasa únicamente el cambio registrado de esa página.

Ambas se limitan a la instantánea registrada. Si la instantánea no explica por qué ha cambiado algo, Moose tiene instrucciones de decirlo en lugar de inventar un motivo.

## Páginas inaccesibles

Si no se puede acceder a una página o a todo el sitio, se informa como un tipo de cambio propio en lugar de descartarse en silencio. Una caída de todo el sitio produce un único elemento **Site unreachable** en lugar de un aviso por página.
