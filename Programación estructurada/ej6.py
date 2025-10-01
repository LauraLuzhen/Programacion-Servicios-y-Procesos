# Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.

num = int(input('Introduce un número:'))
res = 1

for factorial in range(num, 1, -1):
    res *= factorial

print(res)