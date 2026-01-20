# suma.py
def suma(args):
    n, valor_compartido, lock, proceso_num = args

    with lock:
        anterior = valor_compartido.value
        valor_compartido.value += n
        print(f"Proceso {proceso_num}: {anterior} + {n} = {valor_compartido.value}")
