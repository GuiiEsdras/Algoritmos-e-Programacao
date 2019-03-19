lst = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
       [4, 9, 8, 2, 6, 1, 3, 7, 5],
       [7, 5, 6, 3, 8, 4, 2, 1, 9],
       [6, 4, 3, 1, 5, 8, 7, 9, 2],
       [5, 2, 1, 7, 9, 3, 8, 4, 6],
       [9, 8, 7, 5, 2, 6, 5, 3, 1],
       [2, 1, 4, 9, 3, 5, 6, 8, 7],
       [3, 6, 5, 8, 1, 7, 9, 2, 4],
       [8, 7, 9, 6, 4, 2, 1, 5, 3]]

colunas_corretas = True
lista_sudoku = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for l in range(len(lst)):
    verifica_lista = []
    for c in range(len(lst[l])):
        verifica_lista.append(lst[c][l])
    verifica_lista.sort()
    if verifica_lista != lista_sudoku:
        colunas_corretas = False
        break

print(colunas_corretas)