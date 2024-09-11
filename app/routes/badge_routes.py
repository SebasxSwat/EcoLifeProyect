from flask import Blueprint, request, jsonify
from app import db
from app.models.badge import Badge
from app.models.userBadge import UserBadge
from app.models.user import Users

# Crear un Blueprint para las rutas de insignias
bp = Blueprint('badges', __name__)

# Ruta para crear una nueva insignia
@bp.route('/api/badges', methods=['POST'])
def create_badge():
    data = request.get_json()

    # Crear una nueva insignia
    new_badge = Badge(
        name=data['name'],
        description=data['description'],
        icon=data.get('icon')  # El icono es opcional
    )
    db.session.add(new_badge)
    db.session.commit()

    return jsonify({'message': 'Badge created successfully!'}), 201


# Ruta para asignar una insignia a un usuario
@bp.route('/api/users/<int:user_id>/badges/<int:badge_id>', methods=['POST'])
def assign_badge(user_id, badge_id):
    # Verificar si el usuario existe
    user = Users.query.get_or_404(user_id)
    
    # Verificar si la insignia existe
    badge = Badge.query.get_or_404(badge_id)

    # Crear la relación de UserBadge
    user_badge = UserBadge(user_id=user_id, badge_id=badge_id)

    db.session.add(user_badge)
    db.session.commit()

    return jsonify({'message': f'Badge {badge.name} assigned to user {user.username} successfully!'}), 201


# Ruta para obtener todas las insignias de un usuario
@bp.route('/api/users/<int:user_id>/badges', methods=['GET'])
def get_user_badges(user_id):
    user = Users.query.get_or_404(user_id)
    badges = user.badges.all()

    result = []
    for user_badge in badges:
        result.append({
            'id': user_badge.badge.id,
            'name': user_badge.badge.name,
            'description': user_badge.badge.description,
            'icon': user_badge.badge.icon,
            'earned_at': user_badge.earned_at.isoformat()
        })

    return jsonify(result)
