---
source_hash: b5d0a07f31228ccaaa2c18a76dddb8de404f3871f7b879591e111c89bae3e9c5
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/audio/player-and-embed/)

# Reproductor e inserción

## Para qué sirve

Ajustar el estilo del reproductor de audio insertado para que encaje con la página en la que va a colocarse y, después, copiar el código de inserción. Ábralo desde un episodio terminado con **Customize player**, o desde la acción de inserción de la pestaña **History**.

## Opciones del reproductor

- **Tema**: Dark, Light o Auto. Auto sigue la configuración del dispositivo de cada visitante.
- **Disposición**: Full o Compact.
- **Color de acento**: cualquier valor hexadecimal de 6 dígitos, por ejemplo `#5688b0`.
- **Mostrar el título**: desactívelo cuando la inserción vaya debajo de su propio titular.
- **Título personalizado**: déjelo en blanco para usar el título del episodio.
- **Botón de transcripción**: muestre u oculte el conmutador de transcripción del reproductor.

Una vista previa en vivo se actualiza a medida que cambia los ajustes. Si el script del reproductor no está accesible mientras previsualiza, la vista previa muestra un marcado simple; el código de inserción copiado sigue siendo correcto.

## Copiar el código de inserción

Pulse **Copy embed code** y péguelo en su página.

- **WordPress**: péguelo en el bloque HTML o de código de la entrada, o utilice el [plugin Listen to This Article](https://wordpress.org/plugins/listen-to-this-article/).
- **Webflow**: péguelo en un elemento Embed.
- **Grav**: péguelo en el contenido de la página, donde se admita HTML sin procesar.

## La reproducción está limitada por dominio

El audio generado solo se reproduce en el dominio del sitio web de su proyecto y en `himoose.com`. Esto se define a partir del campo de sitio web del proyecto, y es la razón por la que ese campo debe estar relleno antes de poder generar. Si inserta el reproductor en un dominio no autorizado, la reproducción se rechazará.

## Atribución de agencia

En los planes con [marca blanca](../agency/white-label.md), el reproductor insertado puede llevar la atribución de su agencia en lugar de la de Hi, Moose. Se configura en **Configuración → Branding**:

- **Atribución de la inserción de audio**: el texto que se muestra en el reproductor. Déjelo vacío para usar «Audio by» seguido del nombre de su agencia.
- **Enlace de atribución**: una dirección `https://` completa. Déjelo vacío para reutilizar su enlace principal de marca.

La atribución es un enlace real de vuelta a su sitio desde cada página de cliente que lleve el reproductor, que es precisamente su valor para las agencias.

!!! warning "La atribución se aplica al código copiado después de guardar"
    Cambiar la marca no reescribe las inserciones que ya haya colocado. Vuelva a copiar el código de inserción después de guardar para recoger la nueva atribución.

## Por qué ayuda al AEO

La transcripción aporta a la página texto estructurado, propio y rastreable. Es contenido real adicional que un motor de respuesta puede recuperar y citar, y puede reforzar las señales de extractabilidad y exhaustividad de una [AEO audit](../features/aeo-audits.md). No es por sí solo un factor puntuable de «tiene multimedia»: el valor está en el texto que el reproductor lleva consigo.
