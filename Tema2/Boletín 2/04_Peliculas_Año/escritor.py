# escritor.py
import os

def guardar_peliculas(cola, año):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    nombre_fichero = os.path.join(base_dir, f"peliculas{año}.txt")

    with open(nombre_fichero, "w", encoding="utf-8") as f:
        while True:
            pelicula = cola.get()
            if pelicula is None:
                break
            f.write(pelicula + "\n")
    print(f"Fichero '{nombre_fichero}' creado con éxito.")
