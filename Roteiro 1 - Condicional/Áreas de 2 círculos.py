#Escreva um programa que leia os valores (reais) dos raios de dois círculos diferentes e informe qual dos dois possui área maior ou se possuem a mesma área.
#Use pi = 3.14

#RPC = Raio do Primeiro Círculo
#RSC = Raio do Segundo Círculo
RPC = float(input())
RSC = float(input())

if RPC > RSC:
    print("Primeiro circulo")
else:
    if RPC < RSC:
        print("Segundo circulo")
    else:
        print("Iguais")