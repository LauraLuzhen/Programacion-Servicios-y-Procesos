# lector.py
def leer_fichero(ruta, cola):
    """Lee rangos de un fichero y los introduce en la cola."""
    with open(ruta, "r") as f:
        for linea in f:
            a, b = map(int, linea.strip().split())
            cola.put((a, b))
    # Señal de fin
    cola.put(None)
