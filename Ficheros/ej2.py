# EJERCICIO 2
# Crea un programa en python que cree un fichero en modo escritura. A continuación, irá leyendo línea
#  a línea de teclado hasta que el usuario introduzca la cadena “fin”.
# Debe escribir cada línea en el fichero creado

fichero = open('./Ficheros/ficheros/Fichero_escritura.txt', 'w', encoding='utf8')
cad = input("Introduce una línea:")
while cad != "fin":
    fichero.write(cad)
    fichero.write('\n')
    cad = input("Introduce una línea:")
fichero.close()