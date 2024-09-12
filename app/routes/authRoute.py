from flask import Blueprint, request, jsonify
from app import db
from app.models import User  

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()  

    if not all(key in data for key in ('username', 'email', 'password')):
        return jsonify({"message": "Faltan campos requeridos"}), 400

    username = data['username']
    email = data['email']
    password = data['password']
    
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "El correo electrónico ya está registrado"}), 400

    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registro exitoso"}), 201
