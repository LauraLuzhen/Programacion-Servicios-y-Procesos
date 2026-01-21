# main.py
import multiprocessing
from suma import suma_rango

if __name__ == "__main__":
    # Lista de rangos a sumar 
    rangos = [
        (1, 5),
        (10, 7),
        (3, 3),
        (6, 12)
    ]

    print("Iniciando Pool de procesos...")

    # Crear Pool de procesos
    with multiprocessing.Pool(processes=4) as pool:
        # Usamos starmap porque la función tiene 2 argumentos
        pool.starmap(suma_rango, rangos)

    print("Todos los procesos han terminado")
