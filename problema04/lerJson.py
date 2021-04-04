# -*- coding: utf-8 -*-

# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 04
# Disponivel em https://www.youtube.com/watch?v=Q6tCYjkJjBw&t=25s
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

from datetime import datetime
import json

def processarJson(linha):
    json_data = json.loads(linha)
    print(json_data['Title'], json_data['Season'])
    for eps in json_data['Episodes']:
        dt = datetime.strptime(eps['Released'], '%Y-%m-%d')
        print(' Episódio: E%s %s liberado em %s' %
            (eps['Episode'], eps['Title'], dt.strftime('%d/%m/%Y')))

def lerArquivo():
    arq = '/home/fernando/Aplicativos/serie'
    entrada = open(arq, 'r+', encoding='UTF-8')
    for linha in entrada:
        processarJson(linha)

if __name__ == '__main__':
    lerArquivo()