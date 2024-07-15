# Proyecto - Manejo del CRUD

## Contexto
Una empresa dedicada al arriendo de inmuebles requiere de su ayuda para crear un sitio web donde usuarios puedan revisar inmuebles disponibles para el arriendo, separado por comuna y región. El sitio web poseerá dos tipos de usuarios: arrendatarios y arrendadores.

---

## [Hito 1](./Hito1)
### Requerimientos
1. **Instalación de desarrollo**
   - Instalación de PostgreSQL.
   - Creación de un ambiente virtual de Python.
   - Instalación de los paquetes necesarios para la creación de un proyecto de Django.
   - Creación de una aplicación de Django.

2. **Definición de modelo de datos**
   - Representación del modelo relacional de datos.
   - Conexión a la base de datos.
   - Definición y manejo de llaves primarias en columnas foráneas.

3. **Implementación de operaciones en los modelos**
   - Crear un objeto con el modelo.
   - Listar desde el modelo de datos.
   - Actualizar un registro en el modelo de datos.
   - Borrar un registro del modelo de datos utilizando un modelo Django.

---

## [Hito 2](./Hito2)
### Requerimientos
1. **Utilizando las migraciones**
   - Poblar la base de datos con todas las regiones y comunas de Chile usando loaddata.
   - Poblar la base de datos con tipos de inmuebles usando loaddata.
   - Poblar la base de datos con varios inmuebles y usuarios usando loaddata.

2. **Consultas de listado de inmuebles**
   - Consultar listado de inmuebles para arriendo separado por comunas, guardando los resultados en un archivo de texto usando Django y SQL.
   - Consultar listado de inmuebles para arriendo separado por regiones, guardando los resultados en un archivo de texto usando Django y SQL.

---

## [Hito 3](./Hito3)
### Requerimientos
1. **Creación del template básico para página personal de perfil**
   - Generar una vista de login de usuarios.
   - Generar una vista de registro.
   - Realizar redireccionamiento de URLs.
   - Desplegar los datos del usuario.

2. **Modificación de datos personales**
   - Agregar la posibilidad de que Arrendatarios y Arrendadores modifiquen sus datos personales en sus respectivas páginas personales.
