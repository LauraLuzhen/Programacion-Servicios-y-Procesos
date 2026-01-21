EJERCICIO MULTIPROCESSING – PROCESOS ENCADENADOS CON IPs

Tres procesos se comunican en cadena usando colas:

Proceso 1:
- Genera 10 direcciones IP aleatorias.
- Las envía al Proceso 2.

Proceso 2:
- Recibe las IPs.
- Filtra solo las de clase A, B o C.
- Envía las válidas al Proceso 3.

Proceso 3:
- Recibe las IPs filtradas.
- Muestra por pantalla la IP y su clase.

Archivos:
- main.py: lanza los procesos y mide el tiempo.
- generador.py: genera las IPs.
- filtro.py: clasifica y filtra por clase.
- clasificador.py: muestra las IPs finales.
- README.txt: descripción del ejercicio.

Ejecución:
python main.py
