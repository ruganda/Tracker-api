
""" This module contains all the view functions for the auth blue print"""
from flask import Flask, jsonify, request
from ..models.requests import Request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)
import jwt
from . import auth
import psycopg2
from ..models.user import User
from datetime import datetime, timedelta


@auth.route("/register/", methods=['POST'])
def sign_up():
    data = request.get_json()
    if data['name'] and data['username'] and data["password"] and data['isAdmin']:
        data["name"].strip() 
        data["username"].strip()
        if  str(data["username"]).isalpha():
            
            if User.fetch_by_username(data['username']):
                return jsonify({"message": "User with that username already exists."}), 400
            User.insert_data(data)
            return jsonify({"message": "User created successfully."}), 201
        return jsonify({"message": "Invalid input! The inputs should be aphabets"})    
    return "You need to fill all the fields"

@auth.route('/login/', methods=['POST'])
def login():
    """Logs in a registered user and gives a token in return"""
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400
    if User.fetch_by_username(username.strip())and User.fetch_by_password(password.strip()):
        access_token = create_access_token(identity=username)

        return jsonify({'token': access_token})
    return jsonify({"message": "UnAuthorized user"}), 401

###################################################################
