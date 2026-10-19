---
source_hash: 685c1e28ae96f03a47645cdef302b5b0d4b54afda3810ab2ce0dae64df47c45a
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/inbox/notifications/)

# Notificaciones del Inbox

## Para qué sirve

Las preferencias de notificación del Inbox controlan cómo, y con qué urgencia, se le avisa cuando llegan elementos nuevos al [Inbox](overview.md) de un proyecto. Estos ajustes son por proyecto, de modo que un proyecto de prueba de baja prioridad no tiene por qué avisarle igual que el sitio en producción de un cliente.

## Ajustes

- **Mostrar el distintivo del Inbox en esta aplicación**: cuando está desactivado, el distintivo de la barra lateral y del dock no se actualiza para este proyecto, aunque los elementos sigan llegando al Inbox.
- **Mostrar notificaciones de escritorio**: notificaciones nativas de macOS o Windows cuando un elemento alcanza el umbral de severidad indicado más abajo.
- **Severidad mínima para las notificaciones de escritorio**: elija la severidad más baja que debe activar una notificación de escritorio (por ejemplo, Warning). Los elementos por debajo de ese umbral siguen apareciendo en el Inbox, simplemente no le interrumpen.
- **Enviarme un resumen diario por correo**: el ajuste se guarda, pero este resumen todavía no se envía; está por llegar.
- **Incluir cambios AEO informativos**: desactivado de forma predeterminada, para que el Inbox se centre en lo importante. Al activarlo, los cambios AEO de bajo impacto también se envían al Inbox. Tenga en cuenta que las notificaciones de escritorio siguen respetando el umbral de severidad anterior aunque esto esté activado.

## Por qué esto es distinto de la severidad

La severidad (crítica, advertencia, aviso, informativa) se asigna al propio elemento en función de lo que ha ocurrido realmente: no es algo que usted configure. Lo que controla aquí es cuánto de eso se muestra como distintivo, como notificación de escritorio o (próximamente) como correo electrónico, de modo que la señal subyacente se mantenga honesta mientras usted ajusta el volumen con el que se le entrega.
