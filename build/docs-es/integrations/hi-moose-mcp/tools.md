---
source_hash: 02739399b48594689facbef6808edfaaedea42f90e6577cf6c6b9bb9f23939c1
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/hi-moose-mcp/tools/)


# Referencia de herramientas

Todas las herramientas que Hi, Moose MCP ofrece a una app conectada, con lo que reciben y lo que devuelven. Tú no llamas a las herramientas: la app elige la herramienta según lo que pides. Esta página te dice qué pedir y qué esperar.

Todas las herramientas salvo `list_projects` y `get_result` reciben un **proyecto**, por el nombre que aparece en Hi, Moose. Di el nombre del proyecto en tu petición cuando tengas más de uno, por ejemplo «para el proyecto Acme».

## Cuánto tarda cada cosa

| Herramienta | Tiempo habitual |
|---|---|
| Listar proyectos, briefs, borradores | Unos segundos |
| Comprobar cobertura del sitio | Menos de un minuto |
| Comprobación de visibilidad, leer una respuesta | Unos segundos |
| Lista de oportunidades | De unos segundos a un minuto |
| Brief de contenido, borrador, preguntas frecuentes, puntos clave, imagen destacada | De uno a tres minutos |
| Auditoría AEO | De dos a cuatro minutos |
| Enlaces internos | Alrededor de un minuto |
| Episodio de audio | 5 minutos el corto, 9 el estándar, 15 el profundo |

Cuando una herramienta tarda más de lo que la app está dispuesta a esperar, responde «sigue en curso» con un id de trabajo. La app usa entonces `get_result` para recoger el trabajo terminado; pídele que vuelva a comprobarlo si no lo hace.

## Proyectos y Library

### list_projects

Lista los proyectos de Hi, Moose en los que puedes trabajar. Todas las demás herramientas necesitan un proyecto, así que la app suele llamar a esta primero.

Pide: «Lista mis proyectos de Hi, Moose».

### list_briefs

Lista los briefs de contenido guardados en la Library de un proyecto, los más recientes primero, hasta 50. Úsala cuando te refieras a un brief creado antes.

Pide: «Muestra los briefs guardados de Acme».

### list_drafts

Lista los borradores guardados en la Library de un proyecto, los más recientes primero, hasta 50.

Pide: «¿Qué borradores tengo en Acme?».

### get_result

Recoge el trabajo iniciado por otra herramienta, por id de trabajo. Espera hasta un minuto a que termine. La app la llama por su cuenta; solo la necesitas cuando la app dice que el trabajo sigue en curso y quieres que vuelva a comprobarlo.

## Cobertura del sitio

### check_site_coverage

Comprueba en el último rastreo de tu sitio si hay páginas que ya cubren uno o más temas.

| Entrada | Obligatoria | Significado |
|---|---|---|
| topics | sí | De una a quince frases cortas, como «generación de SBOM para Python» |
| parentTopic | no | El tema más amplio al que pertenecen los temas, usado para juzgar la cobertura parcial |

Para cada tema responde **covered**, **partial**, **uncovered** o **unknown**, con las URLs de las páginas más cercanas como evidencia y la fecha del rastreo comprobado. Unknown significa que la comprobación no pudo ejecutarse para ese tema, no que el sitio no lo cubra.

Pide: «¿Nuestro sitio ya cubre SCA frente a SAST?».

## Contenido

### create_content_brief

Crea un brief de contenido informado por la búsqueda: objetivo, audiencia, justificación, grupos de palabras clave, estructura recomendada y restricciones, basado en resultados de búsqueda en vivo, el rastreo de tu sitio, las guías de marca y el Brand Truth.

| Entrada | Obligatoria | Significado |
|---|---|---|
| topic | sí | El tema, la pregunta o el título provisional, hasta 400 caracteres |
| targetUrl | no | La página de tu sitio a la que va dirigido el brief |
| templateType | no | El tipo de contenido: «Blog post», «Landing page», «Comparison page», «Guide» |
| guidance | no | Requisitos decididos en otro sitio: enfoque, puntos imprescindibles, tono. Hasta 4.000 caracteres. |

Devuelve el brief como texto más un id de brief que usa la herramienta de borrador. Se guarda en la Library.

Pide: «Escribe un brief de contenido para una guía de generación de SBOM para equipos de Python».

### create_draft

Escribe un primer borrador publicable a partir de un brief, con la voz de tu marca, basado en el brief, el Brand Truth y las guías de marca, con enlaces internos elegidos del rastreo de tu sitio y una pasada de pulido.

| Entrada | Obligatoria | Significado |
|---|---|---|
| briefId | una de las dos | Un brief creado en Hi, Moose |
| brief | una de las dos | Un brief escrito en otro sitio, como texto, hasta 60.000 caracteres |
| briefTitle | no | El título provisional, cuando se pasa un brief como texto |
| templateType | no | El tipo de contenido, cuando se pasa un brief como texto |
| guidance | no | Requisitos extra, hasta 4.000 caracteres |

Devuelve el borrador como texto más un id de borrador. Se guarda en la Library.

