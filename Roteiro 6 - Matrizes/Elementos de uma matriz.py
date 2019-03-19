def print_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == m[i][-1]:
                print(m[i][j] , end="\n")
            else:
                print(m[i][j], end= " ")

def calcule_DP(m):
    soma_DP = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                soma_DP += m[i][j]
    return soma_DP

def calcule_DS(m):
    soma_DS = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i + j == len(m)-1:
                soma_DS += m[i][j]
    return soma_DS


l_c = input().split()
linhas = int(l_c[0])
coluna = int(l_c[1])

maior = 0
menor = 0

matriz = []

for i in range(linhas):
    matriz.append([])
    for j in range(coluna):
        num = int(input())
        matriz[i].append(num)
        if num > 0:
            maior += 1
        else:
            menor += 1

if coluna == linhas:
    print("Matriz formada:")
    print_matriz(matriz)
    print("A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.".format(calcule_DP(matriz), calcule_DS(matriz)))
    print("A matriz possui {} numero(s) menor(es) que zero.".format(menor))
    print("A matriz possui {} numero(s) maior(es) que zero.".format(maior))

else:
    print("Matriz formada:")
    print_matriz(matriz)
    print("A diagonal principal e secundaria nao pode ser obtida.")
    print("A matriz possui {} numero(s) menor(es) que zero.".format(menor))
    print("A matriz possui {} numero(s) maior(es) que zero.".format(maior))


