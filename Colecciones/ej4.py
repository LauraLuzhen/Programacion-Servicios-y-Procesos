# EJERCICIO 4
# Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.

import random

# Creamos una variable que guarde la longitud de la lista
cont = 10
# Creamos una lista vacía
lista = []

# Creamos un while que añada la cantidad de elementos indicada en el contador a la lista
while len(lista) < cont:
    # Generamos un número random del 0-100
    num = random.randint(0, 101)
    # Lo añadimos a la lista
    lista.append(num)

# Ordenamos la lista
lista.sort()
# Mostramos la lista
print(lista)