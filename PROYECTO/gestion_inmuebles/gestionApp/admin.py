from django.contrib import admin
from .models import TipoUsuario, Usuario, Region, Comuna, TipoInmueble, Inmueble, InmuebleUsuario

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoInmueble)
admin.site.register(Inmueble)
admin.site.register(InmuebleUsuario)