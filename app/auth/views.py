
""" This module contains all the view functions for the auth blue print"""
from flask import Flask, jsonify, request
import jwt 
from . import auth
import psycopg2
from ..models.user import User
from datetime import datetime, timedelta

@auth.route("/register/",methods=['POST'])
def sign_up():
    data = request.get_json()
    print(data)
    # if User.find_by_username(data['username']):
    #     return {"message": "User with that username already exists."}, 400

    connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, username, password) VALUES( %s, %s, %s)",
                (data['name'],data['username'], data['password'])) 

    connection.commit()
    connection.close()

    return jsonify({"message": "User created successfully."}), 201

@auth.route('/login/', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400
    data =request.get_json()
    if User.find_by_username(data['username']):
        token = jwt.encode({'username' : data['username'], 'exp' : datetime.utcnow() 
                            + timedelta(minutes=60)}, 'donttouch')
    
        return jsonify({'token' : token.decode('UTF-8')})