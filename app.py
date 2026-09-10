from flask import Flask, render_template
from conversores.moedas import converter_moeda

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/moedas")
def moedas():
    return render_template("moedas.html")


if __name__ == "__main__":
    app.run(debug=True)