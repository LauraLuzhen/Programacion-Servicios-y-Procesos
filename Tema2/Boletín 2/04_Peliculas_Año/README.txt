EJERCICIO MULTIPROCESSING – FILTRADO DE PELÍCULAS POR AÑO

Este programa utiliza dos procesos que se comunican mediante una cola (Queue):

Proceso 1 (lector.py):
- Lee un fichero con películas en formato Nombre;Año.
- Filtra solo las películas del año indicado por el usuario.
- Envía estas películas al Proceso 2 mediante la cola.

Proceso 2 (escritor.py):
- Recibe las películas filtradas de la cola.
- Las guarda en un fichero llamado peliculasYYYY.txt donde YYYY es el año introducido.

Archivos:
- main.py: solicita año y ruta, lanza los procesos y mide tiempo de ejecución.
- lector.py: filtra las películas.
- escritor.py: guarda las películas filtradas.
- peliculas.txt: ejemplo de fichero con películas.
- README.txt: descripción del ejercicio.

Ejecución:
python main.py

Nota:
- Introduce el año como un número entero.
- Introduce la ruta al fichero relativa al proyecto, por ejemplo: 'peliculas.txt' o 'datos/peliculas.txt'.
