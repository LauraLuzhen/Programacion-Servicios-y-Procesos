# lector.py
def leer_fichero(ruta, cola):
    with open(ruta, "r") as f:
        for linea in f:
            a, b = map(int, linea.strip().split())
            cola.put((a, b))
    cola.put(None)
