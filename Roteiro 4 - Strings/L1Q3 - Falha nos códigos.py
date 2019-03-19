pokemons = {'b': 'Bulbassauro', 'c': 'Charmander', 's': 'Squirtle'}
C = str(input()).lower()
Codigo = C[6]
if Codigo not in pokemons:
    print("Codigo Invalido")
else:
    print(pokemons[Codigo])