X = int(input())
Y = int(input())

if X == 0 and Y == 0:
    print("Sobre a origem")
elif X > 0 and Y > 0:
    print("Primeiro Quadrante")
elif X < 0 and Y > 0:
    print("Segundo Quadrante")
elif X < 0 and Y < 0:
    print("Terceiro Quadrante")
elif X > 0 and Y < 0:
    print("Quarto Quadrante")
elif X == 0 and Y > 0:
    print("Sobre o eixo y")
elif X == 0 and Y < 0:
    print("Sobre o eixo y")
elif Y == 0 and X > 0:
    print("Sobre o eixo x")
elif Y == 0 and X < 0:
    print("Sobre o eixo x")