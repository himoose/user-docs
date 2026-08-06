---
source_hash: 40b089c8c06f81c797410e131c0f51ee08f0beba3baaaf1ad18b0794a101df1a
---
# Visibility

## Para qué sirve

El panel de Visibility muestra cómo se comporta realmente su marca en la búsqueda con IA: las consultas que usan los clientes para encontrarle, si su marca entra en la lista corta y si los motores de IA la describen con exactitud. Es la vista principal para los pasos **supervisar** y **detectar** del [ciclo central de operaciones](../index.md#el-ciclo-central-de-operaciones).

El panel tiene tres pestañas:

| Pestaña | A qué responde |
|---|---|
| **Resumen** | ¿Cómo lo estoy haciendo? |
| **[Competencia](competitors.md)** | ¿Cómo lo estoy haciendo frente a ellos? |
| **Temas y motores** | ¿Dónde soy fuerte o débil exactamente? |

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

## Topics & Engines

Esta pestaña desglosa el rendimiento de dos maneras:

- **Tasa de mención por tema**: con qué frecuencia aparece cada marca en las respuestas de IA de cada tema.
- **Tendencia de la tasa de mención por tema**: lo mismo, desglosado en el tiempo.
- **Tasa de mención por plataforma**: un mapa de calor de la frecuencia con la que aparece cada marca en las respuestas de cada plataforma durante el periodo.

Los temas proceden de las categorías de sus prompts. Si sus prompts no están categorizados, esta pestaña le invita a organizarlos en el [Prompt Manager](prompt-manager.md) en lugar de mostrar un gráfico vacío.

## Exportar

**Exportar** ofrece dos formatos:

- **Hoja de cálculo CSV**: todos los resultados de la vista actual, para Excel o Google Sheets.
- **Informe ejecutivo PDF**: un informe listo para imprimir de la vista actual, con los gráficos y datos competitivos de la pestaña Competition.

Las exportaciones respetan los filtros activos, y la portada del PDF indica qué filtros se aplicaron, de modo que un informe no pueda confundirse con una imagen completa de la cuenta. En los planes de pago, el PDF lleva su [marca blanca](../agency/white-label.md) si la ha configurado.

## Ejecutar comprobaciones de visibilidad

Pulse **Ejecutar ahora** para una comprobación bajo demanda. El comportamiento depende de su [plan](../getting-started/account-modes.md):

- **Preview Mode** ejecuta comprobaciones de consulta local directamente desde su dispositivo contra las superficies públicas de búsqueda con IA. Hi, Moose le pide confirmación primero, porque encadenar comprobaciones puede activar bloqueos temporales por límite de peticiones en esas superficies. La puntuación de sentimiento, narrativa y paridad necesita un modelo local Gemma 4 activado; sin él, esas comprobaciones se omiten.
- **Los planes BYOK** se ejecutan en local con su propia clave de OpenRouter.
- **Los planes gestionados** se ejecutan a través de la infraestructura de Hi, Moose. Si a su espacio de trabajo no le queda asignación suficiente este mes para la programación actual, las ejecuciones programadas se pausan hasta que cambie de plan, ajuste su [cadencia de ejecución](settings.md#programacion-de-ejecuciones) o se reinicie la asignación. Hi, Moose le indica cuántas unidades hacen falta frente a las restantes.

Puede detener una ejecución antes de tiempo, y las ejecuciones interrumpidas por una actualización de la aplicación se reanudan en lugar de perderse.

## Adónde ir a continuación

- **[Competidores y Share of Voice](competitors.md)**: posición competitiva, citas de competidores y brechas.
- **[Prompt Manager](prompt-manager.md)**: añadir, organizar y categorizar los prompts supervisados.
- **[Configuración de Visibility](settings.md)**: programación de ejecuciones, modelo de puntuación, seguimiento de competidores, términos y dominios de marca secundarios y modelos predeterminados.
