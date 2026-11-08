---
source_hash: 0a9a56ce00908be9642b519b71a66ed53535f416da94c0f65e7bb741595259e0
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/getting-started/settings/)

# Configuración

## Para qué sirve

En Configuración gestiona su perfil, su plan, sus modelos, su equipo y el comportamiento de la aplicación en este equipo. Está organizada en secciones en la columna izquierda; algunas solo aparecen para el propietario de la cuenta o en los planes de pago.

| Sección | Qué contiene |
|---|---|
| General | Datos del perfil y comportamiento de la aplicación en este equipo |
| Uso | Saldo de créditos y fecha de reinicio |
| Cuenta | Correo electrónico, contraseña, plan, clave de OpenRouter |
| IA local | Descarga y activación del modelo en el dispositivo |
| Equipo | Puestos, invitaciones, funciones |
| [Supervisión del sitio](../site-monitoring/overview.md) | Programación de rastreo, índice de búsqueda, páginas supervisadas, rutas bloqueadas |
| [Marca](../agency/white-label.md) | Informes de marca blanca y atribución en audio (solo planes de pago) |
| Inicios de sesión | Los sitios en los que Moose tiene la sesión iniciada para las ejecuciones de visibilidad y Send Moose |
| [Hi, Moose MCP](../integrations/hi-moose-mcp.md) | Dispositivo anfitrión, modelo para tareas de redacción, apps conectadas, trabajos recientes |
| [API REST de Hi, Moose](../integrations/developer-api.md) | Claves de API y webhooks (solo propietario) |
| Registros | Registros de acciones y exportación a CSV (solo propietario) |
| Datos y copia de seguridad | Copia de seguridad y restauración local |
| Historial de visibilidad | La copia local de sus respuestas de búsqueda con IA y su límite de espacio |
| Resolución de problemas | Caché, registro de diagnóstico, restablecimiento de datos locales |

## General

**Datos del perfil**: su nombre preferido, su puesto y su ubicación. Sirven para personalizar la aplicación y para dar una atribución más clara al trabajo compartido.

**Comportamiento de la aplicación** controla cómo se ejecuta Hi, Moose en este equipo:

- **Iniciar Hi, Moose al iniciar sesión**: tras un reinicio, la aplicación se abre discretamente en segundo plano para que el trabajo programado siga ejecutándose. Puede abrir la ventana en cualquier momento desde la bandeja del sistema o la barra de menús.
- **Compartir analíticas de uso anónimas**: envía eventos anónimos y agregados (qué funciones se ejecutan, versión de la aplicación, errores) para que podamos mejorar el producto. Nunca envía su contenido, sus prompts, sus claves ni los sitios que analiza, y su IP se descarta. Puede desactivarlo cuando quiera.

## Usage

En los planes gestionados, aquí se muestra su saldo de créditos y lo que queda del mes.

!!! note "El mes es en UTC"
    Los créditos se reinician al comienzo de cada mes en UTC, no en su zona horaria. Configuración le muestra la fecha correspondiente a su ubicación, de modo que a última hora del último día del mes puede parecer que el reinicio se ha adelantado.

Los planes BYOK no consumen saldo de créditos de Hi, Moose para la inferencia, ya que la generación se ejecuta con su propia clave. El coste de los modelos se abona directamente a OpenRouter.

## Cuenta

- Actualice su correo electrónico, verifíquelo y restablezca su contraseña en las cuentas de correo y contraseña. Las cuentas de Google se gestionan a través de Google.
- Los cambios de correo electrónico esperan a que usted lo confirme mediante un enlace antes de aplicarse, y después su sesión en la aplicación se actualiza.
- Consulte su plan actual y cámbielo. Véase [Tipos de cuenta y planes](account-modes.md).

### Añadir su clave de API de OpenRouter

