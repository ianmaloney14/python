from flask import Flask, render_template, redirect, session, request, flash, get_flashed_messages
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    data = {
        "user_id": session['user_id']
    }
    return render_template('index.html', user = User.get_user(data))

@app.route('/register/user', methods=['POST'])
def register():
    #check to see if users inputs are valid
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save_user(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect('/recipes')

@app.route('/login', methods=['POST'])
def login():
    # see if the email provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect('/recipes')

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    return redirect('/')