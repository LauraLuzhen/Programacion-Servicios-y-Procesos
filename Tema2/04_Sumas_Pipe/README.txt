EJERCICIO MULTIPROCESSING CON PIPE

Este programa utiliza dos procesos que se comunican mediante una tubería (Pipe).

- Un proceso lee números desde un fichero (numeros.txt) y los envía usando pipe.send().
- Otro proceso recibe los números con pipe.recv() y realiza la suma acumulativa.
- Cuando el proceso lector termina, envía None para indicar al sumador que finalice.

Archivos:
- main.py: crea la Pipe y lanza los procesos.
- lector.py: lee los números del fichero y los envía por la Pipe.
- suma.py: recibe los números y realiza la suma acumulativa.
- numeros.txt: contiene un número por línea.
- README.txt: descripción del ejercicio.

Ejecución:
python main.py
