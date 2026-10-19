---
source_hash: 25544d4dba4331f336f53923c9a635bc4442b022e472aec88392d921d34dfefb
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/getting-started/context/overview/)

# Context

## Para qué sirve

**Contexto** es la capa de fundamentación de la navegación izquierda de la aplicación de escritorio. Es el contexto operativo compartido de su proyecto actual: la información que el operador, el chat y todas las funciones de generación reutilizan en lugar de partir de cero en cada petición.

Context se compone de cuatro piezas:

| | Alcance | Para qué sirve |
|---|---|---|
| **[Brand Voice](brand-voice.md)** | Por proyecto | Cómo debe sonar su marca: tono, público, valores, terminología. Define el estilo de redacción de todo lo que genera Hi, Moose. |
| **[Brand Truth Profile](brand-truth-profile.md)** | Por proyecto | Una fuente de verdad legible por máquina sobre lo que su empresa es, vende y atiende realmente. Se utiliza para detectar cuándo las respuestas de la IA la tergiversan o se desvían de esa verdad. |
| **[Documentos de marca](brand-documents.md)** | Por proyecto | Su propio message house, guía de estilo y documentos de posicionamiento. Hi, Moose los divide en secciones, aplica sus reglas de redacción a todo y trae el resto cuando un trabajo lo necesita. |
| **[Sobre usted](about-you.md)** | Por dispositivo, no por proyecto | Notas sobre usted como persona: su función, sus objetivos y su forma de trabajar, para que el chat conozca a la persona y no solo a la marca. |

## Por qué son artefactos separados

Brand Voice y Brand Truth Profile responden a preguntas distintas, aunque ambos describan su marca:

- **Brand Voice** responde a «¿cómo debe sonar esto?»: tono, estilo, preferencias de vocabulario. Es una guía creativa y estilística para el contenido generado.
- **Brand Truth Profile** responde a «¿qué es cierto sobre nosotros?»: descripción canónica, cliente ideal, oferta, competidores y los puntos concretos que la IA suele confundir. Es una referencia factual para detectar tergiversaciones, no una guía de estilo.

**Documentos de marca** reúne el material de origen completo que hay detrás de ambos. Brand Voice y el Brand Truth Profile siguen siendo resúmenes breves. Sus documentos conservan el detalle, y Hi, Moose busca en ellos las secciones que encajan con cada trabajo. También puede usarlos para rellenar los dos perfiles.

**Sobre usted** se diferencia de todos ellos: no trata de la marca en absoluto. Es contexto personal sobre **usted**, la persona que utiliza la aplicación, y se guarda en local en su dispositivo en lugar de asociarse a un proyecto, de modo que le acompaña entre proyectos en lugar de reiniciarse cada vez que cambia de espacio de trabajo.

## Dónde se utiliza Context

- **Brand Voice** se reutiliza en [Content Briefs](../../features/content-briefs.md), el [generador de FAQ](../../features/faq-generator.md), el [extractor de Key Points](../../features/key-points.md), [borradores, vista previa y publicación](../../features/drafts-and-publishing.md) y las recomendaciones de las [AEO audits](../../features/aeo-audits.md).
- **Brand Truth Profile** se reutiliza durante las ejecuciones de [Visibility](../../visibility/overview.md), donde Hi, Moose comprueba si la respuesta de un motor de IA sobre su marca concuerda con su descripción canónica, su oferta, sus competidores y los patrones conocidos de tergiversación.
- **Documentos de marca** se reutilizan en Content Briefs, borradores de blog, Key Points, el generador de FAQ, la investigación de [Send Moose](../../send-moose/overview.md) y el [Chat](../../chat/overview.md), donde el chat también puede buscar en ellos. Consulte [Dónde se utilizan sus documentos](brand-documents.md#donde-se-utilizan-sus-documentos).
- **Sobre usted** se reutiliza en el [Chat](../../chat/overview.md) para que las respuestas reflejen su función, sus objetivos y su estilo de comunicación preferido.

## Cómo rellenarlo

Cada artefacto indica cuántos campos ha rellenado y muestra una breve vista previa en cuanto añade algo. Todos los campos son opcionales: Hi, Moose funciona con contexto parcial y gana precisión a medida que usted añade más.

En el caso concreto de Brand Voice, no tiene que rellenar cada campo a mano: una acción de **autocompletado** puede rastrear el sitio web de su proyecto en local y sugerir valores para los campos vacíos.

Si ya tiene un message house o una guía de estilo, súbalo en [Documentos de marca](brand-documents.md) y haga clic en **Rellenar perfiles desde documentos**. Hi, Moose sugiere valores tanto para Brand Voice como para el Brand Truth Profile, cada uno respaldado por una cita de su documento, y usted elige cuáles aplicar.

## Almacenamiento local y sincronización en la nube

De forma predeterminada, Brand Voice, Brand Truth Profile y Documentos de marca se guardan **en local para el proyecto actual**, y Sobre usted se guarda **en local en su dispositivo**. La sincronización en la nube, que respalda Brand Voice, Brand Truth Profile y Documentos de marca y los comparte con su equipo, está disponible en **todos los planes de pago**, incluidos los planes BYOK de pago. Preview Mode y BYOK Free permanecen solo en local; al cambiar a un plan superior se activa la sincronización, de modo que su equipo comparte la misma base y esta queda protegida si le ocurre algo a su equipo local.

!!! note "En los planes BYOK"
    El rastreo del contexto de marca (el paso de autocompletado) y el análisis de Brand Truth se ejecutan en local, en la aplicación de escritorio. Hi, Moose no necesita ver el contenido de su sitio en sus propios servidores para construir o utilizar este contexto.
