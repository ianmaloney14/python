from flask_app import app
from flask import render_template, redirect, request, session, get_flashed_messages
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninja():
    return render_template('ninjas.html', dojos = Dojo.get_dojos())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    if not Ninja.validate_ninja(request.form):
        return redirect('/ninjas')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/ninjas')
