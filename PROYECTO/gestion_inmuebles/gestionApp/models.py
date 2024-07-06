from django.db import models

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=255)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class InmuebleUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
