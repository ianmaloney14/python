from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
#CREATE
    @classmethod
    def save_user(cls, data):
        query = """INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at )
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"""
        return connectToMySQL('login_registration').query_db(query, data)
#READ
    @classmethod
    def show_user(cls):
        query = """SELECT * FROM users"""
        results = connectToMySQL('login_registraion').query_db(query)
        objects = []
        for i in results:
            objects.append(cls(i))
        return objects

    @classmethod
    def get_by_email(cls, data):
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        result = connectToMySQL('login_registration').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

#VALIDATE
    @staticmethod
    def validate_email( user ):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!')
            is_valid = False
        return is_valid