En los planes BYOK, añada aquí su clave de [OpenRouter](https://openrouter.ai). Hi, Moose valida la clave antes de redirigir hacia ella el enrutamiento de IA. Una vez añadida:

- Las funciones de IA se ejecutan en local, en la aplicación de escritorio, con su clave
- Usted elige qué modelos compatibles utilizar para el chat y la generación
- Su clave y sus prompts nunca pasan por los servidores de Hi, Moose para la inferencia BYOK

La clave se guarda por cuenta y no por dispositivo, de modo que le acompaña a una instalación nueva.

## Local Model

Descargue y active un modelo aprobado en el dispositivo, como Gemma 4. Las respuestas de un modelo local se generan en su equipo, sin los modelos gestionados de Hi, Moose ni su clave de OpenRouter, y su uso es gratuito. Por defecto, el chat usa un breve paso de enrutamiento en la nube para elegir la herramienta adecuada para cada mensaje, y para ello envía el texto del mensaje a un servicio de enrutamiento en la nube. Desactive **Enrutamiento inteligente** en **Configuración → IA local** para que ese paso también se quede en su dispositivo.

Los modelos locales están disponibles en todos los planes y son **obligatorios** en Preview Mode para las [AEO audits](../features/aeo-audits.md) y la puntuación de visibilidad.

!!! note "El tamaño del contexto se ajusta a su RAM"
    Hi, Moose dimensiona la ventana de contexto del modelo según la memoria disponible en su equipo, de modo que un mismo modelo utiliza una ventana menor en un portátil de 16 GB que en una estación de trabajo mayor.

## Equipo

Invite a miembros, consulte sus funciones y revoque accesos. Los límites de puestos dependen de su plan. Consulte [Gestión del equipo](team-management.md) para el recorrido completo.

## Site Monitoring

Programación de rastreo, índice de búsqueda local, páginas supervisadas y rutas bloqueadas. Es un área extensa y tiene su propia página: **[Supervisión del sitio](../site-monitoring/overview.md)**.

Las conexiones con CMS y fuentes de datos son otra cosa y viven en la pantalla **Conexiones**, no en Configuración:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

Aplique su marca blanca a los informes PDF exportados y a los reproductores de audio insertados. Disponible en todos los planes de pago y editable por el titular de la suscripción. Véase **[Marca blanca](../agency/white-label.md)**.

## Inicios de sesión

Moose usa su propio navegador para las ejecuciones de visibilidad de consulta local y para Send Moose. Esta sección lista los sitios en los que puede tener la sesión iniciada, agrupados en motores de respuesta con IA (ChatGPT, Google AI Mode y Gemini, Grok, Perplexity, Bing Copilot) y los sitios que usan los agentes de Send Moose (Reddit, LinkedIn, X), cada uno con una insignia **Sesión iniciada** o **Sin sesión**. Abra un sitio aquí e inicie sesión una vez; todas las ejecuciones posteriores recogen la sesión. Iniciar sesión también evita las comprobaciones de «confirme que es humano» que los motores muestran en las primeras ejecuciones. Los inicios de sesión se quedan en este equipo y nunca van a la nube.

La insignia es una estimación a partir de las cookies de cada sitio. Si una ejecución sigue pidiéndole que inicie sesión, abra el sitio aquí e inicie sesión de nuevo.

Se puede añadir un buzón de **correo web** para Send Moose, de modo que Moose pueda leer enlaces de confirmación mientras trabaja en un encargo. Nunca envía, responde, elimina ni cambia ajustes. Use un buzón creado para Moose y mantenga su bandeja personal aparte.

## Hi, Moose MCP

Conecte Claude, ChatGPT o cualquier otra app MCP a su cuenta de Hi, Moose, elija el dispositivo anfitrión que ejecuta el trabajo, elija el **modelo para tareas de redacción** y consulte las apps conectadas y los trabajos recientes. Véase **[Hi, Moose MCP](../integrations/hi-moose-mcp.md)**.

## API REST de Hi, Moose

Esta sección solo aparece para el propietario de la cuenta. Cree y revoque las claves de API que leen sus datos de visibilidad guardados desde sus propios paneles e informes, elija qué puede hacer cada clave (leer datos de visibilidad, gestionar la supervisión, iniciar ejecuciones) y consulte o elimine los webhooks registrados para el proyecto. Véase **[API de Hi, Moose](../integrations/developer-api.md)**.

## Logs

Registros de acciones del proyecto actual, con el tipo, el usuario, la fecha, el estado y los metadatos de cada acción registrada. En los planes gestionados, los registros compartidos del equipo se sincronizan junto a los suyos locales.

**Exportar CSV** los descarga. La exportación de los registros de acciones del equipo está restringida a los titulares de espacios de trabajo gestionados de pago.

## Data & Backup

Cree una copia de seguridad comprimida `.hmbk` de su historial en el dispositivo e impórtela más adelante para restaurarlo.

**Las copias de seguridad incluyen** los registros de la base de datos local y las programaciones de visibilidad BYOK guardadas, de modo que sus briefs, auditorías, vistas previas, historial de site monitoring, estado del Inbox y otros artefactos de trabajo no confidenciales siguen siendo portables.

**Las copias de seguridad no incluyen** el estado de sesión, las credenciales de los conectores, las claves de API, los archivos de modelos locales ni los archivos adjuntos.

!!! warning "La importación sobrescribe los datos locales de forma permanente"
    Una importación sustituye los datos locales de Hi, Moose de este dispositivo por el contenido de la copia de seguridad. El cuadro de diálogo de confirmación le indica cuántos registros se restaurarán y cuándo se creó la copia. Reinicie la aplicación después para que todas las pantallas se recarguen con los datos restaurados.

Las importaciones solo aceptan archivos `.hmbk` exportados por la aplicación de escritorio de Hi, Moose.

## Historial de visibilidad

Hi, Moose guarda en este equipo una copia de sus respuestas de búsqueda con IA para que la página de Visibility pueda mostrar cualquier periodo sin volver a descargarlo. Esta sección muestra cuánto espacio ocupa la copia del proyecto actual y las fechas que abarca, y un **límite de espacio**: cuando la copia supera ese tamaño, los días más antiguos se eliminan solo de este equipo, y vuelven desde la nube cuando elige un periodo que los necesita. En los planes sin copia en la nube no se elimina nada automáticamente; haga una copia de seguridad de las respuestas en Datos y copia de seguridad.

## Troubleshooting

Tres herramientas de recuperación. Todas afectan únicamente al estado local del escritorio y nunca tocan los datos de la nube.

**Borrar caché transitoria**: borra la caché HTTP, los service workers y otros estados desechables. Conserva su sesión y su historial de trabajo local. Pruebe esto primero.

**Registro de diagnóstico**: Hi, Moose mantiene un pequeño registro de errores en este dispositivo. **Abrir la carpeta de registros** le lleva hasta él; si el soporte se lo pide, envíe el archivo `main-errors.log`. El registro permanece en su dispositivo salvo que usted decida compartirlo.

**Restablecer los datos locales de la aplicación**: elimina de forma permanente los artefactos, briefs, vistas previas, historial de visibilidad y demás estado de trabajo local del dispositivo. No se puede deshacer. Su sesión y las credenciales guardadas de los conectores se mantienen.
