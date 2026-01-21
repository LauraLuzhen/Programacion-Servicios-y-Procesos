# suma.py
def sumar_desde_cola(cola):
    """Toma rangos de la cola y suma todos los números entre ellos."""
    while True:
        rango = cola.get()
        if rango is None:
            break

        a, b = rango
        inicio = min(a, b)
        fin = max(a, b)
        total = sum(range(inicio, fin + 1))
        print(f"Suma de {inicio} a {fin} = {total}")
