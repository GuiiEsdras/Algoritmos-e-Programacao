Idade = int(input())
Jogo = input()
Tipos = ['azar', 'mmorpg', 'moba', 'casual']

if Idade <0 or Idade >130:
    print("Idade invalida.")
elif Jogo not in Tipos:
    print("Jogo invalido.")
elif Jogo == "azar" and Idade >= 21:
    print("Pode entrar!")
elif Jogo =="azar" and Idade < 21:
    print("Volte daqui há alguns anos.")
elif Jogo == "mmorpg" and Idade >= 14:
    print("Pode entrar!")
elif Jogo == "mmorpg" and Idade < 14:
    print("Volte daqui há alguns anos.")
elif Jogo == "moba" and Idade >= 10:
    print("Pode entrar!")
elif Jogo == "moba" and Idade < 10:
    print("Volte daqui há alguns anos.")
elif Jogo == "casual":
    print("Pode entrar!")