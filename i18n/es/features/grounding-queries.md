---
source_hash: 3856622231055de776fe82082345666ad4d8429b9d735111e9d399831a122f47
---
# Consultas de grounding de AI Mode

## Para qué sirve

Esta función le muestra las búsquedas de Google que ejecutó Gemini al fundamentar su respuesta a un prompt, junto con las fuentes que citó y la respuesta fundamentada que redactó.

!!! info "Qué es esto, exactamente"
    Hi, Moose pide a la API de Gemini que responda a su prompt con la fundamentación por búsqueda de Google activada y después lee la lista de búsquedas que emitió el modelo. No es una grabación del AI Mode de consumo de Google. AI Mode es una superficie distinta y no expone sus consultas internas a nadie. Lo que obtiene es la aproximación más cercana disponible: el mismo índice de búsqueda, la misma familia de modelos y formulaciones de consulta que se parecen mucho a las que produce AI Mode. Trátelo como una señal sólida, no como una transcripción, y cuente con cierta variación entre ejecuciones del mismo prompt.

!!! note "Disponibilidad"
    Esta función ejecuta en segundo plano una llamada gestionada de fundamentación a Gemini, por lo que requiere un espacio de trabajo **gestionado de pago**. Esto se mantiene incluso en los planes BYOK: BYOK mantiene local la generación principal del chat, pero la captura de consultas de grounding utiliza infraestructura gestionada de Hi, Moose cuyo funcionamiento nos cuesta dinero, así que no se incluye en BYOK Free ni en BYOK Premium. Preview Mode tampoco la incluye.

## Cómo ejecutarla

1. Desde el [Chat](../chat/overview.md), elija el inicio rápido **Capture AI Mode grounding queries** (o pídalo directamente).
2. Introduzca el prompt que quiere analizar.
3. Hi, Moose consulta las consultas de grounding de Gemini para ese prompt y devuelve:
    - Las consultas de grounding que Gemini utilizó realmente.
    - Las fuentes citadas.
    - La propia respuesta fundamentada.

## Por qué importa

Las consultas de grounding le muestran cómo un motor de respuesta convierte un solo prompt en un abanico de búsquedas reales. Eso resulta útil para entender por qué su página se está recogiendo o no, y para detectar variaciones de consulta que actualmente no está supervisando en [Visibility](../visibility/overview.md) ni en el [Prompt Manager](../visibility/prompt-manager.md).

## Si una ejecución falla

Si Hi, Moose no puede recopilar consultas de grounding reales para un prompt, se lo dice en lugar de presentar una suposición. Inténtelo de nuevo en un momento o compruebe que el espacio de trabajo tiene una suscripción gestionada activa.
