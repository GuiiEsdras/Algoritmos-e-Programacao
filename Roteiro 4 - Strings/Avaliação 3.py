cont = 0
sequencia_1 = input().split()
for i, v in enumerate(sequencia_1):
    if len(v) >= 2:
        cont += 1
sequencia_1_junta = []

sequencia_2 = input().split()
for i, v in enumerate(sequencia_2):
    if len(v) >= 2:
        cont += 1
sequencia_2_junta = []

if cont > 0:
    print("Erro em uma ou mais sequencia de entrada de dados")
else:

    for i, v in enumerate(sequencia_1):
        sequencia_1_junta.append(str(v))

    sequencia_1_junta = ''.join(sequencia_1_junta)
    sequencia_1_junta = int(sequencia_1_junta)

    for i, v in enumerate(sequencia_2):
        sequencia_2_junta.append(str(v))

    sequencia_2_junta = ''.join(sequencia_2_junta)
    sequencia_2_junta = int(sequencia_2_junta)

    resultado = sequencia_1_junta + sequencia_2_junta
    resultado = str(resultado)
    for i, v in enumerate(resultado):
        print(v, end=' ')