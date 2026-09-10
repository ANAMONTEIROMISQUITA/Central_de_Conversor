def converter_moeda(valor, conversao):

    cotacao = 5.50

    if conversao == "real_dolar":
        return valor / cotacao

    elif conversao == "dolar_real":
        return valor * cotacao