---
source_hash: 9705deb0dc37b51cf84f956088049d0d7d87b416de55439c84ef17b2ef0d3d9c
---
# Inbox

## Para qué sirve

El Inbox es donde Hi, Moose muestra lo que merece su atención: hallazgos priorizados, auditorías y eventos de publicación, cada uno vinculado a un artefacto real y no a una notificación genérica. Convierte señales dispersas (cambios de sentimiento en la visibilidad, desviación narrativa, inexactitudes de paridad de funciones, resultados de AEO audits, resultados de publicación y solicitudes de aprobación) en una única cola de trabajo priorizada.

## Qué aparece en el Inbox

Cada elemento del Inbox apunta a algo real que puede abrir y sobre lo que puede actuar:

- **Señales de visibilidad**: sentimiento negativo o mixto detectado en una respuesta de IA, desviación narrativa o inexactitud de paridad de funciones respecto a su [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), o una [ejecución de visibilidad](../visibility/overview.md) completada o fallida.
- **Resultados de AEO audits**: una auditoría completada, o una auditoría cuyo plan de acción ha sacado a la luz una recomendación de alta prioridad.
- **Detecciones de cambios en el sitio**: un único resumen por cada rastreo de [site monitoring](../site-monitoring/overview.md), que se abre en una tabla con todas las páginas modificadas y su nivel de impacto. Las páginas inaccesibles y las caídas de todo el sitio se notifican como tipos de cambio propios.
- **Informes de workflows**: resultados de la ejecución de un [workflow](../workflows/overview.md), como un análisis programado que ha generado entradas nuevas o ha señalado una oportunidad en la búsqueda con IA.
- **Eventos de publicación**: una publicación que ha **fallado**, o un cambio pendiente de su aprobación. Las publicaciones correctas ya no generan un elemento en el Inbox, porque un muro de avisos de «esto ha funcionado» sepulta los que sí requieren su atención.
- **Un mensaje de bienvenida** de Moose al terminar la incorporación, que le sugiere un primer paso sensato.

Cada elemento muestra una acción siguiente sugerida cuando tiene sentido (abrir el artefacto, iniciar un brief, dar seguimiento a una auditoría, revisar un borrador, aprobar un cambio o reintentar una ejecución fallida), de modo que no solo lee una notificación, sino que está a un clic de actuar.

Los resúmenes de site monitoring incluyen además una acción **Ask Moose about all of this** que entrega la instantánea del rastreo al [chat](../chat/overview.md) y le pregunta qué hacer primero.

## Filtrar el Inbox

Dos filtros controlan lo que ve:

- **Estado**: el valor predeterminado es **Active**, es decir, todo lo que no se ha descartado (elementos abiertos, en curso y terminados). Cambie a un estado concreto o a **All** para incluir los elementos descartados que quiera recuperar.
- **Severidad**: **Critical**, **Warning**, **Notice**, **Info** o todas.

Los elementos se agrupan por fecha (por ejemplo, «Ayer», «Anteriores») con un contador por grupo, para que vea rápidamente cuánto le espera. Los buzones largos se paginan en lugar de cargarse de una sola vez.

**Marcar todo como leído** borra el distintivo de todo el Inbox, no solo de la página que está viendo.

!!! note "El Inbox conserva sus 200 elementos más recientes"
    Los más antiguos se depuran automáticamente. El Inbox es una cola de trabajo, no un archivo histórico: todo lo duradero vive en la [Library](../library/overview.md) o en el artefacto al que apunta.

## Controlar qué le avisa

Haga clic en **Notifications** para abrir sus preferencias de notificación por proyecto. Consulte [Notificaciones del Inbox](notifications.md) para saber qué hace cada ajuste.

## Gestionado y BYOK

El Inbox funciona igual tanto si su espacio de trabajo es gestionado como si es BYOK: los elementos los escribe el lado que realmente ha generado el evento subyacente (la nube en el caso de los workflows gestionados, el proceso local de escritorio en el caso de BYOK) y usted ve una única cola unificada en ambos casos.
