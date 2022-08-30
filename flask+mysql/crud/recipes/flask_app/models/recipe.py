from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash
from pprint import pprint
from flask_app.models.user import User

class Recipe:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.cook_time = db_data['cook_time']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user = None

# CREATE
    @classmethod
    def create_recipe(cls, data):
        query = """INSERT INTO recipes ( name, description, instructions, cook_time, created_at, updated_at, user_id ) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(cook_time)s, NOW(), NOW(), %(user_id)s);"""
        return connectToMySQL('recipes').query_db(query, data)
# READ
    @classmethod
    def show_all_recipes(cls):
        query = """SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"""
        results = connectToMySQL('recipes').query_db(query)
        objects = []
        for i in results:
            this_recipe = cls(i)
            user_data = {
                "id": i['users.id'],
                "first_name": i['first_name'],
                "last_name": i['last_name'],
                "email": None,
                "password": None,
                "created_at": i['users.created_at'],
                "updated_at": i['users.updated_at']
            }
            this_recipe.user = User(user_data)
            # pprint(i, sort_dicts = False, width = 1)
            objects.append(this_recipe)
        return objects
    @classmethod
    def view_recipe(cls, data):
        query = """SELECT * FROM recipes WHERE recipes.id = %(recipe_id)s;"""
        results = connectToMySQL('recipes').query_db(query, data)
        return cls(results[0])

# UPDATE
    @classmethod
    def edit_recipe(cls, data):
        query = """UPDATE recipes 
        SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, cook_time = %(cook_time)s, updated_at = NOW()
        WHERE recipes.id = %(recipe_id)s"""
        results = connectToMySQL('recipes').query_db(query, data)
        return results
# DELETE
    @classmethod
    def delete_recipe_by_id(cls, data):
        query = """DELETE FROM recipes WHERE recipes.id = %(recipe_id)s;"""
        results = connectToMySQL('recipes').query_db(query, data)
        return results
# VALIDATE
    @staticmethod
    def validate_recipe( recipe ):
        is_valid = True
        if len(recipe['description']) <= 3:
            flash('Description must not be blank')
            is_valid = False
        if len(recipe['instructions']) <= 3:
            flash('Instructions must not be blank')
            is_valid = False
        if len(recipe['name']) <= 3:
            flash('Name must be at least 3 characters')
            is_valid = False
        if recipe['created_at'] == 0:
            flash('Date must not be blank')
            is_valid = False
        if recipe['cook_time'] < 30:
            is_valid = False
        return is_valid
