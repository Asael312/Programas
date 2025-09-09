# Define una función que imprima un saludo con el nombre del usuario.
def saludo(nombre):
    print('Hola,', nombre + '!')

# Haz una función que reciba una lista y muestre todos sus elementos.
def mostrar_lista(elementos):
    for elemento in elementos:
        print(elemento)

# Crea una función que dibuje un cuadrado de asteriscos de tamaño dado.
def dibujar_cuadrado(tamano):
    for i in range(tamano):
        print("* " * tamano)

# Define una función que pida 3 números y muestre el mayor.
def mostrar_mayor():
    numeros = []
    for i in range(3):
        num = float(input("Introduce un número: "))
        numeros.append(num)
    print("El número mayor es:", max(numeros))

# Haz una función que muestre la tabla de multiplicar de un número.
def mostrar_tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

# Define una función que reciba nombre y edad y muestre un mensaje personalizado.
def mostrar_mensaje_personalizado(nombre, edad):
    print('Hola', nombre+', tienes', edad, 'años.')

# Crea una función que imprima los primeros n números pares.
def imprimir_numeros_pares(n):
    for i in range(n):
        print(i * 2)

# Haz una función que muestre los elementos de una lista en orden inverso.
def mostrar_lista_inversa(elementos):
    for elemento in reversed(elementos):
        print(elemento)

# Define una función que reciba dos listas y muestre los elementos comunes.
def mostrar_elementos_comunes(lista1, lista2):
    comunes = set(lista1) & set(lista2)
    for elemento in comunes:
        print(elemento)

# Haz una función que muestre una cuenta regresiva desde n hasta 0.
def cuenta_regresiva(n):
    for i in range(n, -1, -1):
        print(i)
