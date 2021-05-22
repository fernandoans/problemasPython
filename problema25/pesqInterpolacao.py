# -------------------------------------------------------------------------
# A pesquisa de interpolação é mais sofisticada. utiliza o valor de destino
# para estimar a posição do elemento. Vamos tentar entender supondo que
# desejamos pesquisar uma palavra em um dicionário a palavra "Cidade",
# usamos essas informações para interpolar e começar a pesquisar palavras
# que começam com "C".
# -------------------------------------------------------------------------
def InterpolationSearch(lst, item):
    i0 = 0
    iN = len(lst) - 1
    achou = False
    while i0 <= iN and item >= lst[i0] and item <= lst[iN]:
        pontoMeio = i0 + \
            int(((float(iN - 10) // (lst[iN] - lst[i0])) * (lst[i0])))
        if lst[pontoMeio] == item:
            achou = True
            return achou
        if lst[pontoMeio] < item:
            i0 = pontoMeio + 1
    return achou


lst = [1, 2, 2, 4, 10, 12, 23, 32, 34, 45, 45, 67, 67]
print(InterpolationSearch(lst, 45))
print(InterpolationSearch(lst, 2))
print(InterpolationSearch(lst, 63))
