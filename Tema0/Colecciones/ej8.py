# EJERCICIO 8
# Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves son los nombres de los productos y 
# los valores son las cantidades vendidas. El programa debe permitir al usuario agregar nuevas ventas y calcular el total de ventas 
# para un producto específico. Implementa un menú con ambas opciones. 

ventas = {}

op_menu = int(input("Introduce un valor:\n\t1.Añadir venta\n\t2.Total de ventas de un producto\n\t3.Salir"))

while op_menu >= 1 and op_menu <= 2:
    producto = input("Introduce el nombre del producto: ")
    match op_menu:
        case 1: 
            if producto in ventas:
                print("El producto ya está en las ventas")
            else:
                num = int(input("Introduce el número de ventas del producto:"))
                ventas[producto] = num
                print("Producto añadido a ventas")
        case 2:
            if producto in ventas:
                print("Ventas del producto", ventas[producto])
            else:
                print("El producto no existe en las ventas")
        case _:
            print("Error")
    op_menu = int(input("Introduce un valor:\n\t1.Añadir venta\n\t2.Total de ventas de un producto\n\t3.Salir"))
else:
    print("Fin del programa")