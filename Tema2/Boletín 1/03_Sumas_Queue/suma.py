# suma.py
def sumar_desde_cola(cola):
    total = 0
    proceso = 1

    while True:
        numero = cola.get()
        if numero is None:
            break

        anterior = total
        total += numero
        print(f"Proceso {proceso}: {anterior} + {numero} = {total}")
        proceso += 1

    print("Suma final:", total)
