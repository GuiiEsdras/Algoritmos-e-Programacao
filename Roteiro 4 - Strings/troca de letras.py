while True:
    palavra = input().upper()
    palavra = palavra.replace("3", "E")
    palavra = palavra.replace("4", "A")
    palavra = palavra.replace("1", "I")
    palavra = palavra.replace("5", "S")
    if palavra == 'FIM' or palavra == 'SAIR':
        break
    else:
        print(palavra)