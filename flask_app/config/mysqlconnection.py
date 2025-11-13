# Esta clase se encarga de conectarse a MySQL y ejecutar consultas

import pymysql.cursors

class ConexionMySQL:
    def __init__(self, base_datos):
        # Abrimos la conexión a MySQL
        self.connection = pymysql.connect(
            host='localhost',
            user='root',          # tu usuario
            password='1818',      # tu contraseña
            db=base_datos,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    # Método para ejecutar consultas
    def consulta(self, query, datos=None):
        with self.connection.cursor() as cursor:
            try:
                print("Ejecutando:", query)
                cursor.execute(query, datos)
                # Si es SELECT
                if query.lower().startswith("select"):
                    resultado = cursor.fetchall()
                    return resultado
                # Si es INSERT, UPDATE o DELETE
                else:
                    self.connection.commit()
                    # Para INSERT devolvemos el id nuevo
                    if query.lower().startswith("insert"):
                        return cursor.lastrowid
                    return None
            except Exception as e:
                print("Error al ejecutar consulta:", e)
                return False
            finally:
                self.connection.close()

# Función de ayuda para crear una conexión
def conectar_mysql(nombre_bd):
    return ConexionMySQL(nombre_bd)
