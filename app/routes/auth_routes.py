from flask import Blueprint, request, jsonify
from app.models.user import Users  # Importa tu modelo de usuario
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/', methods=['POST'])
def register():
    
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400

    user = Users(username=username, email=email)
    user.set_password(password)
    
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = Users.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful', 'user': {'id': user.id, 'username': user.username}}), 200