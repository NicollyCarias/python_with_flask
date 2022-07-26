from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    variavel = ' The game started: what is the first even number?'

    if request.method == "GET":
        return render_template('index.html', variavel=variavel)

    else:
        number = 2
        kich = int(request.form.get("name"))

        if number == kich:
            return '<h1>Result: you won</h1>'
        else:
            return '<h1>Result: you lost</h1>'


@app.route('/<string:nome>')
def error(nome):
    var = f'Attention: page ({nome}) does not exist, are you sure it is this way?'
    return render_template('error.html', var=var)