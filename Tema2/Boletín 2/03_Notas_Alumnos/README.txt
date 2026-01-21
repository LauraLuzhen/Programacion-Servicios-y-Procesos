EJERCICIO MULTIPROCESSING – NOTAS DE ALUMNOS

Objetivo:
Generar notas aleatorias para 10 alumnos, calcular sus medias y obtener la nota máxima usando multiprocessing.

Archivos:
- main.py: Programa principal. Contiene versión con Process y con Pool.
- generador.py: Genera 6 notas aleatorias por alumno y las guarda en un fichero.
- media.py: Calcula la media de las notas de un fichero y la guarda en medias.txt.
- maximo.py: Obtiene la nota máxima de medias.txt y muestra el alumno correspondiente.
- datos/: Carpeta donde se guardan los ficheros Alumno1.txt ... Alumno10.txt.

Funcionamiento:
1. Se generan 10 ficheros con notas aleatorias (Proceso 1).
2. Se calculan las medias de cada alumno y se guardan en medias.txt (Proceso 2).
3. Se obtiene la nota máxima y el alumno correspondiente (Proceso 3).

Ejecución:
python main.py
