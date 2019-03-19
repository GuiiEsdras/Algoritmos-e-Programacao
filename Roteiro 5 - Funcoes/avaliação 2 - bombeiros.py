def Chegada(lst, k):
    pessoas = 0
    for i, v in enumerate(lst):
        if i != k:
            pessoas += v
        else:
            break
    return pessoas

def Mudanca(lst, k, p):
    lst[k-1] = p


andares_e_eventos = [int(x) for x in input().split()]
pessoas_em_cada_andar = [int(x) for x in input().split()]

for x in range(andares_e_eventos[1]):
    evento = [int(x) for x in input().split()]
    if evento[0] == 1:
        if evento[1] > andares_e_eventos[0]:
            print("nao existe esse andar no predio")
        else:
            print(Chegada(pessoas_em_cada_andar, evento[1]))
    elif evento[0] == 0:
        if evento[1] > andares_e_eventos[0]:
            print("nao existe esse andar no predio")
        else:
            Mudanca(pessoas_em_cada_andar, evento[1], evento[2])
