# lector.py
def leer_fichero(ruta, pipe):
    with open(ruta, "r") as f:
        for linea in f:
            a, b = map(int, linea.strip().split())
            pipe.send((a, b))
    pipe.send(None)
