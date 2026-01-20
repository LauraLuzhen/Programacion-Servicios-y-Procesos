# lector.py
def leer_fichero(ruta, cola):
    with open(ruta, "r") as f:
        for linea in f:
            numero = int(linea.strip())
            cola.put(numero)
    # Señal de fin
    cola.put(None)
