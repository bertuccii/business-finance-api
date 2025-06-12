from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flasgger import swag_from
import os
from app.services import auth_service
DOCS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'docs'))


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
@swag_from(os.path.join(DOCS_PATH, 'auth', 'register.yml'))
def register():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'msg': 'Missing required fields'}), 400

    response, status = auth_service.register_user(
        data['username'], data['email'], data['password']
    )
    return jsonify(response), status

@auth_bp.route('/login', methods=['POST'])
@swag_from(os.path.join(DOCS_PATH, 'auth', 'login.yml'))
def login():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'msg': 'Missing username or password'}), 400

    user = User.query.filter_by(username=data['username']).first()

    response, status = auth_service.authenticate_user(
        data['username'], data['password']
    )

    return jsonify(response), status
