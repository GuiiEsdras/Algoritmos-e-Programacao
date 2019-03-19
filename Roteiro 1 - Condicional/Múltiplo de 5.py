# Escreva um programa que leia um valor qualquer e informe se ele é múltiplo de 5.
# Dica: Use o operador "resto da divisão".

N = int(input())

if N % 5 == 0:
    print("Eh multiplo de 5")
else:
    print("Nao eh multiplo de 5")