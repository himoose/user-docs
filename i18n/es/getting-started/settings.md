---
source_hash: f081840e659e67696268902173c5c0f26e8413e1debac31049488ad42cb5c005
---
# Configuración

## Para qué sirve

En Configuración gestiona su perfil, su plan, sus modelos, su equipo y el comportamiento de la aplicación en este equipo. Está organizada en diez secciones en la columna izquierda.

| Sección | Qué contiene |
|---|---|
| General | Datos del perfil y comportamiento de la aplicación en este equipo |
| Usage | Saldo de créditos y fecha de reinicio |
| Cuenta | Correo electrónico, contraseña, plan, clave de OpenRouter |
| Local Model | Descarga y activación del modelo en el dispositivo |
| Equipo | Puestos, invitaciones, funciones |
| [Site Monitoring](../site-monitoring/overview.md) | Programación de rastreo, índice de búsqueda, páginas supervisadas, rutas bloqueadas |
| [Branding](../agency/white-label.md) | Informes de marca blanca y atribución en audio (solo planes de pago) |
| Logs | Registros de acciones y exportación a CSV |
| Data & Backup | Copia de seguridad y restauración local |
| Troubleshooting | Caché, registro de diagnóstico, restablecimiento de datos locales |

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

Descargue y active un modelo aprobado en el dispositivo, como Gemma 4. La ejecución local nunca utiliza los modelos de Hi, Moose ni su clave de OpenRouter: se ejecuta íntegramente en su equipo y su uso es gratuito.

Los modelos locales están disponibles en todos los planes y son **obligatorios** en Preview Mode para las [AEO audits](../features/aeo-audits.md) y la puntuación de visibilidad.

!!! note "El tamaño del contexto se ajusta a su RAM"
    Hi, Moose dimensiona la ventana de contexto del modelo según la memoria disponible en su equipo, de modo que un mismo modelo utiliza una ventana menor en un portátil de 16 GB que en una estación de trabajo mayor.

## Equipo

Invite a miembros, consulte sus funciones y revoque accesos. Los límites de puestos dependen de su plan. Consulte [Gestión del equipo](team-management.md) para el recorrido completo.

## Site Monitoring

Programación de rastreo, índice de búsqueda local, páginas supervisadas y rutas bloqueadas. Es un área extensa y tiene su propia página: **[Site Monitoring](../site-monitoring/overview.md)**.

Las conexiones con CMS y fuentes de datos son otra cosa y viven en la pantalla **Connections**, no en Configuración:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

Aplique su marca blanca a los informes PDF exportados y a los reproductores de audio insertados. Disponible en todos los planes de pago y editable por el titular de la suscripción. Véase **[Marca blanca](../agency/white-label.md)**.

## Logs

Registros de acciones del proyecto actual, con el tipo, el usuario, la fecha, el estado y los metadatos de cada acción registrada. En los planes gestionados, los registros compartidos del equipo se sincronizan junto a los suyos locales.

**Export CSV** los descarga. La exportación de los registros de acciones del equipo está restringida a los titulares de espacios de trabajo gestionados de pago.

## Data & Backup

Cree una copia de seguridad comprimida `.hmbk` de su historial en el dispositivo e impórtela más adelante para restaurarlo.

**Las copias de seguridad incluyen** los registros de la base de datos local y las programaciones de visibilidad BYOK guardadas, de modo que sus briefs, auditorías, vistas previas, historial de site monitoring, estado del Inbox y otros artefactos de trabajo no confidenciales siguen siendo portables.

**Las copias de seguridad no incluyen** el estado de sesión, las credenciales de los conectores, las claves de API, los archivos de modelos locales ni los archivos adjuntos.

!!! warning "La importación sobrescribe los datos locales de forma permanente"
    Una importación sustituye los datos locales de Hi, Moose de este dispositivo por el contenido de la copia de seguridad. El cuadro de diálogo de confirmación le indica cuántos registros se restaurarán y cuándo se creó la copia. Reinicie la aplicación después para que todas las pantallas se recarguen con los datos restaurados.

Las importaciones solo aceptan archivos `.hmbk` exportados por la aplicación de escritorio de Hi, Moose.

## Troubleshooting

Tres herramientas de recuperación. Todas afectan únicamente al estado local del escritorio y nunca tocan los datos de la nube.

**Borrar caché transitoria**: borra la caché HTTP, los service workers y otros estados desechables. Conserva su sesión y su historial de trabajo local. Pruebe esto primero.

**Registro de diagnóstico**: Hi, Moose mantiene un pequeño registro de errores en este dispositivo. **Abrir la carpeta de registros** le lleva hasta él; si el soporte se lo pide, envíe el archivo `main-errors.log`. El registro permanece en su dispositivo salvo que usted decida compartirlo.

**Restablecer los datos locales de la aplicación**: elimina de forma permanente los artefactos, briefs, vistas previas, historial de visibilidad y demás estado de trabajo local del dispositivo. No se puede deshacer. Su sesión y las credenciales guardadas de los conectores se mantienen.
