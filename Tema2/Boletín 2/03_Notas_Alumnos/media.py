# media.py
def calcular_media(fichero_notas, nombre_alumno, fichero_medias="medias.txt"):
    with open(fichero_notas, "r", encoding="utf-8") as f:
        notas = [float(linea.strip()) for linea in f]
        media = round(sum(notas)/len(notas), 2)

    with open(fichero_medias, "a", encoding="utf-8") as f:
        f.write(f"{media} {nombre_alumno}\n")
