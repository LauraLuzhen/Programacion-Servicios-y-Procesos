# filtro.py
def filtrar_por_año(ruta_fichero, año, cola):
    """Lee el fichero y envía al proceso siguiente solo las películas del año indicado"""
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
    # Señal de fin
    cola.put(None)
