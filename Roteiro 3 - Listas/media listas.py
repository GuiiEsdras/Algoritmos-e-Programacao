N = int(input())
lista_de_notas = list()
soma = acima_media = abaixo_media = 0

for notas in range(1, N+1):
    nota = int(input())
    lista_de_notas.append(nota)
    soma += nota

media = soma / len(lista_de_notas)

for nota in lista_de_notas:
    if nota > media + media * 0.1:
        acima_media += 1
    if nota < media + media * 0.1:
        abaixo_media += 1

print("{:.2f}".format(media))
print(acima_media)
print(abaixo_media)
