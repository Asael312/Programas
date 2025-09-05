# Calificación: Excelente (90+), Bueno (70–89), Regular (<70).

calificacion=int(input('Dame tu calificacion: '))
if calificacion>=90:
    print('Excelente')
elif calificacion>=70:
    print('Bueno')
else:
    print('Regular')
# Día de la semana: lunes, martes u otro.

dia=input('Dame un dia de la semana: ').lower()
if dia=='lunes':
    print('Hoy es lunes')
elif dia=='martes':
    print('Hoy es martes')
else:
    print('Hoy es otro dia')

# Número: positivo, negativo o cero.

num=int(input('Dame un numero: '))
if num>0:
    print('El numero es positivo')
elif num==0:
    print('El numero es cero')
else:
    print('El numero es negativo')

# Número del 1 al 3 con un mensaje distinto.

num=int(input('Dame un numero del 1 al 3: '))
if num==1:
    print('Elegiste el uno')
elif num==2:
    print('Elegiste el dos')
elif num==3:
    print('Elegiste el tres')
else:
    print('Numero fuera de rango')

# Edad: niño, joven o adulto.

edad=int(input('Dame tu edad: '))
if edad<13:
    print('Eres un niño')
elif edad<18:
    print('Eres un joven')
else:
    print('Eres un adulto')

# Mes: enero, febrero u otro.

mes=input('Dame un mes: ').lower()
if mes=='enero':
    print('El mes es enero')
elif mes=='febrero':
    print('El mes es febrero')
else:
    print('El mes es otro') 

# Color: rojo, azul o verde.

color=input('Dame un color: ').lower()
if color=='rojo':
    print('El color es rojo')
elif color=='azul':
    print('El color es azul')
elif color=='verde':
    print('El color es verde')
else:
    print('El color es otro')

# Nota: A, B, C o diferente.

nota=input('Dame una nota: ').upper()
if nota=='A':
    print('Excelente')
elif nota=='B':
    print('Bien')
elif nota=='C':
    print('Regular')
else:
    print('Nota no válida')

# Número: 1, 2, 3 o mayor a 3.

num=int(input('Dame un numero: '))
if num==1:
    print('Elegiste el uno')
elif num==2:
    print('Elegiste el dos')
elif num==3:
    print('Elegiste el tres')
else:
    print('Numero fuera de rango')

# Animal: perro, gato o diferente.

animal=input('Dame un animal: ').lower()
if animal=='perro':
    print('El animal es un perro')
elif animal=='gato':
    print('El animal es un gato')
else:
    print('El animal es diferente')