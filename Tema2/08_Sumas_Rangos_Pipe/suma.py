# suma.py
def sumar_desde_pipe(pipe):
    """Recibe rangos desde la Pipe y suma todos los números entre ellos."""
    while True:
        rango = pipe.recv()
        if rango is None:
            break
        a, b = rango
        inicio = min(a, b)
        fin = max(a, b)
        total = sum(range(inicio, fin + 1))
        print(f"Suma de {inicio} a {fin} = {total}")
