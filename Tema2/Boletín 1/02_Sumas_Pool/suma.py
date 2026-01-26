# suma.py
def suma(n, valor_compartido, lock):
    with lock:  
        valor_anterior = valor_compartido.value
        valor_compartido.value += n
        print(f"Proceso {n}: {valor_anterior} + {n} = {valor_compartido.value}")