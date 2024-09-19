from flask import Blueprint, request, jsonify
from app import db
from app.models.challenge import Challenge

bp = Blueprint('challenges', __name__, url_prefix='/challenges')

@bp.route('/create', methods=['POST'])
def create_challenge():
    data = request.get_json()

    new_challenge = Challenge(
        name=data['name'],
        description=data['description'],
        points=data['points'],
        carbon_reduction=data['carbon_reduction'],
        challenge_type=data['challenge_type']
    )

    db.session.add(new_challenge)
    db.session.commit()

    return jsonify(new_challenge.to_json()), 201

@bp.route('/all', methods=['GET'])
def get_all_challenges():

    challenges = Challenge.query.all()
    return jsonify([challenge.to_json() for challenge in challenges]), 200

@bp.route('/get-one/<int:id>', methods=['GET'])
def get_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    return jsonify(challenge.to_json()), 200

@bp.route('/put/<int:id>', methods=['PUT'])
def update_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    data = request.get_json()

    challenge.name = data.get('name', challenge.name)
    challenge.description = data.get('description', challenge.description)
    challenge.points = data.get('points', challenge.points)
    challenge.carbon_reduction = data.get('carbon_reduction', challenge.carbon_reduction)
    challenge.challenge_type = data.get('challenge_type', challenge.challenge_type)

    db.session.commit()

    return jsonify(challenge.to_json()), 200

@bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    db.session.delete(challenge)
    db.session.commit()

    return jsonify({"message": "Challenge deleted successfully"}), 200

sample_challenges = [
    {
        "name": "Lunes sin carne",
        "description": "Hazte vegetariano durante un día completo para reducir tu huella de carbono.",
        "points": 50,
        "carbon_reduction": 0.251,
        "challenge_type": "Diet"
    },
    {
        "name": "En bici al trabajo",
        "description": "Utilice una bicicleta para sus desplazamientos diarios en lugar de un auto o moto.",
        "points": 75,
        "carbon_reduction": 0.953,
        "challenge_type": "Transportation"
    },
    {
        "name": "Dia cero residuos",
        "description": "Intenta no producir residuos durante todo un día.",
        "points": 100,
        "carbon_reduction": 0.854,
        "challenge_type": "Lifestyle"
    },
    {
        "name": "Planta un arbol",
        "description": "Planta un arbol en tu comunidad.",
        "points": 150,
        "carbon_reduction": 0.999,
        "challenge_type": "Nature"
    },
    {
        "name": "Menos energia",
        "description": "Carga tus dispositivos electronicos una vez al dia.",
        "points": 125,
        "carbon_reduction": 1.028,
        "challenge_type": "Energy"
    }
]

@bp.route('/init', methods=['POST'])
def init_challenges():
    for challenge_data in sample_challenges:
        challenge = Challenge(**challenge_data)
        db.session.add(challenge)
    
    db.session.commit()
    return jsonify({"message": "Sample challenges initialized successfully"}), 201


