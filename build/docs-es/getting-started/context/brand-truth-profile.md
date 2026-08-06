---
source_hash: 266b8292b4154e6b52eab317de9e91cce7429af96c1d84999875493bfb8f09a8
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/getting-started/context/brand-truth-profile/)

# Brand Truth Profile

## Para qué sirve

El Brand Truth Profile es una fuente de verdad legible por máquina sobre cómo debe describir la IA a su empresa: qué vende, a quién atiende y con qué no debe confundirse nunca. Hi, Moose lo utiliza durante las ejecuciones de [Visibility](../../visibility/overview.md) para detectar cuándo la respuesta de un motor de IA tergiversa su marca o repite una narrativa desfasada, en lugar de dejar ese juicio en manos de una puntuación de sentimiento genérica.

Al igual que Brand Voice, el Brand Truth Profile está acotado al [proyecto](../projects.md) actual.

Todos los campos son opcionales, pero cuantos más rellene, con mayor precisión podrá Hi, Moose señalar tergiversaciones y recomendar correcciones.

## Campos que puede rellenar

### Descripción principal

- **¿Cómo debe describir la IA a su empresa hoy?**: la descripción canónica de una o dos frases que le gustaría ver en una respuesta de ChatGPT, Perplexity, Gemini o Google AI.
- **¿Quién es su cliente ideal hoy?**: se selecciona entre segmentos habituales (pymes, mercado medio, gran empresa, agencias, marcas de comercio electrónico y más), con notas de texto libre.

### Qué ofrece

- **Productos, servicios o categorías de producto que la IA debe saber que ofrece**: lo principal que la IA debe saber que usted proporciona; no hace falta enumerar todas las funciones.
- **Funciones o capacidades que la IA debe mencionar**: una por línea. Ayuda a Hi, Moose a detectar cuándo la IA omite algo importante.

### Dónde fallan las descripciones

- **¿Qué suelen confundir la IA o el mercado sobre su empresa?**: se elige entre patrones habituales de tergiversación: tipo de cliente equivocado, categoría de producto equivocada, posicionamiento desfasado, ausencia de productos o funciones nuevos, competidores equivocados, exageración o minimización de las capacidades, confusión con otra marca y más.
- **Un ejemplo de algo que la IA o el mercado confunden**: un ejemplo concreto que respalde el patrón anterior.
- **Descripciones desfasadas que debemos señalar**: categorías, clientes objetivo o limitaciones antiguas que ya no se aplican.
- **¿Qué errores de la IA serían más perjudiciales?**: las categorías de error de mayor riesgo (descripción errónea de la empresa, cliente objetivo equivocado, precios o disponibilidad incorrectos, sentimiento negativo o engañoso, confusión de marca y más).

### Vocabulario

- **Palabras o expresiones que la IA debe utilizar**: vocabulario preferido, uno por línea.
- **Palabras o expresiones que la IA debe evitar**: vocabulario que evitar, uno por línea.

### Contexto competitivo

- **Principales competidores o alternativas**: de 3 a 5 competidores, alternativas o categorías de herramientas, cada uno con una nota opcional (por ejemplo, «posicionado solo para gran empresa»). Se utilizan para probar prompts de comparación.
- **Comparativas que conviene supervisar**: búsquedas concretas de comparación o de categorías alternativas que Hi, Moose debe vigilar (por ejemplo, «mejores herramientas de AEO para pequeñas empresas»).

### Confianza y evidencias

- **Preguntas de clientes que la IA debe responder correctamente**: preguntas diagnósticas alineadas con la forma real en que compran los clientes potenciales.
- **Afirmaciones con las que la IA debe tener cuidado**: precios, rendimiento, certificaciones u otras afirmaciones que requieren un lenguaje matizado.
- **Páginas o fuentes que demuestran su posicionamiento actual**: páginas, documentos o casos de éxito concretos que deben tratarse como prueba importante, cada uno con una nota opcional.
- **Fuentes que ya se sabe que están desfasadas o son inexactas**: páginas de terceros, directorios o citas previas de la IA que se sabe que describen mal a su empresa, cada una con una nota sobre qué es incorrecto.

## Cómo se utiliza

Durante una ejecución de visibilidad, Hi, Moose carga el Brand Truth Profile del proyecto (cuando tiene contenido significativo) y lo utiliza para evaluar cada respuesta de la IA en busca de tergiversaciones o desviaciones, comparándola con su descripción canónica, su oferta, sus competidores, su vocabulario preferido y evitado, y los patrones conocidos de tergiversación, en lugar de limitarse a comprobar si aparece el nombre de su marca.

## En qué se diferencia de Brand Voice

[Brand Voice](brand-voice.md) trata del **estilo**: cómo debe sonar su marca. El Brand Truth Profile trata de los **hechos**: qué es cierto sobre su empresa y qué narrativas incorrectas hay que vigilar. Rellene Brand Voice para definir el tono; rellene el Brand Truth Profile para detectar cuándo la IA se equivoca en los hechos sobre usted.

## Sincronización en la nube

Al igual que Brand Voice, el Brand Truth Profile se guarda de forma predeterminada en local para el proyecto actual. Sincronizarlo con la nube, para respaldarlo y compartirlo con su equipo, requiere un plan de pago. Consulte [Context](overview.md) para más detalles.

## Seguimiento de competidores

La lista de competidores de esta página se comparte con la [configuración de Visibility](../../visibility/settings.md). Los competidores añadidos en cualquiera de los dos sitios aparecen en ambos y alimentan el [Share of Voice, las citas de competidores y las brechas](../../visibility/competitors.md).
