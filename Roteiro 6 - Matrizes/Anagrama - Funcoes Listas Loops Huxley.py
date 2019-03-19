def Verifica_Anagrama(lst1, lst2):
    eh_anagrama = False
    if lst1 == lst2:
        eh_anagrama = True

    return eh_anagrama


frase_1 = input().lower().replace(' ', '')
frase_2 = input().lower().replace(' ', '')

rejeitados = ['.', ',', '!', '?']

frase_1_lst = []
for x in frase_1:
    if x not in rejeitados:
       frase_1_lst.append(x)
frase_1_lst.sort()

frase_2_lst = []
for y in frase_2:
    if y not in rejeitados:
       frase_2_lst.append(y)
frase_2_lst.sort()

print(Verifica_Anagrama(frase_1_lst, frase_2_lst))