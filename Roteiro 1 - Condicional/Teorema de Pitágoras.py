# Faça um programa que calcule o valor da hipotenusa de acordo com o teorema de pitágoras. Você não precisa se preocupar com casos em que os catetos fornecidos não podem formar um triângulo.
# Pesquise como fazer a operação de raiz quadrada.
# O valor de saída deve ser arredondado usando 2 casas decimais.
CatA = float(input())
CatB = float(input())
Hip = ((CatA**2) + (CatB**2)) **(1/2)
print("{:.2f}".format(Hip))