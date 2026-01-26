# main.py
import time
import multiprocessing
from suma import suma

if __name__ == "__main__":
    n = int(input("Introduce un número: "))

    manager = multiprocessing.Manager()
    valor_compartido = manager.Value('i', 0)
    lock = manager.Lock()

    print(f"Suma de 1 a {n}")

    for num_procesos in [1, 2, 4]:
        valor_compartido.value = 0  
        inicio = time.time()

        with multiprocessing.Pool(processes=num_procesos) as pool:
            pool.starmap(
                suma,
                [(i, valor_compartido, lock) for i in range(1, num_procesos + 1)]
            )

        fin = time.time()

        print(f"Suma total: {valor_compartido.value}")
        print(f"Tiempo: {fin - inicio:.2f} segundos")
