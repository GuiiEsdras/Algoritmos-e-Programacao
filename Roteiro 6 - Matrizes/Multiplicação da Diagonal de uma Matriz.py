while True:
    k = int(input())
    if k == 0:
        break

    else:

        matriz = [[],
                  [],
                  [],
                  []]

        for y in range(len(matriz)):
            for x in range(len(matriz)):
                num = int(input())
                if y == x:
                    matriz[x].append(num*k)
                else:
                    matriz[x].append(num)

        for l in range(len(matriz)):
            for c in range(len(matriz[l])):
                if c == len(matriz[l])-1:
                    print(matriz[l][c], end=' \n')
                else:
                    print(matriz[l][c], end=' ')