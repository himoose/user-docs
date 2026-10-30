---
source_hash: c0e86aa287011385729b74d0356154a633aae41651da6757d60dc8ad873cee3a
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/hi-moose-mcp/)

# Hi, Moose MCP

## Para qué sirve

Resumen, lista de herramientas y preguntas y respuestas: [himoose.com/hi-moose-mcp](https://himoose.com/es/hi-moose-mcp/). Esta página es la guía de configuración. La [referencia de herramientas](hi-moose-mcp/tools.md) describe cada herramienta con lo que necesita y lo que devuelve, y la [solución de problemas](hi-moose-mcp/troubleshooting.md) cubre el dispositivo anfitrión, los trabajos en espera y los problemas de conexión. [Seguridad y tratamiento de datos](hi-moose-mcp/security.md) responde a las preguntas que hace una revisión de seguridad antes de que un equipo se conecte.

Hi, Moose MCP permite que las apps de IA en las que ya trabajas usen Hi, Moose. Añádelo como conector MCP en Claude, ChatGPT o cualquier otra app compatible con MCP con inicio de sesión, inicia sesión con tu cuenta de Hi, Moose y pide trabajo a Hi, Moose desde dentro de esa app. MCP (Model Context Protocol) es el estándar que usan estas apps para conectarse a herramientas externas.

El trabajo se ejecuta en uno de tus propios dispositivos, el **dispositivo anfitrión**, donde Hi, Moose permanece abierto y con la sesión iniciada. Los resultados vuelven a la app y se guardan en tu [Library](../library/overview.md).

## Qué puede hacer una app conectada

Con las herramientas actuales, una app conectada puede:

- Ver tus proyectos de Hi, Moose
- Ver los briefs y borradores guardados en tu Library
- Comprobar si tu sitio ya cubre un tema, con las páginas que lo cubren y la fecha del rastreo comprobado
- Crear un brief de contenido
- Escribir un borrador a partir de un brief
- Actualizar contenido que ya tienes: comparar una página publicada, un borrador guardado o un texto pegado con los resultados de búsqueda actuales y recibir un brief de actualización con las carencias y un borrador revisado
- Crear una imagen destacada
- Escribir preguntas frecuentes con esquema FAQPage para un borrador guardado o una página de tu sitio
- Escribir los puntos clave de un borrador guardado o de una página de tu sitio
- Ejecutar una auditoría AEO de una página publicada, un borrador guardado o un texto pegado, con puntuaciones, problemas y correcciones propuestas
- Planificar enlaces internos para una página, un borrador guardado o un texto pegado: a qué páginas rastreadas debería enlazar, con el texto de anclaje, y qué páginas deberían enlazar a ella
- Responder a "¿aparecemos en la búsqueda con IA para este tema?" a partir de los resultados de visibilidad guardados: por motor, si tu marca fue mencionada o citada en la última ejecución y antes, con un breve extracto de la última respuesta
- Leer el texto completo de una respuesta guardada de búsqueda con IA
- Listar las oportunidades en las que merece la pena trabajar, las mismas filas priorizadas que la pestaña Oportunidades: la brecha exacta, el siguiente paso, la prioridad y la evidencia, con el detalle completo de cualquier fila si se pide
- Convertir una página publicada, un borrador guardado o un texto pegado en un episodio de audio "escucha este artículo", con el fragmento del reproductor insertable para la página; las voces, la duración, el idioma y el aspecto del reproductor se eligen en la [página de ajustes de audio](https://himoose.com/es/hi-moose-mcp/audio/) y se pegan en el chat como una sola línea de ajustes
- Cambiar el estilo del reproductor de un episodio de audio existente sin volver a generar el audio
- Recoger el trabajo terminado

No puede cambiar ajustes ni miembros del equipo, y no puede eliminar nada. Habrá más herramientas.

## Antes de empezar

1. Abre Hi, Moose en el dispositivo que debe ejecutar el trabajo e inicia sesión.
2. Ve a **Ajustes → Hi, Moose MCP** y elige ese dispositivo como dispositivo anfitrión del proyecto. Solo el propietario de la cuenta puede elegir el dispositivo anfitrión.
3. Copia la dirección del servidor que aparece ahí:

```text
https://mcp.himoose.com/mcp
```

## Conectar en Claude

Esta sección es para Claude.ai en el navegador y la app de escritorio de Claude. Claude Code, la herramienta de terminal, tiene su propia sección más abajo.

1. Abre **Ajustes → Conectores** (también en claude.ai/customize/connectors).
2. Elige **Añadir conector personalizado**. Escribe un nombre que aparecerá en tu lista de conectores, por ejemplo `Hi, Moose`, pega la dirección del servidor y pulsa **Continuar**.

    ```text
    https://mcp.himoose.com/mcp
    ```

    ![Ventana «Añadir conector personalizado» de Claude con el nombre Hi, Moose y la dirección del servidor rellenados](../assets/images/connect-hi-moose-mcp-to-claude.webp)

3. En la siguiente pantalla, mantén los ajustes que Claude detecta: **Iniciar sesión ahora** en Autenticación y **Usar la identidad publicada de Claude** en Cliente OAuth. No añadas cabeceras de solicitud. En Avanzado, deja el transporte en automático; el servidor usa Streamable HTTP. Pulsa **Añadir**.

4. Pulsa **Conectar** junto a Hi, Moose MCP. Se abre una página de Hi, Moose que muestra lo que podrá hacer la app y te pide iniciar sesión con tu cuenta de Hi, Moose.
5. Empieza un chat nuevo y pide, por ejemplo, «Muestra mis proyectos de Hi, Moose».

En los planes Team y Enterprise, un propietario añade primero el conector para la organización y luego cada miembro se conecta.

## Conectar en Claude Code

Claude Code es la herramienta de línea de comandos de Anthropic para desarrolladores. Si trabajas en Claude.ai o en la app de escritorio de Claude, usa la sección anterior. Ejecuta esto en una terminal:

```text
claude mcp add --transport http himoose https://mcp.himoose.com/mcp
```

Después ejecuta `/mcp` dentro de Claude Code y sigue el inicio de sesión.

## Conectar en ChatGPT

ChatGPT admite servidores MCP personalizados en sus planes de pago. Los nombres de los menús cambian de vez en cuando; esta es la ruta actual.

1. Abre **Ajustes → Apps** (llamado **Conectores** en algunas versiones). En espacios Business y Enterprise, puede que un propietario tenga que permitir primero los conectores personalizados.
2. Elige **Añadir** y luego **Crear servidor MCP personalizado**. Las versiones antiguas muestran **Crear app MCP** y pueden necesitar antes el **Modo desarrollador** en los ajustes avanzados.
3. Pega la dirección del servidor, elige **OAuth** como autenticación y guarda.

    ```text
    https://mcp.himoose.com/mcp
    ```

4. Inicia sesión con tu cuenta de Hi, Moose en la página que se abre.
5. En un chat, activa el conector para esa conversación y pide trabajo a Hi, Moose.

## Otras apps

Cualquier app que pueda añadir un servidor MCP remoto con inicio de sesión OAuth funciona igual: añade la dirección del servidor, inicia sesión con tu cuenta de Hi, Moose y úsalo desde ahí.

```text
https://mcp.himoose.com/mcp
```

## Skills para Claude y ChatGPT

Hi, Moose publica en GitHub skills gratuitas y de código abierto para la optimización para motores de respuesta (AEO), también llamada GEO o AI SEO: [himoose/aeo-skills](https://github.com/himoose/aeo-skills) (licencia MIT). Una skill es una carpeta de instrucciones que tu app de IA sigue para un tipo concreto de tarea; estas usan el formato abierto [Agent Skills](https://agentskills.io).

La primera skill, `ai-visibility`, lee a través de Hi, Moose MCP los resultados de búsqueda con IA que Hi, Moose ya ha guardado. Nunca ejecuta comprobaciones nuevas, no cambia ajustes ni publica nada. Pide, por ejemplo:

- «Crea mi panel de visibilidad en la búsqueda con IA». Es la opción por defecto: un panel interactivo en una sola página HTML. Elige 7, 30 o 90 días o tus propias fechas, filtra por motor de IA, pasa el ratón sobre un gráfico para ver las cifras, compara tu marca seguida con la competencia, revisa las respuestas que dejaron fuera a tu marca y avanza por una lista de tareas con botones **Open in Hi, Moose**. Los gráficos se guardan como PNG, las cifras como CSV y la página como PDF.
- «Escribe mi informe de visibilidad en la búsqueda con IA como texto para un correo». Recibes un informe breve por escrito.
- «¿En qué debería trabajar esta semana para aparecer más en la búsqueda con IA?». Recibes tus correcciones pendientes como una lista de tareas ordenada por prioridad.

La skill funciona en todos los planes. Las puntuaciones de sentimiento, narrativa y precisión de funciones forman parte de los planes de pago; las menciones, las citas, la posición y la competencia funcionan en todos los planes. Como con cualquier herramienta de Hi, Moose MCP, mantén Hi, Moose abierto en el dispositivo anfitrión mientras preguntas.

### Añadir la skill en Claude.ai o en la app de escritorio de Claude

1. En la [página de GitHub](https://github.com/himoose/aeo-skills), haz clic en **Code → Download ZIP** y descomprime el archivo.
2. Abre la carpeta `skills` y comprime solo la carpeta `ai-visibility` en un ZIP, de modo que tengas `ai-visibility.zip` con la carpeta `ai-visibility` dentro.
3. En Claude, ve a **Customize → Skills**, haz clic en **+**, luego en **Create skill → Upload a skill** y elige `ai-visibility.zip`.
4. Comprueba que **code execution** está activado en los ajustes de Claude; las skills lo necesitan.
5. Empieza un chat nuevo, comprueba que el conector de Hi, Moose está activado en él y pregunta.

### Añadir la skill en Claude Code

El repositorio también es un plugin de Claude Code. Una sola instalación añade la skill y el conector de Hi, Moose:

```text
/plugin marketplace add himoose/aeo-skills
/plugin install himoose@himoose
```

Después ejecuta `/mcp`, elige `plugin:himoose:himoose` y **Authenticate** para iniciar sesión. Si ya añadiste Hi, Moose con `claude mcp add` como se indica arriba, las mismas herramientas aparecen dos veces; quita una de ellas en `/mcp`.

### Añadir la skill en ChatGPT

Las skills solo están disponibles en algunos planes de ChatGPT; OpenAI indica los espacios Business, Enterprise, Healthcare y Edu ([Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)).

1. Conecta Hi, Moose MCP en ChatGPT como se describe arriba.
2. Añade la carpeta `skills/ai-visibility` del repositorio de GitHub como skill, siguiendo las instrucciones de OpenAI para tu espacio de trabajo.
3. En un chat, escribe `@` para elegir la skill, o simplemente pregunta.

## Cómo se ejecuta una petición

1. La app envía tu petición a Hi, Moose MCP.
2. Hi, Moose MCP la pasa al dispositivo anfitrión, que ejecuta el trabajo con el rastreo, el Brand Truth y la investigación del proyecto.
3. El resultado vuelve a la app y se guarda en tu Library.

Un brief, un borrador, una imagen, un conjunto de preguntas frecuentes o una lista de puntos clave tardan de uno a tres minutos; una auditoría AEO, de dos a cuatro; una actualización de contenido, de tres a seis. Una pregunta de visibilidad se responde en unos segundos y la lista de oportunidades, en menos de un minuto. Si la app dice que el trabajo sigue en curso, pídele que vuelva a comprobarlo; recoge el resultado cuando está listo. Si el dispositivo anfitrión está apagado o sin sesión, la app recibe un mensaje que lo indica.

Los trabajos se ejecutan con la cuenta con sesión iniciada en el dispositivo anfitrión, así que la Library que leen y escriben es la de esa cuenta. La tabla **Trabajos recientes de agentes** en Ajustes muestra qué se pidió, desde qué app y si terminó.

## Desconectar una app

Ve a **Ajustes → Hi, Moose MCP**. La tabla **Apps conectadas** lista cada app con sesión iniciada en tu cuenta. **Revocar** cierra la sesión de esa app. Puede tardar hasta un minuto en aplicarse, y la app puede volver a conectarse más tarde. El acceso también caduca por sí solo tras 30 días sin uso.
