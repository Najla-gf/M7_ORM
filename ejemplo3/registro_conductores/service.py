from .models import Conductor, Direccion, Vehiculo

def crear_conductor(pRut, pNombre, pApellido, pFecha):
    conductor = Conductor(rut=pRut, fecha_nacimiento=pFecha, nombre=pNombre, apellido=pApellido)
    conductor.save()
    imprimir_modelos()

def agregar_direccion_a_conductor(rut_conductor, pCalle, pNumero, pComuna, pCiudad, pRegion, pDepto=None):
    obj_conductor = Conductor.objects.get(pk=rut_conductor)
    
    direccion = Direccion(calle=pCalle, numero=pNumero, depto=pDepto, comuna=pComuna, ciudad=pCiudad, region=pRegion,
                        conductor=obj_conductor)
    direccion.save()
    imprimir_modelos()


def agregar_un_vehiculo(rut_conductor, pPatente, pMarca, pModelo, pYear):
    obj_conductor = Conductor.objects.get(pk=rut_conductor)
    
    vehiculo = Vehiculo(marca=pMarca, modelo=pModelo, patente=pPatente, year=pYear, conductor=obj_conductor)
    vehiculo.save()
    imprimir_modelos()

def eliminar_vehiculo(vehiculo_id):
    vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
    vehiculo.delete()
    imprimir_modelos()

def eliminar_conductor(rut):
    Conductor.objects.get(pk=rut).delete()
    imprimir_modelos()

def imprimir_modelos():
    #select * from conductores:
    lista_conductores = Conductor.objects.all()
    
    for conductor in lista_conductores:
        print(f"{conductor.rut} - {conductor.nombre} {conductor.apellido} - {conductor.fecha_nacimiento}")
        #print(conductor)
    
        if hasattr(conductor,'direccion'):
            print(f"{conductor.direccion.calle} #{conductor.direccion.numero},....")

        if hasattr(conductor,'vehiculo_set'):
            lista_vehiculos= conductor.vehiculo_set.all()

            for vehiculo in lista_vehiculos:
                print(f"{vehiculo.patente}, {vehiculo.marca}, {vehiculo.modelo}, {vehiculo.year}")




