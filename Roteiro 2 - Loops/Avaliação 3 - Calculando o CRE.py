CRE = 0
CRE_numerador = 0
CRE_divisor = 0
cont = 0
semestre = int(input())

while 0 < semestre <= 10:
    carga_horaria = int(input())
    nota_na_disciplina = int(input())
    situacao_na_disciplina = str(input()).upper()

    desconsiderado = ['T', 'AD', 'DE', 'AE', 'DD', 'DC']
    carga_considerada = [33, 50, 67, 83]

    if (situacao_na_disciplina not in desconsiderado) and (carga_horaria in carga_considerada):
        CRE_numerador += nota_na_disciplina * carga_horaria
        CRE_divisor += carga_horaria
        cont += 1

    semestre = int(input())


if cont != 0:
    CRE = CRE_numerador / CRE_divisor
    print("{:.2f}".format(CRE))

else:
    print("entrada invalida")
