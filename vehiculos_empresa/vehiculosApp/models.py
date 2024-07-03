from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"Patente: {self.patente}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.year}"

class Chofer(models.Model):
    RUT = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    licencia = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.SET_NULL, null=True, unique=True)

    def __str__(self):
        vehiculo_info = f", Vehículo asignado: {self.vehiculo.patente}" if self.vehiculo else ", Sin vehículo asignado"
        return f"RUT: {self.RUT}, Nombre: {self.nombre}, Licencia: {self.licencia}, Activo: {self.activo}, Creación Registro: {self.creacion_registro}{vehiculo_info}"

class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_compra = models.DateField(null=False)
    valor = models.FloatField(null=False)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"ID: {self.id}, Fecha de Compra: {self.fecha_compra}, Valor: {self.valor}, Vehículo: {self.vehiculo.patente}"
