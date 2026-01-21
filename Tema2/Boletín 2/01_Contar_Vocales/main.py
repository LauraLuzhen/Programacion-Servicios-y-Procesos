# main.py
import time
import multiprocessing
import os
from vocales import contar_vocal

if __name__ == "__main__":
    inicio = time.time()

    fichero = os.path.join(os.path.dirname(__file__), "texto.txt")
    vocales = ['a', 'e', 'i', 'o', 'u']

    cola = multiprocessing.Queue()
    procesos = []

    for v in vocales:
        p = multiprocessing.Process(target=contar_vocal, args=(v, fichero, cola))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    while not cola.empty():
        vocal, cantidad = cola.get()
        print(f"La vocal '{vocal}' aparece {cantidad} veces.")

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio:.4f} segundos")
