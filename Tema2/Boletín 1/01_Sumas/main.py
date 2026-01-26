# main.py
import time
import multiprocessing
from suma import suma

if __name__ == "__main__":
    n = int(input("Introduce un número: "))

    inicio = time.time()

    manager = multiprocessing.Manager()
    valor_compartido = manager.Value('i', 0)
    lock = manager.Lock()

    procesos = []

    print(f"Suma de 1 a {n}")

    for i in range(1, n + 1):
        p = multiprocessing.Process(target=suma, args=(i, valor_compartido, lock))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()
    
    fin = time.time()

    print(f"Resultado final: {valor_compartido.value}")
    print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
