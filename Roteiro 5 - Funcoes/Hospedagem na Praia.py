def CalculaHospedagem(tipo, quant):
    valor = 0
    if tipo == "individual":
        valor += 125
    elif tipo == "suite dupla" or tipo == "suíte dupla":
        valor += 140
    elif tipo == "suite tripla" or tipo == "suíte tripla":
        valor += 180

    if quant >= 3:
        valor = valor - (valor * 0.15)

    valor *= quant

    return valor

tipo_apartamento = str(input()).lower()
quant_dias = int(input())

valor = CalculaHospedagem(tipo_apartamento, quant_dias)

print("{:.2f}".format(valor))
