EJERCICIO MULTIPROCESSING CON COLAS (QUEUE)

Este programa utiliza dos procesos que se comunican mediante una cola (Queue).

Un proceso lee números desde un fichero (numeros.txt) y los introduce en la cola.
Otro proceso toma los números de la cola y realiza la suma acumulativa.

Cuando el proceso lector termina, introduce un valor None en la cola para indicar
al proceso sumador que ya no hay más datos.

Archivos:
- main.py: crea la cola y lanza los procesos.
- lector.py: lee los números del fichero y los mete en la cola.
- suma.py: consume la cola y realiza la suma.
- numeros.txt: contiene un número por línea.
- README.txt: descripción del ejercicio.

Ejecución:
python main.py
