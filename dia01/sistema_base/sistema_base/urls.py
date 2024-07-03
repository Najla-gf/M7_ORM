"""
URL configuration for sistema_base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testadl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cliente', views.cliente, name='cliente'),
    path('cliente/crear', views.crear_cliente, name='crear_cliente'),
    path('cliente/eliminar/<int:id>', views.eliminar_cliente, name='eliminar_cliente'),
    path('cliente/editar/<int:id>', views.editar_cliente, name='editar_cliente'),
    path('cliente/actualizar', views.actualizar_cliente, name='actualizar_cliente'),
]
