# 1) Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
# de todos los números enteros entre 1 y el número que indique el usuario

def factorial(num):
    """
    Función factorial(num) calcula el factorial de un número entero y positivo num.

    Args:
        num (int): Número entero y positivo del cual se calcula el factorial.
    
    Returns:
        int: Factorial del número num.
    """
    # Caso Base: Factorial de 0 es 1
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
# Solicitamos al usuario un número entero y positivo:
print("Cálculo del factorial de un número entero y positivo.")
num = int(input("Ingresa un número: "))
while num < 0:
    print("Número inválido. Se debe ingresar un npúmero entero y positivo.")
    num = int(input("Ingresa un número entero y positivo: "))
# Llamada a la función Factorial:
print(f"El factorial de {num} es: {factorial(num)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci 
# en la posición indicada. Posteriormente, muestra la serie completa hasta la 
# posición que el usuario especifique.
def fibonacci(num):
    """
    Función fibonacci(num) calcula la serie de Fibonacci hasta la posición num.

    Args:
        num (int): Número entero y positivo que representa la posición de Fibonacci deseada.
    
    Returns:
        list: Lista con los valores de la serie de Fibonacci hasta la posición num.
    """
    # Casos Base:
    if num == 0:
        return [0]
    elif num == 1:
        return [0, 1]
    # Caso Recursivo:
    else:
        serie_fibonacci = fibonacci(num - 1)
        serie_fibonacci.append(serie_fibonacci[-1] + serie_fibonacci[-2])
        return serie_fibonacci

# Se solicita al usuario que ingrese posición de fibonacci deseada.
print("Ingresa un número entero y positivo que represente la posición de Fibonacci deseada.")
num = int(input("Ingresa la posición Fibonacci:"))

# Se verifica que el número ingresado sea válido.
while num < 0:
    print("El valor ingresado es inválido.")
    num = int(input("Ingresa la posición Fibonacci:"))

# Se llama a la función fibonacci:
serie = fibonacci(num)
print(f"El valor correspondiente a la posición {num} de la serie Fibonacci es: {serie[-1]}")
print(f"La serie completa de Fibonacci hasta la posición {num} es: {serie}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛**𝑚= 𝑛 ∗ 𝑛**(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exp):
    """
    Función potencia(base, exp) calcula la potencia exp de un número base.
    Args:
        base (int): Número base.
        exp (int): Exponente al que se eleva la base.
    Returns:
        int: Resultado de base elevado a exp.
    """
    #Caso Base: exp = 0 
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)
    
# Se solicita al usuario que ingrese base y exponente:
print("Ingresa una base y un exponente para calcular la potencia.")
base = int(input("Ingresa la base: "))
exp = int(input("Ingresa el exponente (número positivo): "))

while exp < 0:
    print("El exponente debe ser un número positivo.")
    exp = int(input("Ingresa el exponente (número positivo): "))

# Se llama a la función potencia e imprime el resultado:
print(f"El resultado de {base} elevado a {exp} es: {potencia(base, exp)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

def decimal_binario(num):
    """
    Función decimal_binario(num) convierte un número entero, positivo en base decimal a binario.
    
    Args:
        num (int): Número entero positivo en base decimal.
    
    Returns:
        str: Representación en binario del número decimal.
    """
    # Caso Base:
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    # Caso Recursivo:
    else:
        return decimal_binario(num // 2) + str(num % 2)
    
# Se solicita al usuario que ingrese un número decimal entero y positivo:
num = int(input("Ingresa un número entero y positivo en base decimal: "))

# Se verifica que el número ingresado sea válido:
while num < 0:
    print("Número inválido. Se debe ingresar un número entero y positivo.")
    num = int(input("Ingresa un número entero y positivo en base decimal: "))

# Se llama a la función decimal_binario e imprime el resultado:
print(f"El número {num} en binario es: {decimal_binario(num)}")


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    """
    La Función es_palindromo(palabra) indica si una palabra es palíndromo o no.

    Args:
        palabra (str): Palabra a verificar.

    Returns:
        (boolean): True si palabra es palíndromo, False si no lo es.
    """
    # Caso Base: Si palabra tiene 0 o 1 caracteres, devuelve True
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    # Caso Recursivo: Compara el primer y último carácter de la palabra
    elif palabra[0] == palabra[-1]:
        # Se llama a la función recursivamente eliminando el primer y último carácter
        return es_palindromo(palabra[1:-1])
    else:
        return False

# Se le solicita al usuario que ingrese una palabra:
palabra = input("Ingresa una palabra: ")
# Se llama a la función es_palindromo e imprime el resultado:
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(num):
    """
    La función suma_digitos(n) calcula la suma de todos los dígitos de un número entero positivo num.
    
    Args:
        num (int): Número entero positivo del cual se suman los dígitos.
    
    Returns:
        int: Suma de los dígitos del número num.
    """
    #Caso Base:
    if num == 0:
        return 0
    else:
        return num % 10 + suma_digitos(num // 10)

# Se solicita al usuario que ingrese un número entero positivo:
num = int(input("Ingresa un número entero positivo: "))

# Verifico que el número sea válido:
while num < 0:
    print("El número ingresado es inválido.")
    num = int(input("Ingresa un número entero positivo: "))

# Se llama a la función suma_digitos y se imprime el resultado:
print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}")


# 7) Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel 
# más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(num):
    """
    Función que determina la cantidad de bloques de una pirámide con num bloques en su base.

    Args:
        num (int): Cantidad de bloques en la base.

    Returns:
        (int): Cantidad de bloques de la pirámide.
    """
    # Caso Base:
    if num == 1:
        return 1
    # Caso Recursivo:
    else:
        return num + contar_bloques(num-1)

# Se solicita al usuario la cantidad de Bloques de la base de la pirámide.
num = int(input("Jaimito, ¿cuántos bloques hay en la base? "))

# Se verifica que el dato ingresado sea un número entero y mayor a cero.
while num < 1:
    num = int(input("El dato es inválido, ¿cuántos bloques hay en la base? "))

# Se llama a la función y se imprime el resultado:
print(contar_bloques(num))


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero 
# positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    """
    Función que recibe 2 parámetros, número y dígito, y cuenta la cantidad de ocurrencias del dígito en numero.

    Args:
        numero (int): Número sobre el cuál realizaremos la búsqueda.
        digito (int): Dígito a buscar en numero.

    Returns:
        (int): Cantidad de ocurrencias de digito en numero
    """
    
    resto = numero % 10
    modulo = numero // 10

    # Caso Base:
    if modulo == 0:
        return (1 if resto == digito else 0)
    # Caso Recursivo:
    else:
        return (1 if resto == digito else 0) + contar_digito(modulo, digito)
    
# Se solicita al usuario que ingrese un número sobre el cuál buscar el dígito:
numero = int(input("Ingresa un número entero: "))
while numero < 0:
    print("Número Inválido.")
    numero = int(input("Ingresa un número entero: "))

digito = int(input("Ingresa el dígito (0-9) que desees buscar: "))
while 0 > digito > 9:
    print("Número Inválido.")
    digito = int(input("Ingresa el dígito (0-9) que desees buscar: "))

# Se llama a la función e imprime el resultado:
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}")