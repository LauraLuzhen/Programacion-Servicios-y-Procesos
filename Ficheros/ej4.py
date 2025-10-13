# EJERCICIO 4
# Implementa un programa que lea números enteros no ordenados de un archivo, con 
# un número por línea, y los almacene en una lista. A continuación, debe guardar los
# números de la lista en otro fichero distinto pero ordenados de forma ascendente.

lista = []

f = open('./Ficheros/ficheros/numeros_aleatorios.txt', 'rt')
for linea in f:
    linea = linea.replace(" ", "")
    lista.append(linea)
f.close()

lista.sort()

for el in lista:
    print(el)