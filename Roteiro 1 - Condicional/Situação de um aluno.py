Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())

Media = (Nota1 + Nota2 + Nota3) /3

if Media < 0:
    print("Media invalida")
elif Media >= 0:
    print("A media do aluno foi {:.2f} e ele foi ".format(Media), end='')

if Media >= 70 and Media <= 100:
    print("APROVADO")
elif Media >= 0 and Media <= 40:
    print("REPROVADO")
elif Media >= 40 and Media <= 70:
    print("FINAL")