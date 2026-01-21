# clasificador.py
def mostrar_ips(cola_entrada):
    while True:
        dato = cola_entrada.get()
        if dato is None:
            break

        ip, clase = dato
        print(f"IP: {ip} -> Clase {clase}")
