Calificaciones = []
for i in range(11):
    Calificaciones.append(int(input("Ingrese la calificación del estudiante: ")))
print('Promedio: ', sum(Calificaciones)/len(Calificaciones))
print('Calificación más alta: ', max(Calificaciones))
print('Calificación más baja: ', min(Calificaciones))
aprobados = []
reprobados = []
aprobados = [x for x in Calificaciones if x >= 60]
reprobados = [x for x in Calificaciones if x < 60]
print('Aprobados: ', aprobados)
print('Reprobados: ', reprobados)
print('Número de aprobados: ', len(aprobados))
print('Número de reprobados: ', len(reprobados))