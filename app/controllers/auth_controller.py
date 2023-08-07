from app import app
from flask import Blueprint, jsonify, request
from app.services.auth_service import login
from app.schemas.auth_schema import AuthSchema

app = Blueprint('auth_app', __name__)

@app.route('/login', methods=['POST'])
def auth():
    data = request.get_json()

    try:
        data = AuthSchema().load(data)
    except Exception as e:
        return jsonify(
            statusCode=400,
            error='Validation error: {}'.format(str(e))
        ), 400
    
    return login(data)
