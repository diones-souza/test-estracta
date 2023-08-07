from app import app
from app.services.user_service import *
from app.schemas.user_schema import *
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

app = Blueprint('user_app', __name__)

@app.route('/users', methods=['GET'])
def get_all():
    users = get_users()

    return jsonify(
            statusCode=200,
            data=[user.serialize() for user in users]
        ), 200

@app.route('/users', methods=['POST'])
def create():
    data = request.get_json()

    try:
        data = CreateSchema().load(data)
    except Exception as e:
        return jsonify(
            statusCode=400,
            error='Validation error: {}'.format(str(e))
        ), 400

    user = create_user(data)

    return jsonify(
            statusCode=201,
            data=user.serialize()
        ), 201

@app.route('/users/<int:id>', methods=['GET'])
def get_item(id):
    user = get_user('id', id)

    if not user:
        return jsonify(
            statusCode=404,
            error='User not found'
        ), 404
    
    return jsonify(
            statusCode=200,
            data=user.serialize()
        ), 200
    
@app.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    data = request.get_json()

    try:
        data = UpdateSchema().load(data)
    except Exception as e:
        return jsonify(
            statusCode=400,
            error='Validation error: {}'.format(str(e))
        ), 400
    
    user = get_user('id', id)

    if not user:
        return jsonify(
            statusCode=404,
            error='User not found'
        ), 404

    update_user(user, data)

    return jsonify(
            statusCode=200,
            data=user.serialize()
        ), 200

@app.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    user = get_user('id', id)

    if not user:
        return jsonify(
            statusCode=404,
            error='User not found'
        ), 404

    delete_user(user)

    return jsonify(
            statusCode=200,
            data=user.serialize()
        ), 200