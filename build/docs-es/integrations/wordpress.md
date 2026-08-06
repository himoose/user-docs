---
source_hash: 57477f3edd7e63b53a23c12a7676c0c723e2f37903e1f4aa75a613f296e8277b
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/wordpress/)

# WordPress

## Para qué sirve

Conectar un sitio de WordPress a Hi, Moose para que la aplicación de escritorio pueda preparar y aplicar directamente ediciones de contenido (FAQ, key points, borradores basados en briefs y recomendaciones de AEO audits), con un paso de vista previa y otro de aprobación antes de que nada se publique.

## Cómo funciona la conexión

La aplicación de escritorio es el lado activo de esta conexión: resuelve la entrada de destino, recupera su contenido actual, construye el cambio propuesto en local y llama directamente por HTTPS a los endpoints REST de su sitio de WordPress para preparar el cambio. Su sitio de WordPress permanece pasivo: expone un endpoint que espera a ser llamado y nunca necesita ponerse en contacto con Hi, Moose por su cuenta.

Esto significa que:

- El token de su sitio y las credenciales de conexión nunca están en manos de la interfaz de usuario, solo del proceso en segundo plano de la aplicación de escritorio.
- En los planes BYOK, los pasos del modelo local que intervienen en la preparación de una edición (como localizar la sección exacta de contenido que hay que sustituir) se ejecutan con su propia clave de OpenRouter, no mediante una llamada alojada por Hi, Moose.

## Configurar una conexión

1. Abra **Conexiones** en la aplicación de escritorio y elija WordPress.
2. Descargue el plugin conector, instálelo en su panel de WordPress y pegue después la URL de su sitio y la clave de API de este proyecto en la configuración del plugin.
3. De vuelta en Hi, Moose, guarde la conexión y confirme que el conector informa de un ping correcto desde su sitio.

## Entornos

Cada instalación de WordPress que conecte (producción, staging o ambas) es un **entorno** propio con su token de sitio y su secreto HMAC, totalmente aislados entre sí. Elija qué entorno es el destino predeterminado de las ediciones nuevas y cambie entre ellos cuando quiera. Si un sitio de staging está protegido con autenticación básica HTTP, puede guardar esas credenciales específicamente para ese entorno, de modo que Hi, Moose pueda acceder a él.

## Parches

Cada edición de WordPress, ya venga de las [FAQ](../features/faq-generator.md), de los [key points](../features/key-points.md), de un [borrador](../features/drafts-and-publishing.md) o de un cambio manual de buscar y reemplazar creado por usted, se registra como un **parche**: una entrada local de registro por entorno con su propio estado.

Un parche pasa por estados explícitos: **Borrador**, **Staged**, **Aplicado**, **Descartado**, **Revertido** o **Failed**. Desde la lista de parches puede:

- **Preparar** un parche en su sitio de WordPress para previsualizarlo.
- **Aplicar** un parche preparado para publicarlo.
- **Descartar** un parche que no quiera utilizar.
- **Revertir** un parche aplicado.
- **Promover** un parche a otro entorno (por ejemplo, de staging a producción) para volver a prepararlo allí y revisarlo.

Una vez que ha enviado un borrador, Hi, Moose lo recuerda, de modo que no puede enviar el mismo varias veces por accidente.

## Plugin Listen to this Article

El plugin de WordPress **Listen to This Article**, que es independiente, inserta el reproductor de audio y la transcripción que genera [Audio](../audio/overview.md) en la aplicación de escritorio. Instálelo desde [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/), o pegue el código de inserción directamente en su entrada. Véase [Reproductor e inserción](../audio/player-and-embed.md).

## Requisitos

- WordPress 6.0 o superior, con acceso de administrador para instalar la conexión en su sitio.
- Un proyecto configurado en la aplicación de escritorio.
