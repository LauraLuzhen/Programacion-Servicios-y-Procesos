# main.py
import time
import multiprocessing
from suma import suma

if __name__ == "__main__":
    n = int(input("Introduce un número: "))

    inicio = time.time()

    # Creamos un valor compartido y un lock
    manager = multiprocessing.Manager()
    valor_compartido = manager.Value('i', 0)  # valor inicial 0
    lock = manager.Lock()

    procesos = []

    for i in range(1, n + 1):
        p = multiprocessing.Process(target=suma, args=(i, valor_compartido, lock, i))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    fin = time.time()
    print(f"Suma total de 1 a {n}: {valor_compartido.value}")
    print(f"Tiempo total de ejecución: {fin - inicio:.2f} segundos")
