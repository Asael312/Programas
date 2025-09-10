def Menu():
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print('5.Presupuesto')
    print("6. Salir")
    Opcion = int(input("Seleccione una opción: "))
    return Opcion
def layout(producto):
    for x in producto.value:
        print(x)
        return
def AgregarProducto(lista,nombre=None,Stock=0):
    if nombre is None:
        nombre = input('Ingrese el nombre del produccto: ')
    if nombre in lista:
        print("El producto ya existe.")
    else:
        Stock = int(input("Ingrese la cantidad en stock: "))
        codigo=input('Ingrese codigo del producto')
        Costo_unitario=int(input('Ingrese el precoi del producto'))
        lista[nombre] = {'codigo':codigo,'Stock':Stock,'precio':Costo_unitario}
        print("Producto agregado.")
        return Stock,Costo_unitario
def calculo():
    Stock,Costo_unitario=AgregarProducto()
    costo = Stock*Costo_unitario
    return costo

def MostrarInventario(lista):
    if len(lista)==0:
        print('No hay nada en el inventario')
        AgregarProducto(lista)
    print("Inventario:")
    for producto in lista.keys():
        layout(producto)
def ActualizarProducto(Inventario):
    Nombre = input("Ingrese el nombre del producto a actualizar: ")
    if Nombre in Inventario:
        Stock = int(input("Ingrese la nueva cantidad en stock: "))
        Inventario[Nombre]['Stock']= Stock
        print("Producto actualizado.")
    else:
        print("Producto no encontrado.")
def EliminarProducto(Inventario):
    Nombre = input("Ingrese el nombre del producto a eliminar: ")
    if Nombre in Inventario:
        del Inventario[Nombre]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")
def Preciototal(lista):
    Precio_total=sum(lista[producto]['precio'] for producto in lista)
    return Precio_total
Contraseña=''
intentos=0
Precio_total=0
Productos ={}
Opcion=0
while intentos < 3 and Contraseña != 'OXXO':
    Contraseña=input("Ingrese la contraseña: ")
    if Contraseña=='OXXO':
        while Opcion !=6:
            Opcion=Menu()
            if Opcion == 1:
                producto=input('Ingrese el nombre del producto')
                AgregarProducto(Productos,producto)
            elif Opcion == 2:
                AgregarProducto(Productos)
            elif Opcion == 3:
                ActualizarProducto(Productos)
            elif Opcion == 4:
                EliminarProducto(Productos)
            elif Opcion == 5:
                calculo()
            elif Opcion == 6:
                print('Saliendo...')
                print(Productos)
    else:
        print("Contraseña incorrecta. No se pueden agregar o eliminar productos.")
        intentos += 1
