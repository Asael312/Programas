# frutas = {
#     "manzana": 'Roja',
#     "banana": 'Amarilla',
#     "naranja": 'Naranja'
# }
# print(frutas)
# print(frutas["manzana"])
# Frutas = {
#     1:{'nombre':'manzana', 'color':'Roja'},
#     2:{'nombre':'banana', 'color':'Amarilla'},
#     3:{'nombre':'naranja', 'color':'Naranja'}
# }
# print(Frutas)
# print(Frutas[2]['nombre'])
# Frutas[4] = {'nombre':'pera', 'color':'Verde'}
# print(Frutas)
# Frutas[1]["nombre"] = 'Achiote'
# Frutas[1]["color"] = 'Verde'
#  # del Frutas[3] # Frutas.pop(3) # Frutas.clear() # Frutas.popietem()
# print(Frutas)
# print(Frutas.keys())
# print(Frutas.items())
# print(Frutas.values())
# for key in Frutas:
#     print(key, Frutas[key])
# for values in Frutas.values():
#     print(values)
# for key, value in Frutas.items():
#     print(key, value)
# Alumno = {
#     "nombre": 'Juan',
#     "edad": 20,
#     "curso": 'Matemáticas',
#     "calificaciones": [85, 90, 78]
# }
# print(Alumno["calificaciones"][1])
# print('Promedio de calificaciones:', sum(Alumno["calificaciones"])/len(Alumno["calificaciones"]))
alumnos = {
    'AL0651': {'nombre':'Asael','edad':18,'carrera': 'Ingeniería'},
    'AL1686': {'nombre':'Luis', 'edad':19,'carrera': 'Medicina'},
    'AL4652': {'nombre':'Ana', 'edad':17,'carrera': 'Derecho'}
}
for alumno in alumnos.values():
    print('Nombre', alumno['nombre'])
# for key in alumnos:
#     print(key, alumnos[key]['nombre'])
print('='*10)
print(alumnos)
alumnos['AL2021'] = {'nombre':'Marta', 'edad':20,'carrera': 'Arquitectura'}
print('='*10)
print(alumnos)
alumnos['AL1686']['edad'] = 20
alumnos.pop('AL0651')
# del alumnos['AL4652']
print(alumnos)