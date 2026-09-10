---
source_hash: 7e432cdd4918eeb01a120c373ca83181288da1c2c0b01d3aee18207e05092124
---
# Send Moose

## Para qué sirve

Send Moose es donde encarga un trabajo en lugar de hacerlo usted mismo. Describe el encargo en lenguaje llano («averigua a quién están recomendando en nuestro lugar para software de gestión de proyectos y por qué», «comprueba si nuestra página de precios sigue coincidiendo con lo que dicen las páginas comparativas de la competencia») y Moose va y lo hace, usando la web y todo lo que Hi, Moose ya sabe de su proyecto.

Es la diferencia entre un chat que le responde y un agente que se pone a trabajar. El chat es una conversación; Send Moose es un encargo que despacha y al que vuelve más tarde.

Lo encontrará en la barra lateral, en **Send Moose**.

!!! warning "Send Moose es experimental"
    Está en la aplicación y funciona, pero es lo más nuevo y lo menos asentado de Hi, Moose. Vigile la calidad de lo que devuelve, y vigile su consumo de tokens en los planes de pago: Scout y Skeptic se ejecutan en la nube aunque Moose corra en local.

## Qué trae Moose consigo

Un agente web genérico parte de cero y hay que contárselo todo. Moose llega ya conectado a su proyecto:

| Puede leer | Qué significa |
|---|---|
| Sus datos de visibilidad | Resumen, Share of Voice, competidores, temas, prompts y qué ha cambiado |
| Su índice del sitio | Páginas rastreadas, qué ha cambiado en ellas, enlaces internos y su [entity graph](../features/entity-graph.md) |
| Su historial de AEO | Auditorías anteriores y su detalle, contexto de citas, acceso de rastreadores, cobertura de temas |
| [Google Search Console](../integrations/google-search-console.md) | Sus datos reales de consultas y páginas, consultados de forma iterativa |
| Su [Biblioteca](../library/overview.md) | Briefs, borradores, key points, FAQ y auditorías que ya ha creado |
| Trabajos anteriores | Qué encontró y qué decidió en ejecuciones previas de este proyecto |

También puede lanzar una [comprobación de visibilidad](../visibility/overview.md) en vivo o una [auditoría AEO](../features/aeo-audits.md) en mitad de un trabajo, cuando la respuesta lo requiere, en lugar de decirle a usted que vaya a ejecutarla.

## Enviar un trabajo

Describa el encargo y pulse **Send Moose**. Dos opciones definen cómo lo aborda:

- **Trabajo profundo**: deje que el trabajo dure horas si hace falta: muchas más páginas, muchas más búsquedas, más comprobaciones intermedias. Úselo cuando la pregunta es realmente amplia, no para una consulta rápida.
- **Adjuntar archivos**: hasta seis archivos por trabajo, como contexto que lee mientras trabaja.

Puede marcar **Avísame cuando Moose termine** y marcharse. El trabajo sigue en marcha esté usted mirando o no, y tanto si permanece en la pantalla como si no.

## Verle trabajar

**Ver navegador** abre la instancia de navegador que está usando Moose, para que vea las páginas mientras las lee. **Tomar el control** le pasa el navegador a usted si se ha atascado en algo que puede resolver en un segundo (un aviso de cookies, un inicio de sesión), y **Volver al trabajo** se lo devuelve.

Puede cerrar esa ventana cuando quiera. Moose sigue trabajando.

## Moose, Scout y Skeptic

En el plan gratuito, Moose trabaja solo.

Los planes de pago añaden otros dos agentes al trabajo:

- **Scout** encuentra ángulos que a Moose se le pasan.
- **Skeptic** cuestiona las pruebas antes de que lleguen a su resultado.

Puede hablar con cualquiera de ellos en mitad del trabajo desde el hilo: decirle algo a Moose, pedirle a Scout otro ángulo, pedirle a Skeptic que apriete más con una afirmación. **Seguir** y **Revisar otros cinco resultados** amplían una ejecución que se ha detenido en un punto útil.

Scout y Skeptic siempre se ejecutan en la nube a través de OpenRouter, incluso cuando Moose corre en un modelo local, así que consumen tokens.

## Cuando Moose le necesita

Dos cosas detienen un trabajo y le esperan en lugar de improvisar:

