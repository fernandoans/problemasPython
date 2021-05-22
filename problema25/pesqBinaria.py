# -------------------------------------------------------------------------
# O algoritmo divide iterativamente uma lista em duas partes e mantém um
# registro dos índices mais baixos e mais altos até encontrar o valor que
# está procurando.
# -------------------------------------------------------------------------
def BinarySearch(lst, item):
    i0 = 0
    iN = len(lst) - 1
    achou = False
    while i0 <= iN and not achou:
        pontoMeio = (i0 + iN) // 2
        if lst[pontoMeio] == item:
            achou = True
        else:
            if item < lst[pontoMeio]:
                iN = pontoMeio - 1
            else:
                i0 = pontoMeio + 1
    return achou


lst = [1, 2, 2, 4, 10, 12, 23, 32, 34, 45, 45, 67, 67]
print(BinarySearch(lst, 45))
print(BinarySearch(lst, 2))
print(BinarySearch(lst, 63))
