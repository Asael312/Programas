Materias=['Matemáticas', 'Ciencias', 'Historia', 'Lengua', 'Inglés']
print(Materias[0])
print(Materias[-1])
Nombres=[]
for i in range(5):
    Nombres.append(input("Ingrese el nombre del estudiante: "))
    break
for n in range(-1,-6,-1):
    print(Nombres[n])
    break
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

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1
    breakpoint()
print(hits)

