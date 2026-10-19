---
source_hash: 7907c08f25052f66801891d4fc6f24fe3bdcd307070021aede9005fe5995996b
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/workflows/recover-lost-visibility/)

# Recuperar visibilidad perdida

## Para qué sirve

Esta es la receta de workflow para el **contenido actual**: vigila sus resultados de [visibilidad](../visibility/overview.md) y, cuando algo cae de forma significativa, determina automáticamente si se puede arreglar una página existente o si hace falta contenido nuevo, y prepara el trabajo para que usted lo revise.

## Construir el workflow

El workflow se lee como una sola frase, formada por estas opciones:

> **Cuando** [el share of mentions caiga / el share of citations caiga / el share of mentions suba / el share of citations suba] **en** [un umbral, de 1 a 99 puntos] **para** [todos los temas / un tema supervisado concreto], Hi, Moose identifica los prompts afectados y después [prepara una corrección de contenido / me avisa].

- **Disparador**: qué métrica vigilar y si le interesan las caídas o las subidas. Tenga en cuenta que si elige un disparador de subida, la única acción final disponible es **avisarme**: las subidas no tienen ruta de corrección de contenido, porque no hay nada que reparar.
- **Umbral**: cuántos puntos de variación deben considerarse significativos, para que el ruido normal no dispare el workflow.
- **Alcance por tema**: aplicar este workflow a todo lo que supervisa o acotarlo a un tema concreto.
- **Acción final**: **preparar una corrección de contenido** (continúa con la lógica de ramificación de más abajo) o **avisarme** (solo crea un elemento en el Inbox, sin preparar ninguna acción de contenido).

## Cuando la acción final es «preparar una corrección de contenido»

Dos opciones más se ramifican según si existe una página adecuada:

- **Si hay páginas coincidentes**: elija qué debe hacer Hi, Moose: **ejecutar una AEO audit**, **generar FAQ y schema**, **generar key points** o **nada**.
- **Si no existe ninguna página coincidente**: elija entre **crear un brief y un borrador nuevo** o **nada**.

Esta ramificación es la clave de la receta: no recomienda a ciegas un artículo nuevo cada vez que cae la visibilidad. Primero comprueba si arreglar algo que ya tiene es la mejor opción, y solo propone contenido nuevo cuando nada de lo existente encaja.

## Cómo se ejecuta

Este workflow no tiene botón de ejecución manual. Se evalúa automáticamente cada vez que termina una ejecución de visibilidad, comparando la última ejecución completada con la anterior. Cuando se dispara, el resultado, incluidos los prompts afectados y la acción realizada, llega a su [Inbox](../inbox/overview.md), vinculado al cambio de visibilidad que lo provocó.
