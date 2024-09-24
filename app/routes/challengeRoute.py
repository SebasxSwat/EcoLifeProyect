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

@bp.route('/complete', methods=['POST'])
def complete_challenge():
    data = request.get_json()
    challenge_id = data.get('challenge_id')

    if not challenge_id:
        return jsonify({"error": "El ID del desafío es obligatorio"}), 400

    challenge = Challenge.query.get_or_404(challenge_id)

    total_points = challenge.points
    total_carbon_reduction = challenge.carbon_reduction

    response = {
        "message": "Desafío completado exitosamente",
        "challenge": {
            "id": challenge.id,
            "name": challenge.name,
            "points": total_points,
            "carbon_reduction": total_carbon_reduction
        }
    }

    return jsonify(response), 200

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
        "carbon_reduction": 0.096,
        "challenge_type": "Diet"
    },
    {
        "name": "Dia de Bici",
        "description": "Utilice una bicicleta para sus desplazamientos diarios en lugar de una moto o auto.",
        "points": 75,
        "carbon_reduction": 0.107,
        "challenge_type": "Transportation"
    },
    {
        "name": "Dia cero residuos",
        "description": "Intenta no producir residuos durante todo un día.",
        "points": 100,
        "carbon_reduction": 0.116,
        "challenge_type": "Lifestyle"
    },
    {
        "name": "Planta un arbol",
        "description": "Planta un arbol en tu comunidad.",
        "points": 150,
        "carbon_reduction": 0.128,
        "challenge_type": "Nature"
    },
    {
        "name": "Menos energia",
        "description": "Carga tus dispositivos electronicos una vez al dia.",
        "points": 125,
        "carbon_reduction": 1.115,
        "challenge_type": "Energy"
    },
    {
        "name": "Menos agua",
        "description": "Minetras te cepillas y enjabonas en la duhca, manten la llave cerrada.",
        "points": 125,
        "carbon_reduction": 0.112,
        "challenge_type": "Watter"
    }
]

@bp.route('/init', methods=['POST'])
def init_challenges():
    for challenge_data in sample_challenges:
        challenge = Challenge(**challenge_data)
        db.session.add(challenge)
    
    db.session.commit()
    return jsonify({"message": "Sample challenges initialized successfully"}), 201


