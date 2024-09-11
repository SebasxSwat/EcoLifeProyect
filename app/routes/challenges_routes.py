from flask import Blueprint, request, jsonify
from app import db
from models import Challenge

challenges_bp = Blueprint('challenges', __name__)

# Ruta para obtener todos los desafíos
@challenges_bp.route('/challenges', methods=['GET'])
def get_challenges():
    challenges = Challenge.query.all()
    result = []
    for challenge in challenges:
        result.append({
            'id': challenge.id,
            'title': challenge.title,
            'description': challenge.description,
            'goal': challenge.goal,
            'reward': challenge.reward,
            'icon': challenge.icon,
            'created_at': challenge.created_at
        })
    return jsonify(result)

# Ruta para crear un nuevo desafío
@challenges_bp.route('/challenges', methods=['POST'])
def create_challenge():
    data = request.get_json()
    new_challenge = Challenge(
        title=data['title'],
        description=data['description'],
        goal=data['goal'],
        reward=data['reward'],
        icon=data.get('icon')
    )
    db.session.add(new_challenge)
    db.session.commit()
    return jsonify({'message': 'Challenge created successfully!'}), 201

# Ruta para obtener un desafío específico por ID
@challenges_bp.route('/challenges/<int:id>', methods=['GET'])
def get_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    return jsonify({
        'id': challenge.id,
        'title': challenge.title,
        'description': challenge.description,
        'goal': challenge.goal,
        'reward': challenge.reward,
        'icon': challenge.icon,
        'created_at': challenge.created_at
    })

# Ruta para actualizar un desafío
@challenges_bp.route('/challenges/<int:id>', methods=['PUT'])
def update_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    data = request.get_json()
    
    challenge.title = data.get('title', challenge.title)
    challenge.description = data.get('description', challenge.description)
    challenge.goal = data.get('goal', challenge.goal)
    challenge.reward = data.get('reward', challenge.reward)
    challenge.icon = data.get('icon', challenge.icon)

    db.session.commit()
    return jsonify({'message': 'Challenge updated successfully!'})

# Ruta para eliminar un desafío
@challenges_bp.route('/challenges/<int:id>', methods=['DELETE'])
def delete_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    db.session.delete(challenge)
    db.session.commit()
    return jsonify({'message': 'Challenge deleted successfully!'})
