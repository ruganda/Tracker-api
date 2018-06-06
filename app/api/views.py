from functools import wraps
import jwt
from flask import jsonify, request
from . import api
from ..models.requests import Request
import psycopg2
from ..models.user import User

def auth_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, 'donttouch')
            current_user = User.find_by_username(data['username'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
@api.route("/requests/<int:id>")
# @jwt_required
def get(id):
    request = Request.find_by_id(id)
    if request:
        return jsonify(request), 200
    return {'message': 'Request not found'}, 404

@api.route("/requests")
def post(self):
    data = request.get_json()
    
    if Request.find_by_id(data["id"]):
        return {'message': "A request with id '{}' already exists.".format(id)}

    response = {'item': data['item'],'type': data['type'], 'description': data['description']}

    try:
        Request.insert(response)
    except:
        return {"message": "An error occurred inserting the request."}

    return response  

@api.route("/requests/<int:id>")
# @jwt_required
def put(id):
    data = request.get_json()
    a_request = Request.find_by_id(data['id'])
    updated_request = {'item': data['item'], 'typ': data['typ'], 'description': data['description']}
    if a_request :
        try:
            Request.update(updated_request)
        except:
            return {"message": "An error occurred updating the item."}
    return updated_request
@api.route("/requests/")
# @jwt_required
def get_all():
    requests = Request.fetch_all()
    
    return {'requests': requests}