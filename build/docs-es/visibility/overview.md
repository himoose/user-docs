---
source_hash: e5cf87efe7298e31a0e0c034a7c0d36431b70c08378225d4dd5c73357dd59a4f
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/visibility/overview/)

# Visibility

## Para qué sirve

El panel de Visibility muestra cómo se comporta realmente su marca en la búsqueda con IA: las consultas que usan los clientes para encontrarle, si su marca entra en la lista corta y si los motores de IA la describen con exactitud. Es la vista principal para los pasos **supervisar** y **detectar** del [ciclo central de operaciones](../index.md#el-ciclo-central-de-operaciones).

El panel tiene seis pestañas:

| Pestaña | A qué responde |
|---|---|
| **Resumen** | ¿Cómo lo estoy haciendo? |
| **[Competencia](competitors.md)** | ¿Cómo lo estoy haciendo frente a ellos? |
| **Menciones** | ¿Qué marcas se nombran en estas respuestas? |
| **Citas** | ¿En qué fuentes se apoyan realmente los motores? |
| **Temas y motores** | ¿Dónde soy fuerte o débil exactamente? |
| **Prompts** | ¿Qué ocurrió en cada prompt concreto? |

## Métricas

Cada ejecución informa de unas métricas principales para el periodo seleccionado:

- **Cuota de menciones**: con qué frecuencia se menciona su marca en los prompts y motores supervisados.
- **Cuota de citas**: con qué frecuencia se cita su dominio como fuente.
- **Sentimiento**: el tono medio (positivo, mixto, neutro, negativo) de las menciones.
- **Posición media**: dónde suele situarse su marca cuando aparece en una lista o clasificación. Muestra **Datos insuficientes** hasta que hay suficientes menciones posicionadas para calcular una media.
- **Desviación narrativa**: si las respuestas de la IA se alejan de su posicionamiento previsto.
- **Paridad de características**: si las respuestas de la IA representan con exactitud lo que usted ofrece.

Narrative Drift y Feature Parity muestran **Sin puntuar** con un enlace para configurar el Brand Truth Profile hasta que lo haya rellenado. Estas dos métricas solo son significativas cuando Hi, Moose sabe qué es cierto sobre su marca para poder compararlo. Véase [Brand Truth Profile](../getting-started/context/brand-truth-profile.md).

!!! note "Las observaciones fallidas se excluyen, no cuentan como ausencias"
    Si un motor no estaba disponible o una petición falló, esa observación queda fuera de todas las métricas en lugar de puntuarse como «su marca no fue mencionada». Una ejecución con problemas de conexión informa sobre menos observaciones en lugar de informar de una caída falsa. La vista por prompt las etiqueta como **Respuesta no disponible** e indica cuántas se han excluido.

## Filtros y periodo

- Filtre por **Tema**, **Motor de IA**, **Prompt** (selección múltiple con búsqueda), **Página**, **Sentimiento**, **Narrativa** o **Paridad de características**, o borre todos los filtros a la vez.
- El filtro **Página** acota a URL concretas y permite buscarlas por ruta. Muestra correctamente los motores en los que la URL **no** fue citada, de modo que puede ver tanto dónde falta una página como dónde aparece.
- Defina un rango de fechas en **Periodo** y pulse **Aplicar**, o pulse **Comparar** para superponer un periodo anterior o la ejecución previa.

## Tendencia en el tiempo

El gráfico de tendencia representa **Menciones**, **Citations**, **% positivo** o la posición media en intervalos de **día**, **semana** o **mes**, desglosado por motor de IA o con **Todos los modelos** combinados, para que vea si un motor concreto está moviendo las cifras.

## Detalle por prompt

Debajo del gráfico:

- **Tasa de mención** desglosa los resultados por motor, mostrando cuáles le mencionaron y cuáles no.
- **Páginas más citadas** muestra qué URL suyas se están citando y desde qué motores.
- **Desglose por prompt** despliega cualquier prompt supervisado para ver los resultados individuales por motor, incluida la respuesta completa de la IA y el razonamiento de sentimiento, narrativa y paridad de funciones.

Cada prompt incluye un enlace para **investigar en el chat** que entrega los datos exactos de la observación a Moose y le pide que recomiende si el siguiente paso es una [AEO audit](../features/aeo-audits.md) de una página existente o un nuevo [brief y borrador de contenido](../features/content-briefs.md).

## La pestaña Resumen

El Resumen abre con un resumen escrito del corte actual: unos párrafos que explican en qué punto está, qué se ha movido y qué merece una mirada, en frases y no en cifras. Se genera a partir de la misma hoja de datos que usa el informe, y puede pulsar **Reescribir el resumen** si quiere otra redacción. Cuando no hay ningún modelo disponible para escribirlo, el Resumen recurre a una versión construida directamente con los números y lo indica.

Debajo del resumen hay dos bloques:

- **En qué punto está**: su Share of Voice, la tasa de mención sobre las respuestas leídas, las citas, la posición media cuando se le nombra y la tasa de mención por motor, con todo el conjunto de marcas supervisadas a su lado.
- **¿La IA le describe con precisión?**: alineación del posicionamiento, desglose del tono y una lista de **respuestas que conviene revisar**: las respuestas concretas en las que un motor describió mal una capacidad o se apartó de su posicionamiento. Cada una abre la respuesta o salta a ella en la pestaña Prompts.

## Menciones

La pestaña **Menciones** es la lista completa de cada marca, producto o sitio web que los motores nombraron en las respuestas del corte actual: no solo usted y sus competidores supervisados, sino todos los que aparecieron.

Cada fila muestra en cuántas respuestas se nombró la marca, ese dato como porcentaje de las respuestas del corte, su cuota sobre todas las menciones, su posición media entre las marcas nombradas en una respuesta y su veredicto de sentimiento más frecuente. Pase el ratón por cualquier valor de sentimiento para ver el desglose positivo/mixto/neutral/negativo, y por un encabezado de columna para su definición exacta.

Encima de la tabla, una **tendencia de presencia de menciones** representa las marcas más mencionadas, y a usted, a lo largo del tiempo.

Aquí es donde aparecen los competidores que no sabía que tenía. Las marcas se leen del texto de la respuesta con el modelo de puntuación, así que la lista saca a la luz nombres que usted nunca añadió a su seguimiento.

## Citas

La pestaña **Citas** es la misma idea aplicada a las fuentes: cada dominio o página que los motores citaron en el corte actual.

Alterne entre **Por dominio** y **Por URL de página**, y filtre por **Todo** o **Ni usted ni un competidor** para ver las fuentes de terceros que están dando forma a las respuestas. Cada fuente se clasifica: su marca, competidor, red social, sitio de reseñas, publicación, referencia, desarrollo u otros.

Las columnas son:

| Columna | Qué significa |
|---|---|
| **Prompts citados** | En cuántas respuestas se citó este dominio o URL |
| **Presencia %** | Ese dato como porcentaje de las respuestas del corte |
| **Número de citas** | Total de veces que se citó, contando repeticiones |
| **Visibilidad %** | Su cuota sobre todas las citas del corte |
| **Posición media** | Su posición media en las listas de citas de los motores |
| **Cambio** | Movimiento frente al periodo de comparación o la ejecución anterior |

**Detalles** en cualquier fila enumera las páginas que hay detrás y los prompts por los que se citó cada página. Cualquier dominio de la tabla puede añadirse directamente a sus competidores supervisados con **Seguir como competidor**, de modo que un nombre que descubra aquí entra en el [Share of Voice](competitors.md) sin volver a teclearlo.

Ambas tablas se descargan en CSV.

!!! note "Los motores que no navegan no devuelven citas"
    Las citas provienen de motores que consultan la web mientras responden. Un modelo local, o un motor que responde solo con su propio entrenamiento, no devuelve ninguna, así que una tabla vacía con un filtro estrecho no significa necesariamente que haya un problema con su sitio.

## Topics & Engines

Esta pestaña desglosa el rendimiento de dos maneras:

- **Tasa de mención por tema**: con qué frecuencia aparece cada marca en las respuestas de IA de cada tema.
- **Tendencia de la tasa de mención por tema**: lo mismo, desglosado en el tiempo.
- **Tasa de mención por plataforma**: un mapa de calor de la frecuencia con la que aparece cada marca en las respuestas de cada plataforma durante el periodo.

Los temas proceden de las categorías de sus prompts. Si sus prompts no están categorizados, esta pestaña le invita a organizarlos en el [Prompt Manager](prompt-manager.md) en lugar de mostrar un gráfico vacío.

## Exportar

**Exportar** ofrece dos formatos:

- **Hoja de cálculo CSV**: todos los resultados de la vista actual, para Excel o Google Sheets.
- **Informe ejecutivo PDF**: un informe completo de trece secciones sobre la vista actual, escrito para entregárselo a alguien que no estuvo en la sala.

El informe abre con una narración escrita en lugar de un volcado de gráficos, y después recorre: en qué punto está, si la IA le describe con precisión, el movimiento del periodo, motor por motor, dónde le cita la IA, preguntas que ganan los competidores, por qué se cita a los competidores, el campo completo, marcas nombradas en las respuestas de IA, dominios que cita la IA, tasa de mención por motor, tasa de mención por tema y una sección final que explica cómo leer cada métrica.

Las exportaciones respetan los filtros activos, y la portada del PDF indica qué filtros se aplicaron, de modo que un informe no pueda confundirse con una imagen completa de la cuenta. En los planes de pago, el PDF lleva su [marca blanca](../agency/white-label.md) si la ha configurado.

## Ejecutar comprobaciones de visibilidad

Pulse **Ejecutar ahora** para una comprobación bajo demanda. El comportamiento depende de su [plan](../getting-started/account-modes.md):

- **Preview Mode** ejecuta comprobaciones de consulta local directamente desde su dispositivo contra las superficies públicas de búsqueda con IA. Hi, Moose le pide confirmación primero, porque encadenar comprobaciones puede activar bloqueos temporales por límite de peticiones en esas superficies. La puntuación de sentimiento, narrativa y paridad necesita un modelo local Gemma 4 activado; sin él, esas comprobaciones se omiten.
- **Los planes BYOK** se ejecutan en local con su propia clave de OpenRouter.
- **Los planes gestionados** se ejecutan a través de la infraestructura de Hi, Moose. Si a su espacio de trabajo no le queda asignación suficiente este mes para la programación actual, las ejecuciones programadas se pausan hasta que cambie de plan, ajuste su [cadencia de ejecución](settings.md#programacion-de-ejecuciones) o se reinicie la asignación. Hi, Moose le indica cuántas unidades hacen falta frente a las restantes.

Puede detener una ejecución antes de tiempo, y las ejecuciones interrumpidas por una actualización de la aplicación se reanudan en lugar de perderse.

## Cuánto historial se conserva

Cada observación que produce una ejecución se archiva localmente, para que las tendencias, las comparaciones y las tablas de Menciones y Citas puedan mirar más atrás que las últimas ejecuciones. El archivo guarda hasta **400 días** por espacio de trabajo y hasta 200.000 observaciones; superado cualquiera de los dos límites, se descartan las filas más antiguas.

En los planes gestionados de pago, las ejecuciones de visibilidad que se realizan en su máquina también sincronizan sus resultados con la nube, de modo que sus compañeros vean el mismo historial que usted y no solo las ejecuciones que ocurrieron en su propio dispositivo.

## Adónde ir a continuación

- **[Competidores y Share of Voice](competitors.md)**: posición competitiva, citas de competidores y brechas.
- **[Prompt Manager](prompt-manager.md)**: añadir, organizar y categorizar los prompts supervisados.
- **[Configuración de Visibility](settings.md)**: programación de ejecuciones, modelo de puntuación, seguimiento de competidores, términos y dominios de marca secundarios y modelos predeterminados.
