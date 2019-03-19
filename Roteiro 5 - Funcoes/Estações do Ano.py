def EstacaoAno(dia, mes):
    estacao = ''
    if (dia >= 21 and mes == 9) or (10 <= mes <= 11) or (dia <= 20 and mes == 12):
        estacao = "PRIMAVERA"

    elif (dia >= 21 and mes == 12) or (1 <= mes <= 2) or (dia <= 20 and mes == 3):
        estacao = "VERÃO"

    elif (dia >= 21 and mes == 3) or (4 <= mes <= 5) or (dia <= 20 and mes == 6):
        estacao = "OUTONO"

    elif (dia >= 21 and mes == 6) or (7 <= mes <= 8) or (dia <= 20 and mes == 9):
        estacao = "INVERNO"

    return estacao

d = int(input())
m = int(input())

print(EstacaoAno(d, m))