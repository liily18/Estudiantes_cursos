# flask_app/controllers/controlador_estudiantes.py
# Rutas relacionadas con los estudiantes

from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/estudiante/nuevo")
def formulario_estudiante():
    # Necesitamos todos los cursos para llenar el <select>
    cursos = Curso.obtener_todos()
    return render_template("nuevo_estudiante.html", lista_cursos=cursos)

@app.route("/estudiante/crear", methods=["POST"])
def crear_estudiante():
    # Tomamos los datos del formulario
    datos = {
        "curso_id": request.form["curso_id"],
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "edad": request.form["edad"]
    }
    Estudiante.crear(datos)
    # Después de crear el estudiante, volvemos a la página de cursos
    return redirect("/cursos")
