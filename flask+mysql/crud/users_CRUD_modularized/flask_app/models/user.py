from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
# CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (nmae, created_at, updated_at)
        VALUES ( %(name)s, NOW(), NOW());"""
        return connectToMySQL('user_schema').query_db(query, data)
# READ
    @classmethod
    def get_user(cls):
        query = """SELECT * FROM users"""
        results = connectToMySQL('user_schema').query_db(query)
        objects = []
        for i in results: 
            objects.append(cls(i))
        return objects
# UPDATE
# DELETE
# VALIDATE
    @staticmethod
    def validate_user_name(user):
        is_valid = True
        if len(user['name']) < 3:
            flash("Name must be more than 3 characters.")
            is_valid = False
        return is_valid
    @staticmethod
    def validate(user):
        is_valid = True
        query = """SELECT * FROM user WHERE email = %(email)s;"""
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            is_valid = False