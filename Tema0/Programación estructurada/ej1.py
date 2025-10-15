# EJERICICO 1
# Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

num = int(input('Introduce un número:'))
num_user = 'par' if (num%2 == 0) else 'impar'
print(num_user)