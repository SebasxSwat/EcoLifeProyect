from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from app.models.user import Users

bp = Blueprint('login', __name__)

jwt = JWTManager()

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Verifica si el usuario existe y la contraseña es correcta
    user = Users.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={
            'user_id': user.id,
            'is_admin': user.is_admin
        })
        return jsonify({
            'access_token': access_token,
            'is_admin': user.is_admin
        }), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
