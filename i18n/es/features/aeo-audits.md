---
source_hash: a8e831ea98a893f4158e5124991eae0686f8eb64e2448fe9541f8444c4680099
---
# AEO Audits

## Para qué sirve

Una AEO audit (auditoría de optimización para motores de respuesta) puntúa el grado de preparación de una página para ser comprendida, recuperada y citada por sistemas de IA como ChatGPT, Google AI Overviews, Perplexity y Gemini, y después le entrega un plan de acción priorizado y respaldado por evidencias para mejorarla.

Esto sustituye los «consejos de AEO» sueltos por un artefacto duradero y comparable: cada auditoría produce una tarjeta de puntuación y un plan de acción que puede revisar, y las auditorías posteriores sobre la misma página pueden verificar si sus cambios han movido realmente la puntuación.

## Qué se puntúa

La puntuación global es un compuesto ponderado de ocho categorías, cada una puntuada de 0 a 100:

1. **Actualidad**: señales de actualidad y de actualización.
2. **Estructura**: encabezados, listas, tablas y párrafos que un motor de respuesta pueda analizar.
3. **Semantic Clarity**: hasta qué punto el contenido se ajusta a su consulta objetivo y a su intención.
4. **Extractabilidad**: con qué facilidad puede un motor de respuesta extraer una definición, un dato o un punto clave.
5. **Citation Potential**: señales de atribución y de fuentes, basadas en los enlaces de referencia externos de la página.
6. **Exhaustividad**: cobertura de los subtemas que las personas y los motores de respuesta esperan para esa consulta.
7. **Trust Signals**: coherencia, concreción y matización de las afirmaciones en la forma en que la página presenta su atribución y sus fuentes. Esta categoría no verifica las afirmaciones frente a fuentes externas: mide lo bien atribuidas y concretas que son las propias afirmaciones de la página.
8. **Answer Readiness**: colocación de la respuesta directa cerca del inicio, una idea por bloque, lenguaje referencial claro (evitando «esto», «ello» o «ellos» de forma vaga) y denominación coherente de las entidades. La puntuación tiene en cuenta el idioma en inglés, alemán, español, francés, italiano y portugués.

La auditoría también registra señales de Engagement, Entity Recognition y Media Enrichment, aunque no influyen en la puntuación global ni aparecen en la tarjeta de puntuación.

## Comprobaciones de infraestructura y recuperación

Junto a la puntuación de contenido, cada auditoría comprueba si un motor de respuesta puede llegar siquiera a recuperar la página:

- **Acceso de los rastreadores de IA**: comprueba las reglas de robots.txt para cada uno de los tokens concretos de rastreador de IA que utilizan OpenAI, Anthropic, Perplexity, Google y Bing (cubriendo por separado sus rastreadores de entrenamiento, de indexación y de consulta en vivo, ya que un sitio puede bloquear uno y permitir otro). Un rastreador de recuperación o de indexación bloqueado se marca como crítico; un agente de consulta en vivo bloqueado es de prioridad media; y un bloqueo solo de entrenamiento se anota como una decisión de política legítima y neutra que no afecta a las citas.
- **Renderizado en servidor y detección de shell renderizado en cliente**: la mayoría de los rastreadores de IA no ejecutan JavaScript. Si el contenido esencial de una página solo aparece tras el renderizado en el cliente, se marca como un hallazgo crítico y destacado, no como una nota técnica menor, porque es un problema de recuperación previo a cualquier optimización de contenido.
- **Higiene de recuperación**: comprueba una muestra de enlaces internos en busca de enlaces rotos y cadenas de redirecciones.
- **Presencia en el índice de Bing**: comprueba si la página parece estar indexada por Bing, ya que Microsoft Copilot y parte de la búsqueda de ChatGPT dependen del índice de Bing. Los veredictos son deliberadamente conservadores: un resultado no concluyente se comunica como no concluyente en lugar de suponerse, y el veredicto de «no listada» solo se muestra cuando la comprobación tiene señales reales que lo respalden.

## Contexto externo y de cobertura

