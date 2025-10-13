# EJERCICIO 3
# Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
# Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, 
# antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.

num_user = int(input('Introduce un número:'))
sum = 0

while num_user > 0:
    sum += num_user
    num_user = int(input('Introduce un número:'))
print('La suma de los números es:', sum)