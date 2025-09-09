# Define una función que reciba dos números y devuelva su suma.
def sumar(num1, num2):
    return num1 + num2
# Crea una función que devuelva el número mayor de una lista.
def mayor_lista(lista):
    return max(lista)

# Haz una función que reciba un número y devuelva su factorial.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Define una función que calcule el promedio de una lista de calificaciones.
def promedio_calificaciones(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Crea una función que devuelva el área de un triángulo dados base y altura.
def area_triangulo(base, altura):
    return (base * altura) / 2

# Haz una función que reciba una lista de nombres y devuelva el más largo.
def nombre_mas_largo(nombres):
    return max(nombres, key=len)

# Define una función que devuelva la cantidad de vocales en un texto.
def contar_vocales(texto):
    return sum(1 for char in texto.lower() if char in 'aeiou')

# Crea una función que determine si un número es primo (True/False).
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Haz una función que convierta grados Celsius a Fahrenheit.
def celsius_a_fahrenheit(grados_celsius):
    return (grados_celsius * 9/5) + 32

# Define una función que reciba una lista de números y devuelva la suma de los pares.
def suma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)
