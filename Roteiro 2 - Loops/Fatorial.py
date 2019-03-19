while True:
    n = int(input())
    if n == -1:
        break
    else:
        fat = 1
        i = 2
        while i <= n:
            fat *= i
            i += 1
        print(fat)