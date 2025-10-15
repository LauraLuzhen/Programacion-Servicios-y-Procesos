# EJERCICIO 9
# Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. 
# Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, y pásalos 
# como parámetros de entrada de la función.

def numeros_comprendidos(num1, num2):
    if num1 > num2:
        for num in range(num2, num1+1, 1):
            print(num)
    else:
        for num in range(num1, num2+1, 1):
            print(num)

numUser1 = int(input('Introduce un número:'))
numUser2 = int(input('Introduce otro número:'))
numeros_comprendidos(numUser1, numUser2)