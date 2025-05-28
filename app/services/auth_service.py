from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta

def register_user(username, email, password):
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return {'msg': 'User already exists'}, 400

    new_user = User(username=username, email=email)
    new_user.password_hash = generate_password_hash(password)

    db.session.add(new_user)
    db.session.commit()

    return {'msg': 'User created successfully'}, 201

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return {'msg': 'Invalid credentials'}, 401

    access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
    return {'access_token': access_token}, 200
