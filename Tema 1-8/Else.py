# Decir si un número es positivo o negativo.

num=int(input('Dame un numero: '))
if num>0:
    print('El numero es positivo')
elif num==0:
    print('El numero es Neutro')
else:
    print('El numero es negativo')
# Preguntar si tienes hambre y responder sí/no.

hambre=input('Tienes hambre? (si/no): ').lower()
if hambre=='si':
    print('Come algo!')
else:
    print('A Chambear!')

# Decir si un número es par o impar.

num=int(input('Dame un numero: '))
if num%2==0:
    print('El numero es par')
else:
    print('El numero es impar')

# Decir si una persona es mayor o menor de edad.

edad=int(input('Dame tu edad: '))
if edad>=18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

# Preguntar si quiere café (sí/no).

cafe=input('Quieres cafe? (si/no): ').lower()
if cafe=='si':
    print('Aqui tienes tu cafe')
else:
    print('Quizas en otra ocasion')

# Verificar si un número es mayor a 50 o no.

num=int(input('Dame un numero: '))
if num>50:
    print('El numero es mayor a 50')
else:
    print('El numero es menor o igual a 50')

# Verificar si un color es “rojo” o no.

color=input('Dame un color: ').lower()
if color=='rojo':
    print('El color es rojo')
else:
    print('El color no es rojo')

# Verificar si un nombre es “Ana” o no.

nombre=input('Dame un nombre: ').lower()
if nombre=='ana':
    print('El nombre es Ana')
else:
    print('El nombre no es Ana')

# Verificar si la clave es correcta o incorrecta.

clave=input('Dame la clave: ')
if clave=='1234':
    print('La clave es correcta')
else:
    print('La clave es incorrecta')

# Verificar si un número es múltiplo de 3 o no.

num=int(input('Dame un numero: '))
if num%3==0:
    print('El numero es multiplo de 3')
else:
    print('El numero no es multiplo de 3')