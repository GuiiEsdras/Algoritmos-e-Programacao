def ParesDecrescente(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        print(n)
    return ParesDecrescente(n -1)


n = int(input())
print(ParesDecrescente(n))