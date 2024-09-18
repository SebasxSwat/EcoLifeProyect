from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
import secrets

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not all(key in data for key in ('username', 'email', 'password', 'name', 'lastname', 'phone')):
        return jsonify({"message": "Faltan campos requeridos"}), 400

    name = data["name"]
    lastname = data["lastname"]
    phone = data["phone"]
    username = data['username']
    email = data['email']
    password = data['password']
    
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "El nombre de usuario ya está registrado"}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "El correo electrónico ya está registrado"}), 400
    
    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password, name=name, lastname=lastname, phone=phone)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registro exitoso"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not all(key in data for key in ('username', 'password')):
        return jsonify({"message": "Faltan campos requeridos"}), 400

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Credenciales incorrectas"}), 401

    token = jwt.encode({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'name': user.name,
        'lastname': user.lastname,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, 'fabian_es_gay', algorithm='HS256')

    return jsonify({
        'access_token': token,
        'message': 'Inicio de sesión exitoso'
    }), 200

@bp.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"message": "Se requiere el correo electrónico"}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        token = secrets.token_urlsafe(32)
        expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        user.set_password_reset_token(token, expiry)
        db.session.commit()

        # Aquí deberías enviar un correo electrónico al usuario con el enlace de restablecimiento
        # Por ahora, solo simularemos el envío imprimiendo el token
        print(f"Token de restablecimiento para {email}: {token}")

        return jsonify({"message": "Si el correo existe, se ha enviado un enlace de restablecimiento"}), 200
    
    return jsonify({"message": "Si el correo existe, se ha enviado un enlace de restablecimiento"}), 200

@bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        return jsonify({"message": "Se requieren el token y la nueva contraseña"}), 400

    user = User.query.filter_by(reset_token=token).first()
    if user and user.check_password_reset_token(token):
        hashed_password = generate_password_hash(new_password)
        user.password = hashed_password
        user.reset_token = None
        user.reset_token_expiry = None
        db.session.commit()
        return jsonify({"message": "Contraseña restablecida con éxito"}), 200
    
    return jsonify({"message": "Token inválido o expirado"}), 400

