# Aqui definimos la clase Ccrso que representa la tabla cursos

from flask_app.config.mysqlconnection import conectar_mysql  # iportamos la conexión

BD = "esquema_estudiantes_cursos"  # nombre de la base de datos que usaremos

class Curso:
    # constructor que recibe un diccionario con los datos de la BD
    def __init__(self, datos):
        self.id = datos['id']              # id del curso
        self.nombre = datos['nombre']      # nombre del curso
        self.created_at = datos['created_at']  # fecha de creación
        self.updated_at = datos['updated_at']  # fecha de última actualización

    # mtodo de clase para obtener todos los cursos
    @classmethod
    def obtener_todos(cls):
        # definimos la consulta SQL
        consulta = "SELECT * FROM cursos;"
        # ejecutamos la consulta y obtenemos una lista de diccionarios
        resultados = conectar_mysql(BD).consulta(consulta)
        # creamos una lista vacia donde guardaremos objetos Curso
        lista_cursos = []
        #recorremos cada fila en resultados
        for fila in resultados:
            # convertimos cada fila en un objeto Curso y lo agregamos a la lista
            lista_cursos.append(cls(fila))
        #devolvemos la lista de cursos
        return lista_cursos

    # metodo de clase para crear un curso nuevo
    @classmethod
    def crear(cls, datos):
        # consulta SQL para insertar un nuevo curso
        consulta = " INSERT INTO cursos (nombre, created_at, updated_at)VALUES (%(nombre)s, NOW(), NOW());"
        #ejecutamos la consulta y devolvemos el id del nuevo curso
        return conectar_mysql(BD).consulta(consulta, datos)

    # metodo de clase para obtener un curso por id
    @classmethod
    def obtener_por_id(cls, id_curso):
        # donsulta SQL para seleccionar un curso especifico
        consulta = "SELECT * FROM cursos WHERE id = %(id)s;"
        # creamos el diccionario con el valor del id
        datos = {"id": id_curso}
        # ejecutamos la consulta
        resultados = conectar_mysql(BD).consulta(consulta, datos)
        # si no hay resultados, regresamos none
        if len(resultados) < 1:
            return None
        # si sí hay resultado, convertimos el primer diccionario en un objeto Curso
        return cls(resultados[0])
