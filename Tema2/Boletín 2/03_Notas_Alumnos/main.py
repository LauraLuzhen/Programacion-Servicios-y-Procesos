# main.py
import os
import time
import multiprocessing
from generador import generar_notas
from media import calcular_media
from maximo import obtener_maximo

def main():
    inicio = time.time()

    # Crear carpeta 'datos' si no existe
    carpeta = "datos"
    os.makedirs(carpeta, exist_ok=True)

    # Limpiar medias.txt si existe
    fichero_medias = "medias.txt"
    if os.path.exists(fichero_medias):
        os.remove(fichero_medias)

    # --- PROCESO 1: Generar notas ---
    procesos_generar = []
    for i in range(1, 11):
        fichero = os.path.join(carpeta, f"Alumno{i}.txt")
        p = multiprocessing.Process(target=generar_notas, args=(fichero,))
        procesos_generar.append(p)
        p.start()

    for p in procesos_generar:
        p.join()

    # --- PROCESO 2: Calcular medias ---
    procesos_media = []
    for i in range(1, 11):
        fichero = os.path.join(carpeta, f"Alumno{i}.txt")
        nombre_alumno = f"Alumno{i}"
        p = multiprocessing.Process(target=calcular_media, args=(fichero, nombre_alumno))
        procesos_media.append(p)
        p.start()

    for p in procesos_media:
        p.join()

    # --- PROCESO 3: Obtener nota máxima ---
    obtener_maximo(fichero_medias)

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio:.4f} segundos")


# --- Versión usando Pool ---
def main_pool():
    inicio = time.time()

    carpeta = "datos"
    os.makedirs(carpeta, exist_ok=True)

    fichero_medias = "medias.txt"
    if os.path.exists(fichero_medias):
        os.remove(fichero_medias)

    # PROCESO 1: Generar notas
    lista_ficheros = [os.path.join(carpeta, f"Alumno{i}.txt") for i in range(1, 11)]
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(generar_notas, lista_ficheros)

    # PROCESO 2: Calcular medias
    args = [(lista_ficheros[i], f"Alumno{i+1}") for i in range(10)]
    with multiprocessing.Pool(processes=4) as pool:
        pool.starmap(calcular_media, args)

    # PROCESO 3: Obtener nota máxima
    obtener_maximo(fichero_medias)

    fin = time.time()
    print(f"Tiempo total de ejecución con Pool: {fin - inicio:.4f} segundos")


if __name__ == "__main__":
    print("=== Versión con Process + for ===")
    main()
    print("\n=== Versión con Pool ===")
    main_pool()
