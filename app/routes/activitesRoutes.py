from flask import Blueprint, request, jsonify
import jwt
from datetime import datetime
from app import db
from app.models import User, Challenge, Activity 

bp = Blueprint('activities', __name__, url_prefix='/activities')

@bp.route('/create', methods=['POST'])
def create_activity():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Token faltante"}), 401

    try:
        token = auth_header.split(" ")[1]  
    except IndexError:
        return jsonify({"message": "Formato del token incorrecto"}), 401

    try:
        decoded_token = jwt.decode(token, 'ecolifepassword', algorithms=['HS256'])
        user_id = decoded_token.get('id')

        if not user_id:
            return jsonify({"message": "Campo 'id' no encontrado en el token"}), 400

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "El token ha expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Token inválido"}), 401

    data = request.get_json()
    if not data or 'challenge_id' not in data:
        return jsonify({"message": "Datos no proporcionados o challenge_id faltante"}), 400

    challenge_id = data['challenge_id']
    challenge = Challenge.query.get(challenge_id)
    
    if not challenge:
        return jsonify({"message": "Desafío no encontrado"}), 404

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    activity = Activity(
        user_id=user_id,
        challenge_id=challenge_id,
        date_completed=datetime.utcnow()  
    )

    try:
        db.session.add(activity)
        
        db.session.commit()

        return jsonify({"message": "Actividad creada y eco score actualizado", "eco_score": user.eco_score}), 201
    except Exception as e:
        db.session.rollback()  
        return jsonify({"message": f"Error al crear la actividad: {str(e)}"}), 500


@bp.route('/all/<int:user_id>', methods=['GET'])
def get_activities(user_id):
    activities = Activity.query.filter_by(user_id=user_id).join(Challenge).all()
    return jsonify([activity.to_json() for activity in activities])

