def VerificaSudoku_Linhas(lst):
    linhas_corretas = True
    lista_sudoku = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for l in range(len(lst)):
        verifica_lista = []
        for c in range(len(lst[l])):
            verifica_lista.append(lst[l][c])
        verifica_lista.sort()
        if verifica_lista != lista_sudoku:
            linhas_corretas = False
            break
    return linhas_corretas


def VerificaSudoku_Colunas(lst):
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
    return colunas_corretas


n = int(input())
sudoku = []

for q in range(n):
    sudoku.append([])
    for e in range(9):
        sudoku[q].append([int(x) for x in input().split()])
    print("Instancia {}".format(q+1))
    if not(VerificaSudoku_Linhas(sudoku[q]) and VerificaSudoku_Colunas(sudoku[q])):
        print("NAO")
    else:
        print("SIM")
    print()
