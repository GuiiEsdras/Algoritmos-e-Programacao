# Um programa que lê o valor do índice de acidez (pH) de uma solução e informa se ela é ácida, básica ou neutra.
pH = float(input())
if pH < 7:
    print("Acida")
else:
    if pH > 7:
        print("Basica")
    else:
        print("Neutra")