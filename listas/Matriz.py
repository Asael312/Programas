# matriz = [['x' for i in range(3)] for i in range(3)]
# print(matriz)
# Matriz1= [    [ [1,2,3],[4,5,6],[7,8,9]],[ [10,11,12],[13,14,15],[16,17,17]],[ [18,19,20],[21,22,24],[24,26,27]],]
# print(Matriz1[1][1][1])
# Matriz2= [ [1,2,3],[4,5,6],[7,8,9]]
# Matriz_C=[]
# for i in range(2):
#   fila=[]
#  for n in range (2):
#    fila.append(Matriz_A[i][n]+Matriz_B[i][n])
#    print(fila)

#for f in range (3):
#   print(Matriz2[f][f])
reprobados=0
mejor_nombre=''
mejor_promedio=-1
Calificaciones = [
   ['Anna',85,90,78],
   ['Luis',70,88,95],
   ['Maria',100,98,95],
   ['Jose',60,75,80],
   ['Elena',85,60,70]
]
print("{:<10} {:>4} {:>4} {:>4} {:>9}".format("Nombre", "P1", "P2", "P3", "Promedio"))
print("-" * 35)
for alumno in Calificaciones:
    califs = alumno['Calificaciones']
    promedio = round(sum(califs) / len(califs), 2)
    alumno['Promedio'] = promedio
    if promedio < 70:
        reprobados += 1
    if mejor_promedio < promedio:
        mejor_promedio = promedio
        mejor_nombre = alumno['Nombre']
    print("{:<10} {:>4} {:>4} {:>4} {:>9.2f}".format(
        alumno['Nombre'], califs[0], califs[1], califs[2], promedio
    ))

print("\n=== Resumen ===")
print(f"Reprobados: {reprobados}")
print(f"Mejor promedio: {mejor_promedio:.2f}  Alumno: {mejor_nombre}")