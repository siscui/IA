#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys

image_path = sys.argv[1]

detectarEspecie = 'python label_image.py \
					--graph=modelos/especies_graph.pb \
					--labels=modelos/especies_labels.txt \
					--input_layer=Placeholder \
					--output_layer=final_result \
					--image='+image_path

print("Detectando especie...")
process = subprocess.Popen(detectarEspecie, stdout=subprocess.PIPE, stderr=None, shell=True)

output = process.communicate()

result = str(output[0])
result = result.split('\n')
deteccion = result[0]

print(deteccion)

especieDetectada = deteccion.split(' ')[0]

if (especieDetectada=='tomate' or especieDetectada=='morron'):
	print("Analizando madurez...")
	detectarMadurez = 'python label_image.py \
					--graph=modelos/madurez_'+ especieDetectada +'_graph.pb \
					--labels=modelos/madurez_'+ especieDetectada +'_labels.txt \
					--input_layer=Placeholder \
					--output_layer=final_result \
					--image='+image_path
	
	process = subprocess.Popen(detectarMadurez, stdout=subprocess.PIPE, stderr=None, shell=True)

	output = process.communicate()
	result = str(output[0])
	result = result.split('\n')
	madurez = result[0]

	print(madurez)
