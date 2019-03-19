# S = 1/4 + 1 + 3/8 + 1 + 5/12 + 1 +  7/16
#
#      0    1    2    3     4    5     6

n = int(input())

dividendo = 1
divisor = 4

soma_str = str(dividendo) + '/' + str(divisor) + ' + '
soma = 1/4

if n == 0:
    print("{:.2f}".format(0.00))

elif n == 1:
    print('{:.2f}'.format(soma))
    print("{}/{}".format(dividendo, divisor))

elif n > 1:
    for i in range(1, n):
        if i % 2 != 0:
            if i == n-1:
                soma_str += '1'
            else:
                soma_str += '1 + '
            soma += 1
        else:
            dividendo += 2
            divisor += 4
            if i == n - 1:
                soma_str += str(dividendo) + '/' + str(divisor)
            else:
                soma_str += str(dividendo) + '/' + str(divisor) + ' + '
            soma += dividendo/divisor

    print('{:.2f}'.format(soma))
    print(soma_str)