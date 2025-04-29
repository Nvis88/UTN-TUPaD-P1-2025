# Actividades
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
# Bucle For, que inicia en 1 y termina en 100:
for i in range(1, 101):
    # Verifico si el número i es múltiplo de 4:
    if i % 4 == 0:
        print(f"{i}") # Imprimo el resutlado.

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

# Defino la lista:
lista = ["Perro", "Gato", "Tortuga", "Paloma", "Rata"]
# Imprimo por consola el penúltimo:
print(f"Penúltimo elemento: {lista[-2]}")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.
# Por ejemplo: lista_vacia = []

#Creo lista vacía:
lista = []
# Solicito al usuario que ingrese 3 palabras:
for i in range(3):
    lista.append(input("Ingrese una palabra: "))
# Imprimo la lista resultante:
print(f"Lista resultante: {lista}")

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar 
# cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

# Defino variable e ingreso los valores:
animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista original: {animales}")

# Reemplazo valores:
animales[1] = "loro"
animales[-1] = "oso"

# Imprimo lista resultante:
print(f"Lista resultante: {animales}")

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# Primero, define una lista llamada números a la que le asigna los siguientes valores: [8, 15, 3, 22, 7]
# Segundo, busca y elimina el mayor valor de la lista.
# Tercero, imprime por consola la lista resultante.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y 
# mostrar por pantalla los dos primeros.

# Defino la lista:
lista = [i for i in range(10, 31, 5)]

# Imprimo sólo los dos primeros elementos:
print(f"Primeros dos elementos: {lista[:2]}")

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista 
# “autos” por dos nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

# Defino la lista:
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazo dos valores:
autos[1] = "blanco"
autos[2] = "negro"

# Imprimo lista resultante:
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 
# usando append directamente. Imprimir la lista resultante por pantalla.

# Defino lista vacía:
dobles = []
# Agrego dobles de 5, 10 y 15:
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimo por consola:
print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a)
compras[2].append("jugo")
# b)
compras[1][1] = "tallarines"
# c)
compras[0].remove("pan")
# d) Imprime lista:
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla. 2

# Defino lista:
lista_anidada = [[15], [True], [[25.5], [57.9], [30.6]], [False]]

print(lista_anidada)