DIAS = 7
TOTAL = 0

for x in range(DIAS):
    Deposito = float(input())
    TOTAL += Deposito

print("R$ {:.2f}".format(TOTAL))
