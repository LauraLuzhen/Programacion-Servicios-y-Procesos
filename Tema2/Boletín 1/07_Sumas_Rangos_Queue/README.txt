EJERCICIO MULTIPROCESSING CON QUEUE – SUMA DE RANGOS DESDE FICHERO

Este programa utiliza dos procesos que se comunican mediante una cola (Queue).

- Un proceso lee rangos de números desde un fichero (numeros.txt) y los mete en la cola.
- Otro proceso toma los rangos de la cola y realiza la suma acumulativa entre los valores.
- Cuando el proceso lector termina, introduce None para indicar al sumador que finalice.

Archivos:
- main.py: crea la cola y lanza los procesos.
- lector.py: lee los rangos del fichero y los mete en la cola.
- suma.py: recibe los rangos y realiza la suma.
- numeros.txt: contiene dos números por línea, separados por espacio.
- README.txt: descripción del ejercicio.

Ejecución:
python main.py
