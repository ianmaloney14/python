from tokenize import cookie_re
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from flask import flash

class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []
# CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name, created_at, updated_at) 
        VALUES ( %(name)s, NOW(), NOW());"""
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
# READ
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id 
        WHERE dojos.id = %(id)s;"""
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojo_id": row_from_db["dojo_id"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data) )
        return dojo
    @classmethod
    def get_dojos(cls):
        query = """SELECT * FROM dojos"""
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        objects = []
        for i in results:
            objects.append(cls(i))
        return objects
# VALIDATE
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be more than 3 characters.")
            is_valid = False
        return is_valid
            