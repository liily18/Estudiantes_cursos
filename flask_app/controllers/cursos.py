# flask_app/controllers/controlador_cursos.py
# Aquí ponemos las rutas relacionadas con los cursos

from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/")
def inicio():
    # Redirigimos a la página de cursos
    return redirect("/cursos")

@app.route("/cursos")
def pagina_cursos():
    # 1) Pedimos todos los cursos al modelo
    cursos = Curso.obtener_todos()
    # 2) Enviamos la lista de cursos al template
    return render_template("cursos.html", lista_cursos=cursos)

@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    # 1) Tomamos los datos del formulario
    datos = {
        "nombre": request.form["nombre"]
    }
    # 2) Mandamos al modelo para que inserte
    Curso.crear(datos)
    # 3) Volvemos a la página de cursos
    return redirect("/cursos")

@app.route("/cursos/<int:id_curso>")
def mostrar_curso(id_curso):
    # 1) Obtenemos la info del curso
    curso = Curso.obtener_por_id(id_curso)
    # 2) Obtenemos estudiantes que pertenecen a ese curso
    estudiantes = Estudiante.obtener_por_curso(id_curso)
    # 3) Enviamos todo al template
    return render_template(
        "mostrar_curso.html",
        curso=curso,
        lista_estudiantes=estudiantes
    )
