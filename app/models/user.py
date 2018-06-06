"""This module defines a user class and methods associated to it"""
from flask_bcrypt import Bcrypt
import jwt

from datetime import datetime, timedelta
import psycopg2
class User:
    table_title = 'users'

    def __init__(self, _id, username,name, password, isAdmin=False):
        self.id = _id
        self.username = username
        self.name = name
        self.password = Bcrypt().generate_password_hash(password).decode()
        self.isAdmin = isAdmin
    
    # @classmethod
    # def password_is_valid(self, password):
    #     """
    #     Checks the password against it's hash to validates the user's password
    #     """
    #     return Bcrypt().check_password_hash(self.password, password)

    @classmethod
    def find_by_username(cls, username):
        connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.table_title)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    # @classmethod
    # def find_by_id(cls, _id):
    #     connection = psycopg2.connect("dbname='tracker_api' user='postgres' host='localhost' password='15december' port ='5432'")
    #     cursor = connection.cursor()

    #     query = "SELECT * FROM {table} WHERE id=?".format(table=cls.table_title)
    #     result = cursor.execute(query, (_id,))
    #     row = result.fetchone()
    #     if row:
    #         user = cls(*row)
    #     else:
    #         user = None

    #     connection.close()
    #     return user
# user =User(1,"mubarak","ruganda","password")
# print(user.find_by_id(1))


    