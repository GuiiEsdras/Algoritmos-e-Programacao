n = int(input())

for x in range(1, n):
    cont = 1
    soma = 0

    while cont < x:
        if x % cont == 0:
            soma = soma + cont
            cont = cont + 1
        else:
            cont = cont + 1

    if soma == x:
        print(x)