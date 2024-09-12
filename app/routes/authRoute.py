from flask import Blueprint, request, jsonify
from app import db
from app.models import User  

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')  
    eco_score = data.get('eco_score', 0)
    carbon_footprint = data.get('carbon_footprint', 0.0)

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'error': 'User already exists'}), 400

    new_user = User(
        username=username,
        email=email,
        password=password, 
        eco_score=eco_score,
        carbon_footprint=carbon_footprint
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'eco_score': new_user.eco_score,
        'carbon_footprint': new_user.carbon_footprint
    }), 201
