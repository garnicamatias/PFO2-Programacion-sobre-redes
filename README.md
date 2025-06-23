# PFO2 - Sistema de Gestión de Tareas con API y Base de Datos - Matías Garnica - Programación Sobre Redes - IFTS 29 - Comisión B

## Descripción:
Este proyecto implementa una API REST con Flask que permite:
- Registrar usuarios
- Iniciar sesión
- Visualizar una página HTML de bienvenida al acceder a `/tareas`

La información de los usuarios se guarda en una base de datos SQLite, y las contraseñas se almacenan de forma segura usando hashes.


## Requisitos:
- Python 3.7+
- pip

### Instalación de dependencias:
```bash
pip install flask flask_sqlalchemy flask_httpauth
```

### Ejecutar el servidor:
```bash
python servidor.py
```
El servidor se iniciará en `http://127.0.0.1:5000/`


## Uso de la API: Se puede utilizar POSTMAN

### 1. Registrar usuario
**Endpoint:** `POST http://127.0.0.1:5000/registro`

**Body JSON:**
```json
{
  "usuario": "Matias",
  "contrasena": "1234"
}
```
**Respuesta esperada:**
```json
{
  "mensaje": "Usuario registrado exitosamente"
}
```

---

### 2. Iniciar sesión
**Endpoint:** `POST http://127.0.0.1:5000/login`

**Body JSON:**
```json
{
  "usuario": "Matias",
  "contrasena": "1234"
}
```
**Respuesta esperada:**
```json
{
  "mensaje": "Inicio de sesión exitoso"
}
```

---

### 3. Acceder a tareas (HTML)
**Endpoint:** `GET http://127.0.0.1:5000/tareas`

**Requiere autenticación HTTP Básica** con usuario y contraseña registrados.

**Respuesta esperada:**
Una página HTML que da la bienvenida al usuario logueado.



## Capturas:

Se encuentran en la carpeta `/capturas`.


## Respuestas a preguntas finales:

### ¿Por qué hashear contraseñas?
Hashear contraseñas permite almacenar de forma segura la información sensible. Si la base de datos es comprometida, los atacantes no podrán ver las contraseñas reales, ya que los hashes no se pueden revertir fácilmente.

### Ventajas de usar SQLite
SQLite es una base de datos liviana y embebida, perfecta para proyectos pequeños o prototipos. No requiere un servidor separado y permite trabajar con archivos locales, lo que simplifica la configuración y el despliegue.
