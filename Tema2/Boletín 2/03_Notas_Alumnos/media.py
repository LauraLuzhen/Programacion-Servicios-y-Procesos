# media.py
def calcular_media(fichero_notas, nombre_alumno, fichero_medias="medias.txt"):
    """Lee notas de un fichero, calcula la media y guarda en medias.txt"""
    with open(fichero_notas, "r", encoding="utf-8") as f:
        notas = [float(linea.strip()) for linea in f]
        media = round(sum(notas)/len(notas), 2)

    # Guardar la media en el fichero medias.txt (append)
    with open(fichero_medias, "a", encoding="utf-8") as f:
        f.write(f"{media} {nombre_alumno}\n")
