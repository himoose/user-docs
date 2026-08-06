---
source_hash: 3b2a6720bd62d36c159ec05f39cfb8f6e59efa7a27d7e6054053a2fcb1d2c950
---
# Consultas fan-out de ChatGPT

## Para qué sirve

Esta función captura las búsquedas «fan-out» individuales que ejecutó el paso de búsqueda web de OpenAI al responder a su prompt, junto con las fuentes que citó y una vista previa de la respuesta.

!!! info "Qué es esto, exactamente"
    Hi, Moose llama a la API Responses de OpenAI con su herramienta de búsqueda web activada y después lee las búsquedas que efectuó esa ejecución. No es una captura del fan-out propio del producto de consumo ChatGPT, que OpenAI no expone. Lo que obtiene es la aproximación más cercana disponible: la misma capa de búsqueda web, impulsada por la misma familia de modelos, de modo que la expansión de consultas se parece mucho a la de ChatGPT Search. Trátelo como una señal sólida, no como una transcripción, y cuente con cierta variación entre ejecuciones del mismo prompt.

!!! note "Disponibilidad"
    Esta función ejecuta en segundo plano una captura gestionada del rastro de búsqueda web de OpenAI, por lo que requiere un espacio de trabajo **gestionado de pago**. Esto se mantiene incluso en los planes BYOK: BYOK mantiene local la ejecución principal del modelo, pero la captura de fan-out utiliza infraestructura gestionada de Hi, Moose cuyo funcionamiento nos cuesta dinero, así que no se incluye en BYOK Free ni en BYOK Premium. Preview Mode tampoco la incluye.

## Cómo ejecutarla

1. Desde el [Chat](../chat/overview.md), elija el inicio rápido **Capture ChatGPT fan-out queries** (o pídalo directamente).
2. Introduzca el prompt que quiere analizar.
3. Hi, Moose captura la respuesta de ChatGPT y devuelve:
    - Las consultas fan-out diferenciadas que ejecutó ChatGPT.
    - Las fuentes citadas.
    - Una vista previa de la respuesta.

Si OpenAI no expuso ninguna consulta fan-out diferenciada en una ejecución concreta, Hi, Moose le muestra igualmente el rastro de búsqueda gestionado y las fuentes citadas que sí pudo capturar, en lugar de presentar un resultado vacío o inventado.

## Por qué importa

Las consultas fan-out revelan la expansión de consultas que hay detrás de una respuesta fundamentada en la web, lo que resulta útil para entender qué formulaciones concretas están generando (o dejando de generar) citas a su contenido. Eso alimenta directamente lo que supervisa en [Visibility](../visibility/overview.md) y lo que planifica en los [Content Briefs](content-briefs.md).
