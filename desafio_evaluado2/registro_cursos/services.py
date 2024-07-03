from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(pCodigo, pNombre, pVersion=None): #Parametros
    #Instancia
    curso = Curso(codigo=pCodigo, nombre=pNombre, version=pVersion)
    #Guarda la info
    curso.save()
    return curso

def crear_profesor(pRut, pNombre, pApellido, pCreado_por, pActivo=False):
    profesor = Profesor(rut=pRut, nombre=pNombre, apellido=pApellido, creado_por=pCreado_por, activo=pActivo)
    profesor.save()
    return profesor

def crear_estudiante(pRut, pNombre, pApellido, pFecha_nac, pCodigo_curso, pActivo=False):
    curso = Curso.objects.get(pk=pCodigo_curso)
    estudiante = Estudiante(rut=pRut, nombre=pNombre, apellido=pApellido, fecha_nac=pFecha_nac, activo=pActivo, curso=curso)
    estudiante.save()
    return estudiante


def crear_direccion(rut_estudiante, pCalle, pNumero, pComuna, pCiudad, pRegion, pDepto=None):
    obj_estu = Estudiante.objects.get(pk=rut_estudiante)
    direccion = Direccion(estudiante=obj_estu, calle=pCalle, numero=pNumero, comuna=pComuna, ciudad=pCiudad, region=pRegion, dpto=pDepto)
    direccion.save()
    return direccion


def obtiene_estudiante(rut):
    return Estudiante.objects.get(pk=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(pk=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(pk=codigo)

def agrega_profesor_a_curso(rut, codigo):
    profesor = obtiene_profesor(rut)
    curso = obtiene_curso(codigo)
    profesor.cursos.add(curso)
    return curso

def agrega_cursos_a_estudiante(rut, codigo):
    estudiante = Estudiante.objects.get(rut=rut)
    curso = Curso.objects.get(codigo=codigo)

    # Agregar el curso al estudiante
    estudiante.curso = curso
    estudiante.save()
    return estudiante

def imprime_estudiante_cursos(rut):
    estudiante = obtiene_estudiante(rut)
    if estudiante:
        curso = estudiante.curso
        if curso:
            print(f"({rut}) - {estudiante.nombre} {estudiante.apellido} Curso: ({curso.codigo}) {curso.nombre}")
        else:
            print(f"El estudiante ({rut}) no está inscrito en ningún curso.")
    else:
        print(f"No se encontró ningún estudiante con el RUT {rut}.")

