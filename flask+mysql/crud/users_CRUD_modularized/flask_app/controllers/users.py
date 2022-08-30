from flask_app import app
from flask import render_template, redirect, request, session, get_flashed_messages
from flask_app.models import User

@app.route('/')
def index():
    return redirect('/create')

@app.route('/create')
def user():
    return render_template('create.html')

@app.route('/process_user', methods=['POST'])
def process_user():
    if not User.validate_user(request.form):
        return redirect('/create')
    user = {
        "name": request.form['name']
    }
    User.save(user)
    return redirect('/create')

@app.route('/show_users/<int:user_id>')
def show_users(user_id):
    data = {
        "id": user_id
    }
    return render_template('read.html', user = User.get_user(data))

