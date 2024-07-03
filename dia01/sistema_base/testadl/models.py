from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(default="") #tiene que ir con parentesis para que se genere la migracion, aunque esté vacio
    
    def __str__(self) -> str:
        return f"({self.id}) - ({self.titulo})"
    
    
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    cliente_activo = models.BooleanField(default=True)
    

#ONE TO ONE
class Direccion(models.Model):
    calle = models.CharField(max_length=100, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=100, blank=False, null=False)
    #OneToOne
    cliente = models.OneToOneField(Cliente, blank=False, null=False, on_delete=models.CASCADE)


#MANY TO MANY
class Libro(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)

class Autor(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    libros = models.ManyToManyField(Libro, related_name="autores")

class AutorLibro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    creado_por = models.CharField(max_length=50, null=False, blank=False)
    creacion = models.DateTimeField(auto_now_add=True)