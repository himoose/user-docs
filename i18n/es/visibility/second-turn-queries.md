---
source_hash: bf06b2d4371815f46d4209e9c058c88a274ce098682e93731da1f9cafde41e72
---
# Consultas de segundo turno

## Para qué sirve

Los motores de IA suelen terminar una respuesta invitando a hacer la siguiente pregunta. Una consulta de segundo turno es esa siguiente pregunta, escrita completa para que se entienda por sí sola. Hi, Moose las captura durante las ejecuciones de visibilidad y las muestra en la pestaña **Consultas de segundo turno**, junto con la frecuencia con la que apareció cada una y si su sitio la cubre.

Por ejemplo, un motor puede terminar una respuesta con «¿Quiere que compare estas dos opciones una al lado de la otra?». La consulta de segundo turno es lo que una persona escribiría para aceptar, como «Comparar los convertidores de escritorio elevable y los escritorios elevables completos para una oficina pequeña en casa».

## Cómo activarlo

Abra la [Configuración de Visibility](settings.md#consultas-de-segundo-turno) y vaya a la sección **Consultas de segundo turno**. Active **Capturar consultas de segundo turno**. La opción está desactivada por defecto y se activa por separado en cada proyecto.

Mientras la opción está desactivada, no se captura nada y la pestaña Consultas de segundo turno queda oculta.

Puede activar la opción con los planes gestionados de pago, BYOK Premium y BYOK Agency. En Preview Mode y BYOK Free el interruptor aparece atenuado y muestra la nota **Disponible en los planes de pago**.

Al activarla se añade una pequeña llamada al modelo por cada respuesta de una ejecución. En los planes gestionados de pago, estas llamadas cuentan para la asignación de su plan. En BYOK Premium y BYOK Agency se cargan a su clave de OpenRouter.

## La pestaña Consultas de segundo turno

La pestaña está justo después de **Oportunidades** en el panel de Visibility. Solo aparece cuando la opción está activada. Permanece vacía hasta la primera ejecución de visibilidad posterior a la activación, porque las respuestas de ejecuciones anteriores no se procesan.

La pestaña sigue el periodo y los filtros seleccionados en la parte superior de Visibility. Una consulta aparece en la lista cuando una respuesta de ese periodo la contenía.

### Vistas

- **Más frecuentes** es la vista predeterminada. Muestra una sola lista ordenada por el número de respuestas que contenían cada consulta.
- **Por prompt** agrupa las consultas bajo el prompt supervisado al que siguió cada una.

### Qué muestra una fila

- La consulta.
- **Respuestas con esta consulta: N**, donde N es el número de respuestas que la contenían.
- Los motores y el tema.
- El resultado de la [cobertura del sitio](#cobertura-del-sitio).
- **Mostrar detalles**, que enumera los prompts a los que siguió la consulta bajo **Aparece después de estos prompts**, con un enlace **Ver respuesta** para cada prompt. También muestra las palabras finales del motor.

## Cómo se clasifican las consultas nuevas

La primera vez que aparece una consulta nueva, Hi, Moose comprueba si es lo bastante concreta y cercana al tema como para seguirla. También comprueba si significa lo mismo que una consulta que ya está en la lista. Las consultas que significan lo mismo se cuentan juntas. Las genéricas, como «cuénteme más», quedan fuera.

Esta clasificación se hace al abrir la pestaña. La primera vez que la abre después de una ejecución, la pestaña muestra **Clasificando consultas nuevas: X de Y**.

## Cobertura del sitio

Cada consulta se comprueba una vez con las páginas rastreadas del sitio de su proyecto. La fila muestra entonces uno de estos resultados:

- **Cubierta en el sitio:** seguido de la página.
- **Cubierta en parte en el sitio:** seguido de la página.
- **Sin cobertura en el sitio**.

La cobertura se vuelve a comprobar cuando termina un nuevo rastreo del sitio.

La comprobación necesita un rastreo del sitio completado en su dispositivo, o en el dispositivo que aloja el índice del sitio. Si no hay ningún rastreo completado, la fila muestra **Cobertura del sitio sin comprobar**. En la aplicación web sin un dispositivo de escritorio anfitrión, la cobertura no se comprueba.

## Botones de cada fila

- **Añadir a los prompts en seguimiento** añade la consulta como prompt supervisado bajo el mismo tema que el prompt al que siguió. Después el botón indica **En seguimiento**.
- **Crear un borrador** aparece cuando su sitio no cubre la consulta. Abre un chat nuevo con el formulario del [brief de contenido](../features/content-briefs.md) ya rellenado.
- **Actualizar esta página** aparece cuando su sitio cubre la consulta en parte. Abre el formulario de actualización de contenido de esa página con la consulta como objetivo.
- **Descartar** oculta la fila. **Mostrar descartadas** vuelve a mostrar las filas descartadas y **Restaurar** devuelve una fila a la lista.

## Cuándo se actualiza la lista

Mientras la opción está activada, las consultas nuevas se capturan de cada respuesta en todas las ejecuciones de visibilidad. Se clasifican la próxima vez que abre la pestaña.

Como la pestaña sigue el periodo seleccionado, una consulta deja de aparecer cuando ninguna respuesta de ese periodo la contenía. Elija un periodo más largo para verla de nuevo.

## Equipos y planes

En los planes gestionados de pago, las consultas capturadas, los descartes y los resultados de cobertura se sincronizan con la nube, de modo que los miembros del equipo ven la misma lista. En BYOK Premium y BYOK Agency, todo permanece en su dispositivo.

## Qué no se incluye

- Las preguntas «Related» de Perplexity y las preguntas «People also ask» de Google no se capturan.
- Las consultas de segundo turno no forman parte del [informe ejecutivo PDF](overview.md#exportar).
- Las consultas de segundo turno no están disponibles a través de las herramientas de [Hi, Moose MCP](../integrations/hi-moose-mcp.md).
