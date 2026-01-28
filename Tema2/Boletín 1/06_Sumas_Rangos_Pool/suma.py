# suma.py
def suma(num_poceso, valor_compartido, num, lock):
    with lock:  
        valor_anterior = valor_compartido.value
        valor_compartido.value += num
        print(f"Proceso {num_poceso}: {valor_anterior} + {num} = {valor_compartido.value}")