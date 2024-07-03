from django.shortcuts import render, HttpResponse, redirect
from .models import Pelicula, Cliente

# Create your views here.
def index(request):
    #SELECT * FROM Peliculas : el equivalente es la consulta de abajo
    peliculas = Pelicula.objects.all()
    print(peliculas)
    
    #SELECT * FROM peliculas WHERE titulo = 'Intensamente' : hacemos una consulta específica de un objeto
    pelicula_intensamente = Pelicula.objects.filter(titulo = 'Intensamente')
    print(pelicula_intensamente)
    pelicula_intensamente.descripcion = "Pelicula sobre las emociones"
    #pelicula_intensamente.save() #Aquí se produce el update
    
    #A NIVEL DE SHELL:
    #Para crear un pelicula sería de esta forma:
    pelicula = Pelicula(titulo="Matrix", descripcion="Pelicula de Neo")
    #pelicula.save()
    #con save guardamos la adición
    
    return HttpResponse("Ejecución correcta")


def cliente(request): #mostrar el html
    lista_clientes = Cliente.objects.all()
    context={
        'lista_clientes': lista_clientes
    }
    #buscamos todos los clientes y generamos un diccionario para pasarselo al html
    return render (request, "cliente.html",context)

def crear_cliente(request): #guarda en base de datos
    if request.method == "POST":
        pApellido = request.POST['apellido'] #parametro apellido
        pEdad = request.POST['edad']
        pEmail = request.POST['email']

        cliente = Cliente(nombre= request.POST['nombre'] ,apellido= pApellido,edad= pEdad, email= pEmail)
        cliente.save()

        return redirect("cliente")

def editar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        return HttpResponse("Cliente no encontrado", status=404)
    
    context = {
        'cliente': cliente
    }
    return render(request, "editar_cliente.html", context)

def actualizar_cliente(request, id):
    if request.method == "POST":
        try:
            cliente = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            return HttpResponse("Cliente no encontrado", status=404)

        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.edad = request.POST['edad']
        cliente.email = request.POST['email']
        cliente.save()
        return redirect("cliente")
    else:
        try:
            cliente = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            return HttpResponse("Cliente no encontrado", status=404)
        context = {
            'cliente': cliente
        }
        return render(request, "editar_cliente.html", context)


def eliminar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        return HttpResponse("Cliente no encontrado", status=404)

    cliente.delete()
    return redirect("cliente")

