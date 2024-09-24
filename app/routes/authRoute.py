from flask import Blueprint, request, jsonify, current_app
from app import db
from app.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
import secrets
from flask_mail import Message
from app import db, mail

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
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
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
        token = secrets.token_urlsafe(32)
        expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        user.reset_token = token
        user.reset_token_expiry = expiry
        db.session.commit()

        reset_url = f"http://localhost:3000/restablecer-contrasena?token={token}"
        
        try:
            msg = Message("Recuperación de Contraseña EcoLife",
                          recipients=[email])
            msg.body = f"""
            Hola,

            Has solicitado restablecer tu contraseña en EcoLife. 
            Por favor, haz clic en el siguiente enlace para restablecer tu contraseña:

            {reset_url}

            Este enlace expirará en 1 hora.

            Si no solicitaste este cambio, puedes ignorar este correo.

            Saludos,
            El equipo de EcoLife
            """
            mail.send(msg)
            current_app.logger.info(f"Correo de restablecimiento enviado a {email}")
        except Exception as e:
            current_app.logger.error(f"Error al enviar el correo: {str(e)}")
            return jsonify({"message": "Error al enviar el correo de restablecimiento"}), 500

    return jsonify({"message": "Si el correo existe, se ha enviado un enlace de restablecimiento"}), 200

@bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        return jsonify({"message": "Se requieren el token y la nueva contraseña"}), 400

    user = User.query.filter_by(reset_token=token).first()
    if user and user.reset_token_expiry > datetime.datetime.utcnow():
        user.password = generate_password_hash(new_password)
        user.reset_token = None
        user.reset_token_expiry = None
        db.session.commit()
        return jsonify({"message": "Contraseña restablecida con éxito"}), 200
    
    return jsonify({"message": "Token inválido o expirado"}), 400

@bp.route('/test-email', methods=['GET'])
def test_email():
    try:
        msg = Message("Test Email",
                      recipients=[current_app.config['MAIL_USERNAME']])
        msg.body = "Este es un correo de prueba desde EcoLife."
        mail.send(msg)
        current_app.logger.info("Correo de prueba enviado con éxito")
        return jsonify({"message": "Correo de prueba enviado con éxito"}), 200
    except Exception as e:
        current_app.logger.error(f"Error al enviar el correo de prueba: {str(e)}")
        return jsonify({"message": f"Error al enviar el correo de prueba: {str(e)}"}), 500
