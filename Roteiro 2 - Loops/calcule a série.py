n = int(input())

dividendo = 1
divisor = 3

soma = 1/3
soma_str = str(dividendo) + '/' + str(divisor) + ' + '

if n == 0:
    print("{:.2f}".format(0.00))

elif n == 1:
    print("{}/{}".format(dividendo, divisor))
    print("{:.2f}".format(soma))

elif n != 0:
    for i in range(1, n):
        dividendo += 1
        divisor += 3
        if i == n - 1:
            soma_str += str(dividendo) + '/' + str(divisor)
        else:
            soma_str += str(dividendo) + '/' + str(divisor) + ' + '
        soma += dividendo/divisor
    print(soma_str)
    print('{:.2f}'.format(soma))

