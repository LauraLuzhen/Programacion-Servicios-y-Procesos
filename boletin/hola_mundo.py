
# ENTRADA Y SALIDA DE DATOS
# La función input siempre devuelve un tipo cadena por lo que es necesario convertir el tipo de dato
# str, int, float, bool, complex --> tipos básicos
# Valores booleanos True o False
# tuple, list, set
# bytes, chr, ord
nombre_usuario = input("Introduce tu nombre: ")
edad_usuario = int(input("Introduce tu edad: "))
print("Hola " + nombre_usuario) # El + es para conectar cadenas 
print("Hola", nombre_usuario)   # La , realiza un espacio
print(f"Hola buenas {nombre_usuario} su edad es {edad_usuario}")

# OPERADORES ARITMÉTICOS
# +   -   *   **   /   //   %

# CADENAS
"""Se mantiene       el formato del texto"""
"Hola \t Hola \n Hola"

# FUNCIONES DE CADENAS
cadena = "Hola buenas tardes"
c = cadena*2
print(c)
a = "Hola " * 3

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
num = 5
if num == 5:
    print("igual")
elif num < 5:
    print("menor")
else:
    print("mayor")
# A if C else B
# se evalúa C si se cumple devuelve A sino B
var = "par" if (num%2 == 0) else "impar"

# BUCLES existe break y continue
# WHILE
while num > 2:
    print(num)
    num -= 1
# FOR
# básico
for numero in [1, 2, 3, 4, 5]:
    print("El número es", numero)
for letra in "Python":
    print(letra)
# range()
for i in range(5):  # Del 0-4
    print(i)
for i in range(0, 10, 2): # Del 0-9 pasando 2
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
    print(f"{indice} - Alumno: {nombre}")
# anidados
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# con else 
for i in range(3):
    print(i)
else:
    print("Bucle terminado sin break")
numeros = [1, 3, 5, 7]
for n in numeros:
    print(n)
    if n % 2 == 0:
        print("Se encontró un número par")
        break
else:
    print("No se encontraron números pares en la lista")

while num > 2:
    print(num)
    num -= 1
else:
    print("Bucle terminado con éxito")



# FUNCIONES
# podemos poner un valor por defecto para los parámetros de entrada pero deben ir después de los que no tienen
# asignados ningún valor, podemos llamar a la función con un parámetro ya q el segundo ya tiene un valor por defecto
def mi_funcion(param2, param1="hola"):
    print(param1, param2)
    return param1   # El return es opcional
mi_funcion("Adiós")
mi_funcion("Hola", "Adiós")

# COLECCIONES LISTAS
lista = [True, "", 2, [1,2]]
lista[1] = "hola"
#lista[3, 1]
lista[-2]
lista[0:3] # -1 # oncepto llamado slicing o particionado, que nos devuelve porciones de listas
lista = [10, 20, 30]
lista[1:4:2] # 20
#lista[0:2] = [1, 2] # modifica la lista
#lista[0:2] = 2 # modifica la lista y su tamaño
# funciones --> pg 27 y 28

# COLECCIONES TUPLAS
# se le aplica todo lo anterior de las listas
# debe tener dos elementos para que se considere tupla
tupla = (1, "hola", False, 123)
# Las tuplas son más “ligeras” que las listas, por lo que si el uso que le vamos a dar a una colección 
# es muy básico, puedes utilizar tuplas en lugar de listas y ahorrar memoria. Ej. los días de la semana


# COLECCIONES DICCIONARIOS
# los diccionarios están compuestos por los tipos primitivos ya que no son mutables
dic = {"C": 1999, "Python": 1823}


#dic["C"] # Devuelve su valor pero si no lo encuentra da KeyError
dic.get("C") # Si no lo encuentra devuelve None
dic.get("C", "No encontrado") # Devuelve no encontrado


# eliminar y obtener clave-valor, devuelve el valor asociado a la clave que se elimina, si no se encuentra KeyError
dic.pop("C", "no encontrado")


# buscar
print("C" in dic) # devuelve true or false


# añadir
dic["Java"] = 2000


# eliminar, no devuelve nada, si el elemento no existe da KeyError y no se soluciona
del dic["C"]


# recorrer las claves o valores con un for
for claves in dic: # o dic.keys()
    print(claves)
for valores in dic.values():
    print(valores)
# iteración de calve-valor
for clave, valor in dic.items():
    print(clave, "-->", valor)

# MÁS
# función type(variable)

# CLASES
from nombre_fichero import *

class Persona:
    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
    # Creamos los métodos, si algún método necesita self, se debe poner como el primer parámetro de entrada
    # Métodos especiales:
    def __str__(self):
        cadena = self.nombre
        return cadena
    def __eq__(self, obj):
        iguales = False
        if self.nombre == obj.nombre:
            iguales = True
        return iguales
    def __lt__(self, obj): # menor a mayor
        menor = False
        if self.nombre < obj.nombre:
            menor = True
        return menor

obj = Persona("Laura")
print(obj.nombre)
obj2 = Persona("Lucía")
print(obj.__lt__(obj2))

# HERENCIA
class Trabajador(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)    
        # Llamar a funciones de la calse padre super()
    def __str__(self):
        return "hola"   
        # Sobreescribir un método de la clase padre

# FICHEROS LECTURA
