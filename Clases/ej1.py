# Diseñar la clase CuentaCorriente, que almacena los datos DNI, nombre y el saldo. Añade los siguientes constructores:
# a) Con el DNI del titular de la cuenta y un saldo inicial. El nombre se inicializará a cadena vacía.
# b) Con el DNI, nombre y el saldo inicial.
# 
# Las operaciones típicas de una cuenta corriente son:
# a) Sacar dinero: el método debe indicar si ha sido posible llevar a cabo la operación, si existe saldo suficiente. 
# Si es posible llevar a cabo la operación se resta la cantidad a sacar al saldo de la cuenta.
# b) Ingresar dinero: se incrementa el saldo. 
# c) Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos cuentas corrientes son iguales si tienen el mismo DNI. 
# Las cuentas corrientes se ordenarán de menor a mayor por el saldo.


class CuentaCorriente:

    def __init__(self, dni, nombre, saldo):
        self.dni = "123456789A"
        self.nombre = ""
        self.saldo = 10000

    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo

    def sacar_dinero(cantidad):
        if (cantidad > saldo):
            saldo -= cantidad
    
    def ingresar_dinero(cantidad):
        saldo += cantidad

    def __str__(self):
        cadena = "Dni: " + self.dni + ", nombre: " + self.nombre + ", saldo: " + self.saldo
        print(cadena)
