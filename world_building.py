# Parcial 2 - Carlos Wendehake - 16-11255 - Laboratorio de algoritmos y estructuras 1.
# Programa que simula un mundo, constituido por una matriz que contiene tierra, ciudades, agua y montañas, representado con caracteres especificos.

import math, copy
from typing import List

# Variables de construccion
tierra:str = "\033[1;32mT\033[0m"
ciudad:str = "\033[1mC\033[0m"
agua:str = "\033[1;36mA\033[0m"
montaña:str = "\033[1;31mM\033[0m"
vacio:str = "\033[40m \033[0m"

# Mundo actual y de respaldo
mundo: List[List[str]] = []
mundo_respaldo: list[List[str]] = []

# Menu inicial para pedir coordenadas del mundo
while True:
    try:
        M = int(input("Ingrese el número de filas del mundo: "))
        if M > 0:
            break
        else:
            print("El número de filas debe ser mayor que 0.")
    except ValueError:
        print("Ingrese un número entero válido.")

while True:
    try:
        N = int(input("Ingrese el número de columnas del mundo: "))
        if N > 0:
            break
        else:
            print("El número de columnas debe ser mayor que 0.")
    except ValueError:
        print("Ingrese un número entero válido.")


#Creamos el mundo con las dimensiones adecuadas.
for i in range(M):
    mundo.append([])
    for j in range(N):
        mundo[i].append(tierra)


#verificaciones
def verificar_fila(fila:int)->bool:
    """
    Verifica si el valor de la fila está dentro del rango válido.

    Parametros:
    - fila (int): El valor de la fila a verificar.

    Retorna:
    - bool: True si el valor es válido, False de lo contrario.
    """
    es_valido: bool = fila >=0 and fila < M
    if not es_valido:
        print("el valor debe estar dentro del rango de filas del mundo")
    return es_valido

def verificar_columna(columna:int)->bool:
    """
    Verifica si el valor de la columna está dentro del rango válido.

    Parametros:
    - columna (int): El valor de la columna a verificar.

    Retorna:
    - bool: True si el valor es válido, False de lo contrario.
    """
    es_valido: bool = columna >=0 and columna < N
    if not es_valido:
        print("el valor debe estar dentro del rango de columnas del mundo")
    return es_valido

def mayor_que_cero(valor:int)->bool:
    """
    Verifica si el valor es mayor que cero.

    Parametros:
    - valor (int): El valor a verificar.

    Retorna:
    - bool: True si el valor es mayor que cero, False de lo contrario.
    """
    es_valido: bool = valor > 0
    if not es_valido:
        print("el valor debe ser mayor que 0")
    return es_valido


#submenus
def submenu_rio() -> int:
    """
    Muestra el submenu para seleccionar la dirección del río.

    Retorna:
    - int: La opción seleccionada por el usuario.
    """
    direcciones: List[str] = [
        "1. Vertical.",
        "2. Horizontal.",
        "3. Diagonal.",
        "4. Diagonal Inverso"
    ]
    print("\nIndique una opción: ")
    for direccion in direcciones:
        print(direccion)

    try:
        direccion = int(input("\nIngrese el la opcion: "))
        if direccion < 0 or direccion > 4:
            print("El numero indicado es inválido para la direccion del rio.")
        else:
            return direccion
    except ValueError:
        print("Por favor, ingrese un numero válido.")

def submenu_forma()->None:
    """
    Muestra el submenu para seleccionar la forma de construcción (ciudad, rio, montaña)
    """
    formas: List[str] = [
        "1. Forma Ciudad.",
        "2. Forma Rio.",
        "3. Forma Montaña.",
    ]
    print("\nIndique una forma: ")
    for forma in formas:
        print(forma)
    
    try:
        forma = int(input("\nIngrese el la opcion: "))
        if forma <= 0 or forma >=4:
            print("El numero indicado es invalido.")
        else:
            return forma
    except ValueError:
        print("Por favor, ingrese un numero válido para la forma a agregar.")


#funciones del menu principal
def imprimir_mundo()->None:
    """
    Imprime el mundo en la consola.
    """
    print()
    for i in range(len(mundo)):
        for j in range(len(mundo[i])):
            print(mundo[i][j], end=" ")
        print() 

