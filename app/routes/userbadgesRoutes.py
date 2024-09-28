from flask import Blueprint, request, jsonify
from app import db
import jwt
from app.models import Badge, UserBadge

bp = Blueprint('badges', __name__, url_prefix='/badges')


@bp.route('/create', methods=['POST'])
def create_badge():

    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    required_challenges = data.get('required_challenges')
    eco_points_required = data.get('eco_points_required', 0)
    trees_planted_required = data.get('trees_planted_required', 0)
    water_saved_required = data.get('water_saved_required', 0)
    waste_recycled_required = data.get('waste_recycled_required', 0)


    existing_badge = Badge.query.filter_by(name=name).first()
    if existing_badge:
        return jsonify({"message": "El badge ya existe"}), 400

    new_badge = Badge(
        name=name,
        description=description,
        required_challenges=required_challenges,
        eco_points_required=eco_points_required,
        trees_planted_required=trees_planted_required,
        water_saved_required=water_saved_required,
        waste_recycled_required=waste_recycled_required
    )

    db.session.add(new_badge)
    db.session.commit()

    return jsonify({"message": "Badge creado exitosamente"}), 201

@bp.route('/assign', methods=['POST'])
def assign_badge():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Token faltante"}), 401

    try:
        token = auth_header.split(" ")[1]  
    except IndexError:
        return jsonify({"message": "Formato del token incorrecto"}), 401

    try:
        decoded_token = jwt.decode(token, 'ecolifepassword', algorithms=['HS256'])
        user_id = decoded_token.get('id')

        if not user_id:
            return jsonify({"message": "Campo 'id' no encontrado en el token"}), 400

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "El token ha expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Token inválido"}), 401

    badge_id = request.json.get('badge_id')
    badge = Badge.query.get(badge_id)

    if not badge:
        return jsonify({"message": "Badge no encontrado"}), 404

    existing_user_badge = UserBadge.query.filter_by(user_id=user_id, badge_id=badge_id).first()
    if existing_user_badge:
        return jsonify({"message": "El badge ya ha sido asignado a este usuario"}), 400

    new_user_badge = UserBadge(user_id=user_id, badge_id=badge_id)
    db.session.add(new_user_badge)
    db.session.commit()

    return jsonify({"message": "Badge asignado exitosamente"}), 201

@bp.route('/all/<int:user_id>', methods=['GET'])
def get_user_badges(user_id):

    all_badges = Badge.query.all()
    
    unlocked_badges = UserBadge.query.filter_by(user_id=user_id).all()
    unlocked_badge_ids = {badge.badge_id for badge in unlocked_badges}

    unlocked = []
    locked = []

    for badge in all_badges:
        if badge.id in unlocked_badge_ids:
            unlocked.append(badge.to_json())  
        else:
            locked.append(badge.to_json())

    return jsonify({
        "unlocked": unlocked,
        "locked": locked
    }), 200



    {
        "name": "Héroe en inicio",
        "description": "Premio por completar 3 desafíos ecológicos",
        "required_challenges": 3,
        "eco_points_required": 650,
        "trees_planted_required": 2,
        "water_saved_required": 15,
        "waste_recycled_required": 2
    },
    {
        "name": "Eco Aventurero",
        "description": "Premio por completar 5 desafíos ecológicos",
        "required_challenges": 5,
        "eco_points_required": 850,
        "trees_planted_required": 3,
        "water_saved_required": 40,
        "waste_recycled_required": 12
    },
    {
        "name": "Guardabosques",
        "description": "Premio por plantar 7 árboles",
        "required_challenges": 8,
        "eco_points_required": 920,
        "trees_planted_required": 7,
        "water_saved_required": 80,
        "waste_recycled_required": 16
    },
    {
        "name": "Salvador del Agua",
        "description": "Premio por ahorrar 2000 litros de agua",
        "required_challenges": 7,
        "eco_points_required": 450,
        "trees_planted_required": 3,
        "water_saved_required": 2000,
        "waste_recycled_required": 15
    },
    {
        "name": "Reciclador Experto",
        "description": "Premio por reciclar 50 kg de residuos",
        "required_challenges": 10,
        "eco_points_required": 750,
        "trees_planted_required": 5,
        "water_saved_required": 1500,
        "waste_recycled_required": 50
    },
    {
        "name": "Héroe del Planeta",
        "description": "Premio por completar 40 desafíos ecológicos",
        "required_challenges": 40,
        "eco_points_required": 1000,
        "trees_planted_required": 100,
        "water_saved_required": 3000,
        "waste_recycled_required": 40
    }





