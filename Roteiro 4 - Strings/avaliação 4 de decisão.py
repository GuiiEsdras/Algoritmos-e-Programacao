emissoras = {'2': 'SBT', '4': 'BAND', '6': 'REDETV!', '9': 'RECORD', '13': 'GLOBO'}
canais = [2, 4, 6, 9, 13]
canal = int(input('Digite um numero de um canal de tv: \n'))
if canal in canais:
    print(emissoras["{}".format(canal)])
else:
    print("Canal Invalido")
