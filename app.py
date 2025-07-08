import os
from flask import Flask
from db import db

app = Flask(__name__, template_folder='plantillas')

# Clave para que puedan ver las sesiones
app.secret_key = 'clave_super_secreta'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data", "productos.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Importa y registra el Blueprint
from controladores.producto_controlador import producto_bp
app.register_blueprint(producto_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
