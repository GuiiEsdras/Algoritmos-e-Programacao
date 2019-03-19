# TdJ = Time do Jogador
TdJ = input()

if TdJ == "GSW" or TdJ == "HOU" or TdJ == "CLE" or TdJ == "BOS":
    NdJ = input() #Nome do Jogador
    AT2 = int(input()) #Arremessos Tentados (2pts)
    AC2 = int(input()) #Arremessos Convertidos (2pt)
    AT3 = int(input()) #Arremessos Tentados (3pts)
    AC3 = int(input()) #Arremessos Convertidos (3pts)

    Pts = AT2 + AC2 + AT3 + AC3
    PA2 = (AC2 / AT2) * 100
    PA3 = (AC3 / AT3) * 100

    if Pts > 30 or PA2 > 50 and AT2 > 10 or PA3 > 40 and AT3 > 7:
        print("O time {} estah jogando, e {} estah indo bem".format(TdJ, NdJ))

    else:
        print("O time {} estah jogando, mas {} nao estah indo bem".format(TdJ, NdJ))

else:
    print("Nenhum time de interesse jogando.")