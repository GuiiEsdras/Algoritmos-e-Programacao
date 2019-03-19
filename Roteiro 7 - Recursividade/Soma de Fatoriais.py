def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n -1)

soma = 0
for x in range(5):
    n = int(input())
    if n % 3 == 0:
        soma += fat(n)

print(soma)