def agregar_ciudad(elemento)->None:
    """
    Agrega una forma de ciudad al mundo.

    Parametros:
    - elemento: El elemento del cual estara conformado la nueva ciudad.
    """
    try:
        fila_x: int = int(input("\nIngrese la fila X: "))
        if verificar_fila(fila_x)==False:
            return
        
        columna_y: int = int(input("Ingrese la columna Y: "))
        if verificar_columna(columna_y)==False:
            return

        lado: int = int(input("Ingrese el tamano L de la ciudad: "))
        if mayor_que_cero(lado)==False:
            return

        for i in range(fila_x,fila_x+lado):
            for j in range(columna_y, columna_y+lado):
                if i<M and j<N and mundo[i][j] != vacio:
                    mundo[i][j]= elemento
    except ValueError:
        print("Ingrese un numero entero válido para la fila, columna y lado de la ciudad.")

#sustitucion de elementos en las diagonales de la forma rio
def agregar_diagonal_principal(fila_x:int, columna_y: int, elemento:str):
    """
    Agrega un elemento en la diagonal principal a partir de la posición (fila_x, columna_y) en la matriz mundo.

    Parámetros:
    - fila_x (int): La fila inicial desde donde se comenzará a agregar el elemento.
    - columna_y (int): La columna inicial desde donde se comenzará a agregar el elemento.
    - elemento (str): El elemento que se agregará en la diagonal principal.
    """
    i, j = fila_x, columna_y 
    while 0 <= i < M and 0 <= j < N:
        if mundo[i][j] != vacio:
            mundo[i][j] = elemento
        #te mueves hacia abajo
        i += 1
        j += 1
        
    i, j = fila_x, columna_y 
    while 0 <= i < M and 0 <= j < N:
        if mundo[i][j] != vacio:
            mundo[i][j] = elemento
        #te mueves hacia arriba
        i -= 1
        j -= 1

def agregar_diagonal_inversa(fila_x:int, columna_y: int, elemento:str):
    """
    Agrega un elemento en la diagonal inversa a partir de la posición (fila_x, columna_y) en la matriz 'mundo'.

    Parámetros:
    - fila_x (int): La fila inicial desde donde se comenzará a agregar el elemento.
    - columna_y (int): La columna inicial desde donde se comenzará a agregar el elemento.
    - elemento (str): El elemento que se agregará en la diagonal inversa.

    """
    #cambias i , j por los valores iniciales del while y te mueves en la diagonal inversa.
    i, j = fila_x, columna_y
    while 0 <= i < M and 0 <= j < N:
        if mundo[i][j] != vacio:
            mundo[i][j] = elemento
        #te mueves hacia abajo
        i += 1
        j -= 1
        
    i, j = fila_x, columna_y
    while 0 <= i < M and 0 <= j < N:
        if mundo[i][j] != vacio:
            mundo[i][j] = elemento
        #te mueves hacia arriba
        i -= 1
        j += 1


def agregar_rio(elemento:str)->None:
    """
    Agrega una forma de río al mundo.

    Parametros:
    - elemento (str): El elemento del cual estara conformado el río.
    """
    try:
        fila_x: int = int(input("\nIngrese la fila X: "))
        if verificar_fila(fila_x)==False:
            return
        
        columna_y: int = int(input("Ingrese la columna Y: "))
        if verificar_columna(columna_y)==False:
            return
    except ValueError:
        print("Ingrese un numero entero válido para la fila y columna del río.")
        return
    
    direccion: int = submenu_rio()

    if direccion == 1:  # vertical
        for i in range(M):
            for j in range(columna_y - 1, columna_y + 2):
                if 0 <= i < M and 0 <= j < N and mundo[i][j] != vacio:  # Verifica límites de la matriz
                    mundo[i][j] = elemento

    elif direccion == 2:  # horizontal
        for i in range(fila_x - 1, fila_x + 2):
            for j in range(N):
                if 0 <= i < M and 0 <= j < N and mundo[i][j] != vacio:  # Verifica límites de la matriz
                    mundo[i][j] = elemento

    elif direccion == 3:  # diagonal
        for i in [-1, 0, 1]:
            agregar_diagonal_principal(fila_x+i, columna_y, elemento)

    elif direccion == 4:  # diagonal inversa
        for i in [-1, 0, 1]:    
            agregar_diagonal_inversa(fila_x+i, columna_y, elemento)

