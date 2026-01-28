# lector.py
def leer_peliculas(ruta_fichero, año, cola):
    try:
        with open(ruta_fichero, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    nombre, año_str = linea.split(";")
                    if int(año_str) == año:
                        cola.put(nombre)
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Error: el fichero '{ruta_fichero}' no existe.")
    
    cola.put(None)
