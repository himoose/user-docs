---
source_hash: 90bb543cefb714f7fdb6facb1f7799b751aff22949ece082264e7713b4992995
---
# Selección de modelo

## Para qué sirve

Cada chat funciona con un modelo de IA concreto, y el selector de modelo le permite ver y cambiar cuál está utilizando, incluidos los modelos locales que se ejecutan en el dispositivo.

## Elegir un modelo

Abra el selector de modelo para ver los modelos disponibles en su [plan](../getting-started/account-modes.md). Cada opción lleva distintivos para que sepa qué obtiene antes de cambiar:

- **Gratis** / **HiMoose Cloud** / **De pago o BYOK**: qué planes pueden utilizar ese modelo.
- **Speed: Slow / Average / Very Fast**: una idea aproximada de la latencia de respuesta.
- **Local**: se ejecuta íntegramente en su dispositivo (véase más abajo).
- Un **distintivo multiplicador** en los modelos más costosos, que indica cuánto más consumen de su saldo respecto a la opción estándar.

La oferta sigue lo que publican los proveedores de modelos y actualmente incluye las familias Claude, GPT, Gemini y Gemma. Si un modelo no está disponible en su plan, Hi, Moose se lo dice directamente en lugar de recurrir a otro en silencio.

## Modelos locales

Los modelos locales aprobados, como Gemma 4 de Google, se ejecutan **íntegramente en su ordenador**. No consumen tokens, no hay ida y vuelta a la nube y ningún dato sale de su dispositivo. La primera vez que seleccione un modelo local, Hi, Moose le guía por la instalación.

Una vez descargado y activado, las respuestas locales son rápidas en Apple Silicon. En los Mac con procesador Intel el modelo se ejecuta en la CPU y será notablemente más lento que los modelos en la nube; Hi, Moose se lo advierte antes de que confirme la descarga.

Los modelos locales no son una opción recortada. Gemma 4 admite el uso de herramientas, de modo que las [herramientas del chat](tools-and-specialists.md) funcionan en un modelo local igual que en uno en la nube.

!!! note "Preview Mode depende de un modelo local"
    En el plan gratuito, las [AEO audits](../features/aeo-audits.md) y la puntuación de visibilidad solo funcionan con un modelo local activado. Es la razón principal para configurar uno cuanto antes.

## Modelos más costosos

Algunos modelos consumen bastante más de su saldo que la opción estándar. Si elige uno, Hi, Moose se lo confirma primero y le indica aproximadamente cuántas veces más tokens consume, para que no agote su saldo por accidente.

Los modelos más caros están limitados por plan. Si el suyo no los incluye, se muestran como no disponibles en lugar de ocultarse.

## Fundamentación con búsqueda web

El chat puede fundamentar sus respuestas en resultados de búsqueda web en vivo para la conversación actual. Está disponible en BYOK Premium, BYOK Agency y todos los planes gestionados. No se incluye en BYOK Free ni en Preview Mode.

## Idioma

El chat sigue una preferencia de idioma, de modo que puede trabajar en un idioma distinto del que utiliza la interfaz de la aplicación.

## Cuando no se puede utilizar un modelo

Puede aparecer un mensaje en lugar de una respuesta si:

- el modelo seleccionado no está disponible temporalmente (pruebe con otro),
- el modelo no está permitido en su plan (elija uno incluido), o
- se ha adjuntado una imagen a un modelo que no admite entrada de imágenes. Hi, Moose le indica un modelo que sí la admite y le ofrece cambiar.

## Cómo encaja esto con BYOK

En los planes BYOK, la selección de modelo determina a qué modelo llama su propia clave de OpenRouter. La inferencia sigue ejecutándose en local, en la aplicación de escritorio. Consulte [Tipos de cuenta y planes](../getting-started/account-modes.md) para ver cómo varía el acceso a modelos entre planes.

Su clave de OpenRouter se guarda por cuenta y no por dispositivo. Si todavía no ha guardado ninguna, Hi, Moose se la pide la primera vez que una función la necesita, en lugar de fallar en silencio.
