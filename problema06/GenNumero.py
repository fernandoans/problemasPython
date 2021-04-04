# -*- coding: utf-8 -*-

#!/usr/bin/env python

from gimpfu import *
import os

def run(*args):
    arquivo, num, tot, nome, dirSaida, zeros = args
    dirSaida = os.path.expanduser('~/' + dirSaida)
    if not os.path.exists(dirSaida):
        os.makedirs(dirSaida)
    for i in xrange(1, tot+1):
        im = pdb.gimp_file_load(arquivo, arquivo)
        camada = filter(lambda  x: x.name == 'Text', im.layers)[0]
        numStr = str(num)
        pdb.gimp_text_layer_set_text(camada, numStr.zfill(zeros))
        num += 1
        merged = pdb.gimp_image_merge_visible_layers(im, 0)
        nomArqSaida = "%s%d.png" % (nome, i)
        nomCompleto = os.path.join(dirSaida, nomArqSaida)
        pdb.file_png_save_defaults(im, merged, nomCompleto, nomCompleto)

register(
    "gennumero",
    "Gerador de números para uma template",
    "Gerador de números de template",
    "Original: Roman Hwang",
    "Adaptado: Fernando Anselmo",
    "Maio de 2013",
    "<Image>/Filters/Fernando/Gerar Número...", "",
    [
        (PF_FILE,   "arg0", "Arquivo Template", ""),
        (PF_INT,    "arg1", "Primeiro número da sequência", 1),
        (PF_INT,    "arg2", "Total de imagens a gerar", 30),
        (PF_STRING, "arg3", "Nome dos arquivos de saída", ""),
        (PF_STRING, "arg4", "Diretório de saída (relativo a pasta USER)", ""),
        (PF_INT,    "arg5", "Tamanho mínimo do número (completa com zeros)", 1),
    ], [], run)

main()
