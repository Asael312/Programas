# biblioteca = [] 
# def normalizar(texto):
#     """Devuelve un texto normalizado (minúsculas y sin espacios extremos)."""
#     return texto.strip().lower()        
# def registrar_libro(biblioteca):
#     """Captura datos del libro y lo agrega a la lista 'biblioteca'."""
#     try:
#         titulo = normalizar(input('Ingrese el nombre del libro: '))
#         autor = normalizar(input('Ingrese el autor del libro: '))
#         anio = int(input('Año de publicación: '))
#         genero = normalizar(input('Género del libro: '))
#         #d = int(input('Día de registro: '))
#         #m = int(input('Mes de registro: '))
#         #a = int(input('Año de registro: '))
#         if not titulo or not autor or not genero:
#             print("Título, autor y género no pueden estar vacíos.")
#             return
#         for libro in biblioteca:
#             if normalizar(libro["titulo"]) == titulo and normalizar(libro["autor"]) == autor:
#                 print("El libro ya existe en la biblioteca.")
#                 return
#         libro = {"titulo": titulo,"autor": autor,"anio": anio,"genero": genero}
#         biblioteca.append(libro)
#         print("Libro agregado exitosamente.")
#     except ValueError:
#         print("Entrada inválida: asegúrate de ingresar números donde corresponde.")
# 
# def consultar_libros(biblioteca,archive):
#     """Muestra todos los libros registrados en forma de tabla simple."""
#     if not biblioteca:
#         print('La biblioteca esta vacía')
#         return    
#     archive.write("{:<30} {:<25} {:<6} {:<20}\n".format('Titulo','Autor','Anio', 'Genero', 'Fecha de registro'))
#     for libros in biblioteca:
#         #d, m, a = libros['fecha_registro']
#         #fecha = f"{d:02d}/{m:02d}/{a}"
#         archive.write("{:<30} {:<25} {:<6} {:<20}\n".format(libros['titulo'],libros['autor'],libros['anio'],libros['genero']))
# def Menu():
#     print('1.Registrar libro','\n','2.Crear Archivo')
# while True:
#     Menu()
#     opcion = input("Seleccione una opcion (1-3): ")
#     if opcion == "1":
#         registrar_libro(biblioteca)
#     elif opcion == "2":    
#         with open ("Biblioteca.txt","w") as archive:
#                 consultar_libros(biblioteca,archive)
#     elif opcion == "3":
#         break
# contador = 0
# with open ("Alumnos.txt","r") as file:
#     for nombre in file:
#         print(nombre)
#         contador+=1
# print(f"Son {contador} elementos")
# 
# with open ("Alumnos.txt","a") as file:
#     file.write(f'\n{input('Agrega un nombre: ')}')
# 
# with open ("Alumnos.txt","r") as file:
#     for nombre in file:
#         print(nombre)

# El programa abre y lee el archivo #
# Mostrar la venta lejible #
# calcular y mostrar, total vendido de cada cliente, total general en ventas, mostrar cliente buscado  #
# si el cliente no existe print('No se a encontrado el cliente') #
def Menu():
    print('1.Costo clientes')
    print('2.Venta por cliente')
    print('3.Total General')
    print('4.Buscar cliente')
    print('5.Salir')
    return input('Elige una opción (1-5): ')

def Mostrar_clientes():
    clientes = Clientes()
    print("\n{:<10}{:<11}{:>11}".format('Cliente','Producto','Monto'))
    for cliente in clientes:
        print("{:<10}{:<11}{:>10.2f}$".format(cliente[0],cliente[1],cliente[2]))
    print()

def Clientes():
    with open('Ventas.txt', 'r') as archivo:
        lista = []
        for linea in archivo:
            datos = linea.strip().split(',')
            cliente,producto,monto = datos
            lista.append([cliente,producto,float(monto)])
    return lista

def Venta_por_cliente():
    clientes = Clientes()
    totales = {}
    for cliente,_,monto in clientes:
        if cliente in totales:
           vendido = totales[cliente]
        else:
           vendido = 0
        vendido+=monto
        totales[cliente] = vendido
    print("\n---Totales por cliente---")
    largo = palabra_mas_larga(cliente)
    for c,total in totales.items():
        print(f"{c:>{largo+2}}: ${total:.2f}")
    print()

def palabra_mas_larga(lista):
    nombre_mas_largo = max([datos[0] for datos in lista], key=len)# palabras es la lista, la key compara todas con su longitut y max escoge el mas largo
    Longitud = len(nombre_mas_largo) # mide la palabra
    return Longitud

def buscar():
    print("\nBusqueda de clientes: ")
    nombre = input("Ingrese un nombre: ")
    clientes = Clientes()
    compras = [(producto,monto)for cliente,producto,monto in clientes if cliente.lower() == nombre.lower()]
    if not compras:
        print(f"El cliente {nombre} no existe")
        return
    total = 0
    for prod,monto in compras:
        print(f"{prod} - ${monto:.2f}")
        total+=monto
    print(f"Total: ${total:.2f}\n")

def Suma_total():
    lista = Clientes()
    total = sum(cliente[2] for cliente in lista)
    print(f"\nEl costo general de clientes es de: {total:.2f}$ \n")
 
while True:
    opcion = Menu()
    if opcion=='1':
        Mostrar_clientes()
    elif opcion=='2':
        Venta_por_cliente()
    elif opcion=='3':
        Suma_total()
    elif opcion=='4':
        buscar()
    elif opcion == '5':
        print('Saliendo...')
        break
    