Pide: «Redacta el artículo a partir de ese brief» o «Aquí tienes un brief que escribí, redáctalo para Acme: ...».

### create_featured_image

Crea una imagen destacada para un artículo, de 1200 por 630, con tu estilo de imagen guardado cuando hay uno definido.

| Entrada | Obligatoria | Significado |
|---|---|---|
| draftId | una de las dos | Un borrador creado en Hi, Moose |
| title y summary | una de las dos | El título del artículo y un resumen breve, hasta 6.000 caracteres, cuando no hay borrador |
| styleIntent | no | Un deseo para esta imagen concreta: ambiente, escena, colores. El estilo guardado sigue aplicándose. |

Devuelve la imagen y un enlace al PNG. El archivo también se guarda en el dispositivo anfitrión.

Pide: «Haz una imagen destacada para ese borrador, luz de tarde, sin personas».

### create_faqs

Escribe preguntas frecuentes con respuestas para un contenido, con la voz de tu marca, más el marcado de esquema FAQPage listo para pegar en la página. En las cuentas de pago, las preguntas se investigan primero a partir del comportamiento real de búsqueda.

| Entrada | Obligatoria | Significado |
|---|---|---|
| draftId | una de las dos | Un borrador guardado |
| url | una de las dos | Una página publicada de tu sitio |
| guidance | no | Audiencia, preguntas que deben aparecer, tono. Hasta 4.000 caracteres. |

Pide: «Escribe preguntas frecuentes para https://acme.example/guides/sbom».

### create_key_points

Escribe los puntos clave de un contenido: afirmaciones cortas y citables con la voz de tu marca que los motores de respuesta pueden recoger.

| Entrada | Obligatoria | Significado |
|---|---|---|
| draftId | una de las dos | Un borrador guardado |
| url | una de las dos | Una página publicada de tu sitio |
| guidance | no | Audiencia, puntos que deben aparecer, tono. Hasta 4.000 caracteres. |

Pide: «Dame los puntos clave del borrador de la guía de SBOM».

## Auditorías y enlaces

### run_aeo_audit

Ejecuta una auditoría de optimización para motores de respuesta sobre un contenido: una puntuación sobre 100, puntuaciones por categoría (estructura, extractabilidad, potencial de cita, señales de confianza, frescura, preparación para responder y más), los problemas encontrados y cambios concretos con texto propuesto.

| Entrada | Obligatoria | Significado |
|---|---|---|
| url | una de las tres | Una página publicada. Es la mejor opción, porque las comprobaciones técnicas como el acceso de rastreadores de IA y las fechas de la página solo se ejecutan sobre una página publicada. |
| draftId | una de las tres | Un borrador guardado |
| content | una de las tres | El contenido como texto, para una página que aún no está publicada. Hasta 50.000 caracteres. |
| targetQuery | no | La pregunta o el prompt de búsqueda que el contenido debería ganar, hasta 200 caracteres. Sin él, Hi, Moose deduce uno. |

En las cuentas de pago se incluye evidencia de búsqueda en vivo.

Pide: «Audita https://acme.example/guides/sbom para la consulta "SBOM generation tools"».

### find_internal_links

Planifica enlaces internos para un contenido usando el rastreo de tu propio sitio. Devuelve dos listas: páginas a las que este contenido debería enlazar, cada una con el texto de anclaje que usar, y páginas existentes que deberían añadir un enlace hacia este contenido, cada una con el texto de anclaje que usar en esa página. Las páginas ya enlazadas en cualquiera de los dos sentidos quedan fuera.

| Entrada | Obligatoria | Significado |
|---|---|---|
| url | una de las tres | Una página de tu sitio, publicada |
| draftId | una de las tres | Un borrador guardado |
| content | una de las tres | El contenido como texto, hasta 50.000 caracteres |
| title | no | El título, cuando se pasa el contenido como texto |

Los resultados cubren las páginas rastreadas hasta ahora e indican la fecha del rastreo. Las páginas publicadas desde el último rastreo no se incluyen.

Pide: «Planifica enlaces internos para el borrador de la guía de SBOM».

## Visibilidad en la búsqueda con IA

### visibility_check_topic

Responde a «¿aparecemos en la búsqueda con IA para X?» a partir de los resultados de visibilidad que Hi, Moose tiene guardados. Pasa la pregunta con tus propias palabras; Hi, Moose la relaciona con los prompts seguidos, en cualquier idioma.

| Entrada | Obligatoria | Significado |
|---|---|---|
| question | sí | El tema o la pregunta, hasta 400 caracteres |
| lookbackDays | no | Cuántos días de resultados guardados leer. Por defecto 90. |
| engine | no | Solo este motor, por nombre, como «ChatGPT» |

Devuelve, por motor, si la marca fue mencionada o citada en la última ejecución y en una anterior, las tasas de mención y de cita en el periodo, un breve extracto de la última respuesta en la que apareció la marca, los prompts relacionados y otras marcas vistas. Cada extracto lleva un id de respuesta para la siguiente herramienta. Los resultados cubren solo los prompts seguidos en los motores seguidos, nunca toda la búsqueda con IA. Lee resultados guardados y nunca lanza comprobaciones nuevas.

