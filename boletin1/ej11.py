# Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de 
# entrada corresponde con una vocal.

def vocal (letra) :
    vocales = ['a','e','i','o','u']
    acierto = bool(False)
    if letra in vocales :
        acierto = True
    return acierto

letra = str(input('Di una letra').lower())
print(vocal(letra))