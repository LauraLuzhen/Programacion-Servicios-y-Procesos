# suma.py
def suma_rango(a, b):
    inicio = min(a, b)
    fin = max(a, b)
    total = sum(range(inicio, fin + 1))
    print(f"Suma de {inicio} a {fin} = {total}")
