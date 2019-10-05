#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys


def getresult(model):
    input_process = subprocess.Popen(model, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = input_process.communicate()[0]
    output = output.decode()
    result = output.split('\n')
    return result[0]


def detect_specie(image_path):
    detectarEspecie = 'python label_image.py \
                    --graph=modelos/especies_graph.pb \
                    --labels=modelos/especies_labels.txt \
                    --input_layer=Placeholder \
                    --output_layer=final_result \
                    --image=' + image_path
    detection = getresult(detectarEspecie)
    detected_species = detection.split(' ')[0]
    return detected_species


def detected_mature(detected_species):
    if detected_species == 'tomate' or detected_species == 'morron':
        # print("Analizando madurez...")
        detectarMadurez = 'python label_image.py \
                    --graph=modelos/madurez_' + detected_species + '_graph.pb \
                    --labels=modelos/madurez_' + detected_species + '_labels.txt \
                    --input_layer=Placeholder \
                    --output_layer=final_result \
                    --image=' + image_path

        mature = getresult(detectarMadurez)
        # detected_matures = mature.split(' ')[0]
        return mature


image_path = sys.argv[1]
# print("Detectando especie...")

result_detection = detect_specie(image_path)
# print("especie detectada " + result_detection)
print(result_detection)

result_mature = detected_mature(result_detection)
print(result_mature)
