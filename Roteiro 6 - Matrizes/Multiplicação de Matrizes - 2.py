def multiplicar(matrizA, matrizB):
    linhasA = len(matrizA)
    linhasB = len(matrizB)
    colunasA = len(matrizA[0])
    colunasB = len(matrizB[0])

    matrizC = []

    for linha in range(linhasA):
        matrizC.append([])
        for coluna in range(colunasB):
            matrizC[linha].append(0)
            for i in range(colunasA):
                matrizC[linha][coluna] += matrizA[linha][i] * matrizB[i][coluna]

    for i in range(len(matrizC)):
        for j in range(len(matrizC[i])):
            if j != len(matrizC[i])-1:
                print(matrizC[i][j], end=' ')
            else:
                print(matrizC[i][j])


dados = input().split()

quantidadeLinhasMatrizA = int(dados[0])
quantidadeColunasMatrizA = int(dados[1])
quantidadeLinhasMatrizB = int(dados[1])
quantidadeColunasMatrizB = int(dados[2])

matrizA = []
matrizB = []

for i in range(quantidadeLinhasMatrizA):
    matrizA.append([int(x) for x in input().split()])

for i in range(quantidadeLinhasMatrizB):
    matrizB.append([int(x) for x in input().split()])

multiplicar(matrizA, matrizB)