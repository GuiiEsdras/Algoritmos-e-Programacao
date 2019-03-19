lista = list()

matriz = []
ordem = int(input())
for x in range(ordem):
    nums = [float(x) for x in input().split()]
    matriz.append(nums)

soma = 0


for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        if x == (len(matriz) - 1):
            if x == y:
                lista.append("({:.2f})".format(matriz[x][y]))
                soma += matriz[x][y]
        else:
            if x == y:
                lista.append("({:.2f}) +".format(matriz[x][y]))
                soma += matriz[x][y]

print("tr(A) =", end=' ')
for x in range(len(lista)):
    print(lista[x], end=' ')
print("= {:.2f}".format(soma))