# FUNCIONES:
# FUNCIÓN QUE CONVIERTE DE DECIMAL A BINARIO:
def convertir_dec_bin(numero_decimal):
    numero_a_convertir = numero_decimal
    numero_binario = ""

    while(numero_a_convertir > 0):
        numero_binario = str(numero_a_convertir % 2) + numero_binario # Resto
        numero_a_convertir = numero_a_convertir // 2 # Entero

    return numero_binario

# ----------------------------------------------------------------------------------------------------------------------
# FUNCIÓN PARA CONVERTIR UN NÚMERO BINARIO A DECIMAL:
def convertir_bin_dec(numero_binario):
    # Inicializamos el valor de la potencia en 0, correspondiente a la posición 0 del dígito del número binario
    potencia = 0
    numero_convertido_decimal = 0

    # Recorremos la cadena de caracteres de derecha a izquierda, multiplicando el valor de cada caracter
    # por 2 elevado a la potencia correspondiente:
    for caracter in reversed(numero_binario):
        numero_convertido_decimal += int(caracter) * (2 ** potencia)

        # Incrementamos la potencia en 1 a medida que aumentamos la posición del dígito en la cadena:
        potencia += 1

    return numero_convertido_decimal

# ----------------------------------------------------------------------------------------------------------------------
# FUNCIÓN PARA VALIDAR ENTRADA DE DATOS:
def validar_numero_entrada(numero_ingresado, operacion):
    if operacion == "D": # Valida si el número es Decimal, entero y positivo.
        return (numero_ingresado % 1 == 0 and numero_ingresado > 0)
    else: # Valida si el nùmero es Binario.
        es_binario_valido = True
        for caracter in numero_ingresado:
            if caracter not in '01':
                es_binario_valido = False
                break
        return es_binario_valido

# ----------------------------------------------------------------------------------------------------------------------
# CÓDIGO PRINCIPAL:

# CONVERSOR DE NÚMEROS DECIMALES A BINARIOS:
# Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
# Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

# INTEGRANTES:
# Belén YARDE BULLER
# Francisco Ezequiel ALARCÓN
# Pablo Sebastián VENTURA
# Nicolás Humberto VISINTIN
# 
# Comisión 23 - TUPaD - 2025


inicio = True
while inicio:

    # Solicitamos al usuario que ingrese qué tipo de operación desea hacer:
    operacion = input("Ingrese tipo de conversión: (D) -> Decimal a Binario   - (B) -> Binario a Decimal: ").upper()

    if operacion == "D": # Decimal a Binario
        # Solicitamos al usuario un número entero y positivo:
        numero_decimal = int(input("Ingrese un número entero positivo: "))

        # Validamos si el número es Positivo y Entero:
        while not validar_numero_entrada(numero_decimal, operacion):
            numero_decimal = int(input("Ingrese un número entero positivo: "))

        # Si el número es válido, llamamos a la función que lo convierte a Binario.
        numero_binario = convertir_dec_bin(numero_decimal)

        print(f"\n El número decimal {numero_decimal} equivale al {numero_binario} en sistema binario. \n")
        # Control del resultado con función bin()
        print(f"Control: {bin(numero_decimal)[2:]} \n")

    elif operacion == "B": # Binario a Decimal
        # Solicitamos al usuario un número binario:
        numero_binario = input("Ingrese un número binario: ")

        # Validamos si el número es Positivo y Entero:
        while not validar_numero_entrada(numero_binario, operacion):
            numero_binario = input("Ingrese un número binario: ")

        # Convertimos el número binario validado a decimal:
        numero_decimal = convertir_bin_dec(numero_binario)

        print(f"\n El número binario {numero_binario} equivale al {numero_decimal} en sistema decimal. \n")
        # TODO armar funcion para validar vs int(numero_validado, 2)
        print(f"Control: {int(numero_binario, 2)} \n")

    else:

        print(f"Operación incorrecta. Programa finalizado.\n")
        exit()

    reiniciar = input("¿Desea volver a iniciar? (S/N) ").upper()
    if reiniciar == "S":
        inicio = True
    elif reiniciar == "N":
        print(f"Programa finalizado.\n")
        inicio = False
    else:
        print(f"Opción incorrecta. Programa finalizado.\n")
        inicio = False