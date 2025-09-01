Materias=['Matemáticas', 'Ciencias', 'Historia', 'Lengua', 'Inglés']
print(Materias[0])
print(Materias[-1])
Nombres=[]
for i in range(5):
    Nombres.append(input("Ingrese el nombre del estudiante: "))
for n in range(-1,-6,-1):
    print(Nombres[n])
print(Nombres[::-1])
Temperaturas=[20,30,80,32,51]
Suma=0
for x in range (5):
    Suma+=Temperaturas[x]
print(Suma/5)
print(max(Temperaturas))
print(min(Temperaturas))
suma=0
cont=0
for a in Temperaturas:
    suma+=a
    cont+=1
print(suma/cont)
print('Promedio: ', sum(Temperaturas)/len(Temperaturas))