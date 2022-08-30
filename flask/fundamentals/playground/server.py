from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/play')
def play():
    return render_template("index.html", num = 3)

@app.route('/play/<num>')
def play_1(num):
    return render_template("index.html", num = int(num))

@app.route('/play/<num>/<color>')
def play_2(num, color):
    return render_template("index.html", num = int(num), color = color)

if __name__ == "__main__":
    app.run(debug=True)