from flask import Flask, render_template, request

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

        cotacao = 5.50

        if conversao == "real_dolar":
            resultado = valor / cotacao

        elif conversao == "dolar_real":
            resultado = valor * cotacao

    return render_template("moedas.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)