# #  1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# # deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# # Defino variable y solicito edad al usuario:
# edad = int(input("Ingrese su edad: "))

# # Analizo si es mayor de edad o no:
# if edad >= 18:
#     print("Es mayor de edad.")
# else:
#     print("Es menor de edad.")


# # 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# # deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 

# # Defino variable nota y se la solicito al usuario:
# nota = int(input("Ingrese su nota: "))

# # Analizo si el usuario está aprobado o no:
# if nota >= 6 and nota <= 10:
#     print("Aprobado.")
# elif nota >= 0 and nota < 6:
#     print("Desaprobado")
# else:
#     print("Nota inválida, debe ingresar una nota entre 0 y 10.")

# # 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en 
# # pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# # Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# # Defino variable numero y solicito al usuario que ingrese un número:
# numero = int(input("Ingrese un número: "))

# # Analizo si el número es Par o Impar:
# if numero % 2 != 0:
#     print("Por favor, ingrese un número par.")
# elif numero % 2 == 0:
#     print("Ha ingresado un número par.")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.

# # Defino variable y solicito edad al usuario:
# edad = int(input("Ingrese su edad: "))

# # Analizamos edad y definimos categoría:
# if edad < 12:
#     categoria = "Niño"
# elif 12 <= edad < 18:
#     categoria ="Adolescente"
# elif 18 <= edad < 30:
#     categoria = "Adulto/a jóven"
# elif edad >= 30:
#     categoria = "Adulto/a"

# print(f"Su categoría es: {categoria}.")

# # 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una 
# # contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, 
# # imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en 
# # Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 

# # Defino variable y solicito al usuario una contraseña:
# contrasena = input("Ingrese su contraseña: ")
# # Calculo largo contraseña:
# largo_contraseña = len(contrasena)

# # Analizo largo de contraseña:
# if 8 <= largo_contraseña <= 14:
#     print("Ha ingresado una contraseña correcta.")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar 
# si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Agregamos las librerías:
from statistics import mode, median, mean
from random import randint

# Creamos lista con 50 números aleatorios:
numeros_aleatorios = [randint(1, 100) for i in range(50)] 

moda = mode(numeros_aleatorios) # Moda: Valor más frecuente
mediana = median(numeros_aleatorios) # Mediana: Valor central de los datos (entre min y max?).
media = mean(numeros_aleatorios) # Media aritmética: Valor intermedio.

# Imprimimos resultados:
print(f"Listado de números aleatorios: {sorted(numeros_aleatorios)} \n")

print(f"Moda: {moda} - Mediana: {mediana} - Media: {media} \n")

# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# Sin sesgo: cuando la media, la mediana y la moda son iguales. 

if media > mediana and mediana > moda:
    print("Hay sesgo POSITIVO.")
elif media < mediana and mediana < moda:
    print("Hay sesgo NEGATIVO.")
elif media == mediana and mediana == moda:
    print("No hay sesgo.")
else:
    print("Sesgo confuso.")


