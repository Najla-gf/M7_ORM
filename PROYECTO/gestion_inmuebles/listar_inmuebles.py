import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_inmuebles.settings')
django.setup()

from gestionApp.models import Inmueble, Region, Comuna

def consultar_inmuebles_por_region():
    with open('Hito2/inmuebles_por_region.txt', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Región', 'Nombre', 'Descripción']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        inmuebles = Inmueble.objects.select_related('region').all()
        for inmueble in inmuebles:
            writer.writerow({
                'Región': inmueble.region.nombre,
                'Nombre': inmueble.nombre,
                'Descripción': inmueble.descripcion
            })

def consultar_inmuebles_por_comuna():
    with open('Hito2/inmuebles_por_comuna.txt', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Comuna', 'Nombre', 'Descripción']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        inmuebles = Inmueble.objects.select_related('comuna').all()
        for inmueble in inmuebles:
            writer.writerow({
                'Comuna': inmueble.comuna.nombre,
                'Nombre': inmueble.nombre,
                'Descripción': inmueble.descripcion
            })

if __name__ == "__main__":
    consultar_inmuebles_por_region()
    consultar_inmuebles_por_comuna()
