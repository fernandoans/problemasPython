# -*- coding: utf-8 -*-

#!/usr/bin/env python

from gimpfu import *
import math

def run(img, layer, angulo, qtd, xCentro, yCentro, merge):
	pdb.gimp_image_undo_group_start(img)
	for x in range(0, qtd):
		newLayer = pdb.gimp_layer_copy(layer, pdb.gimp_drawable_has_alpha(layer))
		pdb.gimp_image_insert_layer(img, newLayer, None, -1)
		newLayer = pdb.gimp_item_transform_rotate(newLayer, angulo * math.pi / 180 / qtd * (x + 1), False, xCentro, yCentro)
	if merge:
		for x in range(0, qtd):
			drawable = pdb.gimp_image_get_active_drawable(img)
			layer = pdb.gimp_image_merge_down(img, drawable, CLIP_TO_BOTTOM_LAYER)	
		
	pdb.gimp_image_undo_group_end(img)

register(
    "girarduplica",
    "Girar e Duplicar",
    "Girar a imagem através da duplicação de camadas",
    "Original: Kota Weaver",
    "Adaptado: Fernando Anselmo",
    "Junho de 2016",
    "<Image>/Filters/Fernando/Girar Duplicar...", "",
    [
        (PF_FLOAT, "angulo", "Angulo de Rotação", 180.0),
        (PF_INT,   "qtd", "Quantidade de camadas", 1),
        (PF_FLOAT, "xCentro", "Centro Horizontal para Rotação", 0.0),
        (PF_FLOAT, "yCentro", "Centro Vertical para Rotação", 0.0),
        (PF_BOOL,  "merge", "Juntar imagens", False)
    ], [], run)

main()
