from django.contrib import admin
from .models import Conductor, Direccion, Vehiculo

# Register your models here.
admin.site.register(Conductor)
admin.site.register(Direccion)
admin.site.register(Vehiculo)