import Funcions
opcion=''
while opcion != 'salir':
    opcion=Funcions.menu()
    if opcion=='1':
        lado=float(input('Ingrese el lado del cuadrado: '))
        cuadrado=Funcions.area_cuadrado(lado)
        print('El area del cuadrado es:',cuadrado,' unidades cuadradas')
    elif opcion=='2':
        base=float(input('Ingrese la base del rectangulo: '))
        altura=float(input('Ingrese la altura del rectangulo: '))
        rectangulo=Funcions.area_rectangulo(base,altura)
        print('El area del rectangulo es:', rectangulo,' unidades cuadradas')
    elif opcion=='3':
        radio=float(input('Ingrese el radio del circulo: '))
        circulo=Funcions.area_circulo(radio)
        print('El area del circulo es:', circulo,' unidades cuadradas')
    elif opcion=='salir':
        print('Saliendo del programa...')
    else:
        print('Opcion no valida, intente de nuevo')
    print('-'*50)