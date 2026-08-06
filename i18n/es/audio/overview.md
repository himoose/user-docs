---
source_hash: 3de48b1823942dd1ca44b6be6cf581f170fdffe9e0e850d467f3322e9e89f1a8
---
# Audio

## Para qué sirve

Convertir un artículo en una conversación a dos voces y, después, descargar el MP3 o insertar el reproductor en su sitio. El reproductor incluye una transcripción, lo que aporta a la página texto real, propio y rastreable: contenido que un motor de respuesta puede recuperar.

Audio vive en la aplicación de escritorio, en **Audio**, dentro de la barra lateral, y se divide en tres pestañas: **Generate**, **History** y **Analytics**.

!!! note "Audio ha salido de la aplicación web anterior"
    La generación de audio vivía antes en `app.himoose.com` con el nombre «Listen to this Article». Ahora forma parte plenamente de la aplicación de escritorio, con acotación por proyecto, analíticas de escucha y personalización del reproductor que la versión web no tenía.

## Antes de empezar

Defina primero el sitio web del proyecto. La reproducción está limitada al dominio de su proyecto y a `himoose.com`, de modo que Hi, Moose necesita conocer el dominio antes de generar nada. Si no está definido, la pestaña Generate muestra un aviso **Set website** en lugar del compositor.

La disponibilidad de audio depende de su [plan](../getting-started/account-modes.md): BYOK Premium y BYOK Agency incluyen 15 generaciones al mes, los planes gestionados son ilimitados y los planes gratuitos no incluyen audio.

## Elegir una fuente

Tres formas de aportar contenido:

- **URL del artículo**: pegue una URL publicada y pulse **Fetch**. Hi, Moose extrae el contenido y muestra el dominio, el número de palabras y el tiempo estimado de lectura. El artículo debe ser accesible públicamente, no estar tras un inicio de sesión o un muro de pago.
- **Pegar texto**: dé un título al episodio y pegue directamente el guion o el texto del artículo.
- **Subir archivo**: suelte un `.txt`, `.md`, `.docx`, `.doc` o `.pdf`. El archivo se lee en su dispositivo y su texto pasa al flujo de pegado.

## Perfilar la conversación

**Focus** (opcional) orienta en qué debe profundizar la conversación. Hay sugerencias rápidas para los enfoques más habituales: conclusiones clave, explicarlo a alguien que empieza, rebatir el argumento, a quién le interesa.

**Length** define la duración objetivo:

| Duración | Tiempo | Guion aproximado |
|---|---|---|
| Short | 4-5 min | ~700 palabras |
| Standard | 8-10 min | ~1400 palabras |
| Deep dive | 15-18 min | ~2600 palabras |

**Language** se ajusta de forma predeterminada al idioma del artículo. Cámbielo para modificar tanto el guion como las voces.

**Voices** se presentan como parejas de anfitrión e invitado, con tres combinaciones predefinidas (cálida y curiosa, serena y analítica, luminosa y escéptica) o una pareja personalizada elegida por usted.

## Dirección avanzada

Es opcional, y todo lo que deje en blanco sigue al artículo y a la pareja de voces. Hay siete campos disponibles: dirección del anfitrión, dirección del invitado, escena, estilo, ritmo, acento y contexto adicional.

- **Escena**: entrevista de estudio, charla informal, mesa redonda, llamada telefónica, conversación en movimiento
- **Estilo**: explicativo, debate, narrativo, entrevista, distendido
- **Ritmo**: más lento, natural, más rápido
- **Acento**: estadounidense (neutro), británico, australiano, irlandés, indio o internacional neutro

Cualquiera de estos campos puede sustituirse por una descripción personalizada con sus propias palabras.

**Contexto adicional** sirve para lo que el artículo no dice: cómo pronunciar el nombre de un producto, afirmaciones que evitar, quién es el público.

!!! warning "El contexto orienta el tono, no los hechos"
    Hi, Moose no inventa hechos para cumplir una indicación. El contexto adicional cambia el enfoque y la interpretación; no añade evidencias que no estén en la fuente.

Cuando tenga una configuración que le convenza, **Save as project default** la reutiliza en el siguiente episodio de este proyecto.

## Generar

Pulse **Generate audio**. El compositor muestra un tiempo estimado de renderizado antes de empezar. La generación se ejecuta en segundo plano, de modo que puede salir de la pantalla y seguir trabajando: el episodio terminado aparece en la lista **Recents** de la barra lateral, y al pulsarlo se abre ese episodio directamente.

Cuando termina, obtiene:

- Un reproductor con búsqueda, saltos de 15 segundos hacia atrás y hacia delante, y velocidad de reproducción
- **Download MP3**
- **Share**, para copiar el enlace del audio
- La **transcripción** completa, con recuento de turnos y de palabras, y un botón para copiarla
- **Embed on your site**, que se explica en [Reproductor e inserción](player-and-embed.md)
- **Regenerate with edits** y **Edit settings**, para ajustar la dirección y volver a ejecutarlo

## History

La pestaña **History** enumera todos los episodios del proyecto actual con su duración, su fecha de creación y su estado. Los episodios se acotan por proyecto, de modo que cambiar de proyecto cambia lo que ve.

- Busque episodios por nombre
- Filtre por **All**, **Ready** o **Needs attention**
- Reproduzca, descargue, abra las opciones de inserción o abra el episodio completo
- **Reintente** un episodio fallido

Los estados son Ready, Processing, Playing, Failed y Canceled.

## Adónde ir a continuación

- **[Reproductor e inserción](player-and-embed.md)**: tema, disposición, color de acento y código de inserción.
- **[Analíticas de escucha](analytics.md)**: qué ocurre una vez que el reproductor está en una página.
