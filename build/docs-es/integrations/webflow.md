---
source_hash: 67912e0c53e927d4836f8b9c545fb59268db0fbc9165037df2930f6cfada0988
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/webflow/)

# Webflow

## Para qué sirve

Conectar un sitio de Webflow para que Hi, Moose pueda inspeccionar sus páginas y su contenido y preparar ediciones previsualizables para su publicación: FAQ, key points, borradores basados en briefs y recomendaciones de AEO audits.

## Configurar una conexión

1. Abra **Conexiones** en la aplicación de escritorio y elija Webflow.
2. Pulse **Conectar MCP de Webflow**. Esto abre la página de autorización de Webflow en su navegador. Complete allí el proceso de OAuth para terminar de conectar.
3. Una vez conectado, elija qué sitio autorizado de Webflow debe utilizar Hi, Moose para este [proyecto](../getting-started/projects.md).

## Preparar un destino de vista previa

Hi, Moose puede descubrir **superficies de contenido** en su sitio conectado de Webflow: páginas, entradas, elementos de colección y código personalizado, además de una plantilla en blanco para contenido que todavía no existe. Elija un destino, añada notas sobre la edición o la intención de publicación y prepárelo como destino de vista previa. A partir de ahí, revise el borrador preparado igual que con cualquier otra conexión. Véase [Borradores, vista previa y publicación](../features/drafts-and-publishing.md).

## Preparación para vista previa y publicación

Todavía no todas las conexiones de Webflow pueden hacerlo todo. Hi, Moose informa de uno de varios estados para su sitio conectado: listo tanto para preparar artefactos de vista previa como para publicar, solo vista previa, solo publicación, o conectado pero aún no listo para ninguna de las dos cosas. Las superficies exclusivas del Designer (cambios que requieren el Webflow Designer directamente) todavía no son compatibles.

## Publicar en colecciones

Al publicar en una colección, Hi, Moose carga primero los demás campos obligatorios de esa colección y le pide que los rellene, para que la publicación no falle a mitad de camino por un campo que no podía ver.

## Seguridad

La autorización de Webflow se realiza a través de su navegador, y la conexión resultante la utiliza únicamente el proceso en segundo plano de la aplicación de escritorio; no se expone a la interfaz de usuario.
