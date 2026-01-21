# vocales.py
def contar_vocal(vocal, ruta_fichero, cola):
    with open(ruta_fichero, "r", encoding="utf-8") as f:
        texto = f.read().lower()
        cantidad = texto.count(vocal)
        cola.put((vocal, cantidad))
