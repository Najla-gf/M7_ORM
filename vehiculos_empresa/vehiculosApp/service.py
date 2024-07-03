from .models import Vehiculo, Chofer, RegistroContabilidad

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo.objects.create(patente=patente, marca=marca, modelo=modelo, year=year)
    return vehiculo

def crear_chofer(RUT, nombre, licencia, activo, creacion_registro, vehiculo_patente):
    vehiculo = Vehiculo.objects.get(patente=vehiculo_patente)
    chofer = Chofer.objects.create(RUT=RUT, nombre=nombre, licencia=licencia, activo=activo, creacion_registro=creacion_registro, vehiculo=vehiculo)
    return chofer

def crear_registro_contable(fecha_compra, valor, vehiculo_patente):
    vehiculo = Vehiculo.objects.get(patente=vehiculo_patente)
    if RegistroContabilidad.objects.filter(vehiculo=vehiculo).exists():
        raise ValueError(f"Ya existe un registro contable para el vehículo con patente {vehiculo_patente}")
    registro = RegistroContabilidad.objects.create(fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo)
    return registro

def deshabilitar_chofer(RUT):
    chofer = Chofer.objects.get(RUT=RUT)
    chofer.activo = False
    chofer.save()

def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = False
    vehiculo.save()

def habilitar_chofer(RUT):
    chofer = Chofer.objects.get(RUT=RUT)
    chofer.activo = True
    chofer.save()

def habilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = True
    vehiculo.save()

def obtener_vehiculo(patente):
    return Vehiculo.objects.get(patente=patente)

def obtener_chofer(RUT):
    return Chofer.objects.get(RUT=RUT)

def asignar_chofer_a_vehiculo(RUT, vehiculo_patente):
    chofer = Chofer.objects.get(RUT=RUT)
    vehiculo = Vehiculo.objects.get(patente=vehiculo_patente)
    chofer.vehiculo = vehiculo
    chofer.save()


def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        chofer_asignado = vehiculo.chofer if hasattr(vehiculo, 'chofer') else None
        chofer_info = chofer_asignado.nombre if chofer_asignado else "Sin chofer asignado"
        print(f"Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}, Chofer: {chofer_info}")
        
    """
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        try:
            chofer_asignado = Chofer.objects.get(vehiculo=vehiculo)
            chofer_info = chofer_asignado.nombre
        except Chofer.DoesNotExist:
            chofer_info = "Sin chofer asignado"
        print(f"Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}, Chofer: {chofer_info}")"""

##No me resulta esta ultima X(