try:
 numero = int(input('Dame un número: '))
 print(numero/5)
except ValueError:
 print('Hay un problema conn tu número') 
try:
  edad = int(input('Dame tu edad: '))
  print('Tu edad es : '+str(edad))
except ValueError:
 print('Hay un problema conn tu número') 

def edad_valida():
 try:
    Edad = input('Dame tu edad: ')
    if int(Edad) < 0:
      print('Intentalo de nuevo')
      edad_valida()
 except ValueError:
        print('Hay un problema con tu número')
        edad_valida()  
edad_valida()