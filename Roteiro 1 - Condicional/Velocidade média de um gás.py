# T = Temperatura (em Kelvin)
# M = Massa molar do gás
# R = Constante Universal dos Gases Perfeitos
T = float(input())
M = float(input())
R = 8.31

# Velocidade Média do Gás
V = ((3 * R * T) /M) **(1/2)

print(round(V, 2))