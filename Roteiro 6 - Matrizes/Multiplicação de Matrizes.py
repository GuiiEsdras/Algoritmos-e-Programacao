def multiplicador(matriz_A, matriz_B):
    matriz_C = []

    for v in range(len(matriz_A)):
        matriz_C.append([])
        for x in range(len(matriz_B[0])):
            soma = 0
            matriz_C[v].append(soma)
            for y in range(len(matriz_A[0])):
                matriz_C[v][x] += matriz_A[v][y] * matriz_B[y][x]

    for l in range(len(matriz_C)):
        for c in range(len(matriz_C)):
            if c == len(matriz_C[l]) - 1:
                print(matriz_C[l][c], end='\n')
            else:
                print(matriz_C[l][c], end=' ')


# N = Quantidade de Linhas da Matriz A;
# M = Quantidade de Colunas da Matriz A e quantidade de Linhas da Matriz B;
# O = Quantidade de Colunas da Matriz B.
N, M, O = [int(x) for x in input().split()]

lista_A = []
for a in range(N):
    lista_A.append([int(x) for x in input().split()])

lista_B = []
for b in range(M):
    lista_B.append([int(x) for x in input().split()])

multiplicador(lista_A, lista_B)