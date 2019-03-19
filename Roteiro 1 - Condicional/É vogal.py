Letra = input()
Vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
if(len(Letra) > 1):
    print("1 caractere, por favor!")
elif Letra in Vogais:
    print("Eh vogal")
else:
    print("Nao eh vogal")