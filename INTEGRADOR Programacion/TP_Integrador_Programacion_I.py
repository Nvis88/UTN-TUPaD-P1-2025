import time

def genera_lista_DNIs(elementos):
    """
    Genera una lista de números de DNI's aleatorios y desordenados.
    
    Args:
        elementos (int): Cantidad de DNIs a generar.
    
    Returns:
        list: Lista de DNIs aleatorios y desordenados.
    """
    from random import randint
    lista = []
    for _ in range(elementos):
        dni = randint(10000000, 50000000)  # Genera un DNI entre 10.000.000 y 50.000.000
        while dni in lista:  # Asegura que el DNI sea único
            dni = randint(10000000, 50000000)
        lista.append(dni)
    return lista

def dni_aleatorio(lista):
    """
    Selecciona un DNI al azar de la lista.
    
    Args:
        lista (list): Lista de DNIs.
    
    Returns:
        int: Un DNI seleccionado al azar de la lista.
    """
    from random import choice
    return choice(lista)

def ordenamiento_bubble_sort(lista):
    """
    Ordena una lista de DNIs utilizando el algoritmo Bubble Sort.
    
    Args:
        lista (list): Lista de DNIs a ordenar.
    
    Returns:
        list: Lista de DNIs ordenada.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]  # Intercambio
    return lista

def ordenamiento_selection_sort(lista):
    """
    Ordena una lista de DNIs utilizando el algoritmo Selection Sort.
    
    Args:
        lista (list): Lista de DNIs a ordenar.
    
    Returns:
        list: Lista de DNIs ordenada.
    """
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]  # Intercambio
    return lista

def busqueda_lineal(lista, dni):
    """
    Realiza una búsqueda lineal para encontrar un DNI en la lista.
    
    Args:
        lista (list): Lista de DNIs.
        dni (int): DNI a buscar.
    
    Returns:
        int: Índice del DNI en la lista, o -1 si no se encuentra.
    """
    for i in range(len(lista)):
        if lista[i] == dni:
            return i
    return -1  # Si no se encuentra el DNI


def busqueda_binaria(lista, dni):
    """
    Realiza una búsqueda binaria para encontrar un DNI en la lista ordenada.
    
    Args:
        lista (list): Lista de DNIs ordenados.
        dni (int): DNI a buscar.
    
    Returns:
        int: Índice del DNI en la lista, o -1 si no se encuentra.
    """
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == dni:
            return medio
        elif lista[medio] < dni:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return -1  # Si no se encuentra el DNI

##############################
### - PROGRAMA PRINCIPAL - ###
##############################

# Definimos una lista de ejecuciones con diferentes cantidades de elementos:
ejecuciones = [2, 5, 10, 50, 100, 500, 1000, 2000, 4000, 8000]

print("Elementos \tBubble Sort \t Selection Sort \t Búsqueda Lineal \t Búsqueda Binaria")
for elementos in ejecuciones:

    # Creamos una lista de "n" cantidad de DNI's:
    lista_desordenada = genera_lista_DNIs(elementos)

    # Seleccionamos un DNI al azar de la lista y muestro por consola:
    dni_a_buscar = dni_aleatorio(lista_desordenada)


    ################################
    ### ORDENAMIENTO DE LA LISTA ###
    ################################

    # Ordenamiento por BUBBLE SORT
    tiempo_inicio_BS = time.time() # Inicio del cronómetro
    lista_ordenada_BS = ordenamiento_bubble_sort(lista_desordenada)
    tiempo_fin_BS = time.time() # Fin del cronómetro

    # Ordenamiento por SELECTION SORT
    tiempo_inicio_SS = time.time() # Inicio del cronómetro
    lista_ordenada_SS = ordenamiento_selection_sort(lista_desordenada)
    tiempo_fin_SS = time.time() # Fin del cronómetro

    ####################
    ### - BUSQUEDA - ###
    ####################

    # BUSQUEDA LINEAL
    tiempo_inicio_BL = time.time() # Inicio del cronómetro
    posicion_dni_BL = busqueda_lineal(lista_desordenada, dni_a_buscar)
    tiempo_fin_BL = time.time() # Fin del cronómetro

    # BUSQUEDA BINARIA - Con lista ordenada.
    tiempo_inicio_BB = time.time() # Inicio del cronómetro
    posicion_dni_BB = busqueda_binaria(lista_ordenada_BS, dni_a_buscar)
    tiempo_fin_BB = time.time() # Fin del cronómetro

    # Imprimo los resultados de las ejecuciones
    print(f"{elementos} \t\t {(tiempo_fin_BS - tiempo_inicio_BS)*1000:.5f} \t\t {(tiempo_fin_SS - tiempo_inicio_SS)*1000:.5f} \t\t {(tiempo_fin_BL - tiempo_inicio_BL)*1000:.5f} \t\t {(tiempo_fin_BB - tiempo_inicio_BB)*1000:.5f}")