#IMPORTS
from flask import Flask, render_template, session, redirect, request
import random
#INITIALIZATION
app = Flask(__name__)
app.secret_key = "suspicious key"

#ROUTES
@app.route('/')
def index():
    if not "guess" in session:
        session['guess'] = 0
    if not "num" in session:
        session['num'] = random.randint(1, 100)
    return render_template('index.html', num = int(session['num']), guess = int(session['guess']))

@app.route('/guess', methods=["POST"])
def process_guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/restart')
def restart():
    session.clear()
    return redirect('/')


#RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)
