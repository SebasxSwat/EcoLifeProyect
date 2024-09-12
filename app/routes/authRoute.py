from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db
from 

bp = Blueprint('auth', __name__)

@bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_json()), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": str(e.orig)}), 400

