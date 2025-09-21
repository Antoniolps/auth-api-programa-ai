from flask import Blueprint, request, jsonify
from ..models import User
from ..auth.service import create_user, authenticate
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['POST'])
def register():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "email e password são obrigatórios"}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email já cadastrado"}), 409
    
    user = create_user(email, password)

    return jsonify({"id": user.id, "email": user.email}), 201
