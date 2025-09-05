# Verificar si un número es positivo.
num=int(input('Dame un numero: '))
if num>0:
    print('El numero es positivo')
elif num==0:
    print('El numero es Neutro')
else:
    print('El numero es negativo')
# Pedir la edad y mostrar si es mayor de edad.
edad=int(input('Dame tu edad: '))
if edad>=18:
    print('Eres mayor de edad')
elif edad==0:
    print('Eres un bebé')
else:
    print('Eres menor de edad')
# Verificar si un número es par.
num=int(input('Dame un numero: '))
if num%2==0:
    print('El numero es par')
else:
    print('El numero es impar')
# Verificar si un número es mayor a 100.
num=int(input('Dame un numero: '))
if num>100:
    print('El numero es mayor a 100')
else:
    print('El numero es menor o igual a 100')
# Verificar si la contraseña es “1234”.
password=input('Dame la contraseña: ')
if password=='1234':
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')
# Verificar si una letra es “a”.
letra=input('Dame una letra: ').lower()
if letra=='a':
    print('La letra es a')
else:
    print('La letra no es a')
# Verificar si un número es múltiplo de 10.
num=int(input('Dame un numero: '))
if num%10==0:
    print('El numero es multiplo de 10')
else:
    print('El numero no es multiplo de 10')
# Preguntar si el día es lunes.
dia=input('Que dia es hoy?: ').lower()
if dia=='lunes':
    print('Hoy es lunes')
else:
    print('Hoy no es lunes')
# Verificar si la calificación es mayor o igual a 70.
calificacion=int(input('Cual es tu calificacion en el curso?: '))
if calificacion>=70:   
    print('Aprobaste')
else:
    print('Reprobaste')
# Verificar si una temperatura es mayor a 30.
temp=int(input('Cual es la temperatura actual?: '))
if temp>30:
    print('Hace calor')
else:
    print('Hace frío')