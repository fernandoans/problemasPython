# -------------------------------------------------------------------------
# 1. Dividimos a lista em 2 partes iguais
# 2. Utilizamos o processo de recursão para dividir até que o comprimento de cada lista seja 1
# 3. Mesclamos as partes classificadas em uma lista ordenada
# -------------------------------------------------------------------------
def MergeSort(lst):
    if len(lst) > 1:
        met = len(lst)//2
        esq = lst[:met]
        dir = lst[met:]

        MergeSort(esq)
        MergeSort(dir)

        a = 0
        b = 0
        c = 0
        while a < len(esq) and b < len(dir):
            if esq[a] < dir[b]:
                lst[c] = esq[a]
                a += 1
            else:
                lst[c] = dir[b]
                b += 1
            c += 1

        while a < len(esq):
            lst[c] = esq[a]
            a += 1
            c += 1

        while b < len(dir):
            lst[c] = dir[b]
            b += 1
            c += 1

    return lst


lst = [45, 32, 23, 4, 67, 12, 34, 67, 45, 10, 2, 1, 2]
MergeSort(lst)
print(lst)
