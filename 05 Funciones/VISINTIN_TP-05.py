# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
# Llamar a esta función desde el programa principal.
# Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# MAIN
# Llamamos a la función imprimir_hola_mundo():
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. 
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# MAIN
# Defino variable nombre y se lo solicito al usuario:
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro 
# parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, teno {edad} y vivo en {residencia}")

# MAIN
# Defino variables y solicito datos al usuario:
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su ciudad de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_ circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from math import pi

def calcular_area_circulo(radio): # Función que calcula el área del círculo:
    area = pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio): # Función que calcula el perímetro del círculo:
    perimetro = 2 * pi * radio
    return perimetro

# MAIN
# Defino variable radio y solicito el dato al usuario:
radio = float(input("Ingrese el radio del círculo: "))

area_circulo = calcular_area_circulo(radio)
perimetro_circulo = calcular_perimetro_circulo(radio)
# Muestro resultados
print(f"El área del círculo es: {area_circulo:.2f}")
print(f"El perímetro del círculo es: {perimetro_circulo:.2f}")


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro 
# y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# MAIN
# Defino variable segundos y solicito el dato al usuario:
segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)
# Muestro resultado:
print(f"{segundos} segundos equivale a {horas:.2f} horas.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de 
# multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# MAIN
# Defino variable numero y solicito el dato al usuario:
numero = int(input("Ingrese un número: "))
# Llamo a la función tabla_multiplicar con el número ingresado por el usuario:
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla 
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# FUNCIÓN: Define una variable tupla, que contiene las operaciones suma, resta, multiplicación y división:
def operaciones_basicas(a, b):
    tupla = [a + b, a - b, a * b, a / b]
    return tupla

# MAIN
# Defino variable a y b, y solicito al usuario que ingrese 2 números enteros:
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

# Llamo a la función operaciones_basicas y guardo el valor de la tupla en la variable operaciones:
operaciones = operaciones_basicas(num1, num2)

# Imprimo los resultados:
print(f"\nSuma de {num1} y {num2}: {operaciones[0]}")
print(f"Resta de {num1} y {num2}: {operaciones[1]}")
print(f"Producto de {num1} y {num2}: {operaciones[2]}")
print(f"División de {num1} y {num2}: {operaciones[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y 
# devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
# FUNCIÓN: 
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# MAIN
# Defino variables peso y variable; y le solicito los datos al usuario:
peso = float(input("Ingrese su peso (Kg): "))
altura = float(input("Ingrese su altura (m): "))

# Defino variable imc, que llama a la función que calcula el IMC.
imc = calcular_imc(peso, altura)

# Se muestra el resultado, formateado a número con 2 decimales.
print(f"Su IMC es: {imc:.2f}")


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y 
# devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    temp_f = celsius * 1.8 + 32
    return temp_f

# MAIN
# Defino variable temperatura y solicito el dato al usuario (en Celsius):
temp_c = int(input("Ingrese la temperatura en Celsius: "))

temp_f = celsius_a_fahrenheit(temp_c)

print(f"La temperatura {temp_c} °C equivale a {temp_f} °F.")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
# devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    prom = (a + b + c) / 3
    return prom

# MAIN
# Defino 3 variables y solicito al usuario que ingrese 3 números enteros:
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
num3 = int(input("Ingrese otro número entero: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"EL promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")