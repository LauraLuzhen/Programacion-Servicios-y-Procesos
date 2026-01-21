EJERCICIO MULTIPROCESSING – FILTRADO DE PELÍCULAS POR AÑO

Este programa utiliza dos procesos que se comunican mediante una cola (Queue):

Proceso 1:
- Lee un fichero con películas (Nombre;Año)
- Filtra las películas del año indicado por el usuario
- Envía los resultados al Proceso 2

Proceso 2:
- Recibe las películas filtradas
- Las guarda en un fichero llamado peliculasYYYY.txt donde YYYY es el año

Archivos:
- main.py: solicita año y ruta, lanza los procesos y mide tiempo de ejecución
- filtro.py: filtra las películas por año
- guardar.py: guarda las películas filtradas
- peliculas.txt: fichero de ejemplo con películas
- README.txt: descripción del ejercicio

Ejecución:
python main.py