- **Necesita su aprobación**: Moose está a punto de ejecutar una acción en un sitio web real, como pulsar un botón de un formulario. Le muestra el botón exacto y espera a **Aprobar y continuar** o **No lo hagas**.
- **Necesita su ayuda**: está bloqueado en algo que solo puede responder usted. Escriba una respuesta, o pulse **Que decida Moose** para que sea él quien resuelva.

Nada se publica, se envía ni se remite a ninguna parte sin que usted lo apruebe antes. Eso vale también para las ejecuciones programadas.

## Leer el resultado

Un trabajo terminado tiene cuatro pestañas:

- **Resultado**: lo que encontró, redactado.
- **Colaboración**: cómo fue y quién aportó qué: notas que añadió Scout, objeciones que planteó Skeptic, veces que usted intervino.
- **Fuentes**: cada página que abrió, con las pruebas que capturó de ella.
- **Actividad**: la ejecución completa, filtrable por herramientas o por agentes.

Desde ahí puede **Guardar en la Biblioteca**, **Descargar informe** o preguntar por el resultado en el [chat](../chat/overview.md). Los archivos que Moose haya guardado durante el trabajo aparecen en **Archivos que guardó Moose**: ábralos, guarde una copia o muéstrelos en su carpeta. Puede guardar archivos CSV, Markdown, texto plano, PDF y Word.

## Contenido que crea Moose

Moose puede producir artefactos reales de Hi, Moose como parte de un trabajo, no solo una respuesta escrita: un **content brief**, un **borrador**, **key points**, **FAQ** o una **auditoría AEO**. Aterrizan en su [Biblioteca](../library/overview.md) como cualquier otra cosa, y el resultado del trabajo enlaza directamente con ellos.

## Ejecutar un trabajo de forma programada

**Ejecutar de forma programada** convierte un trabajo puntual en uno recurrente: cada día, entre semana, cada semana o cada mes, a una o varias horas del día.

Los trabajos programados aparecen en **Trabajos programados** y se pueden pausar, reanudar o eliminar. Se ejecutan sin supervisión: Moose toma las decisiones pequeñas por su cuenta y sigue sin publicar ni enviar nada sin su aprobación.

## Trabajos anteriores

Todos los trabajos se conservan en **Trabajos anteriores**, con búsqueda y filtros por **Hechos**, **Retirados**, **Sin terminar** y **Bloqueados**, agrupados en hoy, esta semana y antes. Los trabajos pertenecen al proyecto en el que se ejecutaron.

## Ajustes

Los **ajustes de Send Moose** se guardan por proyecto:

- **LLM de Moose**: Automático usa el modelo local más grande instalado, o el modelo en la nube de su plan cuando la IA local está desactivada. También puede fijar un modelo concreto.
- **LLM de Scout** y **LLM de Skeptic**: solo en planes de pago; por defecto, Gemma 4 31B.
- **Modelo de contenido**: qué modelo escribe los briefs, borradores y FAQ que Moose crea. Por defecto, el mismo que usa Moose.
- **Motor de búsqueda**: con qué motor busca.

Todo lo marcado como **Consume tokens** se ejecuta en la nube a través de OpenRouter y no en su equipo. Los trabajos profundos son los más largos, así que son los que más cuestan.

## Qué necesita

- **Un modelo local, o un plan de pago.** Moose piensa con un modelo Gemma que se ejecuta en su ordenador. Descárguelo una vez desde el aviso de la pantalla y los trabajos no le cuestan nada. Los planes de pago pueden ponerle en un modelo en la nube. Si ha desactivado la IA local y está en el plan gratuito, Send Moose se lo dice y le ofrece volver a activarla.
- **Un sitio web en el proyecto**, para los trabajos sobre su propio sitio, su marca o sus competidores. Los trabajos generales de web funcionan bien sin él.

## Adónde ir a continuación

- **[Chat](../chat/overview.md)**: para el trabajo que quiere dirigir turno a turno en lugar de encargar.
- **[Workflows](../workflows/overview.md)**: para una receta fija que se ejecuta con un disparador, en lugar de un encargo abierto.
- **[Biblioteca](../library/overview.md)**: donde se guardan los informes y el contenido de un trabajo.
