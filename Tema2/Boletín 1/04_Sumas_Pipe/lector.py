# lector.py
def leer_fichero(ruta, pipe):
    """Lee números del fichero y los envía por la pipe."""
    with open(ruta, "r") as f:
        for linea in f:
            numero = int(linea.strip())
            pipe.send(numero)
    # Señal de fin
    pipe.send(None)
