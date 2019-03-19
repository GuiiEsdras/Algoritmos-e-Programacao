PORCENTO_DE_PORTUGUES = 0.80 * 50
PORCENTO_DE_MATEMATICA = 0.60 * 35

Aprovados = 0

while True:
    Nota_portugues = int(input())

    if Nota_portugues < 0:
        break

    else:
        Nota_matematica = int(input())
        Nota_redacao = float(input())

        if ((Nota_portugues >= PORCENTO_DE_PORTUGUES) and (Nota_matematica >= PORCENTO_DE_MATEMATICA) and (Nota_redacao >= 7.0)):
            Aprovados += 1

print(Aprovados)