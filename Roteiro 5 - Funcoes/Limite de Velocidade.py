def CalculaMulta(v):
    multa = 0
    permitida = 50
    if v > permitida:
        if v <= (permitida + 0.1*permitida):
            multa = 230
        elif v <= (permitida + 0.2*permitida):
            multa = 340
        elif v > (permitida + 0.2*permitida):
            multa = 19.28 * (v - 50)
    return multa

velocidade = int(input())

print("{:.2f}".format(CalculaMulta(velocidade)))