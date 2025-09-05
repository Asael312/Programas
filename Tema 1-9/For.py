	
# Mostrar los números del 1 al 10.
print
for i in range(1, 11):
    print(i)

# Imprimir la tabla de multiplicar del 7.
print("Tabla de multiplicar del 7:")
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

# Mostrar cada letra de una palabra ingresada.
palabra = input("Introduce una palabra: ").upper()
for letra in palabra:
    print(letra, end=' ')

# Calcular la suma de los primeros 5 números.
print("Suma de los primeros 5 números:")
suma = 0
for i in range(1, 6):
    suma += i
print("La suma de los primeros 5 números es:", suma)

# Mostrar los números pares del 1 al 20.
print("Números pares del 1 al 20:")
for i in range(2, 21, 2):
    print(i)

# Mostrar los números impares del 1 al 15.
print("Números impares del 1 al 15:")
for i in range(1, 16, 2):
    print(i)

# Pedir 5 nombres y mostrarlos uno por uno.
nombres = []
for i in range(5):
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)
print("Nombres introducidos:")
for nombre in nombres:
    print(nombre)

# Mostrar el cuadrado de los números del 1 al 10.
print("Cuadrados de los números del 1 al 10:")
for i in range(1, 11):
    print(i, "al cuadrado es:", i ** 2)
# Contar cuántas vocales hay en una palabra.
palabra = input("Introduce una palabra: ").upper()
vocales = "AEIOU"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print("Número de vocales en la palabra:", contador)

# Mostrar una lista de compras con un ciclo.
compras = []
for _ in range(5):
    articulo = input("Introduce un artículo para la lista de compras: ")
    compras.append(articulo)
print("Lista de compras:")
for item in compras:
    print("-", item)