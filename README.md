# Guía de Configuración y Comandos

## Paso 1: Crear y activar el entorno virtual
```bash
python -m venv nombre_entorno
source nombre_entorno/Scripts/activate
```

## Paso 2: Ver las dependencias e instalar lo necesario
```bash
pip list 
pip install django
```

## Paso 3: Instalar driver de la base de datos (PostgreSQL) en nuestro entorno virtual
```bash
pip install psycopg2   
pip install --upgrade pip
pip list
```
## Paso 3.5: Guardar archivo requirements.txt
```bash
pip freeze > requirements.txt
```
```plaintext
Captura todos los paquetes instalados actualmente en el entorno virtual junto a sus versiones.
```

## Paso 4: Crear proyecto e ingresar a la carpeta
```bash
django-admin startproject nombre_proyecto
cd nombre_proyecto
```

## Paso 4.5: Crear la base de datos
### Base de Datos (Terminal Bash)
```sql
CREATE DATABASE nombre_bd;
\l                     -- lista bases de datos creadas 
\c nombre_bd         -- conectarse a la base de datos 
\q                     -- salir de la base de datos
```

### Vincular en `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_bd',
        'USER': 'postgres',
        'PASSWORD': 'Admin1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        }
    }
```

```python
PORT: '3606'  #Puerto para mySQL 
```

## Paso 5: Agregar app al proyecto
```bash
python manage.py startapp nombre_aplicacion
```

### En `settings.py`
```python
INSTALLED_APPS = [
    '...',
    'nombre_aplicacion',
]
```

## Paso 6: TEMPLATES
1. Crear la carpeta `templates` en la app.
2. Crear los archivos HTML con estructura básica.
3. Crear un método que despliega el HTML.
4. Crear una ruta que enlace a `views.py` de la app.

## Paso 7: MODELOS
1. Crear el modelo en `models.py`.
2. Agregar al `admin.py`.
    ```python
    from .models import Nombre_Modelo       #Importa el modelo creado
    admin.site.register(Nombre_Modelo)      #Registra el modelo en el administrador de Django
    ```

## Crear un superusuario
```bash
python manage.py createsuperuser
```
- **Username:** (leave blank to use 'najla')
- **Email address:** najla.gatica@gmail.com
- **Password:** Admin1234
- **Password (again):** Admin1234

```plaintext
Superuser created successfully.
```

## Paso 8: Ejecutar las migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### Revisar en base de datos (Terminal Bash)
```sql
\d     -- verificar el modelo creado en la lista
```

## Ejecutar el servidor
```bash
python manage.py runserver
```

## Conocer todas las migraciones y saber cuales se han ejecutado en la BD
```bash
python manage.py showmigrations
python manage.py showmigrations nombre_aplicacion
```

## Revertir una migración específica
```bash
python manage.py migrate nombre_aplicacion 0001_initial
```

## Entrar a la shell de django desde la terminal
```bash
python manage.py shell              #Inicia una sesión interactiva de Django
```
