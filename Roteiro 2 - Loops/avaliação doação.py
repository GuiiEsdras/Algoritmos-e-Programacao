idade = int(input())
sexo = input()
peso = float(input())
ano_primeira = int(input())
doacoes_feitas = int(input())
mes_ultima = int(input())

mes_atual = 9

if idade >= 16 and idade <= 69 and peso >= 50:

    if sexo == "m" and (doacoes_feitas <= 3) and (mes_ultima <= (mes_atual - 2)):
        print("Pode ser doador")

    elif sexo == "f" and doacoes_feitas <= 2 and mes_ultima <= (mes_atual - 3):
        print("Pode ser doadora")

    else:
        print("Nao pode doar sangue")

else:
    print("Nao pode doar sangue")