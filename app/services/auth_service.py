from flask_jwt_extended import create_access_token
from flask import jsonify
from app.services.user_service import get_user
import bcrypt

def login(data):
    username = data.get('username')
    password = data.get('password')

    user = get_user('username', username)

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        access_token = create_access_token(identity=username)
        return jsonify(
            statusCode=200,
            data={
                "token": access_token,
                "user": user.serialize()
            }
        ), 200
    else:
        return jsonify(
            statusCode=401,
            error='Invalid username or password'
        ), 401
