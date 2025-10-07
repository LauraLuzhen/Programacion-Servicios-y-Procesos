
# ENTRADA Y SALIDA DE DATOS
# La función input siempre devuelve un tipo cadena por lo que es necesario convertir el tipo de dato
# str, int, float, bool, complex --> tipos básicos
# Valores booleanos True o False
# tuple, list, set
# bytes, chr, ord
nombre_usuario = str(input("Introduce tu nombre: "))
print("Hola " + nombre_usuario)     # El + es para conectar cadenas 
print("Hola", nombre_usuario)
print(f"Hola buenas {nombre_usuario}")

# OPERADORES ARITMÉTICOS
# +   -   *   **   /   //   %

# CADENAS
"""Se mantiene       el formato del texto"""
"Hola \t Hola \n Hola"

# FUNCIONES DE CADENAS
cadena = "Hola buenas tardes"
c = cadena*2
print(c)

long_string = "hola buenas amores mios"
print(long_string[::-1])
print(long_string[:3])
print(long_string[3:5:1])
print(cadena[2])
print(cadena[2:4])  # inicio , final-1
# divide la cadena .split() o .split('a') --> devuelve una lista
palabras1 = cadena.split()
palabras2 = cadena.split('a')
print(palabras1)
print(palabras2)
# generar una cadena a partir de una lista indicando un seprador " ".join([])
cadena_palabras = " ".join(['hola', 'buenas'])
print(cadena_palabras)

word1 = "hola".capitalize()

# OPERADORES BOOLEANOS 
# lógicos: and, or, not
# relacionales: ==, !=, <, >, <=, >=
# Su orden es alfabéticamente y las mayúsculas son menores q las minúsculas


# SENTENCIAS CONDICIONALES CUIDADO CON LA IDENTACIÓN
# IF
if cadena == "hola":
    print(cadena)
elif cadena < "adios":
    print("menor")
else:
    print("fin")
# A if C else B
# se evalúa C si se cumple devuelve A sino B
var = "par" if (1 < 2) else "impar"

# BUCLES existe break y continue
# WHILE
while 1 > 2:
    print("adios")
# FOR
# básico
for numero in [1, 2, 3, 4, 5]:
    print(numero)
# range()
for i in range(5):
    print(i)
for i in range(0, 10, 2):
    print(i)
# strings
for letra in "Python":
    print(letra)
# listas o tuplas
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print("Me gusta la", fruta)
# enumerate()
nombres = ["Ana", "Luis", "Marta"]

for indice, nombre in enumerate(nombres):
    print(indice, nombre)
# anidados
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# con else 
for i in range(3):
    print(i)
else:
    print("Bucle terminado sin break")


# FUNCIONES
# podemos poner un valor por defecto para los parámetros de entrada pero deben ir después de los que no tienen
# asignados ningún valor, podemos llamar a la función con un parámetro ya q el segundo ya tiene un valor por defecto
def mi_funcion(param2, param1="hola"):
    print(param1, param2)
    return param1

# COLECCIONES
lista = [True, "", 2, [1,2]]
lista[1] = "hola"
lista[3, 1]
lista[-2]
lista[0:3] # -1 # oncepto llamado slicing o particionado, que nos devuelve porciones de listas
lista = [10, 20, 30]
lista[1:4:2] # 20
lista[0:2] = [1, 2] # modifica la lista
lista[0:2] = 2 # modifica la lista y su tamaño


# MÁS
# función type(variable)
