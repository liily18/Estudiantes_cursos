# aqui van las rutas relacionadas con ESTUDIANTES

from flask import render_template, request, redirect
from flask_app import app 
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante


# ruta para mostrar el formulario de nuevo estudiante
@app.route("/estudiante/nuevo")
def formulario_estudiante():
    # necesitamos todos los cursos para llenar el menú desplegable
    cursos = Curso.obtener_todos()
    #enviamos la lista de cursos al template
    return render_template("nuevo_estudiante.html", lista_cursos=cursos)


#ruta que procesa el formulario de nuevo estudiante
@app.route("/estudiante/crear", methods=["POST"])
def crear_estudiante():
    #construimos un diccionario con los datos del formulario
    datos = {
        "curso_id": request.form["curso_id"],      
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "edad": request.form["edad"]
    }
    #llamamos al modelo estudiante para guardar el nuevo registro
    Estudiante.crear(datos)
    # después de crear al estudiante, volvemos a la página de cursos
    return redirect("/cursos")
