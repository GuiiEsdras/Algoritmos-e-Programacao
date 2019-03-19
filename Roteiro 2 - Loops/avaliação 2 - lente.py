melhor_marca = ''
melhor_preco = 0

while True:

    marca_da_lente = input()
    if marca_da_lente == 'sair':
        break

    marcas_aceitas = ['Sigma', 'Nikkor']

    alcance = int(input())
    nova_ou_usada = input().upper()[0]

    cont_n_u = 0
    if nova_ou_usada == 'U':
        pontos_de_fungos = input().upper()[0]
        avarias = input().upper()[0]
        if pontos_de_fungos == 'S' or avarias == 'S':
            cont_n_u += 1

    if marca_da_lente in marcas_aceitas and alcance >= 300 and cont_n_u == 0:
        preco = float(input())

        if melhor_preco == 0 or preco < melhor_preco:
            melhor_marca = marca_da_lente
            melhor_preco = preco

print(melhor_marca)
print(melhor_preco)