#Nota 1, Nota 2, Nota 3
N1 = int(input())
N2 = int(input())
N3 = int(input())

if (N1 >= 0 and N1 <= 100) and (N2 >= 0 or N2 <= 100) and (N3 >= 0 or N3 <= 100):

    if N1 <= N2 and N1 <= N3:
        print(N1)
        if N2 <= N3:
            print(N2)
            print(N3)
        else:
            print(N3)
            print(N2)

    elif N2 <= N1 and N2 <= N3:
        print(N2)
        if N1 <= N3:
            print(N1)
            print(N3)
        else:
            print(N3)
            print(N1)

    else:
        print(N3)
        if N1 <= N2:
            print(N1)
            print(N2)
        else:
            print(N2)
            print(N1)