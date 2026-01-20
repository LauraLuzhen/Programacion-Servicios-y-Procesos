# lector.py
def leer_fichero(ruta, pipe):
    """Lee rangos de un fichero y los envía por la Pipe."""
    with open(ruta, "r") as f:
        for linea in f:
            a, b = map(int, linea.strip().split())
            pipe.send((a, b))
    # Señal de fin
    pipe.send(None)
