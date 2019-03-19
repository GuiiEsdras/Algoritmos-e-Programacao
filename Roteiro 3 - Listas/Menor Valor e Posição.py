N = int(input())
lista = list()

for x in range(0, N):
    lista.append(input())

print("Menor valor: {}".format(min(lista)))
for i, v in enumerate(lista):
    if v == (min(lista)):
        print("Posicao: {}".format(i))