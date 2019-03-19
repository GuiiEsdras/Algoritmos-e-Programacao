DIAS = 7
TOTAL = 0
CONT = 0

for x in range(DIAS):
    Entregas = float(input())
    TOTAL += Entregas
    Media = TOTAL / 7
    if Entregas >= 100:
        CONT += 1

print("{}".format(CONT))
print("{:.0f}".format(Media))