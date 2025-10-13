# EJERCICIO 7
# Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. 
# La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción.

# agregar, eliminar y buscar contactos
contactos = {}

eleccion_menu = int(input("Introduce la opción:\n\t1.Añadir contacto\n\t2.Eliminar contacto\n\t3.Buscar contacto\n\t4.Salir"))

while eleccion_menu >= 1 and eleccion_menu <= 3:
    nombre = input("Introduce el nombre:")
    match eleccion_menu:
        case 1:
            if nombre in contactos:
                print("El contacto ya está añadido")
            else:
                telefono = int(input("Introduce el número de teléfono:"))
                contactos[nombre] = telefono
                print("Contacto añadido correctamente")
        case 2:
            if nombre in contactos:
                del contactos[nombre]
            else:
                print("El contacto no se encuentra en la agenda")
        case 3:
            if nombre in contactos:
                print(nombre, 'su teléfono es', contactos[nombre])
            else:
                print("El contacto no se encuentra en la agenda")
        case _:
            print("Error")

    eleccion_menu = int(input("Introduce la opción:\n\t1.Añadir contacto\n\t2.Eliminar contacto\n\t3.Buscar contacto\n\t4.Salir"))
else:
    print("Fin del programa")
