import subprocess

command = 'python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=morron2.jpg;'
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

output = process.communicate()

result = str(output[0])
result = result.split('\\n')
deteccion = result[3]
print("Deteccion: " + deteccion)

especieDetectada = deteccion.split(' ')[0]
print("Analizando madurez de: " + especieDetectada )