Fig = input()

if Fig == "Q":
    Lado = float(input())
    QArea = Lado**2
    QPeri = Lado * 4
    print("{:.2f}".format(QArea))
    print("{:.2f}".format(QPeri))
elif Fig == "R":
    Larg = float(input())
    Altu = float(input())
    RArea = Larg * Altu
    RPeri = 2*(Larg + Altu)
    print("{:.2f}".format(RArea))
    print("{:.2f}".format(RPeri))
elif Fig == "C":
    Raio = float(input())
    Pi = 3.14
    CArea = (Raio**2) * Pi
    CComp = 2 * Pi * Raio
    print("{:.2f}".format(CArea))
    print("{:.2f}".format(CComp))
else:
    print("Nenhuma figura selecionada")

