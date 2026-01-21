EJERCICIO MULTIPROCESSING – SUMA ENTRE DOS VALORES USANDO POOL

Este programa permite sumar todos los números comprendidos entre dos valores
utilizando multiprocessing.Pool y el método starmap para pasar dos argumentos
a la función suma_rango.

Archivos:
- suma.py: contiene la función que realiza la suma de un rango.
- main.py: crea un Pool de procesos y ejecuta la función suma_rango con starmap.
- README.txt: descripción del ejercicio.

Funcionamiento:
1. main.py define varios rangos de números.
2. Se crea un Pool de procesos.
3. Cada rango se envía a la función suma_rango mediante starmap.
4. Cada proceso imprime el resultado de su suma.
5. El programa principal indica cuando todos los procesos han terminado.

Ejecución:
python main.py
