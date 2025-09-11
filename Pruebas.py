def Mostrar_menu():
    print("\n--- MENÚ INVENTARIO ---")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Presupuesto total")
    print("7. Salir")
    Opcion = int(input("Seleccione una opción: "))
    return Opcion
def layout(nombre, datos):
    print(f"Producto: {nombre:<15} Código: {datos['codigo']:<10} Stock: {datos['Stock']:<5} Precio: {datos['precio']:<8}")

def AgregarProducto(diccionario):
    nombre = input("Ingrese el nombre del producto: ")
    if nombre in diccionario:
        print("❌ El producto ya existe.")
    else:
        codigo = input('Ingrese código del producto: ')
        stock = int(input("Ingrese la cantidad en stock: "))
        precio = float(input('Ingrese el precio unitario del producto: '))
        diccionario[nombre] = {'codigo': codigo, 'Stock': stock, 'precio': precio}
        print("✅ Producto agregado correctamente.")

def MostrarInventario(diccionario):
    if len(diccionario) == 0:
        print("📦 El inventario está vacío.")
        opcion = input("¿Desea agregar un producto? (s/n): ").lower()
        if opcion == "s":
            AgregarProducto(diccionario)
    else:
        print("\n--- Inventario ---")
        for nombre, datos in diccionario.items():
            layout(nombre, datos)

def ActualizarProducto(diccionario):
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in diccionario:
        stock = int(input("Ingrese la nueva cantidad en stock: "))
        diccionario[nombre]['Stock'] = stock
        print("✅ Producto actualizado.")
    else:
        print("❌ Producto no encontrado.")

def EliminarProducto(diccionario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in diccionario:
        del diccionario[nombre]
        print("✅ Producto eliminado.")
    else:
        print("❌ Producto no encontrado.")

def BuscarProducto(diccionario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in diccionario:
        print("🔍 Producto encontrado:")
        layout(nombre, diccionario[nombre])
    else:
        print("❌ Producto no encontrado.")
        opcion = input("¿Desea agregarlo al inventario? (s/n): ").lower()
        if opcion == "s":
            codigo = input('Ingrese código del producto: ')
            stock = int(input("Ingrese la cantidad en stock: "))
            precio = float(input('Ingrese el precio unitario del producto: '))
            diccionario[nombre] = {'codigo': codigo, 'Stock': stock, 'precio': precio}
            print("✅ Producto agregado correctamente.")

def Preciototal(diccionario):
    total = sum(diccionario[producto]['Stock'] * diccionario[producto]['precio'] for producto in diccionario)
    return total
Inventario = {}
Opcion = 0

print("🔐 Acceso al inventario")
contraseña = input("Ingrese la contraseña: ")

if contraseña == "OXXO":
    while Opcion != 7:
        Opcion = Mostrar_menu()
        if Opcion == 1:
            MostrarInventario(Inventario)
        elif Opcion == 2:
            AgregarProducto(Inventario)
        elif Opcion == 3:
            ActualizarProducto(Inventario)
        elif Opcion == 4:
            EliminarProducto(Inventario)
        elif Opcion == 5:
            BuscarProducto(Inventario)
        elif Opcion == 6:
            print(f"💰 Presupuesto total: ${Preciototal(Inventario):.2f}")
        elif Opcion == 7:
            print("👋 Saliendo...")
            MostrarInventario(Inventario)
else:
    print("❌ Contraseña incorrecta. Acceso denegado.")