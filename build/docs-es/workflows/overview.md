---
source_hash: 64e2aed1c2f7aabf153fe284450b0ab8f444f0f39122092a8b927f546a3f2318
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/workflows/overview/)

# Workflows

## Para qué sirve

Los workflows convierten un patrón operativo recurrente en una rutina en segundo plano descrita en lenguaje corriente, en lugar de obligarle a repetir los mismos pasos manuales cada vez que cambia su visibilidad en IA. En vez de un constructor de automatizaciones en blanco, cada workflow se construye a partir de una frase editable y con criterio: usted rellena los huecos y Hi, Moose la ejecuta.

!!! note "Disponibilidad"
    Los workflows requieren un plan de pago: BYOK Premium, BYOK Agency o cualquier plan gestionado. Preview Mode puede supervisar un proyecto en local, pero no incluye workflows reutilizables, y BYOK Free tampoco los incluye. Véase [Tipos de cuenta y planes](../getting-started/account-modes.md).

## La primera decisión: ¿para qué es este workflow?

Todos los workflows empiezan por una decisión: **«Este workflow es para contenido [ nuevo / actual ]»**.

- **Contenido actual** ejecuta la receta **[Recuperar visibilidad perdida](recover-lost-visibility.md)**: detectar una caída en cómo aparece su marca, localizar la página afectada y preparar una corrección.
- **Contenido nuevo** ejecuta la receta **[Crear contenido nuevo](create-new-content.md)**: analizar los temas supervisados de forma programada y preparar contenido totalmente nuevo para las carencias que encuentre.

## Gestionar varios workflows

No está limitado a un solo workflow:

- Pulse **New Workflow** para crear otro, configurado de forma independiente.
- Cambie entre los workflows guardados desde el selector, que muestra el nombre de cada uno y si está **Enabled** o **Paused**.
- Renombre un workflow haciendo clic en su nombre.
- **Pause** o **Enable** un workflow sin eliminar su configuración.
- **Remove** elimina un workflow por completo. Esto solo lo quita de este dispositivo y no afecta a los demás miembros de su espacio de trabajo, ya que las definiciones de workflow son locales y personales, no estado compartido del equipo.
- **Save** guarda sus cambios; Hi, Moose también guarda automáticamente en cuanto un workflow tiene todo lo necesario para ejecutarse.

## Ejecutar un workflow

- Los workflows de **Crear contenido nuevo** pueden activarse al instante con **Run now**, además de ejecutarse según su programación. Los resultados llegan a su [Inbox](../inbox/overview.md) para que los revise; Hi, Moose le lleva directamente allí cuando una ejecución encuentra algo.
- Los workflows de **Recuperar visibilidad perdida** no tienen botón de ejecución manual: se evalúan automáticamente cada vez que termina una nueva ejecución de [visibilidad](../visibility/overview.md), comparándola con la anterior.

## Antes de poder crear un workflow

Los workflows necesitan al menos un tema de visibilidad supervisado para poder vigilar cambios. Si su proyecto todavía no tiene ninguno, Hi, Moose le pedirá que configure antes el seguimiento de [Visibility](../visibility/overview.md) y vuelva después a Workflows.
