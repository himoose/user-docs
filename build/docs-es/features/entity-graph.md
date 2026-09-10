---
source_hash: 1d8f1dffb939a9b3587c4b3a3f298386f6f202a5a02672b6b3dfd79bbccc2135
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/features/entity-graph/)

# Entity Graph

## Para qué sirve

Un entity graph es el mapa de aquello de lo que trata realmente su sitio: las personas, los productos, los lugares, las organizaciones y los temas que nombran sus páginas, y cómo se relacionan entre sí.

Importa porque los motores de respuesta no leen su sitio como una lista de páginas. Lo leen como un conjunto de cosas y de relaciones. Un sitio que deja claro «somos esta empresa, fabricamos estos productos, para estos clientes, en esta categoría» le da al motor algo que recuperar y citar. Un sitio donde eso se da por supuesto pero nunca se enuncia le deja adivinando.

El entity graph le muestra cuáles de esas cosas ha dejado claras ya su sitio, cuáles están flojas y con qué se quedaría un motor.

Ábralo desde **Herramientas → Crear un entity graph**, o simplemente pídalo en el [chat](../chat/overview.md).

## Antes de poder construir uno

El grafo se construye a partir de las páginas que Hi, Moose ya ha rastreado, así que el proyecto necesita **un sitio web y al menos un rastreo completado**. Si todavía no hay ninguno, la ficha de entrada se lo dice y le enlaza a [Supervisión del sitio](../site-monitoring/overview.md) para lanzar uno.

La ficha le indica con qué está trabajando: cuántas páginas rastreadas y la fecha del último rastreo completado.

## Rápido o completo

Dos profundidades:

- **Rápido**: solo datos estructurados. Lee el marcado de schema, los metadatos y la estructura de página que su sitio ya publica. Se ejecuta al instante y no cuesta nada.
- **Completo**: todo lo del modo rápido, más una pasada de IA que lee sus páginas principales y nombra las entidades que no están marcadas en ninguna parte. Tarda unos minutos.

En el modo completo elige cuántas páginas principales puede leer la pasada de IA. Las ejecuciones grandes tardan más y, en los planes gestionados, las llamadas a modelos en la nube consumen su asignación mensual. La pasada se ejecuta con el modelo seleccionado en el menú de modelos del chat, así que elija el modelo primero si quiere uno concreto: un modelo local cargado mantiene todo el proceso en su equipo y sin coste.

## Qué obtiene

El grafo informa de:

- **Entidades**: todo lo encontrado, con su tipo, sus alias, en cuántas páginas aparece y una puntuación de **relevancia** que indica cuán central es para el sitio.
- **Relaciones**: cómo se conectan esas entidades, divididas en tres tipos:
    - **Etiquetadas**: una relación que sus datos estructurados o la pasada de IA enuncian de forma explícita.
    - **De página compartida**: dos entidades que aparecen una y otra vez en las mismas páginas.
    - **Semánticas**: dos entidades que el lenguaje trata como relacionadas aunque nada las enlace.
- **Entidades por tipo**: el desglose, que suele ser la vista más útil de todas. Un sitio que vende software y muestra cuarenta personas y tres productos tiene un problema de relato que conviene conocer.

Una tabla de **entidades principales** muestra las más relevantes con su tipo, su número de páginas y su relevancia. El conjunto completo se exporta en **CSV** o en **PDF**; la tabla en pantalla está limitada, e indica cuántas más contienen las exportaciones.

## Cuando la pasada de IA no se ejecuta

El modo completo se degrada en lugar de fallar. Si la pasada de IA no puede ejecutarse, sigue obteniendo el grafo a partir de los datos estructurados, las páginas compartidas y la similitud semántica, y la ficha le dice cuál fue el caso:

- **No hay modelo disponible**: cargue un modelo local o añada una clave de OpenRouter, y vuelva a construirlo en modo completo.
- **Nada nuevo que leer**: todas las páginas elegibles ya se habían analizado en una ejecución anterior.
- **La pasada falló**: no pudo completarse.
- **Se agotó la asignación**: en los planes gestionados, la pasada se detiene cuando se agotan sus créditos mensuales, y el grafo incluye todo lo analizado hasta ese punto.

## Moose puede leerlo

Una vez que existe un grafo, el [chat](../chat/tools-and-specialists.md) puede consultarlo directamente. Pregunte en qué entidades es más fuerte su sitio, qué está conectado con un producto concreto o qué falta junto a un tema que quiere ganar, y Moose lee el grafo en lugar de volver a rastrear o de suponer.

[Send Moose](../send-moose/overview.md) también lo lee, como parte de la inteligencia del sitio que lleva consigo a un trabajo.

## Adónde ir a continuación

- **[Supervisión del sitio](../site-monitoring/overview.md)**: el rastreo del que se construye el grafo.
- **[Content Briefs](content-briefs.md)**: convertir un hueco del grafo en una página.
- **[Auditorías AEO](aeo-audits.md)**: comprobar si una página concreta enuncia sus entidades con claridad.
