# filtro.py
def clase_ip(ip):
    primer_octeto = int(ip.split(".")[0])
    if 1 <= primer_octeto <= 126:
        return "A"
    elif 128 <= primer_octeto <= 191:
        return "B"
    elif 192 <= primer_octeto <= 223:
        return "C"
    else:
        return None

def filtrar_ips(cola_entrada, cola_salida):
    while True:
        ip = cola_entrada.get()
        if ip is None:
            cola_salida.put(None)
            break

        clase = clase_ip(ip)
        if clase in ["A", "B", "C"]:
            cola_salida.put((ip, clase))
