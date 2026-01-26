# suma.py
def sumar_desde_pipe(pipe):
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
