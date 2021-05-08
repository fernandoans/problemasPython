# -------------------------------------------------------------------------
# A classificação por seleção é uma melhoria na classificação por bolhas, no qual tentamos minimizar
# o número total de trocas necessárias. Projetado para fazer uma troca para cada passagem, em
# comparação com as N-1 passagens com o algoritmo de classificação de bolhas.
# 1. Procuramos o maior valor em cada passagem e o movemos em direção ao topo.
# 2. Portanto, após a primeira passagem, o maior valor estará no topo.
# 3. Após a segunda passagem, o segundo maior valor estará próximo ao valor superior.
# 4. Conforme o algoritmo avança, os valores subsequentes irão se mover para seus
#    lugares corretos com base em seus valores.
# -------------------------------------------------------------------------
def SelectionSort(lst):
    for ind in range(len(lst) - 1, 0, -1):
        maior = 0
        for loc in range(1, ind + 1):
            if lst[loc] > lst[maior]:
                maior = loc
        lst[ind], lst[maior] = lst[maior], lst[ind]


lst = [45, 32, 23, 4, 67, 12, 34, 67, 45, 10, 2, 1, 2]
SelectionSort(lst)
print(lst)
