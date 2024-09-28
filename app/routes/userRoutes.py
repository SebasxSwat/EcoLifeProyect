from flask import Blueprint, request, jsonify
from app.models.user import User, db  

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

@bp.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [
        {
            'id': user.id,
            'name': f'{user.name} {user.lastname}',
            'email': user.email,
            'role': 'Administrador' if user.role == 'admin' else 'Usuario',
            'ecoScore': user.eco_score
        }
        for user in users
    ]
    return jsonify(user_list)


@bp.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Usuario eliminado correctamente'}), 200
    return jsonify({'message': 'Usuario no encontrado'}), 404
