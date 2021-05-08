# -------------------------------------------------------------------------
# 1. Selecionamos os dois pontos de dados e os classificamos.
# 2. Expandimos nossa seleção e selecionamos o terceiro ponto de dados
# e encontramos sua posição correta, com base em seu valor.
# 3. Avançamos até que todos os pontos de dados sejam movidos para suas posições corretas.
# -------------------------------------------------------------------------
def InsertionSort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        prox = lst[i]
        while (lst[j] > prox) and (j >= 0):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = prox
    return lst


lst = [45, 32, 23, 4, 67, 12, 34, 67, 45, 10, 2, 1, 2]
InsertionSort(lst)
print(lst)
