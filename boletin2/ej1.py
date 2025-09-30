# Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 
import random;

lista = []

while len(lista) < 10:
    lista.append(random.randint(1, 101))

print(lista)