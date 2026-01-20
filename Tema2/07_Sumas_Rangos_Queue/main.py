# main.py
import time
import multiprocessing
import os
from lector import leer_fichero
from suma import sumar_desde_cola

if __name__ == "__main__":
    inicio = time.time()

    cola = multiprocessing.Queue()

    fichero_numeros = os.path.join(os.path.dirname(__file__), "numeros.txt")

    p_lector = multiprocessing.Process(target=leer_fichero, args=(fichero_numeros, cola))
    p_suma = multiprocessing.Process(target=sumar_desde_cola, args=(cola,))

    p_lector.start()
    p_suma.start()

    p_lector.join()
    p_suma.join()

    fin = time.time()
    print(f"Todos los procesos han terminado")
    print(f"Tiempo total de ejecución: {fin - inicio:.2f} segundos")
