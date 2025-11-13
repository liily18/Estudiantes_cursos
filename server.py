#arrancamos la app Flask y cargamos los controladores
from flask_app import app

#importamos los controladores para que se registren las rutas
from flask_app.controllers import cursos, estudiantes

if __name__ == "__main__":
    # debug=True es para que se reinicie solo cuando guardamos
    app.run(debug=True)
