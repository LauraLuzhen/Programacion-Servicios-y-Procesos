def suma(n, valor_compartido, lock, proceso_num):
    with lock:  # Aseguramos acceso exclusivo al valor compartido
        valor_anterior = valor_compartido.value
        valor_compartido.value += n
        print(f"Proceso {proceso_num}: {valor_anterior} + {n} = {valor_compartido.value}")