# TDM = Tipo de Media
TDM = input()

# N1 = Nota 1, N2 = Nota 2, N3 = Nota 3

# MA = Média Aritmética
if TDM == "a":
    N1 = int(input())
    N2 = int(input())
    N3 = int(input())
    MA = (N1 + N2 + N3) / 3
    print("{:.2f}".format(MA))
    if MA >= 70 and MA <= 100:
        print("Aprovado")
    elif MA >= 0 and MA < 40:
        print("Reprovado")
    elif MA >= 40 and MA < 70:
        print("Final")
    else:
        print("Media invalida")
# MP = Média Ponderada
elif TDM == "p":
    N1 = int(input())
    N2 = int(input())
    N3 = int(input())
    P1 = int(input())  # Peso 1
    P2 = int(input())  # Peso 2
    P3 = int(input())  # Peso 3
    MP = ((N1 * P1) + (N2 * P2) + (N3 * P3)) / (P1 + P2 + P3)
    print("{:.2f}".format(MP))
    if MP >= 70 and MP <= 100:
        print("Aprovado")
    elif MP >= 0 and MP < 40:
        print("Reprovado")
    elif MP >= 40 and MP < 70:
        print("Final")
    else:
        print("Media invalida")
# MH = Média Harmônica
elif TDM == "h":
    N1 = int(input())
    N2 = int(input())
    N3 = int(input())
    MH = 3 / (1 / N1 + 1 / N2 + 1 / N3)
    print("{:.2f}".format(MH))
    if MH >= 70 and MH <= 100:
        print("Aprovado")
    elif MH >= 0 and MH < 40:
        print("Reprovado")
    elif MH >= 40 and MH < 70:
        print("Final")
    else:
        print("Media invalida")

else:
    print("Escolha um tipo de media valida.")