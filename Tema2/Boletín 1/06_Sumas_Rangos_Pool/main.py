# main.py
import multiprocessing
from suma import suma
import time

if __name__ == "__main__":
    n1 = int(input("Introduce el inicio del rango (n1): "))
    n2 = int(input("Introduce el fin del rango (n2): "))

    if n1 > n2:
        primero = n2
        segundo = n1
    else:
        primero = n1
        segundo = n2
    
    print(f"Sumando desde {primero} hasta {segundo}")

    inicio = time.time()

    manager = multiprocessing.Manager()
    valor_compartido = manager.Value('i', primero)
    lock = manager.Lock()

    inicio = time.time()

    num_pocesos = segundo-primero

    with multiprocessing.Pool(processes=num_pocesos) as pool:
        pool.starmap(
            suma,
            [(i, valor_compartido, primero + i, lock) for i in range(1, num_pocesos + 1)]
        )
        

    fin = time.time()

    print(f"Resultado final: {valor_compartido.value}")
    print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")