EJERCICIO MULTIPROCESSING – SUMA ENTRE DOS VALORES

Este programa permite sumar todos los números comprendidos entre dos valores
(incluyendo ambos) utilizando varios procesos.

- suma.py: contiene la función que realiza la suma de un rango.
- main.py: crea un proceso por cada rango y espera a que todos terminen.
- README.txt: descripción del ejercicio.

Funcionamiento:
1. main.py define varios rangos de números.
2. Cada proceso ejecuta la función suma_rango para su rango.
3. Cada proceso imprime el resultado de su suma.
4. El programa principal indica cuando todos los procesos han terminado.

Ejecución:
python main.py
