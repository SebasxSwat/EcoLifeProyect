from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from werkzeug.security import check_password_hash
import jwt
import datetime

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not all(key in data for key in ('username', 'email', 'password')):
        return jsonify({"message": "Faltan campos requeridos"}), 400

    username = data['username']
    email = data['email']
    password = data['password']
    
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "El nombre de usuario ya está registrado"}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "El correo electrónico ya está registrado"}), 400
    

    user = User(username=username, email=email, password=password)
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
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, 'fabian_es_gay', algorithm='HS256')

    return jsonify({
        'access_token': token,
        'message': 'Inicio de sesión exitoso'
    }), 200
