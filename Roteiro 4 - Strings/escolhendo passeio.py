acumulador = boliche = cinema = 0

while True:
    acumulador += 1
    if acumulador == 7:
        break

    passeio = str(input()).upper()
    if passeio in 'CINEMA':
        cinema += 1
    elif passeio in 'BOLICHE':
        boliche += 1

if boliche >= cinema:
    print("BOLICHE")
else:
    print("CINEMA")