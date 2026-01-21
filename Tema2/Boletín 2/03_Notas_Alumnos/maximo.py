# maximo.py
def obtener_maximo(fichero_medias="medias.txt"):
    """Lee medias.txt y muestra la nota máxima con su alumno"""
    max_nota = -1
    alumno_max = ""
    with open(fichero_medias, "r", encoding="utf-8") as f:
        for linea in f:
            nota_str, alumno = linea.strip().split()
            nota = float(nota_str)
            if nota > max_nota:
                max_nota = nota
                alumno_max = alumno
    print(f"Nota máxima: {max_nota} - Alumno: {alumno_max}")