def agregar_montaña(elemento:str)->None:
    """
    Agrega una forma de montaña al mundo.
    
    Parametros:
    - elemento (str): El elemento del estara conformada la montaña
    """
        ##agregale verificacion a las entradas
    try:
        centro_x = int(input("\nIngrese la fila X del centro de la montaña: "))
        if verificar_fila(centro_x) == False:
            return
        
        centro_y = int(input("Ingrese la columna Y del centro de la montaña: "))
        if verificar_columna(centro_y) == False:
            return

        radio = int(input("Ingrese el radio de la montaña: "))
        if mayor_que_cero(radio)==False:
            return
    except ValueError:
        print("Ingrese un numero entero válido para el centro y el radio de la montaña.")
        return
    
    #sustituye elementos segun la formula de la distancia euclidiana
    for i in range(M):
        for j in range(N):
            distancia_centro = math.sqrt((i - centro_x)**2 + (j - centro_y)**2)
            if distancia_centro <= radio and mundo[i][j] != vacio:
                mundo[i][j] = elemento

def aplanar() -> None:
    """
    Esta función permite aplanar el terreno del mundo de acuerdo a la forma seleccionada.
    """
    forma: int = submenu_forma()

    if forma == 1: #ciudad
        agregar_ciudad(tierra)
    if forma == 2: #rio
        agregar_rio(tierra)
    if forma == 3: #montaña
        agregar_montaña(tierra)

def eliminar_zona() -> None:
    """
    Esta función permite al usuario eliminar una zona del sistema de construcción de mundos.
    Solicita al usuario que seleccione la forma de la zona a eliminar (ciudad, río o montaña),
    y luego llama a la función correspondiente para llenarla de vacio la zona de esa forma.
    """
    forma: int = submenu_forma()

    if forma == 1: #ciudad
        agregar_ciudad(vacio)
    if forma == 2: #rio
        agregar_rio(vacio)
    if forma == 3: #montaña
        agregar_montaña(vacio)

def redimensionar() -> None:
    """
    Redimensiona el mundo actual a partir de la cantidad de filas y columnas ingresadas por el usuario.

    Al finalizar, el mundo actual se actualiza con el nuevo mundo, y las variables "filas" y "columnas" se actualizan con las
    nuevas cantidades ingresadas por el usuario.
    """
    try:
        nuevas_filas: int = int(input("\nIngrese la cantidad de filas del nuevo mundo: "))
        if mayor_que_cero(nuevas_filas) == False:
            return
        nuevas_columnas = int(input("Ingrese la cantidad de columnas del nuevo mundo: "))
        if mayor_que_cero(nuevas_columnas) == False:
            return

        nuevo_mundo: List[List[str]] = []
        for i in range(nuevas_filas):
            global mundo, M, N
            nuevo_mundo.append([])
            for j in range(nuevas_columnas):
                if i < M and j < N:
                    nuevo_mundo[i].append(mundo[i][j])
                else:
                    nuevo_mundo[i].append(tierra)

        mundo = nuevo_mundo
        M = nuevas_filas
        N = nuevas_columnas
    except ValueError:
        print("Ingrese un numero entero válido para las filas y columnas del nuevo mundo.")

def deshacer() -> None:
    """
    Revierte los cambios realizados en la variable 'mundo' restaurándola desde la copia de respaldo.
    """
    global mundo
    mundo = mundo_respaldo


# Menu de opciones
opciones: List[str] = [
    "1. Imprimir mundo.",
    "2. Agregar ciudad.",
    "3. Agregar rio.",
    "4. Agregar montaña.",
    "5. Aplanar.",
    "6. Eliminar zona.",
    "7. Redimensionar.",
    "8. Deshacer.",
    "9. Salir.",
]

while True:
    print("\nIndique una opción: ")
    for opcion in opciones:
        print(opcion)

    seleccionado: str = input()

    #Copia el mundo con deepcopy antes de ir a alguna opcion que pueda realizar cambios.
    if seleccionado in ["2","3","4","5","6"]:
        mundo_respaldo: list[List[str]] = copy.deepcopy(mundo)
    
    if seleccionado == "1":
        imprimir_mundo()
    elif seleccionado == "2":
        agregar_ciudad(ciudad)
    elif seleccionado == "3":
        agregar_rio(agua)
    elif seleccionado == "4":
        agregar_montaña(montaña)
    elif seleccionado == "5":
        aplanar()
    elif seleccionado == "6":
        eliminar_zona()
    elif seleccionado == "7":
        redimensionar()
    elif seleccionado == "8":
        deshacer()
    elif seleccionado == "9":
        break
    else:
        print("Opción inválida")

imprimir_mundo()

print("\nHasta Luego :D\n")