- **Panorama de citas**: cuando se ejecuta investigación en vivo, la auditoría informa de qué dominios citó realmente un motor de respuesta para la consulta objetivo, si el sitio auditado está entre ellos y si las fuentes de terceros (sitios de comunidad, sitios de reseñas, Wikipedia, YouTube) dominan la respuesta. Se comunica como contexto que en su mayor parte no puede corregir editando su propia página, en lugar de integrarse en la puntuación.
- **Su propio historial de visibilidad**: si la URL auditada ha sido citada en sus [ejecuciones de visibilidad](../visibility/overview.md) recientes, la auditoría lo incorpora, de modo que las recomendaciones tengan en cuenta cómo se está comportando ya la página en las respuestas de IA en lugar de tratarla como una incógnita. Las ejecuciones fallidas se excluyen, para que una caída no se lea como una ausencia de citas.
- **Cobertura fan-out**: contrasta la página con consultas relacionadas en las que un motor de respuesta podría expandir la consulta original (preguntas de «Otras personas también preguntan», búsquedas relacionadas, palabras clave secundarias). Cuando varias de ellas no se abordan en la página, eso se convierte en una recomendación concreta de «cubra estas preguntas relacionadas».

## Niveles de evidencia en las recomendaciones

Cada problema y cada recomendación se etiquetan según la solidez de la evidencia que los respalda:

- **Comprobado**: condiciones previas de recuperación con fuerte respaldo empírico (acceso de los rastreadores, renderizado en servidor, enlaces funcionales, indexación en buscadores).
- **Orientativa**: respaldadas por investigación observacional a gran escala, pero sin garantía (colocación de la respuesta al principio, actualidad, claridad estructural).
- **Best-practice**: plausibles y de bajo coste, pero sin demostración de que muevan las citas de IA (añadir estadísticas, citas textuales o pulir las fuentes).

La auditoría no recomienda marcado schema/JSON-LD, archivos `llms.txt` ni tácticas de acumulación de palabras clave como forma de mejorar las citas de IA, ya que la investigación actual no respalda tratarlos como palancas de citación.

## Cuántas recomendaciones recibe

El número de recomendaciones depende de cuántos problemas reales se encuentren, ponderado por la puntuación global de la página: una página con problemas reales verá más recomendaciones y una que ya puntúa bien verá menos, a veces ninguna. El número nunca se rellena artificialmente para alcanzar una cifra fija.

## Ejecutar una auditoría

1. Facilite una URL en producción o pegue un borrador, junto con la consulta objetivo que alguien utilizaría para encontrar este contenido.
2. Hi, Moose captura una instantánea acotada del contenido y la estructura de la página, utilizando como evidencia principal la versión estática (sin renderizar con JavaScript), porque es lo más parecido a lo que ven realmente la mayoría de los rastreadores de IA.
3. Cuando resulta útil, recopila evidencias reales de motores de respuesta o de citas para la consulta objetivo.
4. Si su proyecto tiene una propiedad conectada de [Google Search Console](../integrations/google-search-console.md) para esa URL, el rendimiento de búsqueda propio se tiene en cuenta en la priorización y en la seguridad de las recomendaciones. No modifica la puntuación AEO subyacente.
5. Hi, Moose puntúa la página, crea una línea base (o verifica frente a una anterior) y monta la auditoría como un artefacto duradero con un plan explícito de siguiente acción.

## Verificar la mejora

Como cada auditoría se guarda como línea base, ejecutar una auditoría nueva sobre la misma página tras hacer cambios produce un **resultado de verificación**, que muestra si la puntuación ha mejorado realmente y no solo si usted ha hecho ediciones.

## Integridad

Las AEO audits nunca inventan evidencias. Si Hi, Moose no puede recopilar las evidencias o completar realmente un paso de puntuación, la auditoría falla de forma explícita y le explica por qué, en lugar de presentar una suposición como resultado terminado. Si la búsqueda en vivo y la investigación de la competencia no pueden completarse en una auditoría gestionada de pago, la auditoría termina igualmente con las evidencias de página de que dispone, indicando explícitamente que la investigación en vivo no estuvo disponible en esa ejecución.

## Derechos según el plan

- **Preview Mode (gratuito)** ejecuta las auditorías con un modelo local Gemma 4 activado. Ya no hay una asignación gratuita mensual de auditorías en la nube: configure un [modelo local](../getting-started/settings.md#local-model) y las auditorías serán gratuitas, tantas veces como quiera.
- **Los planes BYOK** ejecutan las auditorías en local con su propia clave de OpenRouter.
- **Los planes gestionados** utilizan los modelos gestionados de Hi, Moose con el saldo de créditos normal de su cuenta. No hay una moneda aparte de «créditos de auditoría» que controlar.

## Siguientes acciones tras una auditoría

El plan de acción de una auditoría enlaza directamente con otras funciones: generar un [brief de contenido](content-briefs.md), preparar una [edición y su vista previa](drafts-and-publishing.md) o añadir FAQ o key points, de modo que la auditoría sea un punto de partida para actuar y no solo un informe.
