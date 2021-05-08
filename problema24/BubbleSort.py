# -------------------------------------------------------------------------
# 1. O objetivo é colocar o valor mais alto no topo da lista.
# Veremos o valor mais alto da lista borbulhando até o topo
# conforme o progresso um.
# 2. A classificação por bolha compara os valores dos vizinhos
# adjacentes. Se o valor em uma posição superior for maior do
# que o valor em um índice inferior, trocamos os valores.
# Essa iteração continua até chegarmos ao final da lista.
# -------------------------------------------------------------------------
def BubbleSort(lst):
    ultElemento = len(lst) - 1
    for cto in range(ultElemento, 0, -1):
        for ind in range(cto):
            if lst[ind] > lst[ind+1]:
                lst[ind], lst[ind+1] = lst[ind+1], lst[ind]
    return lst


lst = [45, 32, 23, 4, 67, 12, 34, 67, 45, 10, 2, 1, 2]
BubbleSort(lst)
print(lst)
