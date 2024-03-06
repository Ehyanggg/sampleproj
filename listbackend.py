#pip install flask

from flask import Flask, render_template

app = Flask(__name__)

list = ["Mary Grace", "Jocel", "Daisy", "Jhasmin", "Angel", "Kia"]

@app.route('/')
def index():
    return render_template('index.html', items=list)

if __name__=='__main__':
    app.run(debug=True, port=5001)
