# Realiza un programa que pida 8 números enteros y los almacene en una lista. A continuación, 
# recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.

# Creamos una variable contador que van a ser la cantidad de números que le va a pedir al usuario
cont = 8
# Creamos una lista vacía
lista = []

# Creamos un while que le pida la cantidad de números enteros indicada al usuario
while len(lista) < cont:
    num = int(input('Introduce un número:'))
    # Lo añadimos a la lista
    lista.append(num)

# Creamos un for para recorrer cada elemento de la lista
for i in range(0, cont, 1):
    # Creamos un if-else para imprimir si el elemento es par o impar
    if lista[i]%2 == 0:
        print(lista[i], 'es par')
    else:
        print(lista[i], 'es impar')