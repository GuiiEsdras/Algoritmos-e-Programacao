# Escreva um programa que leia dois valores inteiros da entrada padrão e informe qual é o maior. Se os números forem iguais,
# imprima qualquer um deles.

N1 = int(input())
N2 = int(input())

if N1 > N2:
    print(N1)
else:
    if N1 < N2:
        print(N2)
    else:
        if N1 == N2:
            print(N1)