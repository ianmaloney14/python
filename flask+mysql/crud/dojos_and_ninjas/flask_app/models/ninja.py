from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Ninja:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.dojo_id = db_data['dojo_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojos = []
# CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at, updated_at ) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"""
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
# READ
    @classmethod
    def show_ninja(cls, data):
        query = """SELECT * FROM ninjas
        """
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        objects = []
        for i in results:
            objects.append(cls(i))
        return objects
#STATIC METHODS 
    @staticmethod
    def validate_ninja(ninja):
        is_valid = True
        if len(ninja['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(ninja['last_name']) < 2:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if int(ninja['age']) <= 18:
            flash("You must be 18 years or older.")
            is_valid = False
        if ninja['dojo_id'] == None:
            flash("There is no Dojo.")
        return is_valid