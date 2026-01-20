# suma.py
def suma_rango(a, b):
    """Suma todos los números entre a y b inclusive, independientemente del orden."""
    inicio = min(a, b)
    fin = max(a, b)
    total = sum(range(inicio, fin + 1))
    print(f"Suma de {inicio} a {fin} = {total}")
