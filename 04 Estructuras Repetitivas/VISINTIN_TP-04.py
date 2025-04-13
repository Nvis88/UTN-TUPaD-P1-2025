# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), 
# en orden creciente, mostrando un número por línea.

# Bucle for que recorre i desde 0, 101 veces:
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# Defino variable y solicito al usuario que ingrese un número:
numero = int(input("Ingrese un número entero: "))

digitos = 0

if numero == 0:
    digitos = 1
else:
    while numero > 0:
        digitos = digitos + 1
        numero = numero // 10 # División entera entre 10 para quitar un dígito.

print(f"Cantidad de dígitos del número ingresado: {digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# Defino variable y solicito al usuario que ingrese dos números enteros:
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input(f"Ingrese un número entero, mayor que {numero1}: "))
suma = 0

for i in range(numero2 - numero1 - 1):
    suma = suma + numero1 + i + 1

print(f"La suma de los números enteros es: {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# Se define variable y se solicita al usuario que ingrese un número entero:
numero = int(input("Ingrese un número entero: "))
suma = 0

while(numero != 0):
    suma = suma + numero
    numero = int(input("Ingrese otro número entero: "))

print(f"La sumatooria es: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, 
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Importamos librería random
from random import randint
# Defino variable con el número aleatorio entre 0 y 9
numero_secreto = randint(0, 9)
# Defino variable y solicito al usuario que ingrese un número:
numero_usuario = int(input("Ingrese un número entero entre 0 y 9.: "))
intentos = 1

while numero_secreto != numero_usuario:
    intentos += 1
    print("El número ingresado no es correcto.")
    numero_usuario = int(input("Ingrese otro número entero entre 0 y 9.: "))

print(f"Felicitaciones, avivinaste el número secreo: {numero_usuario}, en {intentos} intentos.")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# Creo bucle for, que recorre todos los números entre 0 y 100, y sólo imprime los pares:
for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Defino variable y solicito al usuario que ingrese un número entero:
numero = int(input("Ingrese un número entero positivo: "))

# Verifico si el número ingresado es positivo, sino vuelvo a solicitarlo.
while numero < 0:
    numero = int(input("Ingrese un número entero, pero esta vez positivo: "))

# Sumo todos los números entre 0 y número:
suma = 0
for i in range(1, numero+1):
    suma += i
# Devuelvo resultado:
print(f"La suma entre o y {numero} es: {suma}")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar 
# cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Defino variables que cuentan la cantidad de números pares e impares:
impares = 0
pares = 0

# Solicito al usuario que ingrese 100 números enteros:
cantidad = 100
for i in range(0, cantidad):
    numero = int(input(f"Ingrese un número entero ({i+1}/{cantidad}): "))
    # Incremento cantidad de números pares o impares dependiendo el caso:
    if numero % 2 == 0:
        pares +=1
    else:
        impares += 1
# Devuelvo resultado:
print(f"Se ingresaron {cantidad} de números, de los cuáles {pares} son Pares y {impares} son impares.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

# Importo librería para cálculo de la media:
from statistics import mean

# Solicito al usuario que ingrese 100 números enteros:
cantidad = 100
lista_numeros = []
for i in range(0, cantidad):
    numero = int(input(f"Ingrese un número entero ({i+1}/{cantidad}): "))
    lista_numeros.append(numero)

# Calculo la Media:
media = mean(lista_numeros)

print(f"La media de los números {lista_numeros} es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Defino variable y solicito al usuario un número entero:
numero = int(input("Ingrese un número entero: "))
oremun = 0

while numero > 0:
    modulo = numero % 10
    oremun = oremun * 10 + modulo
    numero = numero // 10

# Devuelvo resultado:
print(f"El número ingresado, al revés es: {oremun}")