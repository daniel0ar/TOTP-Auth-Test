# TOTP-Auth-Test
Aplicación de prueba de autenticación de doble factor TOTP.

## Descripción
Estaes una aplicación cliente-servidor con la pequeña funcionalidad de autenticación de doble factor para códigos de un sólo uso o One Time Passwords (OTP) basados en tiempo (TOTP). 
El servidor se desarrolló en Django y funciona en el puerto 8000.
El cliente se desarrolló en Express y funciona en el puerto 3000.

## Construcción
Acceder a la carpeta cliente:

`cd client`


Instalar las dependencias con el comando:

`npm install`

Acceder a la carpeta del servidor:

`cd server`

Instalar las librerías de Python

`pip install -r requirements.txt`

## Ejecución
Para ejecutar el servidor de Django:

`cd server`

luego:

`python3 manage.py runserver`


Para ejecutar el cliente en Node:

`cd client`

luego:

`node app.js`

### Autor
Daniel Arroyo
