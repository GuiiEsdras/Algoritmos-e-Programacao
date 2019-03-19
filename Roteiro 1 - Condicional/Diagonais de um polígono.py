# A diagonal de um polígono é um segmento de linha que liga 2 vértices não adjacentes
# Faça um programa que calcula a quantidade de diagonais de um polígono baseado na quantidade de lados desse polígono
Lados = int(input())
Diags = (Lados*(Lados-3)/2)
print("{:.0f}".format(Diags))