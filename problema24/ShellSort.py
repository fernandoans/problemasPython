# -------------------------------------------------------------------------
# 1. Em vez de selecionar vizinhos imediatos,
# usamos elementos que estão em uma lacuna fixa, eventualmente
# classificar uma sublista que consiste em um par de pontos de dados.
# 2. Classificar as sublistas com quatro pontos de dados.
# 3. Nas passagens subsequentes, o número de pontos de dados por sublista
# continua a aumentar e o número de sublistas continua a diminuir até chegar
# a uma situação em que há apenas uma sublista que consiste em todos os pontos de dados.
# -------------------------------------------------------------------------
def ShellSort(lst):
    distancia = len(lst) // 2
    while distancia > 0:
        for i in range(distancia, len(lst)):
            tmp = lst[i]
            j = i
            while j >= distancia and lst[j - distancia] > tmp:
                lst[j] = lst[j - distancia]
                j -= distancia
            lst[j] = tmp
        distancia //= 2
    return lst


lst = [45, 32, 23, 4, 67, 12, 34, 67, 45, 10, 2, 1, 2]
ShellSort(lst)
print(lst)
