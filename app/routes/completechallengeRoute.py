from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity
from app import db
from app.models.challenge import Challenge
from app.models.user import User
from app.models.completedchallenge import CompletedChallenge

bp = Blueprint('complete_challenge', __name__, url_prefix='/challenges-complete')


@bp.route('/<int:id>/complete', methods=['POST'])
def complete_challenge(id):
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    challenge = Challenge.query.get_or_404(id)

    if CompletedChallenge.query.filter_by(user_id=user_id, id=id).first():
        return jsonify({"message": "Este desafío ya ha sido completado"}), 400

    completed_challenge = CompletedChallenge(user_id=user_id, id=id)
    db.session.add(completed_challenge)

    user.eco_score += challenge.points
    user.carbon_footprint -= challenge.carbon_reduction

    db.session.commit()

    return jsonify({
        "message": "Desafío completado con éxito",
        "eco_score": user.eco_score,
        "carbon_footprint": user.carbon_footprint
    }), 200

@bp.route('/user', methods=['GET'])
def get_user_challenges():
    user_id = get_jwt_identity()
    
    completed_challenges = CompletedChallenge.query.filter_by(user_id=user_id).all()
    completed_ids = [cc.challenge_id for cc in completed_challenges]
    
    all_challenges = Challenge.query.all()
    
    completed = [c.to_json() for c in all_challenges if c.id in completed_ids]
    available = [c.to_json() for c in all_challenges if c.id not in completed_ids]

    return jsonify({
        "completed": completed,
        "available": available
    }), 200