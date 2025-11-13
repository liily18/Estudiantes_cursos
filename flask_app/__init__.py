# Aquí creamos la instancia principal de Flask

from flask import Flask

app = Flask(__name__)

# Clave secreta para usar mensajes flash (si algún día los usamos)
app.secret_key = "clave_secreta"
