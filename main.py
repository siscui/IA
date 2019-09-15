#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys

image_path = sys.argv[1]

detectarEspecie = 'python label_image.py \
					--graph=retrain/especies_graph.pb \
					--labels=retrain/especies_labels.txt \
					--input_layer=Placeholder \
					--output_layer=final_result \
					--image='+image_path

print("Detectando especie...")
process = subprocess.Popen(detectarEspecie, stdout=subprocess.PIPE, stderr=None, shell=True)

output = process.communicate()

result = str(output[0])
result = result.split('\n')
deteccion = result[0]

print("Deteccion: " + deteccion)

especieDetectada = deteccion.split(' ')[0]

if (especieDetectada=='tomate' or especieDetectada=='morron'):
	print("Analizando madurez...")
	detectarMadurez = 'python label_image.py \
					--graph=retrain/madurez_'+ especieDetectada +'_graph.pb \
					--labels=retrain/madurez_'+ especieDetectada +'_labels.txt \
					--input_layer=Placeholder \
					--output_layer=final_result \
					--image='+image_path
	
	process = subprocess.Popen(detectarMadurez, stdout=subprocess.PIPE, stderr=None, shell=True)

	output = process.communicate()
	result = str(output[0])
	result = result.split('\n')
	madurez = result[0]

	print(madurez)