from django.db import models

# Create your models here.
#Se parte con las relaciones muchos a muchos, puede ser curso o profe
class Curso(models.Model):
    codigo = models.CharField(max_length=10,primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField()

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=True, blank=True)
    #Relacion ManyToMany
    cursos=models.ManyToManyField(Curso, related_name='profesores')

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"



class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=True, blank=True)
    #Relacion OneToMany
    curso = models.ForeignKey(Curso, related_name='estudiantes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50, null=True, blank=True)
    #Relacion OneToOne
    estudiante = models.OneToOneField(Estudiante, related_name='direcciones', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}"

