def menor_ordem_crescente(cartas):
    c = cartas[:]
    c.sort()
    for x in range(1, len(c)):
        if c[x] != c[x - 1]+1:
            return 0
    return c[0]

def menor_iguais(cartas):
    for x in range(1, len(cartas)):
        if cartas[x] != cartas[x -1]:
            return 0
    return cartas[0]

def duas_menores_iguais(cartas):
    c = cartas[:]
    c.sort()
    if c[0] == c[1] and c[2] != c[0]:
        return c[0] // 2
    return 0

def duas_maiores_iguais(cartas):
    c = cartas[:]
    c.sort()
    if c[2] == c[1] and c[0] != c[2]:
        return c[2] // 2
    return 0

def soma_oito(cartas):
    if sum(cartas) == 8:
        return 8
    return 0


paes = [int(x) for x in input().split()]
wily = [int(x) for x in input().split()]

pontos_paes = 0
pontos_wily = 0

pontos_paes += menor_ordem_crescente(paes)
pontos_paes += menor_iguais(paes)
pontos_paes += duas_menores_iguais(paes)
pontos_paes += duas_maiores_iguais(paes)
pontos_paes += soma_oito(paes)

pontos_wily += menor_ordem_crescente(wily)
pontos_wily += menor_iguais(wily)
pontos_wily += duas_menores_iguais(wily)
pontos_wily += duas_maiores_iguais(wily)
pontos_wily += soma_oito(wily)

if pontos_paes > pontos_wily:
    print("1")
elif pontos_wily > pontos_paes:
    print("2")
else:
    print("0")