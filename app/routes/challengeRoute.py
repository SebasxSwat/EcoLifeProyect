from flask import Blueprint, request, jsonify
from app import db
from app.models.challenge import Challenge
from app.models.user import User
from app.models.carbonfootprint import CarbonFootprint
from app.models.completechallenge import CompletedChallenge

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
    user_id = data.get('user_id')

    if not challenge_id or not user_id:
        return jsonify({'error': 'El ID del desafío y el ID del usuario son obligatorios'}), 400

    user = User.query.get_or_404(user_id)
    challenge = Challenge.query.get_or_404(challenge_id)

    completed = CompletedChallenge.query.filter_by(user_id=user_id, challenge_id=challenge_id).first()
    if completed:
        return jsonify({'error': 'Este desafío ya ha sido completado'}), 400

    new_completed = CompletedChallenge(user_id=user_id, challenge_id=challenge_id)

    user.eco_score += challenge.points

    carbon_footprint = CarbonFootprint.query.filter_by(user_id=user_id).first()
    if carbon_footprint:
        carbon_footprint.value -= challenge.carbon_reduction
    else:
        return jsonify({'error': 'No se encontró la huella de carbono para este usuario'}), 404

    if challenge.challenge_type == 'TreeDeciduous':
        user.trees_planted += 1  
    elif challenge.challenge_type == 'Droplet':
        user.water_saved += 32.6  
    elif challenge.challenge_type == 'Trash2':
        user.waste_recycled += 1.5  
    elif challenge.challenge_type == 'Flower2':
        user.water_saved += 1.7  
    elif challenge.challenge_type == 'Recycle':
        user.waste_recycled += 0.7  
    elif challenge.challenge_type == 'ShowerHead':
        user.waste_recycled += 8.7  


    db.session.add(new_completed)
    db.session.commit()

    return jsonify({
        "message": "Desafío completado exitosamente",
        "eco_score": user.eco_score,
        "trees_planted": user.trees_planted,
        "water_saved": user.water_saved,
        "waste_recycled": user.waste_recycled
    }), 200

@bp.route('/all', methods=['GET'])
def get_all_challenges():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Se requiere el ID del usuario"}), 400

    user = User.query.get_or_404(user_id)
    
    completed_challenge_ids = [c.challenge_id for c in user.completed_challenges]
    
    available_challenges = Challenge.query.filter(~Challenge.id.in_(completed_challenge_ids)).all()

    return jsonify([challenge.to_json() for challenge in available_challenges]), 200



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
        "name": "Dia de Bici",
        "description": "Utilice una bicicleta para sus desplazamientos diarios en lugar de una moto o auto.",
        "points": 75,
        "carbon_reduction": 0.097,
        "challenge_type": "Transportation"
    },
    {
        "name": "Dia cero residuos",
        "description": "Intenta no producir residuos durante todo un día.",
        "points": 100,
        "carbon_reduction": 0.096,
        "challenge_type": "Lifestyle"
    },
    {
        "name": "Planta un arbol",
        "description": "Planta un arbol en tu comunidad.",
        "points": 150,
        "carbon_reduction": 0.082,
        "challenge_type": "Nature"
    },
    {
        "name": "Menos energia",
        "description": "Carga tus dispositivos electronicos una vez al dia.",
        "points": 125,
        "carbon_reduction": 0.045,
        "challenge_type": "Energy"
    },
    {
        "name": "Menos agua",
        "description": "Minetras te cepillas y enjabonas en la duhca, manten la llave cerrada.",
        "points": 125,
        "carbon_reduction": 0.045,
        "challenge_type": "Water"
    },
    {
        "name": "Riego eficiente",
        "description": "Riega tus plantas en las primeras horas de la mañana o al atardecer para evitar la evaporación.",
        "points": 110,
        "carbon_reduction": 0.016,
        "challenge_type": "Irrigation"
    },
    {
        "name": "Duchas cortas",
        "description": "Reduce el tiempo de tus duchas a 5 minutos o menos.",
        "points": 125,
        "carbon_reduction": 0.026,
        "challenge_type": "Showers"
    },
    {
        "name": "Reciclaje de papel",
        "description": "Recicla papel y cartón en lugar de tirarlo a la basura.",
        "points": 90,
        "carbon_reduction": 0.097,
        "challenge_type": "Recycle"
    }
]

@bp.route('/init', methods=['POST'])
def init_challenges():
    for challenge_data in sample_challenges:
        challenge = Challenge(**challenge_data)
        db.session.add(challenge)
    
    db.session.commit()
    return jsonify({"message": "Sample challenges initialized successfully"}), 201


@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_challenges(user_id):
    user = User.query.get_or_404(user_id)
    
    completed_challenges = db.session.query(Challenge).join(CompletedChallenge).filter(
        CompletedChallenge.user_id == user_id
    ).all()

    completed_challenge_ids = [challenge.id for challenge in completed_challenges]
    available_challenges = Challenge.query.filter(
        ~Challenge.id.in_(completed_challenge_ids)
    ).all()

    return jsonify({
        'completed_challenges': [challenge.to_json() for challenge in completed_challenges],
        'available_challenges': [challenge.to_json() for challenge in available_challenges]
    }), 200
