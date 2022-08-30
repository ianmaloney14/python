from flask_app import app
from flask import render_template, redirect, request, session, get_flashed_messages
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.get_dojos())

@app.route('/process_dojo', methods=['POST'])
def process_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect('/dojos')
    dojo = {
        "name": request.form['name']
    }
    Dojo.save(dojo)
    return redirect('/dojos')

@app.route('/dojo_show/<int:dojo_id>')
def show_dojo(dojo_id):
    data = { 
        "id": dojo_id
    }
    return render_template('dojo_show.html', dojo = Dojo.get_dojo_with_ninjas(data))