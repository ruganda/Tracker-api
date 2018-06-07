from functools import wraps
import jwt
from flask import jsonify, request
from . import api
from ..models.requests import Request
import psycopg2
from ..models.user import User
from flask_jwt_extended import  jwt_required, get_jwt_identity
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_claims
)



@api.route("/requests/<int:id>")
@jwt_required
def get(id):
    '''Gets a single request by id '''
    request = Request.find_by_id(id)
    if request:
        response ={'id':request[0],'item':request[1],'typ':request[2],
                    'description':request[3],'status':request[4]}
        return jsonify(response), 200
    return {'message': 'Request not found'}, 404

@api.route("/requests/", methods=['POST'])
@jwt_required
def post_requests():
    data = request.get_json()
    
    # if Request.find_by_id(data["id"]):
    #     return jsonify({'message': "A request with id '{}' already exists.".format(data['id'])})
    owner = get_jwt_identity()
    response = {'item': data['item'],'typ': data['typ'], 'description': data['description'],"status":data['status']}

    try:
        Request.insert(response, owner)
    except Exception as e:
        print(e)
        return jsonify({"message": "An error occurred inserting the request."})

    return jsonify({'message':'Request added successfully'}), 201

@api.route("/requests/<int:id>",methods=['PUT'])
# @jwt_required
def put(id):
    data = request.get_json()
    a_request = Request.find_by_id(data['id'])
    updated_request = {'item': data['item'], 'typ': data['typ'], 'description': data['description']}
    if a_request :
        try:
            Request.update(data['id'], updated_request)
        except:
            return jsonify({"message": "An error occurred updating the item."}), 403
    return jsonify({"Message":"Request updated succesfully"}), 200

@api.route("/requests/")
@jwt_required
def fetch_user_requests():

    current_user = get_jwt_identity()
    print(current_user)
    requests = Request.fetch_all(current_user)
    
    return jsonify(requests), 200