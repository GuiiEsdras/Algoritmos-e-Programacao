# Faça um programa que calcule a área da superfície e o volume de um cilindro. Use pi = 3.14.
# O valor de saída deve ser arredondado usando 2 casas decimais.

# H = Altura
# R = Raio
H = float(input())
R = float(input())

Pi = 3.14

# V = Volume
# A = Área da Superfície
V = H*Pi*(R**2)
A = 2*Pi*R**2 + 2*Pi*R*H

print("{:.2f}".format(V))
print("{:.2f}".format(A))