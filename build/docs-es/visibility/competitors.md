---
source_hash: 1c85ff53a55d4b6ecb7d8fbdd11b64ab53c6c37bdd4cb12540b5dc7616afc495
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/visibility/competitors/)

# Competidores y Share of Voice

## Para qué sirve

Responder a la pregunta que sus propias cifras no pueden contestar: cuando un asistente de IA recomienda algo de su categoría, ¿con qué frecuencia es usted y a quién eligen en su lugar?

Lo encontrará en **Visibility → Competencia**.

## Configurar los competidores

Añada competidores en **Visibility → Settings → Competitor tracking**. Cada uno requiere un nombre y, opcionalmente, un sitio web.

Esta lista se comparte con su [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), de modo que los competidores añadidos en cualquiera de los dos sitios aparecen en ambos.

Cuántos se supervisan en las ejecuciones de visibilidad depende de su plan: **5 en Preview Mode y BYOK Free, 15 en todos los planes de pago**. La pantalla de configuración indica el número y le avisa si su lista es más larga, para que sepa que solo se supervisan los primeros.

Entre tres y cinco competidores reales funcionan mejor que una lista larga. Son las marcas con las que realmente le comparan, no todo el sector.

## Share of Voice

El **Share of Voice** es la porción de atención que cada marca se lleva en las respuestas de IA durante el periodo, pero no todas las menciones valen lo mismo.

Aparecer el primero en una respuesta vale más que aparecer el sexto, porque ese es el nombre que el lector se lleva. Por eso cada mención se pondera según el lugar que ocupa en la respuesta:

| Posición en la respuesta | Peso |
|---|---|
| 1.ª | 1,00 |
| 2.ª | 0,70 |
| 3.ª | 0,50 |
| 4.ª | 0,35 |
| 5.ª | 0,25 |
| 6.ª o posterior | 0,15 |

Una mención en la que no se pudo determinar la posición cuenta como 0,50. Además, una respuesta que **cita el sitio web de la marca** suma otro 0,50, porque una cita es una señal más fuerte que una simple mención.

La puntuación ponderada de cada marca se divide después entre el total de todas las marcas supervisadas para obtener su porcentaje.

La pestaña Competition encabeza con su posición («You are 3rd») y la lista ordenada de debajo muestra cada marca supervisada con su porcentaje. Junto a él aparecen la **cuota de menciones** y la **cuota de citas**, que son los recuentos simples sin ponderar, para que pueda ver la imagen en bruto al lado de la ponderada.

!!! note "Por qué la cifra ponderada puede no coincidir con el recuento simple"
    Puede recibir tantas menciones como un competidor y aun así quedar por detrás en Share of Voice, si él aparece siempre el primero y usted siempre el cuarto. Esa diferencia es justo el sentido de la métrica: le está diciendo que las menciones existen pero la prominencia no, que es otro problema y tiene otra solución.

!!! warning "Share of Voice no es Mention Rate"
    Son dos cifras distintas y se mueven de forma independiente.

    El **Share of Voice** es su porción ponderada de la atención total de marca. Es competitivo: un competidor puede hacerlo bajar sin que nada cambie por su parte.

    El **Mention Rate** (en la pestaña Overview) es el porcentaje de prompts supervisados en los que se mencionó su marca. Es absoluto, no está ponderado e ignora por completo a los competidores.

    Su Mention Rate puede subir mientras su Share of Voice baja, si los competidores han crecido más deprisa que usted. Merece la pena vigilar ambos, por motivos distintos.

## Tendencia del Share of Voice

El gráfico de tendencia representa el **Share of Voice** o el **Tasa de mención** a lo largo del tiempo, para que vea si un cambio se debe a que usted ha ganado terreno, a que lo ha ganado un competidor o a que toda la categoría se ha vuelto más ruidosa.

## Top Competitor Citations

Qué páginas de la competencia están citando realmente los motores de IA como fuente. Es el panel más directamente accionable de la pestaña: son las URL concretas que se llevan las citas que usted quiere, y le indican qué considera hoy cada motor de respuesta la mejor fuente sobre esas preguntas.

Compárelo con **Páginas más citadas** de la pestaña Overview, que muestra lo mismo para su propio dominio.

## Competitor Gaps

Preguntas en las que un competidor apareció en una respuesta de IA y su marca no.

Cada brecha muestra qué competidores aparecieron y en qué motores se detectó, con un distintivo:

- **Sin visibilidad**: su marca no aparece para esta pregunta en ningún motor.
- **Parcial**: su marca sí aparece para esta pregunta, pero no en todos los motores. La fila indica en cuáles sí aparece.

Las filas parciales a menudo no requieren ninguna acción. Una pregunta en la que aparece en cuatro motores de cinco no es el mismo problema que una en la que no aparece en ninguno, y el distintivo está ahí para que pueda distinguirlas de un vistazo.

Si la lista está truncada, acote el rango de fechas o los filtros para ver el resto.

## De dónde salen los datos de competidores

Las menciones y citas de competidores se extraen de las mismas observaciones de las ejecuciones de visibilidad que las suyas. No se ejecuta nada adicional ni se rastrean los sitios de la competencia para estos paneles. Si una ejecución falló o un modelo no estaba disponible, esas observaciones se excluyen en lugar de contarse como una ausencia.

## En el informe ejecutivo

El Share of Voice, las principales citas de competidores y las brechas se incluyen en el [informe ejecutivo](overview.md#exportar) exportado, de modo que la imagen competitiva llega a clientes y responsables sin que usted tenga que reconstruirla a mano.
