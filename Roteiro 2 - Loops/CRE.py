CONT = TOTAL = MAIOR = MENOR = 0

while True:
    Matricula = input()

    if Matricula == "999":
        break

    else:
        CRE = float(input())

        CONT += 1
        TOTAL += CRE
        Media = TOTAL / CONT

print("{:.2f}".format(Media))
