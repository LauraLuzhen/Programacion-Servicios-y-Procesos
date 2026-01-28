# generador.py
import random

def generar_notas(fichero):
    notas = [round(random.uniform(1, 10), 2) for _ in range(6)]
    with open(fichero, "w", encoding="utf-8") as f:
        for nota in notas:
            f.write(f"{nota}\n")
