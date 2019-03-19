PESSOAS = 10
QUANT_HOMENS = 0
QUANT_MULHERES = 0

SALARIO_TOTAL = 0
MEDIA_DOS_SALARIOS = 0

for x in range(PESSOAS):
    Salario = float(input())
    Sexo = input()

    SALARIO_TOTAL += Salario
    MEDIA_DOS_SALARIOS = SALARIO_TOTAL /PESSOAS

    if Sexo == "m":
        QUANT_HOMENS += 1

    if Sexo == "f":
        QUANT_MULHERES += 1

print(QUANT_HOMENS)
print(QUANT_MULHERES)
print("{:.1F}".format(MEDIA_DOS_SALARIOS))