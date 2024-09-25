from flask import Blueprint, request, jsonify, current_app, render_template_string
from app import db,mail
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
import secrets
from datetime import datetime
from datetime import timedelta
from flask_mail import Message
from flask_cors import cross_origin



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
    
    user = User(username=username, email=email, password=password, name=name, lastname=lastname, phone=phone)
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

    if not user or user.password != password:  
        return jsonify({"message": "Credenciales incorrectas"}), 401

    token = jwt.encode({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'name': user.name,
        'lastname': user.lastname,
        'exp': datetime.utcnow() + timedelta(hours=2)
    }, 'ecolifepassword', algorithm='HS256')

    first_login = user.first_login
    if first_login:
        user.first_login = False
        db.session.commit()

    return jsonify({
        'access_token': token,
        'first_login': first_login,
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
        user.set_password_reset_token()
        db.session.commit()

        reset_url = f"http://localhost:3000/#/restablecer-contrasena?token={user.reset_token}"
        
        html = render_template_string("""
        <h1>Recuperación de Contraseña EcoLife</h1>
        <p>Hola,</p>
        <p>Has solicitado restablecer tu contraseña en EcoLife. 
        Por favor, haz clic en el siguiente enlace para restablecer tu contraseña:</p>
        <p><a href="{{ reset_url }}">Restablecer Contraseña</a></p>
        <p>Este enlace expirará en 1 hora.</p>
        <p>Si no solicitaste este cambio, puedes ignorar este correo.</p>
        <p>Saludos,<br>El equipo de EcoLife</p>
        """, reset_url=reset_url)

        msg = Message("Recuperación de Contraseña EcoLife",
                      sender=current_app.config['MAIL_DEFAULT_SENDER'],
                      recipients=[email],
                      html=html)
        mail.send(msg)

        current_app.logger.info(f"Correo de restablecimiento enviado a {email}")

    return jsonify({"message": "Si el correo existe, se ha enviado un enlace de restablecimiento"}), 200

@bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        return jsonify({"message": "Se requieren el token y la nueva contraseña"}), 400

    user = User.query.filter(User.reset_token == token).first()
    if user and user.check_password_reset_token(token):
        user.password = (new_password)
        user.reset_token = None
        user.reset_token_expiry = None
        db.session.commit()
        return jsonify({"message": "Contraseña restablecida con éxito"}), 200
    
    return jsonify({"message": "Token inválido o expirado"}), 400

@bp.route('/user/<int:user_id>/update', methods=['PUT'])
def update_password(user_id):
    if request.method == 'OPTIONS':
        return '', 200 

    data = request.get_json()
    if not data:
        return jsonify({"message": "Datos no proporcionados"}), 400

    current_password = data.get('current_password')
    new_password = data.get('new_password')

    if not current_password or not new_password:
        return jsonify({"message": "Se requieren la contraseña actual y la nueva"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    if user.password != current_password:
        return jsonify({"message": "Contraseña actual incorrecta"}), 400

    user.password = new_password
    db.session.commit()

    return jsonify({"message": "Contraseña actualizada con éxito"}), 200
