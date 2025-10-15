# EJERCICIO 1
# Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

import random

# Creamos una lista vacía
lista = []

# Creamos un while que salga cuando la lista tenga 10 elementos
while len(lista) < 10:
    # Guardamos un número random entre el 0-100
    num = random.randint(0, 101)
    # Lo añadimos a la lista
    lista.append(num)

# Imprimimos la lista
print(lista)