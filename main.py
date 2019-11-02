#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys


def getresult(model):
    input_process = subprocess.Popen(model, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = input_process.communicate()[0]
    output = output.decode()
    result = output.split('\n')
    # print(result)
    return result[0]


# def detect_specie(image_path):
#     detectarEspecie = 'python label_image.py \
#                     --graph=modelos/especies_graph.pb \
#                     --labels=modelos/especies_labels.txt \
#                     --input_layer=Placeholder \
#                     --output_layer=final_result \
#                     --image=' + image_path
#     detection = getresult(detectarEspecie)
#     detected_species = detection.split(' ')[0]
#     return detected_species


# MobileNet 100-160
# python -m scripts.label_image --graph=modelos\detect_specie_mobilenet_100_160.pb --image=clasificar\morron1.jpg
def detect_specie(image_path):
    detectarEspecie = 'python -m scripts.label_image \
                    --graph=modelos\detect_specie_mobilenet_100_160.pb \
                    --labels=modelos\detect_specie_mobilenet_100_160.txt \
                    --image=' + image_path
    detection = getresult(detectarEspecie)
    detected_species = detection.split(' ')[0]
    return detected_species


# def detected_mature(detected_species):
#     if detected_species == 'tomate' or detected_species == 'morron':
#         # print("Analizando madurez...")
#         detectarMadurez = 'python label_image.py \
#                     --graph=modelos/madurez_' + detected_species + '_graph.pb \
#                     --labels=modelos/madurez_' + detected_species + '_labels.txt \
#                     --input_layer=Placeholder \
#                     --output_layer=final_result \
#                     --image=' + image_path
#
#         mature = getresult(detectarMadurez)
#         # detected_matures = mature.split(' ')[0]
#         return mature


# MobileNet 100-160
# python -m scripts.label_image --graph=tf_files\detect_specie_mobilenet_100_160.pb --image=tf_files\cactus1.jpg
# python -m scripts.label_image --graph=tf_files\maduro_tomate_100_160.pb --labels=tf_files\maduro_tomate_100_160.txt --image=tf_files\tomate1.jpg

def detected_mature(detected_species):
    if detected_species == 'tomate':
        # print("Analizando madurez...")
        detectarMadurez = 'python -m scripts.label_image \
                    --graph=modelos\maduro_tomate_100_160.pb \
                    --labels=modelos\maduro_tomate_100_160.txt \
                    --image=' + image_path

        mature = getresult(detectarMadurez)
        detected_matures = mature.split(' ')[0]
        # return mature
        return detected_matures

    if detected_species == 'morron':
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


def analizar_planta(image_path):
    result_detection = detect_specie(image_path)
    result_mature = detected_mature(result_detection)
    result = (result_detection, result_mature)
    return result


image_path = sys.argv[1]
# print("Detectando especie...")

# result_detection = detect_specie(image_path)
# # print("especie detectada " + result_detection)
# print(result_detection)
#
# result_mature = detected_mature(result_detection)
# print(result_mature)

result = analizar_planta(image_path)
print("Resultado de la Tupla: %s" % (result,))
