"""This module defines a user class and methods associated to it"""
from flask_bcrypt import Bcrypt
import jwt
from .create_table import connection
from datetime import datetime, timedelta
import psycopg2
class User:
    table_title = 'users'

    def __init__(self,id, username,name, password, isAdmin=False):
        self.id = id
        self.username = username
        self.name = name
        self.password = password
        self.isAdmin = isAdmin
    
    
    
    @classmethod
    def fetch_by_username(cls, username):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()
          
        cursor.execute("SELECT * FROM users WHERE username = %(username)s", {'username': username})
        
        row = cursor.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        print(user)
        return user

    @classmethod
    def fetch_by_password(cls, password):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()
        
        
        cursor.execute("SELECT * FROM users WHERE password = %(password)s", {'password': password})
        
        row = cursor.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user    

    @classmethod
    def insert_data(cls, data):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()
       
        cursor.execute("INSERT INTO users (name, username, password, isAdmin) VALUES( %s, %s, %s,%s)",
            (data['name'], data['username'], data['password'],data['isAdmin']),) 
        connection.commit()
        connection.close()
    @classmethod
    def find_by_id(cls, _id):
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM users WHERE id = %s", [_id])
        
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    ###################################### Admin ####################
    @classmethod
    def admin_get(self):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM requests" )
        rows = cursor.fetchall()
        requests = []
        for row in rows:
            print(row)
            requests.append({'id':row[0], 'item': row[1], 'typ': row[2], 'description': row[3], 'status': row[4],"Requester":row[5] })
        connection.close()
        return requests
