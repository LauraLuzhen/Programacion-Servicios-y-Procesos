# Crea una clase llamada Punto que representará un punto de dos dimensiones en un plano. Solo contendrá dos atributos 
# enteros llamados x e y (coordenadas). Debe tener los siguientes métodos:

# a) Un constructor con parámetros que copie las coordenadas pasadas como argumento a los atributos del objeto.
# b) __str__(): Devuelve una cadena con el formato “(x, y)”. Ejemplo: “(7, -5)”
# c) setXY(x,y): Modifica ambas coordenadas.
# d) desplaza(dx, dy): Desplaza el punto la cantidad (dx,dy) indicada. Ejemplo: Si el punto (1,1) se desplaza (2,5) entonces estará en (3,6).
# e) distancia(punto): Calcula y devuelve la distancia entre el propio objeto (self) y otro objeto (punto) que se pasa como parámetro (distancia entre dos coordenadas).

class Punto:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        cadena = f"({self.x},{self.y})"
        return cadena
    
    def setXY(self, x, y):
        self.x = x
        self.y = y

    def desplaza(self, dx, dy):
        self.x += dx
        self.y += dy

    def distancia(self, punto):
        calx = (punto.x - self.x) ** 2
        caly = (punto.y - self.y) ** 2
        cal = (calx + caly) ** (1/2)
        return cal
    
