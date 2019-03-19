def consecutivo(a, b):
    return (a == b + 1) or (a + 1 == b)

def calculo_de_pontos(lista_de_cartas):
    pontuacao = 0
    for i in range(0, len(lista_de_cartas), 2):
        if lista_de_cartas[i] == lista_de_cartas[i + 1]:
            pontuacao += 2 * (lista_de_cartas[i] + lista_de_cartas[i+1])
        elif consecutivo(lista_de_cartas[i], lista_de_cartas[i+1]):
            pontuacao += 3 * (lista_de_cartas[i] + lista_de_cartas[i + 1])
        else:
            pontuacao += lista_de_cartas[i] + lista_de_cartas[i + 1]
    return pontuacao

while True:
    jogada = input().split()
    if jogada[0] == 'sair':
        print("fim")
        break

    jogador_1 = jogada.pop(0)
    jogador_2 = jogada.pop(0)

    if len(jogada) % 2 != 0:
        print("erro")
        break

    cartas_1 = []
    cartas_2 = []

    alt = True
    for x in range(0, len(jogada), 2):
        if alt:
            cartas_1.append(int(jogada[x]))
            cartas_1.append(int(jogada[x+1]))
        else:
            cartas_2.append(int(jogada[x]))
            cartas_2.append(int(jogada[x+1]))
        alt = not(alt)

    pontuacao_1 = calculo_de_pontos(cartas_1)
    pontuacao_2 = calculo_de_pontos(cartas_2)

    if pontuacao_1 > pontuacao_2:
        print(jogador_1)
    elif pontuacao_2 > pontuacao_1:
        print(jogador_2)
    else:
        print("empate")