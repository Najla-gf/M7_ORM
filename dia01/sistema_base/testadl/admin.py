from django.contrib import admin
from .models import Pelicula, Cliente, Direccion

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Cliente)
admin.site.register(Direccion)