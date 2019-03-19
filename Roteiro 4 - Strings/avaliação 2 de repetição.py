cont = 0

menor_idade = 0
maior_idade = 0

mais_jovem = ''
posicao_mais_velho = ''

idades = []

while True:
    cont += 1
    if cont == 12:
        break

    else:
        nome_jogador = str(input())
        if nome_jogador == "sair":
            break

        idade_jogador = int(input())
        idades.append(idade_jogador)

        posicao_jogador = str(input()).upper()[0]

        if cont == 1:
            menor_idade = maior_idade = idade_jogador
            mais_jovem = nome_jogador
            posicao_mais_velho = posicao_jogador

        else:
            if idade_jogador < menor_idade:
                menor_idade = idade_jogador
                mais_jovem = nome_jogador

            if idade_jogador > maior_idade:
                maior_idade = idade_jogador
                posicao_mais_velho = posicao_jogador

soma_idades = 0
for i in idades:
    soma_idades += i

media_idades = soma_idades / len(idades)

print(mais_jovem)
print(posicao_mais_velho)
print("{:.1f}".format(media_idades))
