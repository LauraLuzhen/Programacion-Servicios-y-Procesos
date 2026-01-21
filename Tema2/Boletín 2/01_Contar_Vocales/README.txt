EJERCICIO MULTIPROCESSING – CONTAR VOCALES

Este programa cuenta cuántas veces aparece cada vocal en un fichero de texto
utilizando procesos en paralelo.

Archivos:
- main.py: crea un proceso por cada vocal y mide el tiempo de ejecución.
- vocales.py: función que cuenta una vocal en el fichero.
- texto.txt: texto sobre el que se realiza el conteo.
- README.txt: descripción del ejercicio.

Funcionamiento:
1. Se lanza un proceso por cada vocal (a, e, i, o, u).
2. Cada proceso cuenta su vocal en el fichero.
3. Los resultados se envían al proceso principal mediante una cola.
4. Se muestran los resultados y el tiempo total.

Ejecución:
python main.py
