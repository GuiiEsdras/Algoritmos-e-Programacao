def ParesCrescente(n):
    if n > 0:
        ParesCrescente(n-1)
    if n % 2 == 0:
        print(n)


n = int(input())
ParesCrescente(n)