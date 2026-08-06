---
source_hash: 185a9611ccdaef3c98b73cc4349bc1d586a1fa03b38212ecab7ffca94af54a21
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/visibility/settings/)

# Configuración de Visibility

## Para qué sirve

La configuración de Visibility controla con qué frecuencia comprueba Hi, Moose la visibilidad, qué modelo puntúa los resultados y qué términos de marca y dominios cuentan para sus métricas. Los prompts y los temas se gestionan en el [Prompt Manager](prompt-manager.md); esta pantalla trata de la mecánica de las ejecuciones.

## Programación de ejecuciones

- **Cadencia**: diaria, días laborables, semanal o solo manual.
- **Hora de ejecución preferida** y, en la cadencia semanal, un **día de la semana**. Las ejecuciones se realizan en su zona horaria local.
- **Muestras por prompt**: las ejecuciones programadas pueden repetir cada prompt varias veces y promediar los resultados para obtener una tasa de visibilidad más estable. El botón manual **Run now** utiliza siempre una sola muestra. Aumentar este valor multiplica el consumo de tokens en la misma proporción, y Hi, Moose le avisa antes de guardar un valor más alto.

!!! note "Las ejecuciones programadas necesitan este dispositivo encendido"
    En **Preview Mode** y en los planes **BYOK**, la programación se ejecuta en local, en su equipo: una ejecución programada no puede iniciarse si el ordenador está apagado o suspendido, o si Hi, Moose está completamente cerrado. Mantenga la aplicación abierta (o minimizada en la bandeja del sistema) para que las ejecuciones programadas puedan realizarse. Los **planes gestionados** desbloquean un programador en la nube siempre activo que no depende de que su dispositivo esté encendido. Los motores de consulta local siguen requiriendo la aplicación abierta sea cual sea el plan, ya que esas comprobaciones se ejecutan desde su equipo.

## Notificaciones por correo

Active **Scheduled visibility email reports** para recibir el informe de visibilidad por correo electrónico cuando terminen las ejecuciones programadas. Es una preferencia de notificación personal, distinta de la [configuración de notificaciones del Inbox](../inbox/notifications.md).

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

Elija qué motores se preseleccionan cada vez que añade un prompt en el [Prompt Manager](prompt-manager.md); después puede cambiar la selección prompt a prompt. Los modelos marcados como **Paid** requieren un plan de pago o BYOK; Preview Mode se limita a los modelos de consulta local. Cada modelo marcado aquí cuenta para el consumo de tokens cuando se ejecutan las comprobaciones de visibilidad.

## Repetir la incorporación

Vuelva a ejecutar el asistente de incorporación de visibilidad en cualquier momento para actualizar desde cero su dominio supervisado, sus prompts y sus preferencias de seguimiento.
