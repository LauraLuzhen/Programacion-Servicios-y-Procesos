# Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego lo recorra para averiguar 
# el máximo y mínimo y mostrarlos por pantalla.

# Creamos una lista vacía
lista = []

# Creamos un while que salga cuando la lista tenga 10 elementos
while len(lista) < 10:
    # Le pedimos un número al usuario
    num = int(input('Introduce un número:'))
    # Añadimos el número a la lista
    lista.append(num)

# Imprimimos todos los elementos de la lista
print('Lista:', lista)
# Imprimimos el máximo valor de la lista
print('Máximo:', max(lista))
# Imprimimos el mínimo valor de la lista
print('Mínimo:', min(lista))