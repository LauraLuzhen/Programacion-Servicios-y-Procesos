# suma.py
def suma(num_proceso, valor_compartido, lock, num):
    with lock:  
        valor_anterior = valor_compartido.value
        valor_compartido.value += num
        print(f"Proceso {num_proceso}: {valor_anterior} + {num} = {valor_compartido.value}")
