#  1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# Defino variable y solicito edad al usuario:
edad = int(input("Ingrese su edad: "))

# Analizo si es mayor de edad o no:
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")