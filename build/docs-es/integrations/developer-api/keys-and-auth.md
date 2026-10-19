---
source_hash: eef50f1fe484ff2af95068f006064217adac902f902e7159b98801260bb5cb9a
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/developer-api/keys-and-auth/)


# Claves y autenticación

## Crear una clave

1. Abre Hi, Moose e inicia sesión como propietario de la cuenta. Solo el propietario puede crear, ver y revocar claves.
2. Ve a **Ajustes → Hi, Moose REST API**.
3. Dale una etiqueta a la clave, elige los proyectos que puede leer (todos o uno), decide cuándo caduca y marca los permisos que necesita.
4. Haz clic en **Crear clave** y copia la clave. Se muestra una sola vez. Hi, Moose no puede mostrarla de nuevo; si la pierdes, revócala y crea otra.

Las claves empiezan por `hmk_live_` seguido de 64 caracteres. La tabla bajo el formulario lista cada clave activa con sus permisos y su fecha de creación, último uso y caducidad. **Revocar** detiene una clave de inmediato.

Hi, Moose guarda solo un hash de la clave, igual que se guardan las contraseñas, así que nadie en Hi, Moose puede recuperar una clave tampoco.

## Una clave por app

Crea una clave distinta para cada app o script, con una etiqueta que diga para qué sirve. Así una clave se puede revocar sin romper nada más, y la columna **último uso** en Ajustes muestra qué app hizo las llamadas.

## Permisos

| Permiso | Qué puede hacer la clave |
|---|---|
| Leer datos de visibilidad | Todos los endpoints `GET`. Siempre activo. |
| Gestionar el seguimiento | Crear proyectos, definir términos de marca y competidores, añadir, cambiar y borrar prompts, definir motores y programación, registrar y borrar webhooks. |
| Iniciar ejecuciones | Iniciar una ejecución de visibilidad. Las ejecuciones gastan el saldo de la cuenta en motores en la nube, así que dáselo solo a una clave que lo necesite. |

Una llamada sin el permiso necesario responde `403 insufficient_scope` y nombra el permiso. Elige los permisos al crear la clave; no pueden cambiarse después. Crea una clave nueva en su lugar.

En la API los permisos aparecen como `visibility:read`, `tracking:write` y `runs:execute`, por ejemplo en la respuesta de `GET /me`.

## Acceso a proyectos

Una clave lee todos los proyectos de la cuenta o un solo proyecto, según se elija al crearla. Un proyecto que la clave no puede leer responde `404 not_found`, igual que un proyecto que no existe, así que una clave no sirve para averiguar qué proyectos tiene una cuenta.

## Autenticación

Envía la clave como token Bearer en la cabecera `Authorization` en cada petición:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

La respuesta indica la clave, sus permisos y los ids de proyecto que puede leer. Es una buena primera llamada para comprobar que una clave funciona.

Una petición sin clave, o con una clave mal formada, revocada o caducada, responde `401` con uno de estos códigos:

| Código | Significado |
|---|---|
| `invalid_key` | No hay cabecera `Authorization`, la clave tiene un formato incorrecto o Hi, Moose no la conoce |
| `key_revoked` | La clave se revocó en Ajustes |
| `key_expired` | La clave pasó su fecha de caducidad |

## Mantén la clave en tu servidor

Usa la clave solo desde tu propio servidor. La API no envía cabeceras CORS, así que una página web no puede llamarla directamente. Un panel en el navegador debe llamar a tu backend, y tu backend llama a la API. Así la clave queda fuera de la página y fuera del registro de red del navegador.

Guarda la clave en una variable de entorno o en un gestor de secretos, nunca en el control de versiones. Si una clave se filtra, revócala en Ajustes y crea otra. La revocación se aplica de inmediato.

## Caducidad

Una clave puede caducar a los 30, 90 o 365 días, o nunca. Una clave con caducidad es la opción más segura para un script que se va a reemplazar; una clave sin caducidad encaja con un panel de larga duración cuya clave vive en un gestor de secretos. La tabla de Ajustes muestra la fecha de caducidad de cada clave.
