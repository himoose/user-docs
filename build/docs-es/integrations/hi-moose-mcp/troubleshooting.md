---
source_hash: 44a098b9f501f2117290c2037c5635c5aa9f250b49d72a34e103dba9d3cb8b5b
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/hi-moose-mcp/troubleshooting/)


# Resolución de problemas

Qué hacer cuando Hi, Moose MCP no responde como esperas. La mayoría de los problemas tienen que ver con el dispositivo anfitrión: el ordenador donde Hi, Moose permanece abierto y hace el trabajo.

## «El dispositivo anfitrión de este proyecto no ha dado señales»

El ordenador elegido como dispositivo anfitrión está apagado, en reposo o sin conexión, o Hi, Moose está cerrado o sin sesión iniciada ahí.

1. Abre Hi, Moose en ese ordenador e inicia sesión.
2. Espera un minuto y vuelve a pedirlo. El anfitrión da señales cada pocos minutos mientras Hi, Moose está abierto.
3. Si el ordenador ya no va a volver, elige otro en **Ajustes → Hi, Moose MCP**. Solo el propietario de la cuenta puede cambiar el dispositivo anfitrión.

Los trabajos esperan hasta 15 minutos al dispositivo anfitrión. Después caducan y la app recibe un mensaje que lo indica; vuelve a pedirlo cuando el anfitrión esté de vuelta.

## «Este proyecto no tiene dispositivo anfitrión»

Nadie ha elegido todavía un dispositivo anfitrión para el proyecto. Abre Hi, Moose en el ordenador que debe hacer el trabajo, ve a **Ajustes → Hi, Moose MCP** y elígelo. Cada proyecto tiene su propio dispositivo anfitrión, así que un proyecto nuevo también necesita uno.

## La app dice que el trabajo sigue en curso

Los briefs, borradores, auditorías y audios tardan minutos, y algunas apps dejan de esperar antes de que termine el trabajo. Pide a la app que vuelva a comprobarlo; recoge el resultado con el id de trabajo que recibió. El trabajo también se guarda en tu [Library](../../library/overview.md) en Hi, Moose, así que no se pierde nada si el chat sigue adelante.

El audio es lo que más tarda: unos 5 minutos un episodio corto, 9 el estándar y 15 el profundo. Mientras tanto el dispositivo anfitrión no trabaja en nada más, así que una segunda petición espera detrás.

## La app eligió el proyecto equivocado

Las herramientas reciben el proyecto por nombre. Dilo en la petición, por ejemplo «para el proyecto Acme», o pide a la app que liste primero los proyectos y luego elija. Si dos proyectos tienen nombres parecidos, usa exactamente el que aparece en Hi, Moose.

## El conector no se conecta

- **La página de inicio de sesión nunca se abre.** Comprueba que la dirección del servidor es `https://mcp.himoose.com/mcp`, sin caracteres de más al final, y que la app usa OAuth y no una clave de API.
- **El código de inicio de sesión caducó.** El código vale dos minutos. Vuelve a iniciar la conexión desde la app.
- **Claude Team o Enterprise.** Un propietario tiene que añadir el conector para la organización antes de que los miembros puedan conectarse.
- **ChatGPT.** Los servidores MCP personalizados necesitan un plan de pago, y en los espacios Business y Enterprise puede que un propietario tenga que permitir primero los conectores personalizados o activar el Modo desarrollador. Los nombres de los menús cambian; consulta [Conectar en ChatGPT](../hi-moose-mcp.md#connect-in-chatgpt).

## La app estaba conectada y ya no lo está

El acceso caduca por sí solo tras 30 días sin uso, y el propietario de la cuenta puede revocar una app en **Ajustes → Hi, Moose MCP**. Vuelve a conectarte desde la app.

## Los resultados parecen desactualizados

- **Cobertura del sitio y enlaces internos** leen el último rastreo de tu sitio e indican su fecha. Las páginas publicadas desde entonces no se incluyen. Ejecuta un rastreo en Hi, Moose y vuelve a pedirlo.
- **Visibilidad y oportunidades** leen solo resultados guardados y nunca lanzan comprobaciones nuevas. Cubren los prompts seguidos en los motores seguidos durante el periodo indicado en la respuesta. Para ver un tema nuevo, añade un prompt para él en la pantalla Visibilidad y deja que ocurra una ejecución.

## Se ejecutó algo que no esperabas

La tabla **Trabajos recientes de agentes** en **Ajustes → Hi, Moose MCP** lista cada trabajo: qué se pidió, desde qué app, cuándo y si terminó. Los trabajos se ejecutan con la cuenta con sesión iniciada en el dispositivo anfitrión, así que una app conectada solo puede leer y escribir la Library de esa cuenta.

## Sigues atascado

Escribe a soporte con el nombre del proyecto, qué app usabas, aproximadamente cuándo ocurrió y qué dijo la app. La tabla de trabajos de agentes también ayuda.
