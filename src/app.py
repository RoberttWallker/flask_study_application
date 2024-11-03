from flask import Flask, request

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario,idade,altura):
    return {
        "Usuário": usuario,
        "Idade": idade,
        "Altura": altura,
    }

@app.route("/bemvindo")
def bem_vindo():
    return {
        "message": "Olá mundo"
    }

@app.route("/about", methods=["GET","POST"])
def about():
    if request.method == 'GET':
        return "<p>This is a GET</p>"
    else:
        return "<p>This is a POST</p>"