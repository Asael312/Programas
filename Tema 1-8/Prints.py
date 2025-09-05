# Imprimir tu nombre completo
print('Emilio Asael Robles Sánchez')
# Mostrar un poema corto en varias líneas.
print('Rosas son rojas,\nVioletas son azules,\nEl código es divertido,\nY tú también lo eres.')
# Mostrar un menú con tres opciones (ej. Sumar, Restar, Salir).
print('--- Menú ---\n1. Sumar\n2. Restar\n3. Salir')
# Imprimir la tabla de multiplicar del 5.
for i in range(1, 11):
    print(5 + ' x ' + i + ' = ' + str(5 * i))
# Mostrar el resultado de una operación matemática (2+3=5).
print('2 + 3 = ' + str(2 + 3))
# Imprimir el uso de caracteres de escape (\n, \t, ").
print('Línea 1\n\tLínea 2 con tabulación\n"Comillas dobles"')
# Mostrar una frase con variables (ejemplo: nombre y edad).
nombre = 'Emilio Asael'
edad = 18
print('Mi nombre es', nombre,  'y tengo', edad ,'años.')
# Imprimir el área de un rectángulo con valores dados.
base = 5
altura = 10
print('El área del rectángulo es:', base * altura)
# Mostrar una lista de compras numerada.
compras = ('1.Manzanas', '2.Pan', '3.Leche', '4.Huevos')
for item in compras:
    print(item)
# Imprimir un triángulo con asteriscos.
for i in range(1, 6):
    print('*' * i)