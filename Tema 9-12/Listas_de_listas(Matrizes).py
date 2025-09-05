# Crea una matriz de 3x3 con números del 1 al 9 e imprímela fila por fila.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    print(fila)

# Pide al usuario nombres y calificaciones de 3 alumnos y guárdalos en una lista de listas.
alumnos = []
for i in range(3):
    nombre = input("Introduce el nombre del alumno: ")
    calificacion = float(input("Introduce la calificación del alumno: "))
    alumnos.append([nombre, calificacion])

# Accede al elemento en la fila 2, columna 3 de una matriz.
# (Recuerda que los índices comienzan en 0)
elemento = matriz[1][2]
print("Elemento en fila 2, columna 3:", elemento)

# Cambia un valor dentro de una matriz (ej. calificación incorrecta).
alumnos[1][1] = 8.5
print("Lista de alumnos después de la modificación:", alumnos)

# Cuenta cuántos números pares hay en una matriz 3x3.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pares = 0
for fila in matriz:
    for num in fila:
        if num % 2 == 0:
            pares += 1
print("Cantidad de números pares en la matriz:", pares)

# Multiplica todos los elementos de una matriz por 2 y muestra el resultado.
matriz_doblada = []
for fila in matriz:
    fila_doblada = [num * 2 for num in fila]
    matriz_doblada.append(fila_doblada)
print("Matriz original:")
for fila in matriz:
    print(fila)
print("Matriz después de multiplicar por 2:")
for fila in matriz_doblada:
    print(fila)

# Crea una matriz de 5x2 inicializada con ceros usando ciclos.
matriz_ceros = []
for i in range(5):
    fila = [0] * 2
    matriz_ceros.append(fila)
print("Matriz de 5x2 inicializada con ceros:")
for fila in matriz_ceros:
    print(fila)

# Crea un programa que busque un nombre dentro de una lista de listas.
nombre_buscado = input("Introduce el nombre a buscar: ")
encontrado = False
for alumno in alumnos:
    if alumno[0] == nombre_buscado:
        encontrado = True
        break
if encontrado:
    print("Nombre encontrado:", alumno)
else:
    print("Nombre no encontrado.")

# Imprime los nombres de cantantes famosos a partir de una matriz con nombre real y artístico.
cantantes = [["Stefani Joanne Angelina Germanotta", "Lady Gaga"],
             ["Adele Laurie Blue Adkins", "Adele"],
             ["Abel Makkonen Tesfaye", "The Weeknd"]]
print("Cantantes famosos:")
for cantante in cantantes:
    print("Nombre real:", cantante[0], "| Nombre artístico:", cantante[1])

# Rota una matriz de 3x3 (transponer filas y columnas).
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_rotada = []
for i in range(3):
    fila = [matriz[j][i] for j in range(3)]
    matriz_rotada.append(fila)
print("Matriz original:")
for fila in matriz:
    print(fila)
print("Matriz después de rotar:")
for fila in matriz_rotada:
    print(fila)