# EJERCICIO 12
# Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación se desea realizar con ellos. 
# Las operaciones disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 
# 2 para la resta, 3 para la multiplicación y 4 para la división. La función devolverá el resultado de la operación mediante un 
# número real.

def calculadora(num1, num2, operacion=1):
    match operacion:
        case 1:
            print("Suma:", num1+num2)
        case 2:
            print("Resta:", num1-num2)
        case 3:
            print("Multiplicación:", num1*num2)
        case 4:
            print("División:", num1/num2)

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
op = int(input("Introduce una opción:\n\t1.Suma\n\t2.Resta\n\t3.Multiplicación\n\t4.División"))
calculadora(num1, num2, op)