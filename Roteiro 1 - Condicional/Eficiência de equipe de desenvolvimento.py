# Escreva um programa que leia a quantidade de linhas de um programa (QUANTL), o número de funções existente nele (QUANTF),
# o tamanho da equipe (TAMEQ) e o número de bugs (NUMB) encontrados e calcule a eficiência da equipe de acordo com a seguinte
# formula: EFICIENCIA = (QUANTL / QUANTF) / TAMEQ – 4.2 x NUMB
QUANTL = input()
QUANTF = input()
TAMEQ = input()
NUMB = input()

EFICIENCIA = (int(QUANTL) / int(QUANTF)) / int(TAMEQ) - 4.2 * int(NUMB)

print("{}".format(EFICIENCIA))