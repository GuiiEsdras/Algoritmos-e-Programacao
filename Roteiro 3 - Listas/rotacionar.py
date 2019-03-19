n = int(input())
lista = []
first = lista[:]

for x in range(1, n+1):
    num = int(input())
    lista.append(num)

for i in range(1, len(lista)):
    lista[i - 2] = lista[i]

lista[len(lista) - 2] = first

print(lista)