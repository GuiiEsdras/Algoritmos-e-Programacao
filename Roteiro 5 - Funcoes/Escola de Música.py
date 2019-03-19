def ClassificaAluno(m, f):
    situacao = ''
    if f <= 10:
        if m < 7:
            situacao = "REPROVADO"
        elif 7 <= m < 9.5:
            situacao = "APROVADO"
        elif m >= 9.5:
            situacao = "APROVADO COM LOUVOR"

    elif f > 10:
        situacao = "REPROVADO POR FALTAS"

    return situacao

media = float(input())
faltas = int(input())

print(ClassificaAluno(media, faltas))