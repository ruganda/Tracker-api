from functools import wraps
import jwt
from flask import jsonify, request
from . import admin
from ..models.requests import Request
import psycopg2
from ..models.user import User
from flask_jwt_extended import  jwt_required, get_jwt_identity
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_claims
)

@admin.route("/requests/")
@jwt_required
def fetch_admin_requests():
    """ Admin to view all the requests on the application"""
    requests = User.admin_get()
    return jsonify(requests), 200

@admin.route("/requests/<int:id>/approve", methods=['PUT'])
@jwt_required
def approve_disapprove_status(id):
    """Allow the Admin to approve/disaprove a request"""
    data = request.get_json()
    a_request = Request.find_by_id(data['id'])
    print(a_request)
    updated_request = { 'status': data['status']}
    r_id =a_request[0]
    if a_request:
        try:
            User.approve_disaprove_status(r_id, updated_request)
        except:
            return jsonify({"message": "An error occurred updating the item."}), 403
    return jsonify({"Message":"Request  status updated succesfully"}), 200


@admin.route("/requests/<int:id>/resolve",methods=['PUT'])
@jwt_required
def resolve_status(id):
    data = request.get_json()
    a_request = Request.find_by_id(data['id'])
    updated_request = { 'status': data['status']}
    r_id =a_request[0]
    if a_request:
        try:
            User.approve_disaprove_status(r_id, updated_request)
        except:
            return jsonify({"message": "An error occurred updating the item."}), 403
    return jsonify({"Message":"Request  status updated succesfully"}), 200
