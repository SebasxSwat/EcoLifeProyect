from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models.challenge import Challenge

# Crear un Blueprint para las rutas de desafíos
challenges_bp = Blueprint('challenges', __name__)

# Ruta para listar todos los desafíos y renderizar el template
@challenges_bp.route('/challenges', methods=['GET'])
def list_challenges():
    challenges = Challenge.query.all()
    return render_template('challenges.html', challenges=challenges)

# Ruta para obtener todos los desafíos en formato JSON
@challenges_bp.route('/api/challenges', methods=['GET'])
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
            'created_at': challenge.created_at.isoformat()
        })
    return jsonify(result)

# Ruta para crear un nuevo desafío
@challenges_bp.route('/api/challenges', methods=['POST'])
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
@challenges_bp.route('/api/challenges/<int:id>', methods=['GET'])
def get_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    return jsonify({
        'id': challenge.id,
        'title': challenge.title,
        'description': challenge.description,
        'goal': challenge.goal,
        'reward': challenge.reward,
        'icon': challenge.icon,
        'created_at': challenge.created_at.isoformat()
    })

# Ruta para actualizar un desafío existente
@challenges_bp.route('/api/challenges/<int:id>', methods=['PUT'])
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
@challenges_bp.route('/api/challenges/<int:id>', methods=['DELETE'])
def delete_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    db.session.delete(challenge)
    db.session.commit()
    return jsonify({'message': 'Challenge deleted successfully!'})
