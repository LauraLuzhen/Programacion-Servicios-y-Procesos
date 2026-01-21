# main.py
import time
import multiprocessing
import os
from lector import leer_fichero
from suma import sumar_desde_pipe

if __name__ == "__main__":
    inicio = time.time()

    # Crear Pipe (dos extremos)
    parent_conn, child_conn = multiprocessing.Pipe()

    # Ruta absoluta del fichero
    fichero_numeros = os.path.join(os.path.dirname(__file__), "numeros.txt")

    # Crear procesos
    p_lector = multiprocessing.Process(target=leer_fichero, args=(fichero_numeros, child_conn))
    p_suma = multiprocessing.Process(target=sumar_desde_pipe, args=(parent_conn,))

    # Iniciar procesos
    p_lector.start()
    p_suma.start()

    # Esperar a que terminen
    p_lector.join()
    p_suma.join()

    fin = time.time()
    print("Todos los procesos han terminado")
    print(f"Tiempo total de ejecución: {fin - inicio:.2f} segundos")
