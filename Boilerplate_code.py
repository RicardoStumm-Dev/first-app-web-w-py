#Importando o módulo flask no projeto
from flask import Flask, render_template

#Crie um objeto da classe Flask
app = Flask(__name__)

#A função route() da classe  Flask
@app.route("/index")

# A URL ‘/’ é ligada à função first_flask.
def first_webpage():
    name = "Flask"
    return render_template("index.html", index_variable = name)

# Execute a aplicação no servidor local
app.run(debug = True)