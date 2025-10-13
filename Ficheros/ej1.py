# EJERCICIO 1
#  Crea con un editor el fichero de texto Alumnos.txt y escribe en él los nombres, edades y estaturas de 
# los alumnos de un grupo, cada uno en una línea:

nombre = input("Introduce el nombre:")
edad = input("Introduce la edad:")
estatura = input("Introduce la estatura:")

media_edad = 0
media_estatura = 0
count = 0

f = open('./Ficheros/ficheros/Alumnos.txt', 'r+', encoding='utf8')
f.write(f'{nombre} {edad} {estatura}')
f.write('\n')
f.seek(0)
for linea in f.readlines():
    datos = linea.split()
    print(datos[0])
    media_edad = media_edad + int(datos[1])
    media_estatura = media_estatura + float(datos[2])
    count = count + 1
f.close()

media_edad /= count
media_estatura /= count

print(media_edad)
print(media_estatura)