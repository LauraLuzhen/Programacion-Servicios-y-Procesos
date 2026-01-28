# main.py
import time
import multiprocessing
from generador import generar_ips
from filtro import filtrar_ips
from clasificador import mostrar_ips

if __name__ == "__main__":
    inicio = time.time()

    cola1 = multiprocessing.Queue()
    cola2 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=generar_ips, args=(cola1,))
    p2 = multiprocessing.Process(target=filtrar_ips, args=(cola1, cola2))
    p3 = multiprocessing.Process(target=mostrar_ips, args=(cola2,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio:.2f} segundos")
