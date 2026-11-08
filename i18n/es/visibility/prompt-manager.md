---
source_hash: 52e4fc142ac45ba9ec93251b7b681cb95c1e09d409fef443f88b56ac8cbebaa7
---
# Prompt Manager

## Para qué sirve

El Prompt Manager es donde crea y organiza las consultas reales que Hi, Moose comprueba en los motores de IA: los prompts que sus clientes escribirían o preguntarían de forma realista.

## Organizar los prompts por categorías

Los prompts se agrupan en categorías que aparecen en la lista de filtros de la izquierda: **Todos los prompts**, **Sin categoría** y las categorías personalizadas que usted cree (por ejemplo, por tema o por campaña). Añada una categoría nueva desde el campo situado al final de la lista. Los espacios de trabajo del plan gratuito están limitados a 5 categorías.

## Añadir y editar un prompt

Escriba un prompt nuevo y añádalo a una categoría. Para cada prompt puede:

- Editar el texto del prompt.
- Elegir en qué motores de IA se ejecuta. **Seleccionar modelos** abre un selector con todos los motores que su plan puede supervisar, tanto las versiones por API como las de consulta local (véase [los motores que puede supervisar](settings.md#los-motores-que-puede-supervisar)). Los motores de consulta local necesitan que la aplicación de escritorio esté abierta cuando se ejecuta la comprobación.
- Retirar el prompt (véase más abajo).
- Eliminar el prompt.

A diferencia de un único ajuste para toda la cuenta, **la selección de modelos es por prompt**: un prompt puede ejecutarse solo en ChatGPT y Gemini mientras otro se ejecuta en todos los motores compatibles, de modo que solo gasta asignación en los motores que importan para esa consulta concreta.

## Buscar y seleccionar varios prompts

**Buscar prompts** filtra la lista por texto. Marque varios prompts y la barra de herramientas ofrece **Asignar categorías**, **Asignar modelos**, **Retirar seleccionados** y **Eliminar seleccionados**, de modo que un cambio en muchos prompts se guarda en un solo paso en lugar de prompt a prompt. Solo puede eliminar los prompts que usted creó, salvo que sea el propietario del equipo.

## Retirar un prompt

Retire un prompt cuando se haya quedado desactualizado pero su historial siga mereciendo la pena, por ejemplo un prompt que menciona el año pasado. Un prompt retirado:

- conserva todos sus resultados anteriores, así que las tendencias y los informes siguen incluyéndolos;
- queda fuera de las nuevas ejecuciones, así que no cuesta nada;
- queda fuera de la lista de [Oportunidades](overview.md#oportunidades).

Los prompts retirados aparecen en la sección **Prompts retirados** de la lista de filtros, cada uno con la fecha en que se retiró, y **Restaurar** lo devuelve a la supervisión. Añadir un prompt nuevo con el mismo texto que uno retirado no hace nada; restáurelo en su lugar. **Eliminar** también saca un prompt de la supervisión futura y conserva los datos históricos de ejecución para los informes, pero no se puede restaurar.

## Diagnostic Prompts

**Prompts de diagnóstico** es una categoría reservada y gestionada por el sistema, basada en su [Brand Truth Profile](../getting-started/context/brand-truth-profile.md). En lugar de escribirlos a mano:

1. Pulse **Generar desde Brand Truth** (o configure antes su Brand Truth Profile si aún no lo ha hecho).
2. Hi, Moose propone prompts diseñados específicamente para detectar que la IA describe mal a sus clientes, sus capacidades o sus competidores.
3. Revise las sugerencias en una ventana: active o desactive cualquier prompt, edite la redacción o elimine alguno por completo antes de añadirlos a la supervisión.
4. La ventana muestra un coste estimado antes de que confirme: prompts × modelos × ejecuciones por semana ≈ total de ejecuciones semanales.

Si su Brand Truth Profile todavía no tiene contenido suficiente para generar prompts de diagnóstico significativos, Hi, Moose se lo dice en lugar de producir relleno genérico: añada antes preguntas de clientes, capacidades clave o competidores a su perfil.

## Almacenamiento local de los prompts

En los planes BYOK, que funcionan solo en local, las categorías de prompts, las definiciones de los prompts y las selecciones de modelos se guardan en su dispositivo en lugar de sincronizarse con la nube.
