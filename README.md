E-COMMERCE GRUPO 3 VERSION 1.0.3

ULTIMAS ACTUALIZACIONES AGREGADAS A LA PLATAFORMA

1. Nueva estrutrua del proyecto, mas legibilidad, dividida en modulos para mayor entendimiento (admin = ficheros, archivos, templates, funciones y metodos para la administracion), (auth = para administrar la parte de los usuarios), (public = para administrar la parte de las rutas publicas y los archivos publicos)

2. sesiones 

3. base de datos

4. validaciones

5. seguridad

6. configuraciones

DEPENDENDENCIAS
-entorno virtual (virtualenv)
-flask

COMO MANEJAR DE FORMA CORRECTA EL PROYECTO EN SUS ORDENADORES
-crear un carpeta con nombre relacionado al proyecto, dentro de ella abrir terminal y crear un entorno virtual
-remplazar la carpeta lib del entorno virtual por la carpeta lib que esta en el proyecto E-commerce-equipo3
-copiar la carpeta app dentro de la carpeta creada, NO dentro de la carpeta del entorno virtual
-copiar el archivo entripoint.py dentro de la carpeta creada, NO dentro de la app


LIBRERIAS
-flask-sqlachemy
-flask-login
-flask-wtf
-slugify
-email-validator



/////////////////////////////////////////////////////////
E-COMMERCE GRUPO 3 VERSION 1.0.4

ULTIMAS ACTUALIZACIONES AGREDAS A LA PLATAFORMA

-CRUD de usuarios
-CRUD de productos
-Actualizacion de la base de datos
-subida de imagenes (en pruebas)
-seguridad en las vistas
-usuarios administrador
-ahora un administrador puede asignarle a un usuario el rol de administrador
-el administrador se crea en la consola de la base de datos (lo crea el super administrador)
-el administrador se logea por el login normalmente pero con los datos que el super administrador les da
-correo electronico que se envia cuando el usuario se registra
-parametros de configuaracion agregados, ahora todo el tema de configuracion lo podran encontrar en la carpeta de config
-como siempre dejo la carpeta lib por si se me olvida decirles que instale un nuevo paquete, recuerden remplazarlos por la carpeta lib que se les crea en su entorno