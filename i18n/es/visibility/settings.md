---
source_hash: 0bf4df4be6bc4ecf9f90b0973d78ad5121f1c5f07aa1f1c11b5f4615df894dae
---
# Configuración de Visibility

## Para qué sirve

La configuración de Visibility controla con qué frecuencia comprueba Hi, Moose la visibilidad, qué modelo puntúa los resultados y qué términos de marca y dominios cuentan para sus métricas. Los prompts y los temas se gestionan en el [Prompt Manager](prompt-manager.md); esta pantalla trata de la mecánica de las ejecuciones.

## Programación de ejecuciones

- **Cadencia**: diaria, días laborables, semanal o solo manual.
- **Hora de ejecución preferida** y, en la cadencia semanal, un **día de la semana**. Las ejecuciones se realizan en su zona horaria local.
- **Muestras por prompt**: las ejecuciones programadas pueden repetir cada prompt varias veces y promediar los resultados para obtener una tasa de visibilidad más estable. El botón manual **Ejecutar ahora** utiliza siempre una sola muestra. Aumentar este valor multiplica el consumo de tokens en la misma proporción, y Hi, Moose le avisa antes de guardar un valor más alto.

!!! note "Las ejecuciones programadas necesitan este dispositivo encendido"
    En **Preview Mode** y en los planes **BYOK**, la programación se ejecuta en local, en su equipo: una ejecución programada no puede iniciarse si el ordenador está apagado o suspendido, o si Hi, Moose está completamente cerrado. Mantenga la aplicación abierta (o minimizada en la bandeja del sistema) para que las ejecuciones programadas puedan realizarse. Los **planes gestionados** desbloquean un programador en la nube siempre activo que no depende de que su dispositivo esté encendido. Los motores de consulta local siguen requiriendo la aplicación abierta sea cual sea el plan, ya que esas comprobaciones se ejecutan desde su equipo.

!!! note "Las ejecuciones en la nube cubren todos los prompts en todos los motores"
    Una ejecución programada en la nube comprueba cada uno de sus prompts supervisados contra cada motor que haya seleccionado para él, en una sola pasada. No hay muestreo de su lista de prompts por ejecución, así que las cifras que devuelve una ejecución programada cubren el conjunto completo y no una parte.

## Notificaciones por correo

Active **Informes de visibilidad por correo electrónico programados** para recibir el informe de visibilidad por correo electrónico cuando terminen las ejecuciones programadas. Es una preferencia de notificación personal, distinta de la [configuración de notificaciones del Inbox](../inbox/notifications.md).

## Términos y dominios de marca secundarios

- **Términos de marca secundarios**: formulaciones alternativas o variantes ortográficas de su marca que también deben contar como mención.
- **Dominios secundarios**: otros dominios que deben contar como citas válidas de marca en este proyecto, además de su dominio principal.

## Seguimiento de competidores

Añada las marcas con las que se compara este proyecto. Cada competidor requiere un nombre y, opcionalmente, un sitio web.

Cuando una respuesta de IA menciona o cita a uno de ellos, alimenta el [Share of Voice, las citas de competidores y las brechas](competitors.md).

Esta lista se comparte con su [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), de modo que los competidores añadidos en cualquiera de los dos sitios aparecen en ambos. Hay un límite de cuántos se supervisan en las ejecuciones de visibilidad: la pantalla indica el número y le avisa si su lista lo supera, para que sepa que solo se están supervisando los primeros.

## Modelo de puntuación

Elija el modelo que utiliza Hi, Moose para puntuar el sentimiento, la desviación narrativa y la paridad de funciones una vez capturada una respuesta:

- El **valor automático** se adapta a su plan:
    - **Preview Mode** utiliza un modelo local Gemma 4 activado. La puntuación se omite hasta que haya uno instalado y activo (Configuración → Local Model).
    - **Los planes BYOK** puntúan con su propia clave de OpenRouter.
    - **Los planes gestionados** puntúan a través del enrutamiento de modelos gestionados de Hi, Moose (la puntuación con modelo local sigue aplicándose donde es compatible).
- También puede seleccionar un modelo concreto en lugar de la opción automática.

Los modelos gratuitos de OpenRouter ya no se ofrecen como opción de puntuación. Resultaban lo bastante poco fiables en la puntuación estructurada como para que los resultados no merecieran comunicarse.

## Modelos predeterminados para prompts nuevos

Elija qué motores se preseleccionan cada vez que añade un prompt en el [Prompt Manager](prompt-manager.md); después puede cambiar la selección prompt a prompt. Los modelos marcados como **De pago** requieren un plan de pago o BYOK; Preview Mode se limita a los modelos de consulta local. Cada modelo marcado aquí cuenta para el consumo de tokens cuando se ejecutan las comprobaciones de visibilidad.

### Los motores que puede supervisar

| Motor | Cómo se ejecuta | Plan |
|---|---|---|
| ChatGPT | API | Cualquiera |
| ChatGPT (local fetch) | Desde su equipo | Cualquiera |
| Claude | API | Cualquiera |
| Gemini | API | Cualquiera |
| Grok | API | Cualquiera |
| Grok (local fetch) | Desde su equipo | Cualquiera |
| Perplexity | API | Cualquiera |
| Perplexity (local fetch) | Desde su equipo | Cualquiera |
| Google AI Mode (local fetch) | Desde su equipo | Cualquiera |
| Google Search AI Overview (local fetch) | Desde su equipo | Cualquiera |
| Google AI Mode | API | De pago |
| Google AI Overviews | API | De pago |
| Bing Copilot | API | De pago |
| DeepSeek | API | De pago |
| Meta AI | API | De pago |

**DeepSeek** y **Meta AI** están desactivados por defecto. Merece la pena activarlos si su categoría tiene tracción real en los mercados donde esos dos son fuertes; si no la tiene, dejarlos apagados mantiene bajo el coste de cada ejecución.

Los motores **local fetch** leen la superficie pública de búsqueda con IA desde su propio equipo en lugar de llamar a una API. No consumen tokens, pero necesitan que la aplicación de escritorio esté abierta cuando se ejecute la comprobación, en cualquier plan.

## Repetir la incorporación

Vuelva a ejecutar el asistente de incorporación de visibilidad en cualquier momento para actualizar desde cero su dominio supervisado, sus prompts y sus preferencias de seguimiento.
