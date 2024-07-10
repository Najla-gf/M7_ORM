class InmuebleModel(bm):

    def sql_obtener_todos_inmuebles():
        sql = "select nombre, arrendada from testadl_inmueble"
        parametros = None
        inmuebles= list(bm.execute(sql,parametros))

        for inmu in inmuebles:
            print(inmu)

        return inmuebles

    def obtener_todos_inmuebles():
        return Inmueble.objects.all()
    
    def raw_obtener_todos_inmuebles():
        sql = "select nombre, arrendada from testadl_inmueble"
        query = Inmueble.objects.raw(sql)
        for p in query:
            print(p.nombre)
            print(p.arrendada)
    
    
class ClienteModel(bm):

    def obtener_cliente():
        select= "select cliente_id, nombre, apellido from testadl_cliente"
        query = Cliente.objects.raw(select)
        for p in query:
            print(p.title)
            print(p.text)