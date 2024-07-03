##Paso 1: Crear y activar el entorno virtual
#python -m venv vdemo
#source vdemo/Scripts/activate

##Paso 2: Ver las dependencias e instalar lo necesario
#pip list 
#pip install django

##Paso 3: Instalar driver de la base de datos (postgres) en nuestro entorno virtual
#pip install psycopg2   

#pip install --upgrade pip
#pip list

##Paso 4: Crear proyecto e ingresar a la carpeta
#django-admin startproject sistema_base
#cd sistema_base

##Paso 4.5: Crear la base de datos
#####################################
### BASE DE DATO: (TERMINAL BASH) ###
#####################################

#CREATE DATABASE sistema_base;
#\l                     lista bases de datos creadas 
#\c sistema_base        conectarse a la base de datos 
#\q                     salir de la base de datos

#Vincular en "settings.py"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sistema_base',
        'USER': 'postgres',
        'PASSWORD': 'Admin1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        }
    }

PORT: '3606'  #Puerto para mySQL 

##Paso 5: Agregar app al proyecto
#python manage.py startapp testadl

INSTALLED_APPS = [
    '...',
    'testadl',
]

##Paso 6: TEMPLATES
#Crear la carpeta templates en la app
#crear los html, con estructura básica
#crear método que despliega el html
#crear ruta que enlaza a views.py de la app


## Paso 7: MODELOS
#Crear el modelo en models.py
#agregar al admin.py
    #from .models import Pelicula
    #admin.site.register(Pelicula)

##Crear un superusuario:
        #CREAR SUPER USUARIO 
        #python manage.py createsuperuser
        #Username (leave blank to use 'najla'):
        #Email address: najla.gatica@gmail.com
        #Password: Admin1234
        #Password (again): Admin1234
        #Superuser created successfully.

##EJECUTAR LAS MIGRACIONES
#python manage.py makemigrations
#python manage.py migrate

#######################################################
#### revisar en base de datos (terminal bash)      ####
#### \d     verificar el modelo creado en la lista ####
#######################################################

##EJECUTAR EL SERVIDOR
#python manage.py runserver


##Conocer todas las migraciones y saber cuales se han ejecutado en la BD
#python manage.py showmigrations
#python manage.py showmigrations testadl

##Revertir una migración específica
#python manage.py migrate testadl 0001_initial

## Entramos a la shell de django desde la terminal
#Cuando se trabaja desde la shel podemos trabajar a nivel de código
#python manage.py shell


from testadl.models import Persona
p1 = Persona(nombre='John', apellido='Doe', correo='jdoe@mail.com')
#Aqui se crea o actualiza
p1.save()
#Aqui se muestra
print(p1.id)
p2 = Persona(nombre='Chuck', apellido='Norris', correo='chuck@mail.com')
p2.save()
print(p2.id) #2
print(p2) #Persona object (2)







