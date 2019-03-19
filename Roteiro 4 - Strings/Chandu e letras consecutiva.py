p = str(input())
lista = []

for x in p:
    lista.append(x)

for pos, valor in enumerate(lista):
    print(pos, valor)
    if valor == pos-1:
        lista.remove(valor)

for x in lista:
    print(x, end='')