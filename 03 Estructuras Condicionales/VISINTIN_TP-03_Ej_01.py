#  1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# Defino variable y solicito edad al usuario:
edad = int(input("Ingrese su edad: "))

# Analizo si es mayor de edad o no:
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 

# Defino variable nota y se la solicito al usuario:
nota = int(input("Ingrese su nota: "))

# Analizo si el usuario está aprobado o no:
if nota >= 6 and nota <= 10:
    print("Aprobado.")
elif nota >= 0 and nota < 6:
    print("Desaprobado")
else:
    print("Nota inválida, debe ingresar una nota entre 0 y 10.")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en 
# pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# Defino variable numero y solicito al usuario que ingrese un número:
numero = int(input("Ingrese un número: "))

# Analizo si el número es Par o Impar:
if numero % 2 != 0:
    print("Por favor, ingrese un número par.")
elif numero % 2 == 0:
    print("Ha ingresado un número par.")

"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
Niño/a: menor de 12 años.
Adolescente: mayor o igual que 12 años y menor que 18 años.
Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
Adulto/a: mayor o igual que 30 años.
"""

# Defino variable y solicito edad al usuario:
edad = int(input("Ingrese su edad: "))

# Analizamos edad y definimos categoría:
if edad < 12:
    categoria = "Niño"
elif 12 <= edad < 18:
    categoria ="Adolescente"
elif 18 <= edad < 30:
    categoria = "Adulto/a jóven"
elif edad >= 30:
    categoria = "Adulto/a"

print(f"Su categoría es: {categoria}.")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una 
# contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, 
# imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en 
# Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 

# Defino variable y solicito al usuario una contraseña:
contrasena = input("Ingrese su contraseña: ")
# Calculo largo contraseña:
largo_contraseña = len(contrasena)

# Analizo largo de contraseña:
if 8 <= largo_contraseña <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


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


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar 
# el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Defino variable que almacena frase o palabra ingresada por el usuario:
cadena = input("Ingrese una frase o palabra: ")
# Variable con último caracter de la variable cadena:
ultima_letra = str.lower(cadena[-1])

# Analizo última letra y devuelvo resultado:
if ultima_letra in 'aeiou':
    print(f"{cadena}!")
else:
    print(cadena)

"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas. 
"""

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opción: 1 (MAYÚSCULAS) - 2 (minúsculas) - 3 (Tipo Oración):"))

if opcion == 1:
    resultado = str.upper(nombre)
elif opcion == 2:
    resultado = str.lower(nombre)
elif opcion == 3:
    resultado = str.title(nombre)
else:
    print("Opción incorrecta")
    resultado = nombre

print(resultado)

"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías 
según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """

terremoto = float(input("Ingrese magnitud terremoto: "))

if terremoto < 3:
    nivel = "Muy leve"
elif 3 <= terremoto < 4:
    nivel = "Leve"
elif 4 <= terremoto < 5:
    nivel = "Moderado"
elif 5 <= terremoto < 6:
    nivel = "Fuerte"
elif 6 <= terremoto < 7:
    nivel = "Muy Fuerte"
elif terremoto >= 7:
    nivel = "Extremo"

print(f"Magnitud del Terremoto: {nivel} ({terremoto})")

"""
10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año Periodo del año
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = str.upper(input("Ingrese en qué hemisferio vive: N (Norte) - S (Sur): "))
mes = int(input("Ingrese mes: (1 a 12): "))
dia = int(input("Ingrese día: (1 a 31): "))

if not(hemisferio in "SN"):
    print("Hemisferio incorrecto.")
    exit()

if (mes == 2 and dia > 29) or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30) or dia > 31:
    print("Fecha incorrecta.")
    exit()


# Fecha 21/12 al 20/03
if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    elif hemisferio == "S":
        estacion = "Verano"

# Fecha 21/03 al 20/06
if (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    elif hemisferio == "S":
        estacion = "Otoño"

# Fecha 21/06 al 20/09
if (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    elif hemisferio == "S":
        estacion = "Invierno"

# Fecha 21/09 al 20/12
if (mes == 9 and dia >= 21) or (mes <= 11) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        estacion = "Otoño"
    elif hemisferio == "S":
        estacion = "Primavera"

print(f"La fecha {dia}/{mes}, en el Hemisferio {"SUR" if hemisferio == "S" else "NORTE"} corresponde a la Estación {estacion}")
