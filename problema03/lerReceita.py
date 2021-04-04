# -*- coding: utf-8 -*-

# -----------------------------------------------------------------
# Arquivo para o Vídeo Problemas em Python 03
# Disponivel em https://www.youtube.com/watch?v=w-24ojvvvuM&t=25s
# Autor: Fernando Anselmo
# Compilado com Python 3.5.1
# -----------------------------------------------------------------

import requests

def montarIngredientes(linha):
    print('"ingredientes":[')
    for ingr in linha.split('<li class="columns small-6">'):
        if len(ingr[0:ingr.find('</')].strip()) > 0:
            ingr = ' "' + ingr[0:ingr.find('</')].strip() + '",'
            print(ingr)
    print("],")

def montarPreparacao(linha):
    print('"preparacao":[')
    for prep in linha.split('<li class="mb10"><span class="fcg fwn">'):
        if len(prep[0:prep.find('</')].strip()) > 0:
            prep = ' "' + prep[0:prep.find('</')].strip() + '",'
            print(prep)
    print("]}")

def montarTitulo(linha):
    linha = '{"titulo":"' + linha + '", '
    print(linha)

def lerSite():
    link = 'http://oquehaparacomer.com.br/panquecas-de-ab%C3%B3bora'
    f = requests.get(link)
    titulo = False
    ingredientes = False
    preparacao = False

    for line in f.text.splitlines():
        if titulo:
            montarTitulo(line.strip())
            titulo = False
        if ingredientes:
            montarIngredientes(line.strip())
        if preparacao:
            montarPreparacao(line.strip())

        if ingredientes and '</ul>' in line:
            ingredientes = False
        if preparacao and '</ol>' in line:
            preparacao = False

        if line.strip() == '<span style="display:block;font-size:35px;" class="mb10 pacifico">':
            titulo = True
        if line.strip() == '<ul style="list-style:inside;" class="row ">':
            ingredientes = True
        if line.strip() == '<div class="bulle hide-for-medium-down"></div>':
            preparacao = True

if __name__ == '__main__':
    lerSite()


















