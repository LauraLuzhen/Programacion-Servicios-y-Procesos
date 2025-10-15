# EJERCICIO 10
# Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.

def mostrarMayor (numero1, numero2) :
    lista = [numero1, numero2]
    print(max(lista))


numero1 = int(input('Di un numero'))
numero2 = int(input('Di otro numero'))
mostrarMayor(numero1, numero2)