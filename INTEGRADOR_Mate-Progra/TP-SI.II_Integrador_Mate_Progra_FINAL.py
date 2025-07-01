# Función que solicita al usuario que ingrese 4 N° de DNI:
def ingresarDNIs():
    """
    Función que solicita al usuario que ingrese 4 Números de DNI válidos.

    Return:
        dniA, dniB, dniC, dniD (str): Retorna 4 cadenas de texto con los N° de DNI.
    """

    dniA = input("Ingrese el primer DNI: ")
    dniB = input("Ingrese el segundo DNI: ")
    dniC = input("Ingrese el tercer DNI: ")
    dniD = input("Ingrese el cuarto DNI: ")
    return dniA, dniB, dniC, dniD

def dni_a_conjunto(dni):
    """
    Función que recibe una cadena "dni" y devuelve una lista "conj"
    con todos los caracteres de la cadena "dni", ordenados y únicos.

    Args:
        dni (str): La cadena que representa el número de DNI.

    Returns:
        list: Una lista con los caracteres únicos y ordenados del DNI.
    """
    # Convertir la cadena a un conjunto para obtener caracteres únicos
    conjunto_caracteres = set(dni)
    # Convertir el conjunto de nuevo a una lista y ordenarla
    conj = sorted(list(conjunto_caracteres))
    return conj

# Función que genera los conjuntos con los N° de DNI:
def generarConjuntos(dniA, dniB, dniC, dniD):
  """
  Función que devuelve una lista por cada DNI ingresado.

  Args:
    dniA, dniB, dniC, dniD (str): DNI's a convertir en conjuntos

  Returns:
    conjA, conjB, conjC, conjD (list): Lista con números contenidos en cada DNI
  """
  conjA, conjB, conjC, conjD = dni_a_conjunto(dniA), dni_a_conjunto(dniB), dni_a_conjunto(dniC), dni_a_conjunto(dniD)
  return conjA, conjB, conjC, conjD

### - Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas. - ###

def contar_frecuencia_digitos(dni):
  """
  Cuenta la frecuencia de cada dígito en una cadena de DNI.

  Args:
    dni (str): La cadena que representa el número de DNI.

  Returns:
    dict: Un diccionario donde las claves son los dígitos y los valores son sus frecuencias.
  """
  frecuencia = {}
  for digito in dni:
    if digito in frecuencia:
      frecuencia[digito] += 1
    else:
      frecuencia[digito] = 1
  return frecuencia


# prompt: Suma total de los dígitos de cada DNI.

def sumar_digitos_dni(dni):
  """
  Calcula la suma total de los dígitos de un DNI.

  Args:
    dni (str): La cadena que representa el número de DNI.

  Returns:
    int: La suma total de los dígitos.
  """
  suma_total = 0
  for digito in dni:
    suma_total += int(digito)
  return suma_total




# --- PROGRAMA PRINCIPAL --- #
print("SEMANA DE INTEGRACIÓN II - Matemáticas - Progamación \n")

### --- Ingreso de los DNIs (reales o ficticios). --- ###

# DNI's por defecto:
dni_1 = "37339424"
dni_2 = "42098659"
dni_3 = "28942841"
dni_4 = "33599495"

# Selección de Datos a utilizar: Por defecto o nuevos.
selec = input("¿Desea operar con DNI's por Defecto (D) o Nuevos (N)?: ").upper()
while selec != "D" and selec != "N":
    print("Opción incorrecta.")
    selec = input("¿Desea operar con DNI's por Defecto (D) o Nuevos (N)?: ").upper()

# Dependiendo de la selección del usuario, pedimos ingresar DNI's o usamos los por defecto.
if selec == "N":
    dniA, dniB, dniC, dniD = ingresarDNIs()
else:
    dniA, dniB, dniC, dniD = dni_1, dni_2, dni_3, dni_4

### - Generación automática de los conjuntos de dígitos únicos. - ###
conjA, conjB, conjC, conjD = generarConjuntos(dniA, dniB, dniC, dniD)


### - Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica. - ###

# Unión
union_conjuntos = sorted(list(set(conjA) | set(conjB) | set(conjC) | set(conjD)))
print(f"Unión de los conjuntos: {union_conjuntos}")

# Intersección
interseccion_conjuntos = sorted(list(set(conjA) & set(conjB) & set(conjC) & set(conjD)))
print(f"Intersección de los conjuntos: {interseccion_conjuntos}")

# Diferencia (A - B)
diferencia_AB = sorted(list(set(conjA) - set(conjB)))
print(f"Diferencia A - B: {diferencia_AB}")

# Diferencia (B - A)
diferencia_BA = sorted(list(set(conjB) - set(conjA)))
print(f"Diferencia B - A: {diferencia_BA}")

# Diferencia simétrica (A ^ B)
diferencia_simetrica_AB = sorted(list(set(conjA) ^ set(conjB)))
print(f"Diferencia simétrica A ^ B: {diferencia_simetrica_AB}")


### - Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas. - ###
print("\nFrecuencia de dígitos en cada DNI:")
frecuenciaA = contar_frecuencia_digitos(dniA)
print(f"DNI A ({dniA}): {frecuenciaA}")

frecuenciaB = contar_frecuencia_digitos(dniB)
print(f"DNI B ({dniB}): {frecuenciaB}")

frecuenciaC = contar_frecuencia_digitos(dniC)
print(f"DNI C ({dniC}): {frecuenciaC}")

frecuenciaD = contar_frecuencia_digitos(dniD)
print(f"DNI D ({dniD}): {frecuenciaD}")

# Suma total de los dígitos de cada DNI.
print("\nSuma total de los dígitos de cada DNI:")
sumaA = sumar_digitos_dni(dniA)
print(f"Suma de los dígitos del DNI A ({dniA}): {sumaA}")

sumaB = sumar_digitos_dni(dniB)
print(f"Suma de los dígitos del DNI B ({dniB}): {sumaB}")

sumaC = sumar_digitos_dni(dniC)
print(f"Suma de los dígitos del DNI C ({dniC}): {sumaC}")

sumaD = sumar_digitos_dni(dniD)
print(f"Suma de los dígitos del DNI D ({dniD}): {sumaD}")


# Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.
# Ejemplos:
# Si un dígito aparece en todos los conjuntos, mostrar "Dígito compartido".
# Si algún conjunto tiene más de 6 elementos, mostrar "Diversidad numérica alta".


### - Evaluación de condiciones lógicas (condicionales) - ###

# Si un dígito aparece en todos los conjuntos
if interseccion_conjuntos:
  print("\nDígito(s) compartido(s) en todos los conjuntos:", interseccion_conjuntos)
else:
  print("\nNingún dígito es compartido por todos los conjuntos.")

# Si algún conjunto tiene más de 6 elementos
if len(conjA) > 6 or len(conjB) > 6 or len(conjC) > 6 or len(conjD) > 6:
  print("Diversidad numérica alta en al menos un conjunto.")
else:
  print("La diversidad numérica en los conjuntos no es alta.\n")
