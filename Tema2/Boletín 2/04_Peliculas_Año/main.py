# main.py
import multiprocessing
from filtro import filtrar_por_año
from guardar import guardar_peliculas
import os
import time

if __name__ == "__main__":
    # Solicitar datos al usuario
    año = int(input("Introduce un año menor o igual al actual: "))
    ruta_fichero = input("Introduce la ruta al fichero de películas: ")

    if not os.path.exists(ruta_fichero):
        print("El fichero no existe.")
        exit()

    inicio = time.time()

    # Crear cola para comunicación
    cola = multiprocessing.Queue()

    # Crear procesos
    p1 = multiprocessing.Process(target=filtrar_por_año, args=(ruta_fichero, año, cola))
    p2 = multiprocessing.Process(target=guardar_peliculas, args=(cola, año))

    # Iniciar procesos
    p1.start()
    p2.start()

    # Esperar a que terminen
    p1.join()
    p2.join()

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio:.4f} segundos")
