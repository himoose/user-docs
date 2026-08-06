---
source_hash: 807f4fd0f8157bf27491590b13dd7b2b18f5cb12dd648c025f2c46cabf3ea0ed
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/getting-started/account-modes/)

# Tipos de cuenta y planes

Hi, Moose ejecuta el trabajo de IA de dos maneras: con su propia clave de OpenRouter (BYOK) o con los modelos gestionados de Hi, Moose. Esa elección, y no el precio, es la verdadera bifurcación. Todo lo demás son números de proyectos, puestos y cuántos créditos mensuales recibe.

Los planes se agrupan en dos pestañas dentro de la pantalla **Upgrade**: **Startup** y **Enterprise & Agencies**.

## Las dos formas de ejecutar la IA

### BYOK: aporte su propia clave

Usted facilita una clave de API de [OpenRouter](https://openrouter.ai) y las llamadas a los modelos se ejecutan **desde la aplicación de escritorio, en su equipo**, con esa clave. Hi, Moose nunca canaliza la inferencia BYOK a través de sus propios servidores, de modo que su clave y sus prompts permanecen en local.

Pagar por un plan BYOK no cambia eso. Usted paga por más capacidad de trabajo (proyectos, puestos, memoria, workflows, Search Console), no para que Hi, Moose ejecute sus llamadas a los modelos. El coste de los modelos se abona directamente a OpenRouter y no hay ningún contador de tokens de Hi, Moose que vigilar.

### Gestionado: Hi, Moose ejecuta los modelos

Sin clave de API. Los modelos gestionados de Hi, Moose hacen el trabajo y usted consume de un saldo mensual de **créditos**. Un solo contador, no varios. La compatibilidad con modelos locales sigue disponible como opción opcional en el dispositivo en todos los planes gestionados.

## Planes Startup

### Preview Mode (gratuito)

Preview Mode es la forma gratuita de probar Hi, Moose. Es realmente local: 1 proyecto, 1 puesto, almacenamiento local y ejecuciones de visibilidad que consultan las superficies públicas de búsqueda con IA directamente desde su dispositivo.

- 1 proyecto, 1 puesto de usuario
- Solo LLM gratuitos y locales
- Ejecuciones de visibilidad locales
- Almacenamiento y recuperación de contexto, Brand Voice y guía de estilo
- Conexiones: WordPress, Webflow, Grav
- Datos limitados de búsqueda en vivo y de competidores, calidad de IA limitada, opciones de exportación limitadas

!!! warning "Preview Mode necesita un modelo local para la puntuación y las auditorías"
    Preview Mode no incluye ninguna asignación de IA en la nube. Las [AEO audits](../features/aeo-audits.md) y la puntuación de sentimiento, narrativa y paridad de funciones de las [ejecuciones de visibilidad](../visibility/overview.md) solo funcionan cuando haya activado un modelo local Gemma 4 en **Configuración → Local Model**. Mientras no haya uno activo, esas comprobaciones se omiten en lugar de ejecutarse en la nube.

### BYOK Free

La forma gratuita de trabajar con su propia clave. Mismo formato de 1 proyecto y 1 puesto que Preview Mode, pero con acceso a todos los modelos que ofrece OpenRouter y no solo a los gratuitos.

- 1 proyecto, 1 puesto de usuario
- Su propia clave de OpenRouter, tokens ilimitados
- Todos los LLM, incluidos los modelos locales
- Ejecuciones de visibilidad solo en local
- Conexiones: WordPress, Webflow, Grav
- Almacenamiento y recuperación de contexto limitados, [Library](../library/overview.md) limitada
- Sin búsqueda web en el chat, sin Workflows, sin Google Search Console

### BYOK Premium: 39 USD al mes o 390 USD al año

El plan local completo, y el punto en el que se desbloquean los puestos de equipo y el programador.

- 3 proyectos, más proyectos adicionales por 10 USD al mes cada uno
- Hasta 10 puestos de equipo
- Ejecuciones de visibilidad completas con programador personalizado
- Búsqueda web desde el chat
- Almacenamiento y recuperación de contexto completos, [Library](../library/overview.md) completa
- [Workflows](../workflows/overview.md)
- Brand Voice, guía de estilo y [Brand Truth Profile](context/brand-truth-profile.md)
- Conexiones: WordPress, Webflow, Grav, [Google Search Console](../integrations/google-search-console.md)
- 15 [generaciones de audio](../audio/overview.md) al mes

### Planes gestionados

Los tres funcionan con los modelos de Hi, Moose e incluyen puestos de equipo ilimitados, generaciones de audio ilimitadas, registro y exportación para administradores, y almacenamiento local y en la nube.

| Plan | Precio | Proyectos | Créditos mensuales | Modelos |
|---|---|---|---|---|
| Standard | 79 USD/mes o 849 USD/año | 3 | 1.700.000 | Modelos estándar, más locales |
| Professional | 129 USD/mes o 1389 USD/año | 5 | 3.000.000 | Todos los modelos, más locales |
| Premium | 249 USD/mes o 2689 USD/año | 10 | 6.000.000 | Todos los modelos, más locales |

## Planes Enterprise y para agencias

### BYOK Agency: 149 USD al mes o 1490 USD al año

BYOK Premium a escala de agencia. El mismo modelo local y el mismo conjunto de funciones, dimensionado para gestionar muchos clientes.

- 25 proyectos, más proyectos adicionales por 10 USD al mes cada uno
- Hasta 25 puestos de equipo
- 15 generaciones de audio al mes
- [Marca blanca](../agency/white-label.md) en informes e inserciones de audio, igual que en todos los planes de pago

### Planes gestionados para agencias

| Plan | Precio | Proyectos | Créditos mensuales | Almacenamiento |
|---|---|---|---|---|
| Agent Core | 449 USD/mes o 4849 USD/año | 25 | 15.000.000 | Nube de equipo |
| Agent Studio | 999 USD/mes o 10.789 USD/año | 75 | 40.000.000 | Nube de equipo |
| Agent Scale | 1999 USD/mes o 21.589 USD/año | Ilimitados | 120.000.000 | Nube de equipo |

## Comparativa rápida

| | Preview Mode | BYOK Free | BYOK Premium | BYOK Agency | Planes gestionados |
|---|---|---|---|---|---|
| Requiere clave propia | No | Sí | Sí | Sí | No |
| Dónde se ejecuta la inferencia | En su dispositivo | En su dispositivo | En su dispositivo | En su dispositivo | Nube de Hi, Moose (local opcional) |
| Proyectos | 1 | 1 | 3 | 25 | De 3 a ilimitados |
| Puestos de equipo | 1 | 1 | 10 | 25 | Ilimitados |
| Búsqueda web en el chat | No | No | Sí | Sí | Sí |
| [Workflows](../workflows/overview.md) | No | No | Sí | Sí | Sí |
| [Google Search Console](../integrations/google-search-console.md) | No | No | Sí | Sí | Sí |
| [Audio](../audio/overview.md) | No | No | 15 al mes | 15 al mes | Ilimitado |
| [Marca blanca](../agency/white-label.md) | No | No | Sí | Sí | Sí |

## Puestos, proyectos y créditos

Los **proyectos adicionales** cuestan 10 USD al mes cada uno en todos los planes de pago. Puede añadirlos o quitarlos desde **Upgrade → Extra projects**.

Los **puestos** son la verdadera línea entre lo gratuito y lo de pago. Preview Mode y BYOK Free se limitan al titular de la cuenta. BYOK Premium permite hasta 10, BYOK Agency hasta 25, y los planes gestionados no tienen límite, porque todos los miembros consumen del saldo de créditos del titular.

Las **recargas de créditos** están disponibles en los planes gestionados cuando se queda sin saldo a mitad de mes:

- 500.000 créditos por 25 USD
- 2.500.000 créditos por 100 USD

Las recargas son compras únicas, no suscripciones. Solo se consumen cuando se agotan sus créditos mensuales y nunca caducan.

!!! note "Las escuchas de audio se contabilizan aparte"
    Todos los planes que incluyen audio incluyen también las primeras 10.000 escuchas para toda la cuenta. A partir de ahí, las escuchas se facturan a 5,00 USD por cada 10.000 al mes. En los planes gestionados, la *generación* de audio también consume de su saldo de créditos.

## Cupones

Si dispone de un código de descuento, introdúzcalo durante el pago en la pantalla **Upgrade**.

## Cambiar de plan

Puede cambiar de plan en cualquier momento desde **Configuración → Cuenta** o desde la pantalla **Upgrade**. Si pasa de un plan gestionado a uno BYOK, añada antes su clave de API de OpenRouter. Hi, Moose valida la clave antes de redirigir hacia ella el enrutamiento de IA.

Su clave de OpenRouter se guarda por cuenta y no por dispositivo, de modo que le acompaña a una instalación nueva.
