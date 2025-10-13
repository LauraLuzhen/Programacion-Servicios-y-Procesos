# EJERCICIO 2
# Pedir dos números y mostrarlos ordenados de menor a mayor.

num1 = int(input('Introduce un número:'))
num2 = int(input('Introduce otro número:'))

if num1 < num2:
    print(num1, num2)
else:
    print(num2, num1)