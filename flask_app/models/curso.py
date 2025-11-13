# Modelo Curso: aquí va la lógica para trabajar con la tabla cursos

from flask_app.config.mysqlconnection import conectar_mysql

NOMBRE_BD = "esquema_estudiantes_cursos"

class Curso:
    def __init__(self, datos):
        # Guardamos los datos que vienen del diccionario de la BD
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']

    @classmethod
    def obtener_todos(cls):
        # Trae todos los cursos
        consulta = "SELECT * FROM cursos;"
        resultados = conectar_mysql(NOMBRE_BD).consulta(consulta)
        cursos = []
        for fila in resultados:
            cursos.append(cls(fila))   # Creamos objetos Curso
        return cursos

    @classmethod
    def crear(cls, datos):
        # Inserta un curso nuevo
        consulta = """
            INSERT INTO cursos (nombre, created_at, updated_at)
            VALUES (%(nombre)s, NOW(), NOW());
        """
        return conectar_mysql(NOMBRE_BD).consulta(consulta, datos)

    @classmethod
    def obtener_por_id(cls, id):
        # Trae un curso específico por id
        consulta = "SELECT * FROM cursos WHERE id = %(id)s;"
        datos = {"id": id}
        resultados = conectar_mysql(NOMBRE_BD).consulta(consulta, datos)
        if len(resultados) < 1:
            return None
        return cls(resultados[0])
