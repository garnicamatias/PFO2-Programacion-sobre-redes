from flask import Flask, request, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

# Importación para poder hashear las contraseñas
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Genera los modelos que van a existir en la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contrasena_hash = db.Column(db.String(120), nullable=False)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

# Crea las tablas correspondientes
with app.app_context():
    db.create_all()

# Autenticación de usuarios
@auth.verify_password
def verificar_password(usuario, contrasena):
    user = Usuario.query.filter_by(usuario=usuario).first()
    if user and check_password_hash(user.contrasena_hash, contrasena):
        return user

# Rutas con sus requerimientos y funciones
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contrasena')

    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({'mensaje': 'Usuario ya existe'}), 400

    hash_pw = generate_password_hash(contrasena)
    nuevo_usuario = Usuario(usuario=usuario, contrasena_hash=hash_pw)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario registrado exitosamente'})

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contrasena')
    user = Usuario.query.filter_by(usuario=usuario).first()
    if user and check_password_hash(user.contrasena_hash, contrasena):
        return jsonify({'mensaje': 'Inicio de sesión exitoso'})
    return jsonify({'mensaje': 'Credenciales inválidas'}), 401

@app.route('/tareas')
@auth.login_required
def tareas():
    html = f"""
    <h1>Bienvenido, {auth.current_user().usuario}!</h1>
    <p>Has iniciado sesión correctamente.</p>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
