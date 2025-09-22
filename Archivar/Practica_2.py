def Menu():
    print('---Menu----')
    print('1.Registrar venta')
    print('2.Mostrar ventas')
    print('3.Total')
    print('4.Eliminar venta')
    print('5.Salir')
    return input('Elige una opción (1-5):')

def Registrar_venta(nombre):
    with open (f'{nombre}.txt','a') as file:
        producto = input('Nombre del producto: ')
        cantidad = input('Cantidad para el stock: ')
        precio = input('Precio unitario del producto: ')
        file.write(f'{producto},{cantidad},{precio}\n')
def Mostrar_venta(nombre):
    with open(f'{nombre}.txt', 'r') as archivo:
        lista = []
        for linea in archivo:
            datos = linea.strip().split(',')
            producto,cantidad,precio = datos
            lista.append([producto,cantidad,precio])
        print("\n{:<10}{:>8}{:>16}".format('Producto','Cantidad','Precio unitario'))
        for d in lista:
            print("{:<10} {:>7} ${:<10.2f}".format(d[0],d[1],float(d[2])))


def calular_total(nombre):
   with open(f'{nombre}.txt', 'r') as archivo:
        lista = []
        for linea in archivo:
            datos = linea.strip().split(',')
            producto,cantidad,precio = datos
            lista.append([producto,cantidad,precio])
        total = sum((int(p[2])*int(p[1])) for p in lista)
        return print(f"\nTotal general: ${total:.2f} \n")

def eliminar_venta(nombre):
   with open(f'{nombre}.txt', 'r') as archivo:
        lista = []
        for linea in archivo:
            datos = linea.strip().split(',')
            producto,cantidad,precio = datos
            lista.append([producto,cantidad,precio])
        name = input('Producto a Eliminar: ').lower().strip()
        for dato in lista:
            if name == dato[0]:
                lista.remove(dato)
                continue
   with open(f'{nombre}.txt', 'w') as archivo:
    for c in lista:
        producto,cantidad,precio = c
        archivo.write(f'{producto},{cantidad},{precio}\n')

nomrbre_archivo = input('¿Qué nombre tiene el archivo?: ')
try:
    archivo = open (f'{nomrbre_archivo}.txt','r')
except FileNotFoundError:
    desicion = input('El archivo no fue encontrado\n Deseas crear uno (si/no)').lower().strip()
    if desicion == 'si':
        archivo = open (f'{nomrbre_archivo}.txt','a')
            
while True:
    opcion = Menu()
    if opcion == '1':
        Registrar_venta(nomrbre_archivo)
    elif opcion == '2':
        Mostrar_venta(nomrbre_archivo)
    elif opcion == '3':
        calular_total(nomrbre_archivo)
    elif opcion == '4':
        eliminar_venta(nomrbre_archivo)
    elif opcion == '5':
        print('Saliendo...')
        break
    else:
        print('Esta no es una opción')
