# VISINTIN NICOLAS HUMBERTO
# Práctico 1: Estructuras Secuenciales

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

# El comando print() imprime por consola el contenido entre paréntesis:
print("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

# Defino variable, solicito al usuario que ingrese su nombre:
nombre_usuario = input("Ingresa tu nombre: ")
# Imprimo por consola
print(f"Hola {nombre_usuario}!")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

# Defino variables, y solicito al usuario que ingrese su nombre, apellido, edad y lugar de residencia:
nombre = input("Ingresa tu Nombre: ")
apellido = input("Ingresa tu Apellido: ")
edad = int(input("Ingresa tu Edad: "))
lugar_residencia = input("¿Dónde vives?: ")
# Imprimo por consola:
print(f"Soy {nombre} {apellido}, tendo {edad} años y vivo en {lugar_residencia}")


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

# Defino variable radio, y solicito al usuario que ingrese el dato:
radio = float(input("Ingresa el Radio del círculo: "))
# Calculo area y perímetro:
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
# Imprimo por consola:
print(f"El perímetro del círculo es: {perimetro}")
print(f"El área del círculo es: {area}")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

# Defino variable segundos, y solicito al usuario que ingrese el dato:
segundos = int(input("Ingresa cantidad de segundos: "))
# Convierto segundos a horas. Redondeo a 2 decimales:
horas = roud(segundos / 3600, 2)
# Imprimo resultado por consola:
print(f"Horas: {horas}")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

# Defino variable número, y solicito al usuario que ingrese un número para generar tabla de multiplicar:
numero = int(input("Ingresa un número: "))
# Imprimo por consola Tabla de Multiplicar:
print(f"{numero} * 0 = ", numero * 0)
print(f"{numero} * 1 = ", numero * 1)
print(f"{numero} * 2 = ", numero * 2)
print(f"{numero} * 3 = ", numero * 3)
print(f"{numero} * 4 = ", numero * 4)
print(f"{numero} * 5 = ", numero * 5)
print(f"{numero} * 6 = ", numero * 6)
print(f"{numero} * 7 = ", numero * 7)
print(f"{numero} * 8 = ", numero * 8)
print(f"{numero} * 9 = ", numero * 9)



# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# Defino variables numero_1 y numero_2, solicito al usuario que ingrese valor:
numero_1 = int(input("Ingresa el primer número (distinto de 0): "))
numero_2 = int(input("Ingresa el segundo número (distinto de 0): "))

# Imprimo por consola resultados:
# SUMA:
print(f"La suma de {numero_1} + {numero_2} es: {numero_1 + numero_2}")
# DIVISION:
print(f"La división de {numero_1} / {numero_2} es: {numero_1 / numero_2}")
# MULTIPLICACIÓN:
print(f"La multiplicación de {numero_1} * {numero_2} es: {numero_1 * numero_2}")
# RESTA:
print(f"La resta de {numero_1} - {numero_2} es: {numero_1 - numero_2}")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:  
# 𝐼𝑀𝐶 =  𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) ** 2

# Defino variables y solicito al usuario que ingrese su Peso en Kg y Altura en metros
peso = float(input("Ingresa tu peso en Kg: "))
altura = float(input("Ingresa tu altura en metros: "))
# Calculo IMC, redondeo a 2 dígitos:
imc = round(peso / altura ** 2, 2)
# Imprimo resultado por consola:
print("Tu índice de masa corporal es: ", imc)


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente 
# en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
#  𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   +  32

# Defino variable y solicito al usuario que ingrese la Temperatura en °C:
temperatura_c = float(input("Ingresa la Temperatura (°C): "))
# Calculo Temperatura en °F:
temperatura_f = 9/5 * temperatura_c + 32
# Imprimo resultado por consola:
print("La Temperatura (°F) es:", temperatura_f)


# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.

# Defino variables y solicito al usuario que ingrese 3 números:
numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))
numero_3 = int(input("Ingresa el tercer número: "))
# Calculo promedio de los números:
promedio = (numero_1 + numero_2 + numero_3) / 3
# Imprimo resultado por consola:
print(f"El promedio de los números {numero_1}, {numero_2} y {numero_3} es: {promedio}")
