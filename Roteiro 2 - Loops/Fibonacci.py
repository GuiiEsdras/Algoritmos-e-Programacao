[i, j] = [0, 1]
while True:
    n = int(input(""))
    if n == 0:
        break
for x in range(0, n):
    k = i + j
    if (x != n - 1):
        print(k, end=', ')
    else:
        print(k, end='.')
    j = i
    i = k