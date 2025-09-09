# cumpleaños = (15, "junio", 1995)
#print('Dia: ', cumpleaños[0])
#print('Mes: ', cumpleaños[1])
#print('Año: ', cumpleaños[2])
#print(len(cumpleaños))

#Hora_de_nacimiento = (10, 30, 45)
#print('Hora: ', Hora_de_nacimiento[0])
#print('Minuto: ', Hora_de_nacimiento[1])
#print('Segundo: ', Hora_de_nacimiento[2])
#print(str(Hora_de_nacimiento[0]+':'+str(Hora_de_nacimiento[1])+':'+str(Hora_de_nacimiento[2])))

# clases = ('Matemáticas', 'Física', 'Química', 'Historia', 'Español')
# print(clases[0])
# print(clases[-1])
# if 'FDP' in clases:
#     print('FDP está en la lista de clases')
# else:
#     print('FDP no está en la lista de clases')
#     nueva_clase = input('Introduce la nueva clase: ')
#     clases = clases + (nueva_clase,)
# if 'FDP' in clases:
#     print('La nueva clase se ha añadido correctamente')
# else:
#     print('La nueva clase no se ha añadido correctamente')
matrícula = input('Introduce tu matrícula: ')
nombre = input('Introduce tu nombre completo: ')
edad = int(input('Introduce tu edad: '))
carrera = input('Introduce tu carrera: ')
alumno = (matrícula, nombre, edad, carrera)
print('---Alumno---')
for dato in alumno:
    print(dato)
print()