# EJERCICIO 7
# Realiza un programa que pida un número entero positivo y nos diga si es primo o no.

num_usuario = int(input('Introduce un número:'))
cont = 0

for numero in range(1, num_usuario+1, 1):
    if num_usuario % numero == 0:
        cont += 1
        
if cont == 2:
    print('El número es primo')
else:
    print('El número no es primo')