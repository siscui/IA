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
                    --image=' + image_path

print("Detectando especie...")


def getresult(input_process):
    output = input_process.communicate()[0]
    output = output.decode()
    result = output.split('\n')
    return result[0]


process_detection = subprocess.Popen(detectarEspecie, stdout=subprocess.PIPE, stderr=None, shell=True)

detection = getresult(process_detection)

detected_species = detection.split(' ')[0]
print("especie detectada " + detection)

if detected_species == 'tomate' or detected_species == 'morron':
    print("Analizando madurez...")
    detectarMadurez = 'python label_image.py \
                    --graph=modelos/madurez_' + detected_species + '_graph.pb \
                    --labels=modelos/madurez_' + detected_species + '_labels.txt \
                    --input_layer=Placeholder \
                    --output_layer=final_result \
                    --image=' + image_path

    process_mature = subprocess.Popen(detectarMadurez, stdout=subprocess.PIPE, stderr=None, shell=True)

    mature = getresult(process_mature)
    print(mature)
