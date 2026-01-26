# main.py
import multiprocessing
from suma import suma_rango

if __name__ == "__main__":
    rangos = [
        (1, 5),
        (10, 7),
        (3, 3),
        (6, 12)
    ]

    with multiprocessing.Pool(processes=4) as pool:
        pool.starmap(suma_rango, rangos)
