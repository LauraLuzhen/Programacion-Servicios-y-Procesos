# lector.py
def leer_fichero(ruta, pipe):
    with open(ruta, "r") as f:
        for linea in f:
            numero = int(linea.strip())
            pipe.send(numero)
    pipe.send(None)
