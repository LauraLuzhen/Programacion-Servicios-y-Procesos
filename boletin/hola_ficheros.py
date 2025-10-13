# "r"	Abrir para leer (modo por defecto)
# "t"	Leer como texto (caracteres legibles) → se usa con .read() o .readline()
# "b"	Leer como binario (imágenes, PDF, etc.)
# "rt"	Leer texto línea a línea (modo más común) --> .readlines()

# El fichero debe estar previamente creado
# El modo w sobreescribe el fichero
"""
fichero = open("./boletin/ficheros/texto.txt", 'a', encoding="utf8")
fichero.write("Hola ")
fichero.write("me llamo Laura.\n")
fichero.write("¿Qué tal?")
fichero.close()
"""

fichero = open('texto.txt', 'w', encoding="utf8")
fichero.write("Hola ")
fichero.write("me llamo Laura.\n")
fichero.write("¿Qué tal?")
fichero.close()