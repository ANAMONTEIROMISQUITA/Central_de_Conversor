def converter_moeda(valor, moeda_origem, moeda_destino, cotacoes):

    if moeda_origem == moeda_destino:
        return valor

    valor_em_dolar = valor / cotacoes[moeda_origem]

    resultado = valor_em_dolar * cotacoes[moeda_destino]

    return resultado