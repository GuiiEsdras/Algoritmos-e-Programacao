# Um programa que recebe as características (massa e altura) de uma pessoa e retorna seu IMC - Índice de Massa Corporal.
Massa = float(input())
Altura = float(input())
IMC = Massa / (Altura**2)
print("{:.2f}".format(IMC))