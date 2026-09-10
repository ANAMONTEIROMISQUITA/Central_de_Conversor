from flask import Flask, render_template, request
from conversores.moedas import converter_moeda

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/moedas", methods=["GET", "POST"])
def moedas():

    resultado = None

    if request.method == "POST":

        valor = float(request.form["valor"])
        conversao = request.form["conversao"]

        resultado = converter_moeda(valor, conversao)

    return render_template(
        "moedas.html",
        resultado=resultado
    )


if __name__ == "__main__":
    app.run(debug=True)