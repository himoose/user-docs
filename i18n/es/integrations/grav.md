---
source_hash: 1d027fe8d7c0bf155818720c05a7777b1744c302a9ab057860377dc301df1947
---
# Grav

## Para qué sirve

Conectar un sitio [Grav](https://getgrav.org) en producción mediante el plugin de Hi, Moose para Grav, de modo que la aplicación de escritorio pueda inspeccionar el contenido de Grav y ejecutar directamente acciones remotas de creación, actualización, publicación y reversión.

## Instalar el plugin

1. Desde **Connections → Grav** en la aplicación de escritorio, abra el enlace de descarga y descargue el ZIP del plugin de Hi, Moose. La versión actual es la **0.1.1** y requiere Grav 1.7.0 o posterior.
2. En su panel de administración de Grav, abra **Plugins**, suba el ZIP y complete la instalación.
3. Active el plugin y abra su configuración en el panel de Grav.
4. Copie el paquete de conexión que se muestra allí: lo pegará en Hi, Moose en el paso siguiente.

## Conectar en Hi, Moose

1. Abra **Connections** en la aplicación de escritorio y elija Grav.
2. Introduzca la URL de su sitio Grav.
3. Deje en blanco la ruta del conector salvo que su plugin de Grav utilice una ruta distinta de la predeterminada. En caso contrario, Hi, Moose utiliza la ruta del paquete de conexión o recurre a `/himoose-connector`.
4. Pegue el paquete de conexión copiado del plugin y guarde.
5. Pulse **Test connector** para validar la conexión con su sitio Grav en producción.

## Estado de la conexión

Tras la prueba, Hi, Moose informa de uno de varios estados: el conector aún no está configurado del todo, está guardado pero todavía sin validar, ha respondido pero las acciones remotas de escritura no están plenamente habilitadas (solo lectura), está totalmente listo para acciones de lectura y de escritura remota, o la última validación falló y hay que revisar los ajustes del sitio o los secretos del plugin.

## Qué puede hacer la conexión

Una vez lista, el conector de Grav puede listar contenido, leer contenido sin procesar y crear, actualizar y publicar contenido directamente, siguiendo la misma ruta preparada y revisable que utilizan [Borradores, vista previa y publicación](../features/drafts-and-publishing.md) para las demás conexiones.

## Seguridad

La URL de su sitio Grav y el paquete de conexión se guardan en local y solo son accesibles para el proceso en segundo plano de la aplicación de escritorio; nunca se exponen a la interfaz de usuario.
