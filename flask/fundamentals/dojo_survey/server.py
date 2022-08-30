#IMPORTS
from flask import Flask, redirect, render_template, request, session

#INITIALIZATION
app = Flask(__name__)
app.secret_key = 'suspicious key'

#ROUTES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_reults():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')


#RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)