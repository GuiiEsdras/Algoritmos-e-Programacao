# R = Raio.
# G = A medida do ângulo em graus.
R = float(input())
G = float(input())

Pi = 3.14

# A medida do comprimento do arco.
# A área do setor.
C = (2*Pi*R)*G/360
A = (G*Pi*(R**2)) / 360

print(round(C, 2))
print(round(A, 2))