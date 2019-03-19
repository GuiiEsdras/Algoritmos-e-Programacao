n = 0
while True:
    n = int(input())
    if n == -1:
        break
    else:
        for x in range(1, n+1):
            if n % x == 0:
                print("0")