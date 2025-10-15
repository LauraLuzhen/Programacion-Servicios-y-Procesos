# EJERCICIO 4 "El número secreto"
# Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
# Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, según sea mayor 
# o menor con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde 
# (introduciendo un -1).

import random

num_secreto = random.randint(1, 100)
num_user = int(input('Introduce un número:'))

while (num_user != num_secreto) or (num_user != -1):
    if num_user > num_secreto:
        print('El número secreto es menor')
    else:
        print('El número secreto es mayor')
    num_user = int(input('Introduce un número:'))

if num_user == -1:
    print("Te has rendido\nEl número secreot era", num_secreto)
else:
    print("HAS ACERTADO")