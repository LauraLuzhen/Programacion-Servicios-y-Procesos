# guardar.py
import os

def guardar_peliculas(cola, año):
    """Recibe películas desde la cola y las guarda en peliculasYYYY.txt"""
    nombre_fichero = f"peliculas{año}.txt"
    with open(nombre_fichero, "w", encoding="utf-8") as f:
        while True:
            pelicula = cola.get()
            if pelicula is None:
                break
            f.write(pelicula + "\n")
    print(f"Fichero {nombre_fichero} creado con éxito.")
