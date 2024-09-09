from flask import Blueprint, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from flask_login import login_user  # Importamos login_user
from app.models.user import Usuario
from app import db  # Asegúrate de importar la base de datos

bp = Blueprint('auth', __name__)

# Reemplaza esto con el CLIENT_ID de tu aplicación Google
GOOGLE_CLIENT_ID = "TU_GOOGLE_CLIENT_ID"

@bp.route('/google-login', methods=['POST'])
def google_login():
    token = request.json.get('token')
    
    try:
        # Verifica el token usando la API de Google
        idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), GOOGLE_CLIENT_ID)

        # El token es válido. Obtener información del usuario
        google_id = idinfo['sub']
        email = idinfo['email']
        nombre = idinfo['name']

        # Busca al usuario en la base de datos o crea uno nuevo
        user = Usuario.query.filter_by(email=email).first()
        if not user:
            # Crear nuevo usuario si no existe
            user = Usuario(nombre=nombre, email=email)
            db.session.add(user)
            db.session.commit()

        # Iniciar sesión en Flask (con Flask-Login)
        login_user(user)

        return jsonify({'success': True, 'message': 'Login successful!'})

    except ValueError:
        # Token inválido
        return jsonify({'success': False, 'message': 'Invalid token!'}), 401
