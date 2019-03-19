cont = 0
pontuacao_total = 0
maior_pontuacao = 0
menor_pontuacao = 999
melhor_jogador = ''
pior_jogador = ''
MEDIA = 0

while True:
    Jogador = input()

    if Jogador == "sair":
        if cont == 0:
            print("Nenhum jogador foi registrado.")
        break

    else:
        cont += 1
        Pontuacao = int(input())
        pontuacao_total += Pontuacao

        if Pontuacao >= maior_pontuacao:
            maior_pontuacao = Pontuacao
            melhor_jogador = Jogador

        if Pontuacao <= menor_pontuacao:
            menor_pontuacao = Pontuacao
            pior_jogador = Jogador
print(pior_jogador)
print(melhor_jogador)
if cont != 0:
    MEDIA = pontuacao_total / cont
    print("{:.2f}".format(MEDIA))