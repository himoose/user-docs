---
source_hash: f262de43811a037ebe40f0f411828409a4bc1eda0f592f12d08358e5530d41e6
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](http://localhost:8000/integrations/hi-moose-mcp/security/)


# Seguridad y tratamiento de datos

Esta página es para las personas que revisan un conector antes de que un equipo lo conecte. Describe cómo funciona Hi, Moose MCP hoy, en el orden en que suele preguntar una revisión de seguridad. Última comprobación contra el servidor en funcionamiento: 2026-10-19.

## Respuestas breves

| Pregunta | Respuesta |
|---|---|
| ¿Quién opera el servidor? | Hi, Moose, el fabricante de la app. No un tercero. |
| ¿Puede cambiar la lista de herramientas después de conectarnos? | No. Las herramientas son código fijo. La lista exacta se publica con un hash en [mcp.himoose.com/tools.json](https://mcp.himoose.com/tools.json). |
| ¿Cómo inician sesión las personas? | OAuth 2.1, el flujo estándar de MCP remoto, con su cuenta existente de Hi, Moose. Sin claves de API. |
| ¿Cuánto duran los tokens? | Los tokens de acceso, una hora. Los tokens de actualización caducan tras 30 días sin uso, 90 días como máximo. |
| ¿Podemos revocar el acceso? | Sí, por app, en Hi, Moose en **Ajustes → Hi, Moose MCP**. |
| ¿Qué puede cambiar una app conectada? | Trabajo de contenido y lecturas dentro de los proyectos de la cuenta con sesión iniciada. No puede publicar, borrar ni cambiar ajustes, miembros del equipo o seguimiento. |
| ¿Llega a algo fuera de Hi, Moose? | No. Nunca ve los chats, archivos, repositorios u otros conectores de la app desde la que se usa. |
| ¿Dónde se ejecuta el trabajo? | En la app Hi, Moose en un dispositivo que tú eliges, el dispositivo anfitrión. |
| ¿Se marca el texto externo en los resultados? | Sí. Los pasajes de páginas y las respuestas de motores de IA vuelven entre marcadores etiquetados como datos, no como instrucciones. |
| ¿Dónde informamos de un problema? | [legal@himoose.com](mailto:legal@himoose.com), o la [página de contacto](https://himoose.com/es/contact/). |

## Quién opera el servidor

Hi, Moose MCP está construido y operado por Hi, Moose. Es el único servidor MCP que llega a una cuenta de Hi, Moose, y no es un servidor comunitario ni de terceros. La dirección del servidor es:

```text
https://mcp.himoose.com/mcp
```

El servidor en sí es pequeño. Gestiona el inicio de sesión y los tokens, ofrece la lista de herramientas y pasa cada solicitud a la nube de Hi, Moose, que la entrega al dispositivo anfitrión. El trabajo, como leer el rastreo del sitio o escribir un brief, se ejecuta en la app Hi, Moose en ese dispositivo, igual que cuando alguien pulsa el botón en la app.

## La lista de herramientas está publicada y no cambia

Un servidor MCP puede, en principio, cambiar las descripciones de sus herramientas después de que te conectes, u ocultar en ellas instrucciones para el agente de IA. El nombre que OWASP da a esto es envenenamiento de herramientas (tool poisoning).

Las herramientas de Hi, Moose MCP son código fijo en el servidor. Los nombres, las descripciones y los esquemas de entrada no cambian entre llamadas, y nunca se escribe en ellos contenido del usuario. Una herramienta nueva significa una nueva versión del servidor.

La lista exacta que sirve el servidor se publica en:

```text
https://mcp.himoose.com/tools.json
```

Contiene la versión del servidor, la fecha del último cambio de la lista, el número de herramientas, el texto completo de cada herramienta, el texto de instrucciones que el servidor da al agente y un hash SHA-256. El hash cubre el JSON compacto de los campos `instructions` y `tools`, así que puedes recalcularlo a partir del archivo o compararlo con lo que recibió tu cliente MCP. Anota el hash en tus notas de revisión y compáralo de forma periódica. El mismo hash es la cabecera `ETag` del archivo.

Antes de que alguien inicie sesión, la página de consentimiento muestra la misma lista de herramientas en palabras sencillas, bajo "Esta app podrá" y "No podrá".

## Inicio de sesión y tokens

Todos los clientes siguen el mismo flujo: Claude en la web, la app de escritorio de Claude, Claude Code, ChatGPT y cualquier otra app MCP. No hay atajos, ni tokens compartidos, ni claves de API.

- OAuth 2.1 tal como lo describe la especificación de autorización MCP actual: metadatos de recurso protegido (RFC 9728) con un desafío `WWW-Authenticate`, metadatos del servidor de autorización (RFC 8414), PKCE obligatorio para todos los clientes, indicadores de recurso (RFC 8707) para que un token de este servidor no pueda reutilizarse en otro sitio, registro dinámico de clientes (RFC 7591) y Client ID Metadata Documents, y revocación de tokens (RFC 7009).
- El inicio de sesión ocurre en `console.himoose.com`, con la cuenta existente de Hi, Moose de la persona, por correo y contraseña o con Google. La app MCP nunca ve la contraseña. Hi, Moose MCP solo conoce el id y el correo de la cuenta, y qué proyectos puede ver la cuenta.
- La página de consentimiento nombra a la app que solicita acceso. Cuando la app publica su identidad, la página muestra su dominio editor. Cuando no lo hace, la página dice "Nombre no verificado".
- Los tokens de acceso duran una hora. Los tokens de actualización duran 90 días como máximo y caducan tras 30 días sin uso. Los tokens, códigos y secretos se almacenan solo como hashes.
- Una conexión pertenece a una persona. Los miembros del equipo se conectan con sus propias cuentas.

Para desconectar una app, abre Hi, Moose y ve a **Ajustes → Hi, Moose MCP**. La tabla **Apps conectadas** lista cada app con sesión iniciada en la cuenta, con el dominio editor y la hora de conexión. **Revocar** cierra la sesión de esa app en menos de un minuto. La app solo puede volver a conectarse pasando de nuevo por el inicio de sesión.

## Qué puede y qué no puede hacer una app conectada

Todo lo que puede hacer una app conectada está en la [guía de configuración](../hi-moose-mcp.md) y se describe herramienta por herramienta en la [referencia de herramientas](tools.md). Es trabajo de contenido e investigación dentro de los proyectos de la cuenta: briefs, borradores, imágenes, FAQ, puntos clave, auditorías AEO, planes de enlaces internos, episodios de audio, comprobaciones de cobertura y lecturas de resultados de búsqueda con IA almacenados.

No puede:

- Publicar en un sitio web ni cambiar nada en él
- Borrar nada
- Cambiar ajustes, miembros del equipo, facturación o el dispositivo anfitrión
- Cambiar lo que Hi, Moose sigue, ni iniciar una ejecución de visibilidad
- Llegar a ninguna cuenta distinta de la que inició sesión
- Llegar a nada de la app desde la que se usa: ni chats, ni archivos, ni repositorios, ni memoria, ni otros conectores

Cada solicitud nombra un proyecto. Antes de que empiece cualquier trabajo, Hi, Moose comprueba que la cuenta con sesión iniciada tiene acceso a ese proyecto. Una solicitud para un proyecto que la cuenta no puede ver falla de inmediato.

## Dónde se ejecuta el trabajo y qué datos se mueven

Hi, Moose MCP nunca tiene una copia del rastreo del sitio, del perfil Brand Truth ni de la Library. Esos viven en la app Hi, Moose en el dispositivo anfitrión, el único ordenador o servidor que eliges en Ajustes. El anfitrión ejecuta cada trabajo igual que la app lo ejecuta desde un botón.

Este es el camino que sigue una solicitud:

1. La app MCP envía al servidor el nombre de la herramienta y su entrada.
2. El servidor comprueba el token y pide a la nube de Hi, Moose que cree un registro de trabajo para el proyecto. La nube comprueba el acceso al proyecto y escribe el registro.
3. El dispositivo anfitrión, que vigila los trabajos de sus proyectos, recoge el trabajo y lo ejecuta.
4. El anfitrión escribe el resultado en el registro de trabajo y lo guarda en la Library. El servidor devuelve el resultado a la app MCP.

Qué significa eso para tus datos:

- La solicitud y el resultado viajan por la nube de Hi, Moose (Google Cloud, región de Estados Unidos) como un registro de trabajo. El registro se queda con el proyecto para que la tabla **Trabajos recientes de agentes** de Ajustes pueda mostrar qué se pidió, desde qué app y cuenta, y si terminó.
- Las imágenes generadas se guardan en el almacenamiento en la nube de Hi, Moose de la cuenta y se devuelven como un enlace.
- Las llamadas a modelos usan el mismo camino que la app: los modelos gestionados de tu plan, tus propias claves de modelo si las aportaste, o un modelo local si ejecutas uno. Conectar una app MCP no cambia qué modelos ven tu contenido.
- Los registros propios del servidor guardan el nombre de la herramienta, cuánto tardó la llamada y si el cliente usó streaming. Nunca guardan la entrada ni el resultado.

## Texto externo en los resultados

Algunos resultados contienen texto que Hi, Moose no escribió: pasajes de páginas de tu sitio, texto ancla citado de una página, extractos breves de lo que respondió un motor de IA, o el texto completo de una respuesta almacenada. Un texto así podría llevar instrucciones dirigidas a un agente de IA. El nombre que OWASP da a esto es inyección indirecta de prompts.

Cada resultado que lleva texto externo lo marca. El texto vuelve entre un marcador de inicio y uno de fin, con una línea delante que indica de dónde viene y que todo lo que hay entre los marcadores son datos, no instrucciones. La forma estructurada del mismo resultado lleva un campo `dataNotice` que dice lo mismo. Esto aplica a `check_site_coverage`, `run_aeo_audit`, `find_internal_links`, `visibility_check_topic`, `visibility_get_answer` y `visibility_list_opportunities`.

Los briefs, borradores, FAQ, puntos clave y guiones de audio los escribe Hi, Moose para ti. La investigación que hay detrás se lee en el dispositivo anfitrión y no se pasa al agente.

Los marcadores ayudan a un agente a tratar el texto como datos. No hacen a un agente inmune a las instrucciones del contenido que lee, y ningún proveedor de herramientas puede prometer eso. Mantén los permisos del agente que conectas tan acotados como exija su trabajo, igual que harías con cualquier conector.

## Informar de un problema de seguridad

Escribe a [legal@himoose.com](mailto:legal@himoose.com) o usa la [página de contacto](https://himoose.com/es/contact/). Cuéntanos qué encontraste y cómo reproducirlo. Respondemos a todos los informes y te diremos qué cambiamos.
