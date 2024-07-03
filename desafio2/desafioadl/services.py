from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    lista_tareas = Tarea.objects.filter(eliminada=False)
    arreglo_tareas_subtareas = []

    for tarea in lista_tareas:
        sub_tareas = tarea.subtareas.filter(eliminada=False)
        dicc_tareas = {
            'tarea': tarea,
            'sub_tareas': sub_tareas
        }
        arreglo_tareas_subtareas.append(dicc_tareas)

    return arreglo_tareas_subtareas

def crear_nueva_tarea(pdescripcion='', peliminada=False):
    tarea = Tarea(descripcion=pdescripcion, eliminada=peliminada)
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, pdescripcion=''):
    obj_tarea = Tarea.objects.get(pk=tarea_id)
    subtarea = SubTarea(descripcion=pdescripcion, eliminada=False, tarea=obj_tarea)
    subtarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    obj_tarea = Tarea.objects.get(pk=tarea_id)
    obj_tarea.eliminada = True
    obj_tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    obj_subtarea = SubTarea.objects.get(pk=subtarea_id)
    obj_subtarea.eliminada = True
    obj_subtarea.save()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(arreglo_tareas):
    for item in arreglo_tareas:
        print(f"[{item['tarea'].id}] {item['tarea'].descripcion}")
        for subtarea in item['sub_tareas']:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
