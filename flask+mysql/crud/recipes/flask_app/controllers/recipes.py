from flask import Flask, render_template, redirect, session, request, flash, get_flashed_messages
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes')
def all_recipes():
    data = {
        "user_id": session['user_id']
    }
    return render_template('recipes.html', user = User.get_user(data), recipes = Recipe.show_all_recipes())

@app.route('/recipes/<int:recipe_id>')
def view_recipe(recipe_id):
    data = {
    "user_id": session['user_id']
    }
    recipe_data = {
        "recipe_id": recipe_id
    }
    return render_template('view_recipe.html', user = User.get_user(data), recipe = Recipe.view_recipe(recipe_data))

# CREATE ROUTES
@app.route('/recipes/new')
def render_new_recipe():
    data = {
        "user_id": session['user_id']
    }
    return render_template('add_recipe.html', user = User.get_user(data))

@app.route('/recipes/new/create', methods=['POST'])
def add_recipe():
    data = {
        "user_id": session['user_id'],
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "cook_time": request.form['cook_time'],
        "created_at": request.form['created_at']
    }
    
    Recipe.create_recipe(data)
    return redirect('/recipes')

# EDIT ROUTES
@app.route('/recipes/edit/<int:recipe_id>')
def show_edit_recipe(recipe_id):
    data = {
        "user_id": session['user_id'],
    }
    recipe_data = {
        "recipe_id": recipe_id
    }
    return render_template('edit_recipe.html', user = User.get_user(data), recipe = Recipe.view_recipe(recipe_data))

@app.route('/recipes/edit/<int:recipe_id>/apply', methods=['POST'])
def edit_recipe(recipe_id):
    data = {
        "recipe_id": recipe_id,
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "cook_time" : request.form["cook_time"],
        "created_at": request.form["created_at"]
    }
    Recipe.edit_recipe(data)
    return redirect('/recipes')

# DELETE ROUTES
@app.route('/delete/recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    Recipe.delete_recipe_by_id(data)
    return redirect('/recipes')

