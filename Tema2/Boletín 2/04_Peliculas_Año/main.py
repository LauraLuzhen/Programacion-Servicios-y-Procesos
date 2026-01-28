# main.py
import os
import time
import multiprocessing
from lector import leer_peliculas
from escritor import guardar_peliculas

def main():
    while True:
        try:
            año = int(input("Introduce un año menor o igual al actual: "))
            if año > 2026 or año < 1800:
                print("Introduce un año válido (entre 1800 y 2026).")
                continue
            break
        except ValueError:
            print("Debes introducir un número entero para el año.")

    while True:
        ruta = input("Introduce la ruta del fichero de películas (ej: peliculas.txt): ").strip()
        if os.path.exists(ruta) and os.path.isfile(ruta):
            break
        print("Ruta no válida. Asegúrate de que el fichero existe y escribe algo como 'peliculas.txt' o 'carpeta/peliculas.txt'.")

    inicio = time.time()

    cola = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=leer_peliculas, args=(ruta, año, cola))
    p2 = multiprocessing.Process(target=guardar_peliculas, args=(cola, año))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin:.4f} segundos")

if __name__ == "__main__":
    main()