Pide: «¿Aparecemos en la búsqueda con IA para generación de SBOM?».

### visibility_get_answer

Obtiene una respuesta guardada por su id de respuesta: el prompt, el motor, la fecha, si la marca fue mencionada o citada, las fuentes que listó el motor, las notas del evaluador y el texto completo de la respuesta. El texto es lo que escribió el motor en ese momento.

Pide: «Muéstrame la respuesta completa de ChatGPT de ese resultado».

### visibility_list_opportunities

Devuelve la cola de trabajo priorizada que Hi, Moose construye a partir de los resultados de visibilidad guardados, las mismas filas que la pestaña Oportunidades. Cada fila nombra la brecha exacta, el siguiente paso en una frase, la prioridad con sus motivos, con qué constancia se mantuvo la brecha entre ejecuciones, el esfuerzo, el estado que puso el equipo y un id de oportunidad.

| Entrada | Obligatoria | Significado |
|---|---|---|
| lookbackDays | no | Días de resultados guardados que leer. Por defecto 7, igual que la pestaña Oportunidades. Como máximo 90. |
| limit | no | Filas que devolver, las mejores primero. Por defecto 10, como máximo 25. |
| action | no | Solo un tipo de fila: `create-coverage`, `improve-page`, `earn-inclusion`, `correct-description` o `investigate-change` |
| priority | no | `high`, `medium` o `low` |
| includeClosed | no | Devolver también las filas marcadas como hechas, descartadas o pospuestas. Por defecto false. |
| opportunityId | no | Un id de un resultado anterior. Devuelve la evidencia completa de esa fila en lugar de la lista. |

Los cinco tipos de fila: **create-coverage** (ninguna página tuya responde a un prompt que ganan los competidores), **improve-page** (una página tuya está citada o es la más cercana pero la marca queda fuera o por detrás), **earn-inclusion** (una página de terceros que citan los motores nombra a competidores pero no a ti), **correct-description** (las respuestas repiten una afirmación sobre la marca que hay que comprobar) e **investigate-change** (la marca se nombraba o citaba antes y ya no).

Pide: «¿En qué deberíamos trabajar para la búsqueda con IA esta semana?» y después «Muéstrame la evidencia de la primera».

## Audio

### create_audio

Crea un episodio «escucha este artículo»: una conversación hablada a dos voces sobre el contenido, generada como MP3 y alojada por Hi, Moose, más el fragmento HTML del reproductor insertable.

| Entrada | Obligatoria | Significado |
|---|---|---|
| url | una de las tres | Una página publicada |
| draftId | una de las tres | Un borrador guardado |
| content y title | una de las tres | El artículo como texto, de 1.200 a 200.000 caracteres, con su título |
| length | no | `short` (unos 4 minutos), `standard` o `deep`. Por defecto short. |
| hostVoice, guestVoice | no | Dos voces distintas. Por defecto Sulafat y Fenrir. |
| language | no | Idioma de la narración. Por defecto: el idioma del contenido. |
| focus | no | En qué debe centrarse la conversación, hasta 500 caracteres |
| theme, layout, color, showTitle, customTitle, showTranscript, hideAttribution | no | El aspecto del reproductor, ver más abajo |

La [página de ajustes de audio](https://himoose.com/hi-moose-mcp/audio/) te permite escuchar todas las voces, elegir la duración, el idioma y el aspecto del reproductor, y copiar una línea de ajustes para pegar en el chat. Mientras se genera el episodio, el dispositivo anfitrión no trabaja en nada más. Si el resultado dice que el episodio aún se está generando, la siguiente herramienta lo recoge unos minutos después.

Pide: «Convierte https://acme.example/guides/sbom en audio, corto, con Zephyr y Charon».

### get_audio_embed

Devuelve el fragmento del reproductor de un episodio existente, con un aspecto nuevo cuando se pasan campos del reproductor. El audio no se vuelve a generar. También es la forma de recoger un episodio que aún se estaba generando.

| Entrada | Obligatoria | Significado |
|---|---|---|
| audioId | sí | El id del episodio |
| theme | no | `dark`, `light` o `auto`. Por defecto dark. |
| layout | no | `full` o `compact`. Por defecto full. |
| color | no | Color de acento en hexadecimal, por ejemplo `#5688b0` |
| showTitle, customTitle | no | Mostrar una línea de título, o poner el tuyo |
| showTranscript | no | Mostrar el botón de transcripción. Por defecto true. |
| hideAttribution | no | Ocultar la línea «Audio by Hi, Moose». Solo en planes de pago. |

Pide: «Dame el reproductor compacto claro de ese episodio».

## Qué no pueden hacer las herramientas

No pueden cambiar ajustes ni miembros del equipo, cambiar lo que Hi, Moose sigue, iniciar ejecuciones de visibilidad ni eliminar nada. Para paneles y automatización, usa la [Hi, Moose API](../developer-api.md).
