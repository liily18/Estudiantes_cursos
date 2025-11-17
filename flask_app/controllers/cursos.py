# Aca ponemos las rutas relacionadas con CURSOS

from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/")
def inicio():
    #mandamos al usuario a la página de cursos
    return redirect("/cursos")


# ruta para ver la página principal de cursos
@app.route("/cursos")
def pagina_cursos():
    # pedimos al modelo todos los cursos de la base de datos
    cursos = Curso.obtener_todos()
    # enviamos la lista de cursos al template cursos.html
    return render_template("cursos.html", lista_cursos=cursos)


# ruta para crear un nuevo curso
@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    # armamos el diccionario con los datos enviados desde el formulario
    datos = {
        "nombre": request.form["nombre"]
    }
    # llamamos al modelo para guardar el curso
    Curso.crear(datos)
    #redirigimos de vuelta a la página de cursos para ver la lista actualizada
    return redirect("/cursos")


#ruta para mostrar un curso especifico y sus estudiantes
@app.route("/cursos/<int:id_curso>")

def mostrar_curso(id_curso):
    # obtenemos la información de ese curso por id
    curso = Curso.obtener_por_id(id_curso)
    #obtenemos todos los estudiantes que pertenecen a ese curso
    estudiantes = Estudiante.obtener_por_curso(id_curso)
    # mandamos ambos al template mostrar_curso.html
    return render_template(
        "mostrar_curso.html",
        curso=curso,
        lista_estudiantes=estudiantes
    )
