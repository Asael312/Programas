# Pedir el nombre del usuario y mostrarlo en pantalla.
print(input('Ingrese su nombre: '))
#   Solicitar la edad y mostrarla sumada con 5.
print(int(input('Ingrese su edad: '))+5)
# Preguntar la ciudad de nacimiento y mostrarla en una frase.
print('Vienes de :' + input('De que ciudad vienes?: '))
#Capturar dos números y mostrar su suma.
print(int(input('Dame un numero: '))+int(input('Dame otro numero: ')))
# Pedir un número y mostrar su doble.
print(int(input('Dame un numero: '))*2)
# Pedir tres números y mostrar el promedio.
sum = 0
for i in range(3):
    sum+=int(input('Dame un numero: '))
print(sum/3)
# Solicitar el año de nacimiento y calcular la edad.
print('Tienes ' + str(2025-int(input('En que año naciste?: '))))
# Pedir el nombre de una mascota y mostrarlo en mayúsculas.
print(input('Cual es el nombre de tu mascota?: ').upper())
# Pedir una calificación y mostrar si es mayor o menor que 70.
calificacion=int(input('Cual es tu calificacion en el curso?: '))
if calificacion<70:
    print('Reprobaste')
else:
    print('Aprobaste')