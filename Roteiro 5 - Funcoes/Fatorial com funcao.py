def fat(n):
    for i in range(n-1, 1, -1): n *= i
    return n
n = int(input())
while n != -1:
    print(fat(n))
    n = int(input())
