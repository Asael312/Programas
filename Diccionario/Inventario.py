def Menu():
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    Opcion = int(input("Seleccione una opción: "))
    return Opcion
def MostrarInventario(Inventario):
    print("Inventario:")
    for producto, stock in Inventario.items():
        print(stock, ':', producto)
def AgregarProducto(Inventario):
    Nombre = input("Ingrese el nombre del producto: ")
    if Nombre in Inventario:
        print("El producto ya existe.")
    else:
        Stock = int(input("Ingrese la cantidad en stock: "))
        Inventario[Nombre] = Stock
        print("Producto agregado.")
def ActualizarProducto(Inventario):
    Nombre = input("Ingrese el nombre del producto a actualizar: ")
    if Nombre in Inventario:
        Stock = int(input("Ingrese la nueva cantidad en stock: "))
        Inventario[Nombre] = Stock
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
Inventario = {
    'Laptop': 5,
    'Mouse': 10,
    'Teclado': 15
}
Opcion = 0
while Opcion != 5:
    Opcion = Menu()
    if Opcion == 1:
        MostrarInventario(Inventario)
    elif Opcion == 2:
        AgregarProducto(Inventario)
    elif Opcion == 3:
        ActualizarProducto(Inventario)
    elif Opcion == 4:
        EliminarProducto(Inventario)
    elif Opcion == 5:
        print("Saliendo del programa.")
