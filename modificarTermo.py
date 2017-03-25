# -*- coding: utf-8 -*-

import os

def trocarTexto(dir, arq, orig, troca):
    dirCompl = os.path.join(dir, arq)
    with open(dirCompl, 'r+') as file:
        lines = file.readlines()
        index = repr(lines).find(orig) - 1
        if index > 0:
            file.seek(0)
            for line in lines:
                line = line.replace(orig, troca)
                file.write(line)

def paraSubPasta(dirRaiz, pasta):
    dirCompl = os.path.join(dirRaiz, pasta)
    if (os.path.isdir(dirCompl)):
        for arqProc in os.listdir(dirCompl):
            trocarTexto(dirCompl, arqProc, 'Curso de Java', 'Curso de Vue.js')

def listar_arquivos():
    dirRaiz = '/home/fernando/Aplicativos/Teste'
    for pasta in os.listdir(dirRaiz):
        paraSubPasta(dirRaiz, pasta)

if __name__ == '__main__':
    listar_arquivos()