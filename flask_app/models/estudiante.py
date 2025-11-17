# modelo Estudiante: trabaja con la tabla estudiantes

from flask_app.config.mysqlconnection import conectar_mysql

BD = "esquema_estudiantes_cursos"

class Estudiante:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.edad = datos['edad']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        self.curso_id = datos['curso_id']

    @classmethod
    def crear(cls, datos):
        # crear un nuevo estudiante
        consulta = "INSERT INTO estudiantes (nombre, apellido, edad, created_at, updated_at, curso_id)VALUES (%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW(), %(curso_id)s);"
        return conectar_mysql(BD).consulta(consulta, datos)

    @classmethod
    def obtener_por_curso(cls, curso_id):
        # traer todos los estudiantes de un curso
        consulta = "SELECT * FROM estudiantes WHERE curso_id = %(curso_id)s;"
        datos = {"curso_id": curso_id}
        resultados = conectar_mysql(BD).consulta(consulta, datos)
        estudiantes = []
        for fila in resultados:
            estudiantes.append(cls(fila))
        return estudiantes
