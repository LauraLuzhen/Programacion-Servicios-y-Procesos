# EJERCICIO 6
# Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de 
# cada palabra en el texto.

# Pedimos un texto al usuario
texto = str(input('Introduce un texto:'))
# Creamos una lista con todas las palabras
palabras = texto.split()
# Creamos un diccionario vacío 
diccionario_palabras = {}

# Creamos un for para recorrer cada elemento de la lista
for palabra in palabras:
    if palabra in diccionario_palabras:
        # Si la palabra ya está en el diccionario aumenta el número de veces
        diccionario_palabras[palabra] += 1
    else:
        # En caso contrario se crea un nuevo conjunto clave-valor en el diccionario
        diccionario_palabras[palabra] = 1

# Creamos un for para imprimir el diccionario
for clave, valor in diccionario_palabras.items():
    print(clave, '-->', valor)