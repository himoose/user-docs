---
source_hash: 07b1b5e8bf746dc48362fa004a86b7566ef960fafcbe265cebb6ecd32d7aff91
---
!!! note "Traducción automática"
    Esta página fue traducida por IA. La versión en inglés es la versión autorizada.

    [Leerla en inglés](https://himoose.com/docs/integrations/google-search-console/)

# Google Search Console

## Para qué sirve

Conectar Google Search Console para que Hi, Moose pueda incorporar el rendimiento de búsqueda propio de Google (impresiones, clics y datos de consultas) a la misma base local de evidencias que utilizan [Visibility](../visibility/overview.md), las [AEO audits](../features/aeo-audits.md) y los [briefs de contenido](../features/content-briefs.md).

!!! note "Disponibilidad"
    La conexión con Google Search Console se incluye en todos los planes de pago: BYOK Premium, BYOK Agency y todos los planes gestionados. No se incluye en BYOK Free ni en Preview Mode. Véase [Tipos de cuenta y planes](../getting-started/account-modes.md).

## Por qué esto se queda en local

El acceso a Search Console requiere las credenciales de OAuth de su cuenta de Google, y Hi, Moose las trata como sensibles por diseño: la autorización se realiza en su navegador y los tokens resultantes se guardan **únicamente en su equipo**. Los servicios en la nube de Hi, Moose nunca reciben sus tokens de acceso, sus tokens de actualización ni sus secretos de cliente de Google para esta conexión: la aplicación de escritorio es lo único que habla con Google Search Console en su nombre.

## Configurar una conexión

1. Abra **Connections** en la aplicación de escritorio y elija Google Search Console.
2. Autorice el acceso en su navegador.
3. Vincule una propiedad de Search Console al [proyecto](../getting-started/projects.md) activo.

## Qué puede hacer con ello

- Obtener una instantánea local del rendimiento de páginas y consultas de la propiedad vinculada.
- Comparar la última instantánea con una ventana anterior para ver cambios significativos.
- Preguntar por sus datos de Search Console directamente en el chat. Moose los consulta de forma agéntica, acotando mediante varias consultas para responder a una pregunta vaga, en lugar de ejecutar un informe fijo. El modelo interpreta su pregunta, pero es la aplicación de escritorio la que valida y ejecuta en local cada consulta subyacente, de modo que sus datos y la custodia de los tokens permanecen en el dispositivo.
- Incorporar las evidencias de Search Console al diagnóstico de visibilidad y a la priorización de qué páginas merecen un brief de contenido o una AEO audit.

## Dónde residen los datos

Los datos de Search Console incorporados a Hi, Moose se guardan **en local en su dispositivo**, no en la nube de Hi, Moose. Forman parte de su base local de evidencias y se incluyen en una [copia de seguridad local](../getting-started/settings.md#data-backup) en lugar de sincronizarse entre equipos.

## Alcance actual

Esta conexión es de solo lectura en la versión 1: Hi, Moose no escribe en Search Console. Por ahora puede vincularse una propiedad por proyecto.

Search Console requiere un plan de pago. No se incluye en Preview Mode ni en BYOK Free.

!!! note "Actualice la aplicación si la conexión falla en Windows"
    Los instaladores de Windows anteriores a la v0.3.245 se distribuyeron sin las credenciales de Google que necesita la conexión, por lo que la conexión siempre fallaba en la aplicación instalada. Actualizar lo soluciona.
