# suma.py
def sumar_desde_pipe(pipe):
    """Recibe números desde la pipe y hace la suma acumulativa."""
    total = 0
    proceso = 1

    while True:
        numero = pipe.recv()
        if numero is None:
            break
        anterior = total
        total += numero
        print(f"Proceso {proceso}: {anterior} + {numero} = {total}")
        proceso += 1

    print("Suma final:", total)
