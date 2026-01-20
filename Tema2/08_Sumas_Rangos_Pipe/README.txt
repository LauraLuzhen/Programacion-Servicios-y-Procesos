EJERCICIO MULTIPROCESSING CON PIPE – SUMA DE RANGOS DESDE FICHERO

Este programa utiliza dos procesos que se comunican mediante una tubería (Pipe).

- Un proceso lee rangos de números desde un fichero (numeros.txt) y los envía por pipe.send().
- Otro proceso recibe los rangos con pipe.recv() y realiza la suma acumulativa entre los valores.
- Cuando el proceso lector termina, envía None para indicar al sumador que finalice.

Archivos:
- main.py: crea la Pipe y lanza los procesos.
- lector.py: lee los rangos del fichero y los envía por la Pipe.
- suma.py: recibe los rangos y realiza la suma.
- numeros.txt: contiene dos números por línea, separados por espacio.
- README.txt: descripción del ejercicio.

Ejecución:
python main.py
