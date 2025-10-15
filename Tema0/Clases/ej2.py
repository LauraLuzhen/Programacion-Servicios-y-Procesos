# Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca. La clase debe guardar 
# el título del libro, autor, número de ejemplares del libro y número de ejemplares prestados. La clase contendrá los siguientes métodos:

# a) Constructor con todos los parámetros (se le indica valores para todos los atributos).
# b) prestamo(): incrementa el atributo correspondiente cada vez que se realice un préstamo. No se pueden prestar libros si no quedan 
# ejemplares disponibles para prestar. Devuelve true si se ha podido realizar el préstamo y false en caso contrario.
# c) devolucion(): decrementa el atributo correspondiente cada vez que se devuelva un libro. No se podrán devolver libros que no se hayan prestado. 
# Devuelve true si se ha podido realizar la operación y false en caso contrario.
# d) Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  libros son iguales si tienen el mismo título y el mismo autor. 
# Los libros se ordenarán de menor a mayor por el nombre del autor.

class Libro:
    # título, número_ejemplares, número_prestados, autor
    def __init__(self, titulo, numero_ejemplares, numero_prestados, autor):
        self.titulo = titulo
        self.numero_ejemplares = numero_ejemplares
        self.numero_prestados = numero_prestados
        self.autor = autor
    
    def prestamo():
        res = True
        if numero_prestados > numero_ejemplares:
            res = False
        else:
            numero_prestados -= 1
            numero_ejemplares += 1
        return res

    def devolucion():
        res = True
        if numero_prestados == 0:
            res = False
        else:
            numero_prestados -= 1
            numero_ejemplares += 1
        return res

    def __str__(self):
        cadena = "Título", self.titulo, ", número de ejemplares", self.numero_ejemplares, ", número prestados", self.numero_prestados, ", autor", self.autor
        return cadena

    def __eq__(self, objeto):
        iguales = False
        if (self.titulo == objeto.titulo) and (self.autor == objeto.autor):
            iguales = True
        return iguales
    
    def __lt__(self, objeto):
        menor = False
        if self.autor < objeto.autor:
            menor = True
        return menor