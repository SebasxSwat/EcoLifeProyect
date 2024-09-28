from flask import Blueprint, request, jsonify
from app.models.user import User, db  
import jwt

bp = Blueprint('user', __name__)

@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "lastname": user.lastname,
        "username": user.username,
        "email": user.email,
        "phone": user.phone,
        "eco_score": user.eco_score,
        "trees_planted": user.trees_planted,
        "waste_recycled": user.waste_recycled,
        "water_saved": user.water_saved
    }), 200

@bp.route('/user/<int:id>', methods=['PUT'])
def update_user(id):

    data = request.json  
    user = User.query.get(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if 'name' in data:
        user.name = data['name']
    if 'lastname' in data:
        user.lastname = data['lastname']
    if 'email' in data:
        user.email = data['email']
    if 'phone' in data:
        user.phone = data['phone']

    try:
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@bp.route('/avatar', methods=['PUT'])
def assign_avatar():
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

    avatar = data.get('avatar')
    if not avatar:
        return jsonify({"error": "No avatar provided"}), 400

    allowed_avatars = [
        "/avatars/tree.png",
        "/avatars/leaf.png",
        "/avatars/flower.png",
        "/avatars/recycle.png",
        "/avatars/water-drop.png",
        "/avatars/sun.png",
        "/avatars/planet.png",  
        "/avatars/earth.png",   
        "/avatars/butterfly.png" 
    ]

    if avatar not in allowed_avatars:
        return jsonify({"error": "Invalid avatar selected"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    user.avatar = avatar
    db.session.commit()

    return jsonify({"message": "Avatar updated successfully", "avatar": user.avatar}), 200
