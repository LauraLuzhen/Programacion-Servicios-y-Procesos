# generador.py
import random

def generar_ips(cola_salida):
    for _ in range(10):
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        cola_salida.put(ip)
    cola_salida.put(None)  # Señal de fin
