# EJERCICIO 5
# Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.

num_usuario = int(input('Introduce un número:'))

for num in range(1, num_usuario + 1, 1):
    print(num)
