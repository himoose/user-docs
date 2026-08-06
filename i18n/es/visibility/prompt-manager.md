---
source_hash: b6472884da7df3e651f78be6893eb9896b38a6327a26378ca1d4cc26b2d0454e
---
# Prompt Manager

## Para qué sirve

El Prompt Manager es donde crea y organiza las consultas reales que Hi, Moose comprueba en los motores de IA: los prompts que sus clientes escribirían o preguntarían de forma realista.

## Organizar los prompts por categorías

Los prompts se agrupan en categorías que aparecen en la lista de filtros de la izquierda: **All prompts**, **Uncategorized** y las categorías personalizadas que usted cree (por ejemplo, por tema o por campaña). Añada una categoría nueva desde el campo situado al final de la lista. Los espacios de trabajo del plan gratuito están limitados a 5 categorías.

## Añadir y editar un prompt

Escriba un prompt nuevo y añádalo a una categoría. Para cada prompt puede:

- Editar el texto del prompt.
- Elegir en qué motores o modelos de IA se ejecuta. **Select models** abre un selector con ChatGPT, Claude, Gemini, Grok, Perplexity, Google AI Mode, Google AI Overview y Bing Copilot (la disponibilidad depende de su plan y, en los motores de consulta local, de que la aplicación de escritorio esté en ejecución).
- Eliminar el prompt.

A diferencia de un único ajuste para toda la cuenta, **la selección de modelos es por prompt**: un prompt puede ejecutarse solo en ChatGPT y Gemini mientras otro se ejecuta en todos los motores compatibles, de modo que solo gasta asignación en los motores que importan para esa consulta concreta.

## Diagnostic Prompts

**Diagnostic Prompts** es una categoría reservada y gestionada por el sistema, basada en su [Brand Truth Profile](../getting-started/context/brand-truth-profile.md). En lugar de escribirlos a mano:

1. Pulse **Generate from Brand Truth** (o configure antes su Brand Truth Profile si aún no lo ha hecho).
2. Hi, Moose propone prompts diseñados específicamente para detectar que la IA describe mal a sus clientes, sus capacidades o sus competidores.
3. Revise las sugerencias en una ventana: active o desactive cualquier prompt, edite la redacción o elimine alguno por completo antes de añadirlos a la supervisión.
4. La ventana muestra un coste estimado antes de que confirme: prompts × modelos × ejecuciones por semana ≈ total de ejecuciones semanales.

Si su Brand Truth Profile todavía no tiene contenido suficiente para generar prompts de diagnóstico significativos, Hi, Moose se lo dice en lugar de producir relleno genérico: añada antes preguntas de clientes, capacidades clave o competidores a su perfil.

## Almacenamiento local de los prompts

En los planes BYOK, que funcionan solo en local, las categorías de prompts, las definiciones de los prompts y las selecciones de modelos se guardan en su dispositivo en lugar de sincronizarse con la nube.
