#Este archivo se encarga de conectarse a MySQL y ejecutar las consultas SQL

import pymysql.cursors


class ConexionMySQL:
    # esta clase representa una conexión a una base de datos MySQL
    def __init__(self, base_datos):
        # guardamos una conexion abierta a MySQL en self.connection
        self.connection = pymysql.connect(
            host='localhost',                 
            user='root',                
            password='1818',           
            db=base_datos, 
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor, 
            autocommit=True                   
        )


    def consulta(self, query, datos=None):
        with self.connection.cursor() as cursor:  # abrimos un cursor para hacer la consulta
            try:
                print("Ejecutando consulta SQL:", query)  #mostramos la consulta en consola
                cursor.execute(query, datos)  #ejecutamos la consulta con los datos

                #si la consulta empieza con select, devolvemos los resultados
                if query.lower().startswith("select"):
                    resultado = cursor.fetchall()  # bbtenemos todas las filas
                    return resultado          

        
                else:
                    self.connection.commit()  # guardamos los cambios

                    #si la consulta es INSERT, devolvemos el id insertado
                    if query.lower().startswith("insert"):
                        return cursor.lastrowid  #id del nuevo registro

                    # para UPDATE o DELETE no necesitamos devolver nada especial
                    return None

            except Exception as e:
                #sii algo sale mal mostramos el error
                print("Error al ejecutar la consulta:", e)
                return False

            finally:
                # cerramos la conexion siempre, pase lo que pase
                self.connection.close()


def conectar_mysql(base_datos):
  
    return ConexionMySQL(base_datos)
