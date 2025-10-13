# EJERCICIO 11
# Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de 
# entrada corresponde con una vocal.

def vocal (letra) :
    vocales = ['a','e','i','o','u']
    es_vocal = False
    if letra in vocales :
        es_vocal = True
    return es_vocal

cad = str(input('Di una letra').lower())
letra = cad[0]
print("La letra es vocal:", vocal(letra))