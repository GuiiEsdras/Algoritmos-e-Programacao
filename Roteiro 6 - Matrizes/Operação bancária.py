matriz = []

while True:
    op_valor = input().split()
    if op_valor[0] == "-1":
        break
    else:
        op_valor[0] = int(op_valor[0])
        op_valor[1] = float(op_valor[1])

        matriz.append(op_valor)

creditos = 0
debitos = 0

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] == 1:
            creditos += matriz[l][c+1]
        elif matriz[l][c] == 0:
            debitos += matriz[l][c+1]

saldo = creditos - debitos

print("Creditos: R$ {:.2f}".format(creditos))
print("Debitos: R% {:.2f}".format(debitos))
print("Saldo: R$ {:.2f}".format(saldo))