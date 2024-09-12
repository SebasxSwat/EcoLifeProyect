from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

bp = Blueprint('User', __name__, url_prefix='/user')

@bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_json() for user in users ])

@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

