# Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10. 
# Luego pedirá un valor N y mostrará cuántas veces aparece N. 

import random

# Creamos un variable que será el tamaño de la lista
cont = 100
# Creamos una variable que guarde el número de veces que se repite el númeor N
num_veces = 0
# Creamos una lista vacía
lista = []

# Creamos un while que añada la cantidad de elementos indicada en el contador a la lista
while len(lista) < cont:
    # Generamos un número random del 1-10
    num = random.randint(1, 11)
    # Lo añadimos a la lista
    lista.append(num)

# Le pedimos un número al usuario
n = int(input('Introduce un número(1-10):'))

# Comprobamos que esté en el rango
while n<1 or n>10:
    n = int(input('Introduce un número(1-10):'))

# Contamos el número de veces que aparece el número N
for i in range(1, cont, 1):
    if lista[i] == n:
        num_veces += 1

# Imprimimos el resultado
print('El número', n, 'aparece un total de', num_veces, 'veces')