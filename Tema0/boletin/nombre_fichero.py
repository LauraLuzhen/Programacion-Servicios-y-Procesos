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


