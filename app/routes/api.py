from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import Users

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/some-endpoint', methods=['GET'])
@jwt_required()
def some_endpoint():
    try:
        current_user_id = get_jwt_identity()
        user = Users.query.get(current_user_id)
        
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404
        
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "eco_score": user.eco_score,
            "carbon_footprint": user.carbon_footprint
        }
        
        return jsonify({
            "message": "Datos obtenidos exitosamente",
            "user": user_data
        }), 200
    except Exception as e:
        print(f"Error in some_endpoint: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

