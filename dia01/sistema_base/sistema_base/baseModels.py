from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()
    return row


#metodos genericos que permiten realizar consultas sql
class BaseModel:
    
    def executeQuery(self, sql, parametros=None): #los parametros pueden o no pueden ir
        #Obtenemos un objeto cursos que nos entrega la conexión
        cursor = connection.cursor()
        #with connection.cursor() as cursor:
        cursor.execute(sql, parametros if parametros is not None else [])
        
        print(cursor.description) #data que tenemos como respuesta
        data = cursor.description # recorrer la data
        #retornar lista[dicc]
        
        row = cursor.fetchone()
        return row


    def execute(self,sql,parametros=None):
            cursor = connection.cursor()
            cursor.execute(sql, parametros if parametros is not None else [])
            try:
                row = cursor.fetchone()
                if row is not None:
                    return row
                else:
                    return []
            except Exception as e:
                print("Error de consulta", e)
                return []

