# Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
# Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, según sea mayor 
# o menor con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).

import random

numSecreto = random.randint(1, 101)
numUser = int(input('Introduce un número:'))

while numUser != numSecreto:
    if numUser > numSecreto:
        print('El número secreto es menor')
    else:
        print('El número secreto es mayor')
    numUser = int(input('Introduce un número:'))

print('Has acertado!!')