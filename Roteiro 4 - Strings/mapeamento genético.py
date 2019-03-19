sequencia = input()
base = input()

posicao_da_maior_seq = 0
tamanho_da_maior_seq = 0

if base not in sequencia:
    print("ERRO")

else:
    posicao = 0
    tamanho = 0
    cont = 0
    for pos, caracter in enumerate(sequencia):
        if caracter == base and cont == 0:
            posicao = pos
            tamanho += 1
            cont += 1
        elif caracter == base and cont > 0:
            tamanho += 1

        if tamanho > tamanho_da_maior_seq:
            tamanho_da_maior_seq = tamanho
            posicao_da_maior_seq = posicao

        elif caracter != base:
            posicao = 0
            tamanho = 0
            cont = 0

    print(posicao_da_maior_seq)
    print(tamanho_da_maior_seq)