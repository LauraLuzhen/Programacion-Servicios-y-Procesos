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

    procesos = []

    # Crear un proceso para cada rango
    for idx, (a, b) in enumerate(rangos, start=1):
        p = multiprocessing.Process(target=suma_rango, args=(a, b))
        procesos.append(p)
        p.start()

    # Esperar a que todos los procesos terminen
    for p in procesos:
        p.join()

    print("Todos los procesos han terminado")
