from flask import Blueprint, request, jsonify
from app.models.carbonfootprint import CarbonFootprint
from app import db

bp = Blueprint('carbon_footprint', __name__, url_prefix='/carbon-footprint')

@bp.route('/save', methods=['POST'])
def save_carbon_footprint():
    data = request.get_json()
    
    if not data or 'value' not in data or 'user_id' not in data:
        return jsonify({"message": "User ID and carbon footprint value are required"}), 400

    value = data['value']
    user_id = data['user_id']

    try:
        new_footprint = CarbonFootprint(user_id=user_id, value=value)
        db.session.add(new_footprint)
        db.session.commit()
        return jsonify({
            "message": "Carbon footprint saved successfully",
            "id": new_footprint.id,
            "user_id": new_footprint.user_id,
            "value": new_footprint.value,
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "An error occurred while saving the carbon footprint"}), 500
