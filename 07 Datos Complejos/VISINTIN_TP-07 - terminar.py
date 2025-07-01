# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
# actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
# crear una lista que contenga únicamente las frutas sin los precios.
frutas = list(precios_frutas.keys())
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:

contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
if nombre_buscar in contactos:
    print("Número de teléfono:", contactos[nombre_buscar])
else:
    print("Contacto no encontrado.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo:

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. Ejemplo:

alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial1 = {1, 2, 3, 4, 5, 6}
parcial2 = {3, 4, 5, 6, 7, 8, 9}

aprobados_ambos = parcial1.intersection(parcial2)
aprobados_uno = parcial1.symmetric_difference(parcial2)
aprobados_total = parcial1.union(parcial2)
print("Aprobados en ambos parciales:", aprobados_ambos)
print("Aprobados en solo uno de los parciales:", aprobados_uno)
print("Total de estudiantes que aprobaron al menos un parcial:", aprobados_total)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {}
while True:
    print("1. Consultar stock")
    print("2. Agregar stock")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        stock = productos.get(producto, 0)
        print("Stock de", producto, ":", stock)

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        productos[producto] = productos.get(producto, 0) + cantidad
        print("Stock actualizado de", producto, ":", productos[producto])

    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad inicial: "))
        productos[producto] = cantidad
        print("Producto agregado:", producto)

    elif opcion == "4":
        break

    else:
        print("Opción inválida.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
# Permití consultar qué actividad hay en cierto día y hora.
agenda = {}
while True:
    print("1. Agregar evento")
    print("2. Consultar evento")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        dia = input("Ingrese el día (formato DD/MM): ")
        hora = input("Ingrese la hora (formato HH:MM): ")
        evento = input("Ingrese el evento: ")
        agenda[(dia, hora)] = evento
        print("Evento agregado:", agenda[(dia, hora)])

    elif opcion == "2":
        dia = input("Ingrese el día a consultar (formato DD/MM): ")
        hora = input("Ingrese la hora a consultar (formato HH:MM): ")
        evento = agenda.get((dia, hora), "No hay eventos programados.")
        print(f"Evento en {dia} a las {hora}: {evento}")

    elif opcion == "3":
        break

    else:
        print("Opción inválida.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. Ejemplo:
paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Italia': 'Roma',
    'Rusia': 'Moscú'
}

capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario de capitales y países:", capitales)
