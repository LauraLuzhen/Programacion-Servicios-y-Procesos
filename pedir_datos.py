user_name = input("Introduce your name:")
# Por defecto el input la respuesta que recibe es string
print("Your name is", user_name)
print("Your name is " + user_name)
# con coma te mete espacio y +


age = int(input("Introduce your age:"))
age += 1
print("Your age is", age)
# print("Your age is" + age)
# El + es para concatenar cadenas
print(f"Your age is {age}")

# Valores booleanos True o False

cadena = "hola \t Buenas \n tonto"
cadena_sin_modificar = """Hola Buenas
            tontoooo"""
print(cadena)
print(cadena_sin_modificar)

c = cadena*2
print(c)

a="ho"
b="la"
print((((a+b) + " "))*5)

long_string = "hola buenas amores mios"
print(long_string[::-1])
print(long_string[:3])
print(long_string[3:5:1])

print(long_string.split())
print(long_string.split("a"))

words = ["hi", "every", "body", "how", "are", "you"]
new_phrase = "-".join(words)

# Las cadenas se pueden comparar con == < >
# Su orden es alfabéticamente y las mayúsculas son menores q las minúsculas

word1 = "hola".capitalize()
word2 = "Hola"
print(word1 > word2)

