# Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.

numUser = int(input('Introduce un número:'))

for num in range(1, numUser+1, 1):
    print(num)
