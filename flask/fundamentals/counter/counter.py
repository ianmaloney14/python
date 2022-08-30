from flask import Flask, redirect, render_template, session

app = Flask(__name__)
app.secret_key = 'suspicious key'

@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else: 
        session['count'] = 0
    return render_template('counter.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two_visits')
def count_by_two():
    session['count'] += 1
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)