# app/auth.py

from flask import jsonify, request
from flask_jwt_extended import create_access_token

from app import app, bcrypt
from app.models import User

# Authentication

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input data
    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Missing username or password'}), 400

    # Validate credentials against the database
    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        # Generate JWT token
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
