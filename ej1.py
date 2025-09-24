# Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

num = int(input('Introduce un número:'))
numUser = 'par' if (num%2 == 0) else 'impar'
print(numUser)