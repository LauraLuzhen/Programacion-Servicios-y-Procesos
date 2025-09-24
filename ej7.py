# Realiza un programa que pida un número entero positivo y nos diga si es primo o no.

numUser = int(input('Introduce un número:'))
cont = 0

for numero in range(1, numUser+1, 1):
    if numUser % numero == 0:
        cont += 1
if cont == 2:
    print('El número es primo')
else:
    print('El número no es primo')