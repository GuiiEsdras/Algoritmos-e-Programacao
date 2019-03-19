def SomaSucessiva(n1, n2):
    if n2 == 0:
        return 0
    elif n2 == 1:
        return n1
    elif n2 < 0:
        return - SomaSucessiva(n1, -n2)
    else:
        return n1 + SomaSucessiva(n1, n2-1)

a = int(input())
b = int(input())

print(SomaSucessiva(a, b))