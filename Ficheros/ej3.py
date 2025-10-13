# EJERCICIO 3
# Diseña una aplicación que pida al usuario su nombre y edad. Estos datos deben
# guardarse en el fichero datos.txt. Si este fichero existe, deben añadirse al final en una
# nueva línea, y en caso de no existir, debe crearse.

nombre = input("Introduce un nombre:")
edad = int(input("Introduce una edad:"))

f = open('./Ficheros/ficheros/datos.txt', 'a', encoding='utf8')
f.write(f'{nombre} {edad}\n')
f.close()